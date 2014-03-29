.. part2

Materials and methods
#####################

.. Actin
Actin
*****

.. Profiline
Profiline
*********

.. Arp2/3
Arp2/3
******

:cite:`Foley`

.. Bead Motility
Bead Motility
*************

Indentation experiment
**********************

To determine the mechanical properties of an actin gel growing on bead as used
in motility assay, I used an indentation assay close to what can be done using
Atomic Force Microscopy. In the part I will describe the different choice as
made for the experiment parameters and the reason that govern them. 

global description of protocol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The indentation experiment is done as follow. 
In the actin polymerisation buffer, two population of beads are mixed: 

    - Bead covered with an activator of nucleation of actin polymerisation (hereafter referred to as "actin-beads"
    - Passivated bead (refer hereafter as probe bead)

Once mixed together in the polymerisation buffer the actin-bean have an actin
network that start polymerising on it and can be identify using
epi-fluorescence then one bead of each kind in two generated trap of chosen
stiffness. Then the probe bead will be approached toward the actin-bead,
eventually indenting the actin network, before being retracted to its initial
position. In-between the approach and retraction phase a resting phase where
the two trap are immobile is added to observe an eventual relaxation of the
system.  

The sequence can then be repeated a few time on the same bead couple before
passing to another one, then changing sample once to much symmetry  breaking is
happening.


It should be noted that this system have several particularly, indeed
measurement are effectuated while the actin network on the actin bead is
polymerising. It has been show previously that only  in the right conditions of
Arp2/3 and CP concentration :cite:`kawska2012` a dense gel is formed around the
bead and is both able to generate and accumulate enough stress for a certain
time until symmetry is broken. As it is such condition that are mostly relevant
I choose to do experiment only near theses condition. 

.. todo::
    - describe the biochemical condition here.

The symmetry breaking time of theses system also strongly depend on the
diameter of the diameter of the used polystyrene beads. In system with higher
curvature, the accumulation of stress is faster, leading to time before
symmetry breaking to quick to get mechanical measurement. A bead diameter of
~4.5 µm diameter allow symmetry breaking to start occurring around 20 minutes
after triggering actin polymerisation, and allowing up to 40 minutes to perform
many indentation on the same sample. Moreover a smaller bead diameter in our
case practically suffers from the being too close to the diameter of the laser
waist we used, leading to a poor linear relation between the bead displacement
and the laser deflection. (cf chap1)

.. todo::
    - argue against bigger beads.

Selection of diameter for probe bead.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The selection of the bead diameter is a interesting parameter to vary in order
to test different models for the indented materials. Indeed, having a prob bead
much smaller (or bigger) than the actin bead could be used to test the same
model in a sphere-plan or plan-sphere approximation instead of a plan-plan or
sphere-sphere approximation. Practically the use of probe and actin-bead of
different size lead to impossibility of achieving high indentation force, and the lost of one of the bead while performing the experiment.

To understand the reason, one need to get slightly back at the exact point
where the bead is trapped in the Gaussian beam. Besides being attracted near
the laser waist, the particle — here the bead — is affected by other forces
that will affect it exact position of equilibrium. In our case, the particle
is affected by its weight and by the radiation pressure exerted by the laser.
Both being different depending on the bead diameter, this will lead to bead of
each diameter lying at equilibrium on a slightly different focus plane in the
microscope chamber.

The non-alignment of the bead in the same plane lead to the force between the
two bead having a component along the direction of propagation of the light,
which is the direction in which the trap stiffness is the weaker. Hence the use
of bead of different size hinder the experiment by weakening the ability to
hold both bead in the trap during the indentation experiment. Measuring the
difference in distance in the Z direction (perpendicular to observation plane)
is also challenging, which is another factor which would prevent the correct
determination of the distance between bead center.

For those reason we decided to use identical beads for actin growth and as probe bead. Only the surface treatment would differ to prevent actin polymerisation and sticking on probe bead.

.. figure:: /figs/otm.png
    :width: 70%

    A bigger bead will be trapped higher in the optical tweezer. The forced
    exerted between the two bead by the intermediate of the actin network
    growing on the actin bead will be along the direction between the two
    center. It decomposes along the observation plane (green arrows), direction
    along which the trapping is strong, and along the orthogonal direction (red
    arrow) along which the trapping is weak. Further approach of the two bead
    would lead to one of the bead escaping the trap.


Positioning of the bead in observation plane
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




















.. 3D fitting
3D fitting
**********

.. ?? ?? ??
?? ?? ??
********
