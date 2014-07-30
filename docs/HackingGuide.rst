============================
Hacking Guide for handbookof
============================

``handbookof`` has ambitious goals, which can only be
reached by incorporating contributions from the larger
community.  This document is a guide to structuring your
contributions to that they can be easily merged into the
code base.

Guiding Philosophy
==================

``handbookof`` is intended to be a repository of validated reference
information in a convenient form.  There are no pre-conceived notions
of how the information will be used in applications.
In many cases, the information is simply a table represented
as a list of namedtuples.
Data represented in this way is easy to convert to the particular needs
of the client application, often using a single list comprehension.

Consider this example where an application needs a table of tap drill
sizes for machine screws.  The machinescrews handbook defines (among
many other things) a data
table with several columns of information about metric machine screws.
In this example, the application needs a look-up table
mapping machine screw sizes onto tap drill sizes.  This can be
easily contstructed using a generator expression or list comprehension 
as follows: ::

  import handbookof.machinery.machinescrews as sc
  tap = dict((screw.size,screw.tap_drill) for screw in sc.metric_screws)

Our motto: Useful data in a Pythonic format.

License
=======

BSD

Version Numbering
=================

Versions: <Major>.<Minor><validation>

Versions are numbered with the familar <Major>.<Minor> numbering scheme.
The level of validation is reflected by a single letter suffix.
The version number applies to the entire ``handbookof`` package, there
is no separate versioning of sub-packages.

The <Minor> number increments with each validated release.  
There are *no* API or data organization changes associated with a
minor relase.  There *may* be significant additions and/or corrections,
including the addition of entirely new handbook sections.
A minor release should not break any existing use, except for code
that relies on buggy behavior in ``handbookof``.

The <Major> number increments with any release incorporating
a change to the API, or to the organization of any data tables
in any handbook.

A release in X.Y format with no suffix letter is a production
release.  A suffix letter and point release number N are appended
to releases that are not fully validated.
The suffix 'a<N>' is used for alpha releases.  Alpha releases
may not be fully tested and are under active development.
The suffix 'b<N>' is used for beta releases.  Beta releases
are snapshots of code that is freezing for release, and is only
open to stability and correctness updates.  Beta releases
have a complete test suite in the master repository and
are ready for vigorous testing by users.

Coding Standards and Guidelines
===============================

PEP8 and <project specific>.

Organization and Naming
=======================

TBW

Representing Information
========================

TBW

- Lists of namedtuples are full of goodness.
- Constructed lists of named tuples are good for naturally
  regular information.
- Minimize/eliminate redundancy.  Derivable information should
  not be explicitly listed.  This minimizes inconsistencies.

Documentation
=============

TBW

Validation
==========


TBW
