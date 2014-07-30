==========
handbookof
==========

``hadbookof`` is based on a very simple idea: Useful data in Pythonic format.

After the Nth time of creating a table of tap drills, or machine screw diameters, or whatnot,
I decided it was time to do generic reference modules that could be validated and put in a package.
From that germ of an idea, the concept of collecting general reference data into a
Python module took root.

Underneath ``handbookof`` there are sub-packages for various areas of knowledge.
Inside those sub-packages, there are modules for a specific category of knowledge.
For example: ::

  import handbookof.mechanics.machinescrews as sc

brings in useful data and formulas related to machine screws.
Making an application-specific table is a simple generator expression: ::

  tap = dict((screw.size,screw.tap_drill) for screw in sc.metric_screws)
  print tap[3.0]
  2.5

The ultimate aim is the creation of a handy collection of reference data and formulas that can
be relied upon for solving real-world problems, especially in CAD and CAM,
allowing you to concentrate on your goals, not on transcribing encyclopedias.

It goes without saying that a module like ``hadnbookof`` will never be done. 
There is always something more that could be added, and no single person
could ever catalog and organize it all.  
Contributions to ``handbookof`` are most welcome.

``handbookof`` is BSD licensed.

Table of Contents
+++++++++++++++++

- dimensions

  - arithmetic -- Dimensioned numbers with automated unit analysis.
  - conversions -- Unit conversions.

- electronics

  - resistors -- Standard value series and utilities.

- mechanics

  - machine screws  -- Metric and ANSI machine screw data.

