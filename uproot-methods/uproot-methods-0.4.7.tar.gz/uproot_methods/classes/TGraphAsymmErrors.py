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

import uproot_methods.base

class Methods(uproot_methods.base.ROOTMethods):
	
	@property
	def xerrorshigh(self):
		return self._fEXhigh
		
	@property
	def xerrorslow(self):
		return self._fEXlow
		
	@property
	def yerrorshigh(self):
		return self._fEYhigh
		
	@property
	def yerrorslow(self):
		return self._fEYlow
		
	def matplotlib(self, showtitle=True, show=False, **kwargs):
		import matplotlib.pyplot as pyplot
		
		_xerrs = [self.xerrorslow, self.xerrorshigh]
		_yerrs = [self.yerrorslow, self.yerrorshigh]

		_xlabel = _decode(self.xlabel if self.xlabel is not None else "")
		_ylabel = _decode(self.ylabel if self.ylabel is not None else "")
		
		pyplot.errorbar(self.xvalues, self.yvalues, xerr=_xerrs, yerr=_yerrs, **kwargs)
		pyplot.xlabel(_xlabel)
		pyplot.ylabel(_ylabel)
		if showtitle:
			_title = _decode(self.title)
			pyplot.title(_title)
			
		if show:
			pyplot.show()
			
def _decode(sequence):
	return sequence.decode() if isinstance(sequence, bytes) else sequence
