import pytest
import tempfile
import copy

import numpy as np

from astropy.coordinates import SkyCoord, ICRS, Angle
import astropy.units as u
from astropy.io import fits

from astropy_healpix import HEALPix

from ..moc import MOC, WCS

def get_random_skycoords(size):
    return SkyCoord(ra=np.random.uniform(0, 360, size),
                    dec=np.random.uniform(-90, 90, size),
                    unit="deg")


skycoords1 = get_random_skycoords(size=1000)
skycoords2 = get_random_skycoords(size=2000)
skycoords3 = get_random_skycoords(size=50000)

@pytest.fixture()
def skycoords_gen_f():
    def gen_f(size):
        return SkyCoord(np.random.uniform(0, 360, size), np.random.uniform(-90, 90, size), unit='deg')

    return gen_f


@pytest.fixture()
def lonlat_gen_f():
    def gen_f(size):
        return np.random.uniform(0, 360, size) * u.deg, np.random.uniform(-90, 90, size) * u.deg

    return gen_f


@pytest.mark.parametrize("size", [
    1000,
    10000,
    50000
])
def test_moc_from_skycoords(skycoords_gen_f, size):
    skycoords = skycoords_gen_f(size)
    moc = MOC.from_skycoords(skycoords, max_norder=7)


@pytest.mark.parametrize("size", [
    1000,
    10000,
    50000
])
def test_moc_from_lonlat(lonlat_gen_f, size):
    lon, lat = lonlat_gen_f(size)

    moc = MOC.from_lonlat(lon=lon, lat=lat, max_norder=7)


def test_moc_from_fits():
    fits_path = 'resources/P-GALEXGR6-AIS-FUV.fits'
    moc = MOC.from_fits(fits_path)


def test_moc_from_fits_images():
    image_path = 'resources/image_with_mask.fits.gz'

    moc = MOC.from_fits_images([image_path],
                                max_norder=10)


@pytest.fixture()
def moc_from_fits_image():
    image_path = 'resources/image_with_mask.fits.gz'

    with fits.open(image_path) as hdulist:
        moc = MOC.from_image(header=hdulist[0].header,
                             max_norder=7,
                             mask=hdulist[0].data)

    return moc


def test_moc_from_fits_image(moc_from_fits_image):
    assert moc_from_fits_image


def test_moc_serialize_and_from_json(moc_from_fits_image):
    ipix_d = moc_from_fits_image.serialize(format="json")
    moc2 = MOC.from_json(ipix_d)
    assert moc_from_fits_image == moc2

@pytest.mark.parametrize("expected, moc_str", [
    (MOC.from_json({'5': [8, 9, 10, 42, 43, 44, 45, 54, 46], '6':[4500], '7':[], '8':[45]}),
    '5/8-10,42-46,54,8 6/4500 8/45'),
    (MOC.from_json({}), '0/'),
    (MOC.from_json({'29': [101]}), '29/101'),
    (MOC.from_json({'0': [1, 0, 9]}), '0/0-1,9'),
    (MOC.from_json({'0': [2, 9], '1': [9]}), '0/2,9'),
    (MOC.from_json({'0': [2], '8': [8, 9, 10], '11': []}), '0/2\r ,\n 8/8-10\n 11/'),
])
def test_from_str(expected, moc_str):
    assert MOC.from_str(moc_str) == expected

@pytest.mark.parametrize("moc, expected", [
    (MOC.from_json({'5': [8, 9, 10, 42, 43, 44, 45, 54, 46], '6':[4500], '7':[], '8':[45]}),
    '5/8-10,42-46,54 6/4500 8/45'),
    (MOC.from_json({}), ''),
    (MOC.from_json({'29': [101]}), '29/101'),
    (MOC.from_json({'0': [1, 0, 9]}), '0/0-1,9'),
    (MOC.from_json({'0': [2, 9], '1': [9]}), '0/2,9'),
])
def test_serialize_to_str(moc, expected):
    assert moc.serialize(format="str") == expected

def test_moc_write_and_from_json(moc_from_fits_image):
    tmp_file = tempfile.NamedTemporaryFile()
    moc_from_fits_image.write(tmp_file.name, format='json')

    with open(tmp_file.name, 'r') as moc_file:
        import json
        moc_d = json.load(moc_file)
        moc2 = MOC.from_json(json_moc=moc_d)
        assert moc_from_fits_image == moc2


def test_moc_write_to_fits(moc_from_fits_image):
    hdulist = moc_from_fits_image.serialize(format='fits')
    assert isinstance(hdulist, fits.hdu.hdulist.HDUList)


def test_moc_write_to_json(moc_from_fits_image):
    moc_json = moc_from_fits_image.serialize(format='json')
    assert isinstance(moc_json, dict)

def test_moc_contains():
    order = 4
    size = 20
    healpix_arr = np.random.randint(0, 12*4**order, size)
    all_healpix_arr = np.arange(12*4**order)
    healpix_outside_arr = np.setdiff1d(all_healpix_arr, healpix_arr)

    moc = MOC.from_json(json_moc={str(order): list(healpix_arr)})

    hp = HEALPix(nside=(1 << order), order='nested', frame=ICRS())
    lon, lat = hp.healpix_to_lonlat(healpix_arr)
    lon_out, lat_out = hp.healpix_to_lonlat(healpix_outside_arr)

    should_be_inside_arr = moc.contains(ra=lon, dec=lat)
    assert should_be_inside_arr.all()
    should_be_outside_arr = moc.contains(ra=lon_out, dec=lat_out)
    assert not should_be_outside_arr.any()

    # test keep_inside field
    should_be_outside_arr = moc.contains(ra=lon, dec=lat, keep_inside=False)
    assert not should_be_outside_arr.any()
    should_be_inside_arr = moc.contains(ra=lon_out, dec=lat_out, keep_inside=False)
    assert should_be_inside_arr.all()

def test_mpl_fill():
    fits_path = 'resources/P-GALEXGR6-AIS-FUV.fits'
    moc = MOC.from_fits(fits_path)

    import matplotlib
    matplotlib.use('Agg') # Disable the need of a X-server when importing matplotlib.pyplot. This gets rid of a
                          # Python 2.7 RuntimeError.

    import matplotlib.pyplot as plt
    fig = plt.figure(111, figsize=(10, 10))
    with WCS(fig,
         fov=50 * u.deg,
         center=SkyCoord(0, 20, unit='deg', frame='icrs'),
         coordsys="icrs",
         rotation=Angle(0, u.degree),
         projection="AIT") as wcs:
        ax = fig.add_subplot(1, 1, 1, projection=wcs)
        moc.fill(ax=ax, wcs=wcs, alpha=0.5, color='r')

def test_mpl_border():
    fits_path = 'resources/P-GALEXGR6-AIS-FUV.fits'
    moc = MOC.from_fits(fits_path)

    import matplotlib
    matplotlib.use('Agg') # Disable the need of a X-server when importing matplotlib.pyplot. This gets rid of a
                          # Python 2.7 RuntimeError.

    import matplotlib.pyplot as plt
    fig = plt.figure(111, figsize=(10, 10))
    with WCS(fig,
         fov=50 * u.deg,
         center=SkyCoord(0, 20, unit='deg', frame='icrs'),
         coordsys="icrs",
         rotation=Angle(0, u.degree),
         projection="AIT") as wcs:
        ax = fig.add_subplot(1, 1, 1, projection=wcs)
        moc.border(ax=ax, wcs=wcs, color='g')

def test_boundaries():
    fits_path = 'resources/P-GALEXGR6-AIS-FUV.fits'
    moc = MOC.from_fits(fits_path)
    moc = moc.degrade_to_order(6)
    boundaries_l = moc.get_boundaries()

@pytest.fixture()
def mocs():
    moc1 = {'1': [0]}
    moc1_increased = {'0': [0], '1': [17, 19, 22, 23, 35]}
    moc2 = {'1': [30]}
    moc2_increased = {'0': [7], '1': [8, 9, 25, 43, 41]}

    return dict(moc1=MOC.from_json(moc1),
                moc1_increased=MOC.from_json(moc1_increased),
                moc2=MOC.from_json(moc2),
                moc2_increased=MOC.from_json(moc2_increased))


def test_add_neighbours(mocs):
    mocs['moc1'].add_neighbours()
    assert mocs['moc1'] == mocs['moc1_increased']

    mocs['moc2'].add_neighbours()
    assert mocs['moc2'] == mocs['moc2_increased']


def test_remove_neighbours(mocs):
    mocs['moc1_increased'].remove_neighbours()
    mocs['moc2_increased'].remove_neighbours()
    assert mocs['moc1_increased'] == mocs['moc1']
    assert mocs['moc2_increased'] == mocs['moc2']


def test_neighbours(mocs):
    moc1 = copy.deepcopy(mocs['moc1'])
    moc2 = copy.deepcopy(mocs['moc2'])
    moc1.add_neighbours().remove_neighbours()
    moc2.add_neighbours().remove_neighbours()
    assert moc1 == mocs['moc1']
    assert moc2 == mocs['moc2']


def test_moc_skyfraction():
    moc = MOC.from_json({
        '0': [0, 1, 2, 3, 4, 5]
    })
    assert moc.sky_fraction == 0.5


@pytest.fixture()
def mocs_op():
    moc1 = MOC.from_json({
        '0': [0, 2, 3, 4, 5]
    })
    moc2 = MOC.from_json({
        '0': [0, 1, 7, 4, 3]
    })
    return dict(first=moc1, second=moc2)


def test_moc_union(mocs_op):
    assert mocs_op['first'].union(mocs_op['second']) == MOC.from_json({
        '0': [0, 1, 2, 3, 4, 5, 7]
    })


def test_moc_intersection(mocs_op):
    assert mocs_op['first'].intersection(mocs_op['second']) == MOC.from_json({
        '0': [0, 3, 4]
    })


def test_moc_difference(mocs_op):
    assert mocs_op['first'].difference(mocs_op['second']) == MOC.from_json({
        '0': [2, 5]
    })


def test_moc_complement():
    moc = MOC.from_fits('resources/P-GALEXGR6-AIS-FUV.fits')
    assert moc.complement().complement() == moc
