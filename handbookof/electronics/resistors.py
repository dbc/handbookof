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

"""Tables and utilities for resistors.
Table of the 5,10, and 20 percent tolerance standard resistor series.
Table of resistor color codes, including hex RGB value.
Value-to-color translation function.
Function to chose nearest standard value."""

from collections import namedtuple

# Standard resistor values, and series they are part of.
StdResistor = namedtuple('StdResistor','value series_list')

ResistorColorCode = namedtuple('ResistorColorCode','digit color_name hex_color')

_tens = [1,10,100,1000,10000,100000]
_ser20 = [1, 1.5, 2.2, 3.3, 4.7, 6.8]
_ser10 = [1.2, 1.8, 2.7, 3.9, 5.6, 8.2]
_ser05 = [1.1, 1.3, 1.6, 2.0, 2.4, 3.0, 3.6, 4.3, 5.1, 6.2, 7.5, 9.1]

standard_resistor_series = [StdResistor(int(x*s) if x*s >= 10.0
                                        else x*s,[20,10,5])
                            for x in _tens for s in _ser20]
standard_resistor_series.append([StdResistor(10000000,[20,10,5])])
standard_resistor_series.extend([StdResistor(int(x*s) if x*s >= 10.0
                                        else x*s,[10,5])
                            for x in _tens for s in _ser10])
standard_resistor_series.extend([StdResistor(int(x*s) if x*s >= 10.0
                                        else x*s,[5])
                            for x in _tens for s in _ser05])
standard_resistor_series.sort()


resistor_color_code_list = [
    ResistorColorCode(0,'Black','#000000'),
    ResistorColorCode(1,'Brown','#993300'),
    ResistorColorCode(2,'Red','#FF0000'),
    ResistorColorCode(3,'Orange','#FF6600'),
    ResistorColorCode(4,'Yellow','#FFFF00'),
    ResistorColorCode(5,'Green','#0000FF'),
    ResistorColorCode(6,'Blue','#00FF00'),
    ResistorColorCode(7,'Violet','#CC00FF'),
    ResistorColorCode(8,'Gray','#909090'),
    ResistorColorCode(9,'White','#FFFFFF'),
    ResistorColorCode(-1,'Gold','#FFD700'),
    ResistorColorCode(-2,'Silver','#C0C0C0'),
]

resistor_color_code_dictionary = dict([
    (str(digit),color) for digit,color,_ in resistor_color_code_list])

def resistor_colors(v):
    if v >= 10.0:
        t = '{0:10.0f}'.format(float(v)).strip()
        z = str(len(t) - 2)
        c1,c2 = t[0:2]
    elif v >= 1.0:
        t = '{0:2.1f}'.format(float(v)).strip()
        c1,c2,z = t[0],t[2],'-1'
    else:
        t = '{0:3.2f}'.format(float(v)).strip()
        c1,c2,z = t[2],t[3],'-2'
    return (resistor_color_code_dictionary[c1],
            resistor_color_code_dictionary[c2],
            resistor_color_code_dictionary[z])

def nearest_value(desired, series):
    if series not in [5,10,20]:
        raise ValueError('Series must be one of 5,10,20 percent.')
    lower,upper = None,None
    for value, included in standard_resistor_series:
        if lower is None:
            if series in included:
                lower = value
        else:
            if value < desired and series in included:
                lower = value
            elif series in included:
                upper = value
                break
    return lower if upper is None or abs(desired-lower) < abs(desired-upper)\
           else upper

if __name__ == '__main__':
    nv = nearest_value(5364, 20)
    print nv, resistor_colors(nv)
