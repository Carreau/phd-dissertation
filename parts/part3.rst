.. Actin Cloud:

Actin Cloud
###########
.. 1

Introduction 
*************
.. 2


We have seen previously that the actin cytoskeleton play a major role in
cellular mechanics in many domains. It is necessary for force generation, and a
key component to cell motility. It has also be extensively studied both in
cells and biomimetic systems. 

Actin can for a variety of network in cell, ranging from dense branch network
at the leading Edge of the lamelipodia to bundled parallel structure forming
the filopodia.  Reconstruction of actin network have been done in biomimetic
systems using purified component, and many properties of these network have
been measured.

It has been determined that the actin cortex is  a mechanical support for the
plasma membrane and that it extend over a few hundreds of nanometers. Many
cells processes also hint for actin structure connected to this cortex that are
key elements to organelle and chromosome positioning. 

In this part of the manuscript we investigate how a sparse actin structure can
emanate from the actin cortex, and what its properties are. Using a biomimetic
system to reconstitute the actin cortex and its dendritic structure on bead, we
show that from the cortex emanate a network of filaments that have mechanical
effect up to tens of micrometers from the actin cortex.

The branched structure of the actin cortex underneath the plasma membrane of of
cell hint for a structure governed by Arp2/3. How Arp2/3 and CP can be used to
form a biomimetic actin cortex has been studied. In :cite:`Kawska2012`, both in
vitro measurement on reconstituted actin cortex on bead as well as simulation
investigate the effect of cross linking and capping on the formed gel. They can
see both experimentally ad in simulation that a network of filament escape from
what is defined as the active cortex. The effect of these long filament is not
take into account in the in-silica system where measurement is restricted to
filament shorter than 10 µm. Only the effect of dense entangle actin network
generated from primers randomly placed  on the bead surface participate in the
increase of tension and contribute to symmetry breaking.

.. figure:: /figs/Bead-tirf-fluo-sim.png
    :width: 70%

    Upper Left : Fluorescence image of a actin bead with a growing actin
    cortex. Escaping filament can difficultly be seen. Scale bar is 2 µm. Lower
    Left: Tiff image of actin polymerising on an actin bead.Escaping filament
    can be seen. Gray circle  overladed to represent the size of the bead.
    Right : Representation of the actin growth simulation with delimitation
    between entangled branched actin network and escaping filaments. 
    Adapted from :cite:`Kawska2012`


The limit of the dense network visible in epifluorescence is defined in
:cite:`Kawska2012` by the position of the half-maximum fluorescent intensity.
The properties of these network are measured by :cite:`Pujol2012` using
magnetic beads after stabilising with phalloidin. Though they do not
investigate the sparse and softer actin network that originate from he visible
part.


Using :ref:`time-shared optical tweezer <time_shared_ot>` we are able to probe
the mechanics of this soft actin structure at time scale than actin
polymerisation and pN force range. We show that the beyond the dense dendritic
mimicking the actin cortex which as been measured to have :ref:`Elastic Modulus
<elastic_modulus>` in the order of kPa :cite:`Pujol2012` the soft actin cloud
we probe is much softer with stiffness around 3 order of magnitude smaller.
This might explain why such a structure as not previously been seen by less
sensitive techniques. Nonetheless the size of this actin cloud and its ability
to sustain forces suggest that in cell the actin cortex is not sharply
delimited and that structure escaping from it have a role in organelle
positioning.


How does the external part of the gel which is below the half fluorescent intensity behave ? What are its mechanical properties ?  How does it change through time ? 
if the gel is elastic or 


.. figure:: /figs/intensity_profile_25nM_Arp_20nM_CP_09min.pdf
    :width: 100%

    Upper Left : Epifluorescence image of polystyrene bead with a growing actin gel in
    presence of 25 nM of Arp2/3 and 25 nM of Capping Protein scale bar is 5 µm.
    Upper Right : Normalized intensity profile of fluorescence image with thickness of the gel shown
    with dashed line as defined in :cite:`Kawska2012` : Distance between
    maximum intensity and half-maximum intensity.
    Lower Left: Epifluorescence image of log(intensity).

.. figure:: /figs/intensity_profile_25nM_Arp_0nM_CP_30min.pdf
    :width: 100%

    Upper Left : Epifluorescence image of polystyrene bead with a growing actin
    gel in presence of 25 nM of Arp2/3 and absence of Capping Protein scale bar
    is 5 µm.  Upper Right : Normalized intensity profile of fluorescence image with
    thickness of the gel shown with dashed line as defined in
    :cite:`Kawska2012` : Distance between maximum intensity and half-maximum
    intensity.  Lower Left: Epifluorescence image of log(intensity). In the
    absence of Capping Protein the growth of filament is not prevented away
    from the bead surface

.. todo:: scheme of experimental setup.

Actin-Bead System
*****************
.. 2

To reproduce the actin cortex and study the mechanics of actin structure
emanating from it `we prepare polystyrene bead <bead_preparation>` of 4.3 µm
diameter coated with a nucleation promoting factor. Theses bead are placed in
the `ATP mix Buffer <atp_mix_buffer>` in presence of 25µm of Arp2/3 complex,
4µm of monomeric actin 20% fluorescent 12 µM of Profilin and a varying amount
of Capping Protein. `Cf Material and Methods <m_et_m>`. These beads are
referred to as actin-bead.

These condition are chosen in order to grow a dense network on the surface of
actin-bead as in :cite:`Kawska2012`. We place ourself at 25nM ATP and a varying
amount of capping protein concentrating in order to cover condition where the
dense gel that form on the actin-bead is able to accumulate sufficient stress
to lead to symmetry breaking (CP between 12  and 35 nM ). We also investigate
condition where the amount of Capping Protein is to low (< 15nM) or to high
(>35 nM) to permit symmetry breaking.

We select a bead diameter of 4.3 µm in order to get a characteristic symmetry
breaking time of 20 to 40 minutes, leaving enough time to proceed with the
experiments before symmetry breaking occurs.  A smaller bead radius imply a
faster increase of stress and a shorter symmetry breaking time. 

All measured on actin bead were made on an actively growing actin network which
was not stabilized unlike in :cite:`Pujol2012`, and before symmetry breaking
occur for capping concentration in the range 15 to 35 nM.

Probe Bead System
*****************
.. 2

To indent the network formed on actin-bead we used polystyrene bead passivated
with BSA referred to as probe-bead.  The size of probe-bead have to be chosen
to be the same of actin-bead in order to achieve optical trapping of both actin
and probe bead. In the case of bead with different diameter the forced exerted
between the two bead during the indentation process has a non-negligible
component along the z-axis which is the axis with the weaker trapping stiffness
leading to bead escaping the traps.



Experimental description
************************
.. 2

To probe the actin network growing on bead we trap an actin-bead with a growing
actin-network and a probe-bead using time-shared optical trap and measure force
on the actin-bead using a QPD placed in the back focal plane of the condenser.

To avoid systematic error  on force measurement on displacing trap all the
force recording is made on the static bead, that is to say in our case on the
actin bead.


The indentation is a three step process :num:`Fig #figindent-time`.

Approach Phase
==============
.. 3
 
The approach of the probe-trap at constant speed (10 µm/s), as seen in
:num:`Fig #figindent-time` for :math:`t < t_1`. During the approach the actin bead
will repel the probe bead due the actin network growing on it. The force felt
by the actin bead will progressively increase as the probe bead approach
eventually reaching the maximum as the probe-trap reach its closest position
from the actin trap. Note that during this process as both bead fell the force
exerted in-between them they move away from the traps center. Though the trap
stiffness of :math:`>20 pN/µm` and the maximum for measured of :math:`~20 pN`
insure the displacement of the beads in the trap are small compared to the
distance between the two beads.


Relaxation Phase
================
.. 3

After the approach phase is a 3 seconds resting phase during which the probe
and actin-trap remain static. The relaxation phase start at :math:`t_1` and
finish at :math:`t_3`. The duration of the relaxation phase is long enough to
allow the relaxation of the actin cloud to happen, and sufficiently short for
the actin polymerisation not to change the properties of the network as well as
allow repetitive indentation to be done :ref:`ref repetitive figure`.

While the actin network relaxes, the forces between the two beads will slowly
decrease thus leading to the bead getting closer to their trap center and
closer to each other. The decrease in distance during the relaxation phase is
small compared to the distance between beads. The decrease of force as well as
the minimal change in distance between the two bead can be seen on :num:`Fig #figindent-time`
in the middle part.

.. _figindent-time:

.. figure:: /figs/force_time.png
    :width: 80%
    
    Upper graph : Force as a function of time on the actin-bead.  Lower graph :
    distance between beads (distance between traps + displacement of bead from
    the trap center) as a function of time. First part of each graph (green
    curve, yellow back) represent the approach phase. Middle part (orange on
    white) is the relaxation phase, and right part (blue on pale yellow) is the
    retraction.  Shown data is a subsample of around 1 every 1000 points of
    acquired data.


Retraction part
===============
.. 3


After the three seconds of the retraction phase, the probe trap return to it's
initial position at 10 µm/s (:math:`t > t_2`). During this phase, the force
exerted between the two beads decrease, becomes negative, reach a minimum, and
eventually reaching zero asymptotically as the probe bead recover its initial
position.

Reconstitution of Force-distance-curve
======================================
.. 3

From the position of he trap with time and the signal measured by the QPD the
position of bead in the trap as well as the forced exerted on each bead can be
calculated we can then recover the distance between beads center as a function
for time. Note that the displacement of bead from their respective trap center
is small compared to the distance between bead center and thickness of the
actin gel, thus the distance between beads center could be approximated as the
distance between traps without change of the overall further results.  The
force-distance curve curve representing the force exerted by the probe bead on
the actin bead as a function of the distance can be computed :num:`Fig #force-distance`. 


.. _force-distance:

.. figure:: /figs/force-distance.png
    :width: 100%

    Force exerted on the actin bead as a function of the distance between the
    two beads center. Color and data are the same as in :num:`Fig
    #figindent-time`. The probe bead start from the far right, and get closer
    while the force get higher (green upper part of the curve), reach a
    maximum, and enter the relaxation phase (orange part) where the force
    between the probe and actin bead decrease, while the distance slightly
    decrease. During the retraction part (Blue) the force decrease, reaches
    negative value while the bead return to its initial position. Shown data is
    a subsample of around 1 every 1000 points of acquired data.


Repetitive indent
=================
.. 3

To check for reproducibility and non-plastic deformation of the network after
indentation, the indentation cycle can be reputed several time at a few seconds
intervals. As the network is constantly growing during the measurement, this
also allow to check for the change of network properties due to actin
polymerisation.


.. _reproc-time:

.. figure:: /figs/reproc-time.png
    :width: 100%

    Force exerted on actin bead as a function of time for ten repetitive
    indent at a few seconds of interval. In one of the cycle a sticking event
    can be seen in the retraction phase 6 seconds after the beginning of the
    cycle.


.. _reproc:

.. figure:: /figs/reproc.png
    :width: 80%

    Figure showing the reproducibility of indentation process on a bead with
    25nM Arp2/3 and 10nM CP Subset of data from :num:`Fig #reproc-time` shown
    with different color to represent evolution of indentation curve with time.

Effect of approach speed
========================
.. 3

:cite:`Gardel2003` suggest that for frequency higher than 0.1 Hz, the effect of
force due to the viscous part of actin network can be in the same order of the
force dur to the elastic component.  It is though important to check the effect
of the approach speed on the force measurement. We check in :num:`Fig
#many-speed` how the indentation speed affect the measurement by varying the
approach speed from 10 to 30 µm/s onthe same actin bead.


.. _many-speed:

.. figure:: /figs/many_speed.png
    :width: 80%

    Aproach phase of repetitive indent at multiple speed on the same actin-bead


Results
*******
.. 2

Discussion
**********
.. 2



.. Doublets:

Doublets
********

.. Oocytes:

Oocytes
*******

