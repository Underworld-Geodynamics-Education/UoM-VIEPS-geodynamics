# Introduction to Geodynamics

We will begin the course by thinking about the observations allow us to develop a quantitative understanding of large-scale geodynamics. Of particular interest is the relationship between convection in the deep Earth and the surface expression of this circulation in the form of plate tectonics.

We will discuss how we use geology, geodesy, seismology, model building (mathematical and computational), to understand how Earth works at this scale.

In order to explore how global geodynamics works, we will be using the computational modeling tool `underworld` which is one of the research codes written by (predominantly) the University of Melbourne and Monash University geodynamics groups.

## Introduction to Underworld

First of all we will work through some hands-on tutorials to build up a general understanding of the way the underworld code works, how its concepts are expressed in python, and how to run the given examples.

The underworld manual/tutorial is split into three parts:

  - The <a href="/notebooks/Introduction/user_guide"> user guide </a> takes you
    through various aspects of the code such as building a mesh, adding variables (unknowns to be solved),
    equation solvers, using tracers to track information and so on.
    You might find it helpful to work your way through
    these notebooks before trying to do any of the problem sets.

  - The <a href="/notebooks/Introduction/examples"> examples </a> show you how to solver certain
    problems by combining all of the elements of underworld which were touched upon in the _user guide_.
    These generally progress from simple to complicated and from trivial examples to the template problems
    which lead to many geodynamics research areas. You will find these a useful template for the
    exercises as there is a convection example, a buoyancy-driven instability example, and an
    extension modeling case.

  - The <a href="/notebooks/Introduction/publications"> publications </a> notebooks show how to reproduce
    the results from specific papers. These include "standard" benchmark cases to show the code is working
    and some examples where underworld was used in research papers. At the moment, this directory is a little
    bare !
