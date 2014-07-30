# Copyright (c) 2014, David B. Curtis
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

"""Unit conversions.
A conversion is defined by the namedtuple ``Conversion``, which relates
a unit of measure to the equivalent SI units.  Where a simple factor
yielding an SI value exists, it is given.  In all cases, functions to
convert to and convert from the SI units are given.  The list
``conversions`` contains instances of ``Conversion``."""

from collections import namedtuple

Dimensionality = namedtuple('Dimensionality',
    'meter kilogram second ampere kelvin mole candela')

Conversion = namedtuple('Conversion',
    'system_list unit factor_to_si function_to_si function_from_si dimensionality')

conversions = [
    Conversion(['imperial','us_customary'],'inch',0.0254,
               (lambda x:x*0.0254),(lambda x:x/0.0254),
               Dimensionality(1,0,0,0,0,0,0)),
    Conversion(['us_customary'],'yard',0.9144,
               (lambda x:x*0.9144),(lambda x:x/0.9144),
               Dimensionality(1,0,0,0,0,0,0)),
    Conversion(['us_customary'],'foot',0.3048,
               (lambda x:x*0.3048),(lambda x:x/0.3048),
               Dimensionality(1,0,0,0,0,0,0)),
    Conversion(['us_customary'],'statute_mile',1609.344,
               (lambda x:x*1609.34),(lambda x:x/1609.34),
               Dimensionality(1,0,0,0,0,0,0)),
    Conversion(['imperial','us_customary'],'pound_mass',0.45359237,
               (lambda x:x*0.453592),(lambda x:x/0.453592),
               Dimensionality(0,1,0,0,0,0,0)),
    Conversion(['metric_customary'],'celsius', None,
               (lambda x:x+273.15),(lambda x:x-273.15),
               Dimensionality(0,0,0,0,1,0,0)),
    Conversion(['us_customary'],'fahrenheit', None,
               (lambda x:(5.0/9.0)*(x-32.0)+273.15),
               (lambda x:(9.0/5.0)*(x-273.15) + 32.0),
               Dimensionality(0,0,0,0,1,0,0)),
    Conversion(['imperial','us_customary'],'acre', 4046.8564224,
               (lambda x:x*4046.8564224),(lambda x:x/4046.8564224),
               Dimensionality(2,0,0,0,0,0,0)),
    Conversion(['imperial'],'gallon', 0.00454609,
               (lambda x:x*0.00454609),(lambda x:x/0.00454609),
               Dimensionality(3,0,0,0,0,0,0)),
    Conversion(['us_constomary'],'gallon', 0.003785411784,
               (lambda x:x*0.003785411784),(lambda x:x/0.003785411784),
               Dimensionality(3,0,0,0,0,0,0)),
    Conversion(['us_constomary'],'dry_gallon', 0.00440488377086,
               (lambda x:x*0.00440488377086),(lambda x:x/0.00440488377086),
               Dimensionality(3,0,0,0,0,0,0)),
]

if __name__ == '__main__':
    pass
