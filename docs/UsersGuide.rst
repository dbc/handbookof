=======================
handbookof User's Guide
=======================

Should be written some day.

Contents of handbookof
======================

FIXME: Insert internal links here.

handbookof.dimensions
---------------------

Measurement, dimensions, conversions.

handbookof.dimensions.arithmetic
................................

Provides numbers that carry along units of measure.  
Arithmetic does automatic units analysis. Example: ::

  In [1]: import handbookof.dimensions.arithmetic as ar
  In [2]: a = ar.Dn('2m')
  In [3]: b = ar.Dn('3m')
  In [4]: print a*b
  6m^2

handbookof.electronics
----------------------

Electronics and related information.

handbookof.electronics.resistors
................................

Standard resistor series tables and resistor utilities.

handbookof.machinery
--------------------

Mechanical engineering reference data.

handbookof.machinery.machinescrews
..................................

Data tables for metric and ASME machine screws. Example: ::

  In [1]: import handbookof.machinery.machinescrews as sc
  In [2]: tap = dict((screw.size,screw.tap_drill) for screw in sc.metric_screws )
  In [3]: print tap[3.0]
  2.5


Usage Idioms and Examples
=========================

Illustratitive examples.

Constructing Look-Up Table Dictionaries
---------------------------------------

TBW

Use generators where possible, instead of list comprehensions.

Generating Optimized Modules
----------------------------

For those that don't want to pull in a lot of handbook stuff.

Creating a Static Module From a Handbook
........................................

Minimum module.  Staticly defined at packaging time.

Creating a Module at Install-Time
.................................

Give an example of a setup.py command to build a module from
a handbook dictionary.
