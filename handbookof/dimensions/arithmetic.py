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

"""Dimensioned numbers with units arithmetic."""
#FIXME: Complete the module-level doc string.


# FIXME: Should allow unicode characters in unit definition for
# things like mu and omega.  --> Do this on Python3 conversion?

from numbers import Number
from collections import namedtuple
import re


# FIXME: Do dimension exponents need to be rationals??????
# FIXME: the list of measureables needs to be more inclusive, and checked
#  at dimension instantiation time.  Or maybe should be a dictionary that
#  accumulates definitions.

# FIXME: perhaps a dict of <measureable>:(system, unit).  Build as definitions
# are instantiated.
_measureable = ['length', 'mass', 'time', 'charge', 'electric_current',
                'luminousity', 'temperature', 'amount_of_substance', 'angle']


class GenericRoot(object):
    def __repr__(self):
        s = self.__class__.__name__ + '('
        s += ','.join([repr(x) for x in self.reprvals()])
        s += ')'
        return s
    def reprvals(self):
        return []
    def must_be(self, a_class):
        if isinstance(self, a_class):
            return self
        raise TypeError(''.join(['Expected ',a_class]))
    
class UnitDef(GenericRoot):
    def __init__(self, name, abbreviation, display_order):
        self.name = name
        self.abbreviation = abbreviation
        self.display_order = display_order        

# FIXME: BaseUnitDef's should have a dimension property associated with
# them after they are put in the _udict dictionary of a DimensionSystem.
# This needs to happen late in __init__ for DimensionSystem.
# Then parse_dimension_exp can be considerably simplified.
class BaseUnitDef(UnitDef):
    def __init__(self, name, abbreviation, display_order, unit_index):
        UnitDef.__init__(self, name, abbreviation, display_order)
        self.unit_index = unit_index
    def reprvals(self):
        return [self.name, self.abbreviation, self.display_order,
                self.unit_index]

class DerivedUnitDef(UnitDef):
    def __init__(self, name, abbreviation, display_order, dimension):
        UnitDef.__init__(self, name, abbreviation, display_order)
        self.dimension = dimension
    def reprvals(self):
        return [self.name, self.abbreviation, self.display_order,
                self.dimension]

UnitDisplayKey = namedtuple('UnitDisplayKey', 'exponent_index abbreviation')

class Scalar(GenericRoot):
    def __init__(self, factor, prefix=''):
        self.factor = factor
        self.prefix = prefix
    def reprvals(self):
        t = [self.factor]
        if prefix:
            t.append(self.prefix)
        return t
    def __eq__(self, other):
        return self.prefix == other.prefix and self.factor == other.factor
    def __ne__(self, other):
        return self.prefix != other.prefix or self.factor != other.factor
    def __mul__(self, other):
        return self.__class__(self.factor * other.factor)
                 
class Dimension(GenericRoot):
    def __init__(self, unit_spec=None, **kwargs):
        if isinstance(unit_spec,Dimension):
            self._exponents = unit_spec._exponents
            return
        if isinstance(unit_spec,list):
            if len(unit_spec) != len(self._system._base_unit_order):
                raise ValueError('Wrong number of unit exponents.')
            self._exponents = [int(x) for x in unit_spec]
            return
        elif isinstance(unit_spec,str):
            kwargs = self.__class__.parse(unit_spec)
        valid_kwargs = self._system._base_unit_set
        valid_kwargs.add('scalar')
        for p in kwargs:
            if p not in valid_kwargs:
                raise ValueError(p + ' not a base unit.')
        self._exponents = []
        for name in self._system._base_unit_order:
            try:
                self._exponents.append(kwargs[name])
            except:
                self._exponents.append(0)
        try:
            self.scalar = kwargs['scalar']
        except KeyError:
            self.scalar = None
    def reprvals(self):
        return self._exponents
    def __str__(self):
        # FIXME: This doesn't handle partial simplifications.
        try:
            return self._system._derived_units[tuple(self._exponents)].abbreviation
        except KeyError:
            num,denom = [],[]
            for index, abbr in self._system.display_key:
                exp = self._exponents[index]
                if exp > 0:
                    s = abbr
                    if exp > 1:
                        s += '^' + str(exp)
                    num.append(s)
                if exp < 0:
                    s = abbr
                    if exp < -1:
                        s += '^' + str(-exp)
                    denom.append(s)
            s = '-'.join(num) if num else '1'
            if denom:
                s += '/'
                s += '-'.join(denom)
            return s
    def simple(self):
        "Returns (str, scale) for a complex unit."
        pass
    # FIXME: All arith must now check scalar, too.
    def __mul__(self, other):
        if self._system != other._system:
            raise ConversionError
        return self.__class__([x+y for x,y in
                zip(self._exponents,other._exponents)])
    def __div__(self, other):
        if self._system != other._system:
            raise ConversionError
        return self.__class__([x-y for x,y in
                zip(self._exponents,other._exponents)])
    def __add__(self, other):
        if self._system != other._system:
            raise ConversionError
        if min([x==y for x,y in zip(self._exponents, other._exponents)]):
            return self
        raise TypeError('Adding mismatched units.')
    def __sub__(self, other):
        if self._system != other._system:
            raise ConversionError
        if min([x==y for x,y in zip(self.uexp, other.uexp)]):
            return self
        raise TypeError('Subtracting mismatched units.')
    def __eq__(self, other):
        return self.__class__ == other.__class__ \
               and min(se == oe for se,oe in
                       zip(self._exponents, other._exponents))
    # FIXME: add other operations
        

class DimensionSystem(object):
    "Creates a dimension system and a Dimension sub-class for it."
    _implied_system={}
    _named={}
    def __init__(self, name, dimension_class_name, dimensions):
        if not set(dimensions.keys()).issubset(set(_measureable)):
            raise ValueError('Extra dimensions.')
        self.name = name
        self._spec = dimensions
        self._prefixed_units = {}
        self._name_from_abbr = dict([(unit.abbreviation, unit.name)
                                     for unit in self._spec.values()])
        self._udict=dict([(unit.name,unit) for unit in self._spec.values()])
        t = [(unit.abbreviation, unit) for unit in self._spec.values()]
        self._udict.update(t)
        for abbr,_ in t:
            self.__class__.abbr_implies(abbr, self)
        t = sorted([(u.unit_index, u.name)
            for u in self._spec.values()])
        self._base_unit_order = [unit_name for _,unit_name in t]
        self._base_unit_set = set(self._base_unit_order)
        t = sorted([(u.display_order, u.unit_index, u.abbreviation)
                    for u in self._spec.values()])
        self.display_key = [(base_order, abbr) for _,base_order,abbr in t] 
        self._derived_units = {}
        self._dimclass = type(dimension_class_name, (Dimension,),{})
        setattr(self._dimclass, '_system', self)
        self.__class__._named[name] = self
        self.derive('dimensionless','(dimensionless)','',9999)
        globals()[dimension_class_name] = self._dimclass
        setattr(self.__class__, name, self)
        globals()[name + '_system'] = self
    def __repr__(self):
        return self.name + '_system'
    def derive(self, measureable, name, abbreviation, display_order, **kwargs):
        basis = self._dimclass(**kwargs)
        unit = DerivedUnitDef(name, abbreviation, display_order, basis)
        self._spec[measureable] = unit
        t = tuple(basis._exponents)
        self._derived_units[t] = unit
        self._udict[name] = unit
        self._udict[abbreviation] = unit
        self._name_from_abbr[abbreviation] = name
        self.__class__.abbr_implies(abbreviation, self)
    def apply_prefix(self, prefix, scale_factor, applies_to):
        for unit in applies_to:
            prefixed_unit = prefix + unit
            unit_def = self._udict[unit]
            unit_def.scalar = unit_def.scaler * Scalar(scale_factor)
            self._prefixed_units[prefixed_unit] = (unit_def)
    @classmethod
    def abbr_implies(cls, abbreviation, system):
        try:
            cls._implied_system[abbreviation].append(system)
        except KeyError:
            cls._implied_system[abbreviation] = [system]
    @classmethod
    def parse(cls, a_str):
        """Returns a tuple of (Dimension, remaining_str).
        Might be (None, a_str) if nothing found."""
        a_str = a_str.lstrip() # consume white space
        m = re.match('([a-z]+):',a_str) # look for <system>:
        if m:
            sys = m.group(1)
            a_str = a_str[len(m.group(0)):]
        else:
            sys = None
            # Try to infer system.
        m = re.match('[a-zA-Z]+',a_str)
        if m:
            unit = m.group(0)
        else:
            return (None, a_str)
        try:
            syslist = [cls._named[sys]] if sys else cls._implied_system[unit]
        except KeyError:
            raise ValueError('Unrecognized unit.')
        if len(syslist) > 1:
            raise ValueError('Ambiguous. Unit found in multiple systems.')
        system = syslist[0]
        unit, remainder = system.parse_dimension_exp(a_str)
        return (unit, remainder)
    def parse_dimension_exp(self, a_str):
        "Returns a Dimension instance from a string dimension expression."
        #FIXME: This is a cheezy parser with no error checking.
        # [<prefix>] unit [^ <exp>] {- [<prefix>] unit [^ <exp> } [ / <denom> ]
        ul = []
        for state in ['num','denom']:
            m = re.match('[a-zA-Z]+',a_str)
            while m:
                u,exp = m.group(0),1 if state == 'num' else -1
                a_str = a_str[len(u):]
                if a_str and a_str[0] == '^':
                    a_str = a_str[1:]
                    m = re.match('\d',a_str)
                    exp = int(m.group(0))
                    exp = exp if state == 'num' else -exp
                    a_str = a_str[len(m.group(0)):]
                ul.append((u,exp))
                m = re.match('-',a_str)
                if m:
                    a_str = a_str[1:]
                    m = re.match('[a-zA-Z]+',a_str)
            m = re.match('/',a_str)
            if m:
                a_str = a_str[1:]
        accum = self._udict['(dimensionless)'].dimension
        for abbr,exp in ul:
            try:
                unit_def = self._prefixed_units[abbr]
            except KeyError:
                unit_name = self._name_from_abbr[abbr]
                if unit_name in self._base_unit_set:
                    kw = {unit_name:exp}
                    unit_def = self._dimclass(**kw)
                else:
                    unit_def = self._udict[unit_name].dimension
            accum *= unit_def
        return (accum, a_str)
    def unit_for(self, measureable):
        return self._spec[measureable]
    def __getitem__(self, key):
        return self._udict[key]
    @property
    def base_unit_order(self):
        return self._base_unit_order # FIXME: Maybe copy here??
    
DimensionSystem('si','SIDimension',{
        'length':               BaseUnitDef('meter',   'm',  20, 0),
        'mass':                 BaseUnitDef('kilogram','kg', 10, 1),
        'time':                 BaseUnitDef('second',  's',  30, 2),
        'electric_current':     BaseUnitDef('ampere',  'A',  40, 3),
        'temperature':          BaseUnitDef('kelvin',  'K',  50, 4),
        'amount_of_substance':  BaseUnitDef('mole',    'mol',60, 6),
        'luminousity':          BaseUnitDef('candela', 'cd', 70, 6),
        'angle':                BaseUnitDef('radian',  'rad',80, 7),
    }
)
si_system.derive('charge','coulomb','C',90,second=1,ampere=1)
si_system.derive('force','newton','N',5,meter=1,kilogram=1,second=-2)
si_system.derive('pressure','pascal','Pa',25,meter=-1,kilogram=1,second=-2)
si_system.derive('energy','joule','J',23,meter=2,kilogram=1,second=-2)
si_system.derive('power','watt','W',28,meter=2,kilogram=1,second=-3)
si_system.derive('frequency','hertz','Hz',45,second=-1)
si_system.derive('volume','liter','L',24,meter=3,scalar=Scalar(0.001))
                 
                          
# FIXME: Handle conversion errors from dimension arithmetic.
class Dn(object):
    "Dimensioned number. Has: value, dimension, & optionally preferred display units."
    def __init__(self, *args):
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, str):
                self.v, self.dim = self.__class__.parse(args[0])
                self.ddim = None
            elif isinstance(arg, Dn):
                self.v = arg.v
                self.dim = arg.dim
                self.ddim = arg.ddim
            else:
                raise ValueError('Ambiguous dimensionality.')
        elif len(args) in [2,3]:
            self.v = args[0]
            self.dim = args[1]
            self.ddim = args[2] if len(args) == 3 else None
        else:
            raise TypeError(''.join(['Can not convert ', repr(args), ' to dimensioned number.']))
    @property
    def v(self):
        return self._v
    @v.setter
    def v(self,v):
        if isinstance(v,Number):
            self._v = v
        else:
            try:
                self._v = int(v)
                return
            except TypeError:
                pass
            try:
                self._v = float(v)
                return
            except TypeError:
                pass
            self._v = complex(v)
    @property
    def dim(self):
        return self._dim
    @dim.setter
    def dim(self, v):
        self._dim = v.must_be(Dimension)
    @property
    def ddim(self):
        return self._dim
    @ddim.setter
    def ddim(self, v):
        self._ddim = v if v is None else v.must_be(Dimension)
    @classmethod
    def parse(self, s):
        s = s.lstrip()
        m = re.match('(\d+)(\.)?(\d*)j?', s)
        if m:
            vs = m.group(0)
            s = s[len(vs):]
            d,_ = DimensionSystem.parse(s)       
            return vs, d
        return None,None
    def __repr__(self):
        s = self.__class__.__name__ + '('
        s += ','.join([repr(x) for x in [self.v, self.dim, self.ddim]])
        s += ')'
        return s
    def __str__(self):
        s = str(self.v)+str(self.ddim) # FIXME: ignores prefered display unit.
        return s
    def __mul__(self, other):
        return self.__class__(self.v * other.v, self.dim * other.dim, self.ddim)
    def __div__(self, other):
        return self.__class__(self.v / other.v, self.dim / other.dim, self.ddim)
    def __eq__(self, other):
        return self.v == other.v and self.dim == other.dim
    def __ne__(self, other):
        return self.v != other.v or self.dim != other.dim

if __name__ == '__main__':
    pass

