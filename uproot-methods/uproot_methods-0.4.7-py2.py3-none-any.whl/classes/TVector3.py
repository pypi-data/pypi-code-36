#!/usr/bin/env python

# Copyright (c) 2019, IRIS-HEP
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import math
import numbers

import awkward.array.jagged

import uproot_methods.base
import uproot_methods.common.TVector

class Common(object):
    def dot(self, other):
        out = self.x*other.x
        out = out + self.y*other.y
        out = out + self.z*other.z
        return out

    def _cross(self, other):
        return (self.y*other.z - self.z*other.y,
                self.z*other.x - self.x*other.z,
                self.x*other.y - self.y*other.x)

    @property
    def cottheta(self):
        out = self.rho
        out /= self.z
        return out

    def _rotate_axis(self, axis, angle):
        u = axis.unit
        c = self.awkward.numpy.cos(angle)
        s = self.awkward.numpy.sin(angle)
        c1 = 1 - c

        x = (c + u.x**2 * c1) * self.x + (u.x * u.y * c1 - u.z * s) * self.y + (u.x * u.z * c1 + u.y * s) * self.z
        y = (u.x * u.y * c1 + u.z * s) * self.x + (c + u.y**2 * c1) * self.y + (u.y * u.z * c1 - u.x * s) * self.z
        z = (u.x * u.z * c1 - u.y * s) * self.x + (u.y * u.z * c1 + u.x * s) * self.y + (c + u.z**2 * c1) * self.z

        return x, y, z

    def _rotate_euler(self, phi, theta, psi):
        # Rotate Z (phi)
        c1 = self.awkward.numpy.cos(phi)
        s1 = self.awkward.numpy.sin(phi)
        c2 = self.awkward.numpy.cos(theta)
        s2 = self.awkward.numpy.sin(theta)
        c3 = self.awkward.numpy.cos(psi)
        s3 = self.awkward.numpy.sin(psi)

        # Rotate Y (theta)
        fzx2 = -s2*c1
        fzy2 =  s2*s1
        fzz2 =  c2

        # Rotate Z (psi)
        fxx3 =  c3*c2*c1 - s3*s1
        fxy3 = -c3*c2*s1 - s3*c1
        fxz3 =  c3*s2
        fyx3 =  s3*c2*c1 + c3*s1
        fyy3 = -s3*c2*s1 + c3*c1
        fyz3 =  s3*s2

        # Transform v
        x = fxx3*self.x + fxy3*self.y + fxz3*self.z
        y = fyx3*self.x + fyy3*self.y + fyz3*self.z
        z = fzx2*self.x + fzy2*self.y + fzz2*self.z

        return x, y, z

    def rotatex(self, angle):
        return self.rotate_axis(TVector3(1.0, 0.0, 0.0), angle)

    def rotatey(self, angle):
        return self.rotate_axis(TVector3(0.0, 1.0, 0.0), angle)

    def rotatez(self, angle):
        return self.rotate_axis(TVector3(0.0, 0.0, 1.0), angle)

class ArrayMethods(Common, uproot_methods.common.TVector.ArrayMethods, uproot_methods.base.ROOTMethods):
    def _initObjectArray(self, table):
        self.awkward.ObjectArray.__init__(self, table, lambda row: TVector3(row["fX"], row["fY"], row["fZ"]))

    def __awkward_persist__(self, ident, fill, prefix, suffix, schemasuffix, storage, compression, **kwargs):
        self._valid()
        x, y, z = self.x, self.y, self.z
        return {"id": ident,
                "call": ["uproot_methods.classes.TVector3", "TVector3Array", "from_cartesian"],
                "args": [fill(x, "TVector3Array.x", prefix, suffix, schemasuffix, storage, compression, **kwargs),
                         fill(y, "TVector3Array.y", prefix, suffix, schemasuffix, storage, compression, **kwargs),
                         fill(z, "TVector3Array.z", prefix, suffix, schemasuffix, storage, compression, **kwargs)]}

    @property
    def x(self):
        return self["fX"]

    @property
    def y(self):
        return self["fY"]

    @property
    def z(self):
        return self["fZ"]

    def cross(self, other):
        x, y, z = self._cross(other)
        out = self.empty_like()
        out["fX"] = x
        out["fY"] = y
        out["fZ"] = z
        return out

    @property
    def theta(self):
        return self.awkward.numpy.arctan2(self.rho, self.z)

    def rotate_axis(self, axis, angle):
        x, y, z = self._rotate_axis(axis, angle)
        out = self.empty_like()
        out["fX"] = x
        out["fY"] = y
        out["fZ"] = z
        return out

    def rotate_euler(self, phi=0, theta=0, psi=0):
        x, y, z = self._rotate_euler(phi, theta, psi)
        out = self.empty_like()
        out["fX"] = x
        out["fY"] = y
        out["fZ"] = z
        return out

    def sum(self):
        if isinstance(self, self.awkward.JaggedArray):
            return TVector3Array.from_cartesian(self.x.sum(), self.y.sum(), self.z.sum())
        else:
            return TVector3(self.x.sum(), self.y.sum(), self.z.sum())

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if "out" in kwargs:
            raise NotImplementedError("in-place operations not supported")

        if method != "__call__":
            return NotImplemented

        inputs = list(inputs)
        for i in range(len(inputs)):
            if isinstance(inputs[i], self.awkward.numpy.ndarray) and inputs[i].dtype == self.awkward.numpy.dtype(object) and len(inputs[i]) > 0:
                idarray = self.awkward.numpy.frombuffer(inputs[i], dtype=self.awkward.numpy.uintp)
                if (idarray == idarray[0]).all():
                    inputs[i] = inputs[i][0]

        if ufunc is self.awkward.numpy.add or ufunc is self.awkward.numpy.subtract:
            if not all(isinstance(x, (ArrayMethods, Methods)) for x in inputs):
                raise TypeError("(arrays of) TVector3 can only be added to/subtracted from other (arrays of) TVector3")
            out = self.empty_like()
            out["fX"] = getattr(ufunc, method)(*[x.x for x in inputs], **kwargs)
            out["fY"] = getattr(ufunc, method)(*[x.y for x in inputs], **kwargs)
            out["fZ"] = getattr(ufunc, method)(*[x.z for x in inputs], **kwargs)
            return out

        elif ufunc is self.awkward.numpy.power and len(inputs) >= 2 and isinstance(inputs[1], (numbers.Number, self.awkward.numpy.number)):
            if inputs[1] == 2:
                return self.mag2
            else:
                return self.mag2**(0.5*inputs[1])

        elif ufunc is self.awkward.numpy.absolute:
            return self.mag

        else:
            return super(ArrayMethods, self).__array_ufunc__(ufunc, method, *inputs, **kwargs)

class Methods(Common, uproot_methods.common.TVector.Methods, uproot_methods.base.ROOTMethods):
    _arraymethods = ArrayMethods

    @property
    def x(self):
        return self._fX

    @property
    def y(self):
        return self._fY

    @property
    def z(self):
        return self._fZ

    def __repr__(self):
        return "TVector3({0:.5g}, {1:.5g}, {2:.5g})".format(self.x, self.y, self.z)

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        return isinstance(other, Methods) and self.x == other.x and self.y == other.y and self.z == other.z

    def _scalar(self, operator, scalar, reverse=False):
        if not isinstance(scalar, (numbers.Number, self.awkward.numpy.number)):
            raise TypeError("cannot {0} a TVector3 with a {1}".format(operator.__name__, type(scalar).__name__))
        if reverse:
            return TVector3(operator(scalar, self.x), operator(scalar, self.y), operator(scalar, self.z))
        else:
            return TVector3(operator(self.x, scalar), operator(self.y, scalar), operator(self.z, scalar))

    def _vector(self, operator, vector, reverse=False):
        if not isinstance(vector, Methods):
            raise TypeError("cannot {0} a TVector3 with a {1}".format(operator.__name__, type(vector).__name__))
        if reverse:
            return TVector3(operator(vector.x, self.x), operator(vector.y, self.y), operator(vector.z, self.z))
        else:
            return TVector3(operator(self.x, vector.x), operator(self.y, vector.y), operator(self.z, vector.z))

    def _unary(self, operator):
        return TVector3(operator(self.x), operator(self.y), operator(self.z))

    def cross(self, other):
        x, y, z = self._cross(other)
        return TVector3(x, y, z)

    @property
    def theta(self):
        return math.atan2(self.rho, self.z)

    def rotate_axis(self, axis, angle):
        x, y, z = self._rotate_axis(axis, angle)
        return TVector3(x, y, z)

    def rotate_euler(self, phi=0, theta=0, psi=0):
        return TVector3(x, y, z)

class TVector3Array(ArrayMethods, uproot_methods.base.ROOTMethods.awkward.ObjectArray):
    jaggedtype = uproot_methods.base.ROOTMethods.awkward.JaggedArray
    awkcls = ArrayMethods.mixin(ArrayMethods, jaggedtype)

    def __init__(self, x, y, z):
        if isinstance(x, awkward.array.jagged.JaggedArray) or isinstance(y, awkward.array.jagged.JaggedArray) or isinstance(z, awkward.array.jagged.JaggedArray):
            raise TypeError("TVector3Array constructor arguments must not be jagged; use TVector3.from_cartesian for jaggedness-handling")
        self._initObjectArray(self.awkward.Table())
        self["fX"] = x
        self["fY"] = y
        self["fZ"] = z

    @classmethod
    def origin(cls, shape, dtype=None):
        if dtype is None:
            dtype = cls.awkward.numpy.float64
        return cls(cls.awkward.numpy.zeros(shape, dtype=dtype),
                   cls.awkward.numpy.zeros(shape, dtype=dtype),
                   cls.awkward.numpy.zeros(shape, dtype=dtype))

    @classmethod
    def origin_like(cls, array):
        return array * 0.0

    @classmethod
    def from_cartesian(cls, x, y, z):
        wrap, (x, y, z) = cls._unwrap_jagged(cls.awkcls, cls._normalize_arrays((x, y, z)))
        return wrap(cls(x, y, z))

    @classmethod
    def from_spherical(cls, r, theta, phi):
        wrap, (r, theta, phi) = cls._unwrap_jagged(cls.awkcls, cls._normalize_arrays((r, theta, phi)))
        return wrap(cls(r * cls.awkward.numpy.sin(theta) * cls.awkward.numpy.cos(phi),
                        r * cls.awkward.numpy.sin(theta) * cls.awkward.numpy.sin(phi),
                        r * cls.awkward.numpy.cos(theta)))

    @classmethod
    def from_cylindrical(cls, rho, phi, z):
        wrap, (rho, phi, z) = cls._unwrap_jagged(cls.awkcls, cls._normalize_arrays((rho, phi, z)))
        return wrap(cls(rho * cls.awkward.numpy.cos(phi),
                        rho * cls.awkward.numpy.sin(phi),
                        z))

    @property
    def x(self):
        return self["fX"]

    @x.setter
    def x(self, value):
        self["fX"] = value

    @property
    def y(self):
        return self["fY"]

    @y.setter
    def y(self, value):
        self["fY"] = value

    @property
    def z(self):
        return self["fZ"]

    @z.setter
    def z(self, value):
        self["fZ"] = value

class TVector3(Methods):
    def __init__(self, x, y, z):
        self._fX = float(x)
        self._fY = float(y)
        self._fZ = float(z)

    @classmethod
    def origin(cls):
        return cls(0.0, 0.0, 0.0)

    @classmethod
    def from_spherical(cls, r, theta, phi):
        return cls(r * math.sin(theta) * math.cos(phi),
                   r * math.sin(theta) * math.sin(phi),
                   r * math.cos(theta))

    @classmethod
    def from_cylindrical(cls, rho, phi, z):
        return cls(rho * math.cos(phi),
                   rho * math.sin(phi),
                   z)

    @property
    def x(self):
        return self._fX

    @x.setter
    def x(self, value):
        self._fX = value

    @property
    def y(self):
        return self._fY

    @y.setter
    def y(self, value):
        self._fY = value

    @property
    def z(self):
        return self._fZ

    @z.setter
    def z(self, value):
        self._fZ = value
