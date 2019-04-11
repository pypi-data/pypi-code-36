# -*- coding: utf-8 -*
from __future__ import absolute_import, division, print_function, unicode_literals
from .py23_compat import range, int

import numpy as np

from astropy.io import fits
from astropy.table import Table

from .interval_set import IntervalSet
from . import utils

__author__ = "Thomas Boch, Matthieu Baumann"
__copyright__ = "CDS, Centre de Données astronomiques de Strasbourg"

__license__ = "BSD 3-Clause License"
__email__ = "thomas.boch@astro.unistra.fr, matthieu.baumann@astro.unistra.fr"


class AbstractMOC:
    """
    Basic functions for manipulating MOCs.
    """
    HPY_MAX_NORDER = 29
    LARK_PARSER_STR = None

    def __init__(self, interval_set=None):
        interval = IntervalSet() if interval_set is None else interval_set
        self._interval_set = interval
        # Must be overridden in subclasses
        self._fits_header_keywords = None

    def __repr__(self):
        return self._interval_set.__repr__()

    def __eq__(self, another_moc):
        """
        Test equality between thr MOC instance and ``another_moc``

        Parameters
        ----------
        another_moc : `~mocpy.moc.MOC`
            The moc object to test the equality with

        Returns
        -------
        result : bool
            True if the interval sets of self and ``another_moc`` are equal (the interval sets are checked
            for consistency before comparing them).
        """
        if not isinstance(another_moc, AbstractMOC):
            raise TypeError('Cannot compare an AbstractMOC with a {0}'.format(type(another_moc)))

        return self._interval_set == another_moc._interval_set

    def empty(self):
        """
        Checks whether the MOC is empty.

        A MOC is empty when its list of HEALPix cell ranges is empty.

        Returns
        -------
        result: bool
            True if the MOC instance is empty.
        """
        return self._interval_set.empty()

    @property
    def max_order(self):
        """
        Depth of the smallest HEALPix cells found in the MOC instance.
        """
        # TODO: cache value
        combo = int(0)
        for iv in self._interval_set._intervals:
            combo |= iv[0] | iv[1]

        ret = AbstractMOC.HPY_MAX_NORDER - (utils.number_trailing_zeros(combo) // 2)
        if ret < 0:
            ret = 0

        return ret

    def intersection(self, another_moc, *args):
        """
        Intersection between the MOC instance and other MOCs.

        Parameters
        ----------
        another_moc : `~mocpy.moc.MOC`
            The MOC used for performing the intersection with self.
        args : `~mocpy.moc.MOC`
            Other additional MOCs to perform the intersection with.

        Returns
        -------
        result : `~mocpy.moc.MOC`/`~mocpy.tmoc.TimeMOC`
            The resulting MOC.
        """
        interval_set = self._interval_set.intersection(another_moc._interval_set)
        for moc in args:
            interval_set = interval_set.intersection(moc._interval_set)

        return self.__class__(interval_set)

    def union(self, another_moc, *args):
        """
        Union between the MOC instance and other MOCs.

        Parameters
        ----------
        another_moc : `~mocpy.moc.MOC`
            The MOC used for performing the union with self.
        args : `~mocpy.moc.MOC`
            Other additional MOCs to perform the union with.

        Returns
        -------
        result : `~mocpy.moc.MOC`/`~mocpy.tmoc.TimeMOC`
            The resulting MOC.
        """
        interval_set = self._interval_set.union(another_moc._interval_set)
        for moc in args:
            interval_set = interval_set.union(moc._interval_set)

        return self.__class__(interval_set)

    def difference(self, another_moc, *args):
        """
        Difference between the MOC instance and other MOCs.

        Parameters
        ----------
        another_moc : `~mocpy.moc.MOC`
            The MOC used that will be substracted to self.
        args : `~mocpy.moc.MOC`
            Other additional MOCs to perform the difference with.

        Returns
        -------
        result : `~mocpy.moc.MOC` or `~mocpy.tmoc.TimeMOC`
            The resulting MOC.
        """
        interval_set = self._interval_set.difference(another_moc._interval_set)
        for moc in args:
            interval_set = interval_set.difference(moc._interval_set)

        return self.__class__(interval_set)

    def complement(self):
        """
        Returns the complement of the MOC instance.

        Returns
        -------
        result : `~mocpy.moc.MOC` or `~mocpy.tmoc.TimeMOC`
            The resulting MOC.
        """
        complement_interval = self._complement_interval()
        return self.__class__(complement_interval)

    def _complement_interval(self):
        res = []
        intervals_l = sorted(self._interval_set._intervals.tolist())

        if intervals_l[0][0] > 0:
            res.append((0, intervals_l[0][0]))

        last = intervals_l[0][1]

        for itv in intervals_l[1:]:
            res.append((last, itv[0]))
            last = itv[1]

        max_pix_depth = self._get_max_pix()

        if last < max_pix_depth:
            res.append((last, max_pix_depth))

        return IntervalSet(np.asarray(res))

    def _get_max_pix(self):
        pass

    @staticmethod
    def _neighbour_pixels(hp, ipix):
        """
        Returns all the pixels neighbours of ``ipix``
        """
        neigh_ipix = np.unique(hp.neighbours(ipix).ravel())
        # Remove negative pixel values returned by `~astropy_healpix.HEALPix.neighbours`
        return neigh_ipix[np.where(neigh_ipix >= 0)]

    @classmethod
    def from_cells(cls, cells):
        """
        Creates a MOC from a numpy array representing the HEALPix cells.

        Parameters
        ----------
        cells : `numpy.ndarray`
            Must be a numpy structured array (See https://docs.scipy.org/doc/numpy-1.15.0/user/basics.rec.html).
            The structure of a cell contains 3 attributes:

            - A `ipix` value being a np.uint64
            - A `depth` value being a np.uint32
            - A `fully_covered` flag bit stored in a np.uint8

        Returns
        -------
        moc : `~mocpy.moc.MOC`
            The MOC.
        """
        shift = (AbstractMOC.HPY_MAX_NORDER - cells["depth"]) << 1

        p1 = cells["ipix"]
        p2 = cells["ipix"] + 1

        intervals = np.vstack((p1 << shift, p2 << shift)).T

        return cls(IntervalSet(intervals))

    @classmethod
    def from_json(cls, json_moc):
        """
        Creates a MOC from a dictionary of HEALPix cell arrays indexed by their depth.

        Parameters
        ----------
        json_moc : dict(str : [int]
            A dictionary of HEALPix cell arrays indexed by their depth.

        Returns
        -------
        moc : `~mocpy.moc.MOC` or `~mocpy.tmoc.TimeMOC`
            the MOC.
        """
        intervals = np.array([])
        for order, pix_l in json_moc.items():
            if len(pix_l) == 0:
                continue
            pix = np.array(pix_l)
            p1 = pix
            p2 = pix + 1
            shift = 2 * (AbstractMOC.HPY_MAX_NORDER - int(order))

            itv = np.vstack((p1 << shift, p2 << shift)).T
            if intervals.size == 0:
                intervals = itv
            else:
                intervals = np.vstack((intervals, itv))

        return cls(IntervalSet(intervals))

    def _uniq_pixels_iterator(self):
        """
        Generator giving the NUNIQ HEALPix pixels of the MOC.

        Returns
        -------
        uniq :
            the NUNIQ HEALPix pixels iterator
        """
        intervals_uniq_l = IntervalSet.to_nuniq_interval_set(self._interval_set)._intervals
        for uniq_iv in intervals_uniq_l:
            for uniq in range(uniq_iv[0], uniq_iv[1]):
                yield uniq

    @classmethod
    def from_fits(cls, filename):
        """
        Loads a MOC from a FITS file.

        The specified FITS file must store the MOC (i.e. the list of HEALPix cells it contains) in a binary HDU table.

        Parameters
        ----------
        filename : str
            The path to the FITS file.

        Returns
        -------
        result : `~mocpy.moc.MOC` or `~mocpy.tmoc.TimeMOC`
            The resulting MOC.
        """
        table = Table.read(filename)

        intervals = np.vstack((table['UNIQ'], table['UNIQ']+1)).T

        nuniq_interval_set = IntervalSet(intervals)
        interval_set = IntervalSet.from_nuniq_interval_set(nuniq_interval_set)
        return cls(interval_set)

    @classmethod
    def from_str(cls, value):
        """
        Create a MOC from a str.
        
        This grammar is expressed is the `MOC IVOA <http://ivoa.net/documents/MOC/20190215/WD-MOC-1.1-20190215.pdf>`__
        specification at section 2.3.2.

        Parameters
        ----------
        value : str
            The MOC as a string following the grammar rules.
        
        Returns
        -------
        moc : `~mocpy.moc.MOC` or `~mocpy.tmoc.TimeMOC`
            The resulting MOC
        
        Examples
        --------
        >>> from mocpy import MOC
        >>> moc = MOC.from_str("2/2-25,28,29 4/0 6/")
        """
        # Import lark parser when from_str is called
        # at least one time
        from lark import Lark, Transformer
        class ParsingException(Exception):
            pass

        class TreeToJson(Transformer):
            def value(self, items):
                res = {}
                for item in items:
                    if item is not None: # Do not take into account the "sep" branches
                        res.update(item)
                return res

            def sep(self, items):
                pass

            def depthpix(self, items):
                depth = str(items[0])
                pixs_l = items[1:][0]
                return {depth: pixs_l}

            def uniq_pix(self, pix):
                if pix:
                    return [int(pix[0])]

            def range_pix(self, range_pix):
                lower_bound = int(range_pix[0])
                upper_bound = int(range_pix[1])
                return np.arange(lower_bound, upper_bound + 1, dtype=int)

            def pixs(self, items):
                ipixs = []
                for pix in items:
                    if pix is not None: # Do not take into account the "sep" branches
                        ipixs.extend(pix)
                return ipixs

        # Initialize the parser when from_str is called
        # for the first time
        if AbstractMOC.LARK_PARSER_STR is None:
            AbstractMOC.LARK_PARSER_STR = Lark(r"""
                value: depthpix (sep+ depthpix)*
                depthpix : INT "/" sep* pixs
                pixs : pix (sep+ pix)*
                pix : INT? -> uniq_pix
                    | (INT "-" INT) -> range_pix
                sep : " " | "," | "\n" | "\r"

                %import common.INT
                """, start='value')

        try:
            tree = AbstractMOC.LARK_PARSER_STR.parse(value)
        except Exception as err:
            raise ParsingException("Could not parse {0}. \n Check the grammar section 2.3.2 of http://ivoa.net/documents/MOC/20190215/WD-MOC-1.1-20190215.pdf to see the correct syntax for writing a MOC from a str".format(value))

        moc_json = TreeToJson().transform(tree)

        return cls.from_json(moc_json)

    @staticmethod
    def _to_json(uniq):
        """
        Serializes a MOC to the JSON format.

        Parameters
        ----------
        uniq : `~numpy.ndarray`
            The array of HEALPix cells representing the MOC to serialize.

        Returns
        -------
        result_json : {str : [int]}
            A dictionary of HEALPix cell lists indexed by their depth.
        """
        result_json = {}

        depth, ipix = utils.uniq2orderipix(uniq)
        min_depth = np.min(depth[0])
        max_depth = np.max(depth[-1])

        for d in range(min_depth, max_depth+1):
            pix_index = np.where(depth == d)[0]
            if pix_index.size:
                # there are pixels belonging to the current order
                ipix_depth = ipix[pix_index]
                result_json[str(d)] = ipix_depth.tolist()

        return result_json

    @staticmethod
    def _to_str(uniq):
        """
        Serializes a MOC to the STRING format.

        HEALPix cells are separated by a comma. The HEALPix cell at order 0 and number 10 is encoded
        by the string: "0/10", the first digit representing the depth and the second the HEALPix cell number
        for this depth. HEALPix cells next to each other within a specific depth can be expressed as a range and 
        therefore written like that: "12/10-150". This encodes the list of HEALPix cells from 10 to 150 at the
        depth 12.

        Parameters
        ----------
        uniq : `~numpy.ndarray`
            The array of HEALPix cells representing the MOC to serialize.

        Returns
        -------
        result : str
            The serialized MOC.
        """
        def write_cells(serial, a, b, sep=''):
            if a == b:
                serial += '{0}{1}'.format(a, sep)
            else:
                serial += '{0}-{1}{2}'.format(a, b, sep)
            return serial

        res = ''

        if uniq.size == 0: 
            return res

        depth, ipixels = utils.uniq2orderipix(uniq)
        min_depth = np.min(depth[0])
        max_depth = np.max(depth[-1])

        for d in range(min_depth, max_depth+1):
            pix_index = np.where(depth == d)[0]

            if pix_index.size > 0:
                # Serialize the depth followed by a slash
                res += '{0}/'.format(d)

                # Retrieve the pixel(s) for this depth
                ipix_depth = ipixels[pix_index]
                if ipix_depth.size == 1:
                    # If there is only one pixel we serialize it and
                    # go to the next depth
                    res = write_cells(res, ipix_depth[0], ipix_depth[0])
                else:
                    # Sort them in case there are several
                    ipix_depth = np.sort(ipix_depth)

                    beg_range = ipix_depth[0]
                    last_range = beg_range

                    # Loop over the sorted pixels by tracking the lower bound of
                    # the current range and the last pixel.
                    for ipix in ipix_depth[1:]:
                        # If the current pixel does not follow the previous one
                        # then we can end a range and serializes it
                        if ipix > last_range + 1:
                            res = write_cells(res, beg_range, last_range, sep=',')
                            # The current pixel is the beginning of a new range
                            beg_range = ipix

                        last_range = ipix

                    # Write the last range
                    res = write_cells(res, beg_range, last_range)

                # Add a ' ' separator before writing serializing the pixels of the next depth
                res += ' '

        # Remove the last ' ' character
        res = res[:-1]

        return res

    def _to_fits(self, uniq, optional_kw_dict=None):
        """
        Serializes a MOC to the FITS format.

        Parameters
        ----------
        uniq : `numpy.ndarray`
            The array of HEALPix cells representing the MOC to serialize.
        optional_kw_dict : dict
            Optional keywords arguments added to the FITS header.

        Returns
        -------
        thdulist : `astropy.io.fits.HDUList`
            The list of HDU tables.
        """
        depth = self.max_order
        if depth <= 13:
            fits_format = '1J'
        else:
            fits_format = '1K'

        tbhdu = fits.BinTableHDU.from_columns(
            fits.ColDefs([
                fits.Column(name='UNIQ', format=fits_format, array=uniq)
            ]))
        tbhdu.header['PIXTYPE'] = 'HEALPIX'
        tbhdu.header['ORDERING'] = 'NUNIQ'
        tbhdu.header.update(self._fits_header_keywords)
        tbhdu.header['MOCORDER'] = depth
        tbhdu.header['MOCTOOL'] = 'MOCPy'
        if optional_kw_dict:
            for key in optional_kw_dict:
                tbhdu.header[key] = optional_kw_dict[key]

        thdulist = fits.HDUList([fits.PrimaryHDU(), tbhdu])
        return thdulist

    def serialize(self, format='fits', optional_kw_dict=None):
        """
        Serializes the MOC into a specific format.

        Possible formats are FITS, JSON and STRING

        Parameters
        ----------
        format : str
            'fits' by default. The other possible choice is 'json' or 'str'.
        optional_kw_dict : dict
            Optional keywords arguments added to the FITS header. Only used if ``format`` equals to 'fits'.

        Returns
        -------
        result : `astropy.io.fits.HDUList` or JSON dictionary
            The result of the serialization.
        """
        formats = ('fits', 'json', 'str')
        if format not in formats:
            raise ValueError('format should be one of %s' % (str(formats)))

        uniq_l = []
        for uniq in self._uniq_pixels_iterator():
            uniq_l.append(uniq)

        uniq = np.array(uniq_l)

        if format == 'fits':
            result = self._to_fits(uniq=uniq,
                                   optional_kw_dict=optional_kw_dict)
        elif format == 'str':
            result = self.__class__._to_str(uniq=uniq)
        else:
            # json format serialization
            result = self.__class__._to_json(uniq=uniq)

        return result

    def write(self, path, format='fits', overwrite=False, optional_kw_dict=None):
        """
        Writes the MOC to a file.

        Format can be 'fits' or 'json', though only the fits format is officially supported by the IVOA.

        Parameters
        ----------
        path : str, optional
            The path to the file to save the MOC in.
        format : str, optional
            The format in which the MOC will be serialized before being saved. Possible formats are "fits" or "json".
            By default, ``format`` is set to "fits".
        overwrite : bool, optional
            If the file already exists and you want to overwrite it, then set the  ``overwrite`` keyword. Default to False.
        optional_kw_dict : optional
            Optional keywords arguments added to the FITS header. Only used if ``format`` equals to 'fits'.
        """
        serialization = self.serialize(format=format, optional_kw_dict=optional_kw_dict)
        if format == 'fits':
            serialization.writeto(path, overwrite=overwrite)
        else:
            import json
            with open(path, 'w') as h:
                h.write(json.dumps(serialization, sort_keys=True, indent=2))

    def degrade_to_order(self, new_order):
        """
        Degrades the MOC instance to a new, less precise, MOC.

        The maximum depth (i.e. the depth of the smallest HEALPix cells that can be found in the MOC) of the
        degraded MOC is set to ``new_order``. 

        Parameters
        ----------
        new_order : int
            Maximum depth of the output degraded MOC.

        Returns
        -------
        moc : `~mocpy.moc.MOC` or `~mocpy.tmoc.TimeMOC`
            The degraded MOC.
        """
        shift = 2 * (AbstractMOC.HPY_MAX_NORDER - new_order)
        ofs = (int(1) << shift) - 1
        mask = ~ofs
        adda = int(0)
        addb = ofs

        iv_set = []

        for iv in self._interval_set._intervals:
            a = (iv[0] + adda) & mask
            b = (iv[1] + addb) & mask
            if b > a:
                iv_set.append((a, b))

        return self.__class__(IntervalSet(np.asarray(iv_set)))

    def refine_to_order(self, min_depth):
        return self.__class__(IntervalSet(self._interval_set._intervals, min_depth=min_depth))