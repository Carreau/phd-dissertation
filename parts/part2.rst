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


Positioning and first trapping of bead
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once mixed in the microscope chamber, one bead of each kind need to be trapped.
The solution chosen to be able to distinguish the probe bead from the actin
bead was to use fluorescently labeled actin. A thin layer of actin network
forming quickly on the surface covered with an activator of actin nucleation
using epifluorescence the experimenter can quickly distinguish both kind.
Bright field can be used when discriminating the beads is no longer necessary.

It should be noted that long  exposition to fluorescence need to be avoided as
an over exposition of fluorescent actin to UV light seem to deteriorate the
network.

In our particular case, because of the use of one accousto optic deflector for
each of the direction, we decided to always perform the experiments with the
two trap aligned along one of the two axis of the microscope to avoid the
phenomenon of ghost trap due to the slight delay in position switching between
the two AODs. The alternative would have been to decrease the laser power for a
short amount of time between each  trap switching, which would have decrease
the apparent maximal trap stiffness achievable for each of the tweezer.

We then dispose of two traps, that are aligned along the X axis, at initial
position they are separated from a sufficient distance for the probe bead to to
already interact with the actin network polymerising on the actin bead. The
actin bead can be discriminated from the probe bead by using fluorescent and
lie in what will hereafter be the static trap wile the probe bead is stationed
in what will be referred to as the moving trap.

To check that the only force exerted on the trapped bead are from the tweezer
themselves, the chamber is before each experiment moved in the three direction,
and it should be checked that no important force are detected on each of the
bead. It should be noted that especially at low capping concentration where
long filament are supposed to escape from the actin-bead, the procedure lead to
bead moving with the microscope stage, hinting for an adhesion between the
actin bean and the chamber. In such a case the rest of the experiment was not
performed and another couple of actin-bead/probe-bead was selected.

Approach at constant speed
^^^^^^^^^^^^^^^^^^^^^^^^^^

We are now certain that we are in presence of a actin bead trapped in the
tweezer free from any other external forces, and a probe bead situated
relatively far (~15-20µm) from the actin bead. 

To probe the mechanical property we will now effectuate a indentation at
constant speed, followed by a resting phase and finally a retraction. A few
parameters can be varied fro theses 3 phases.

    - initial distance between beads
    - speed of the approach
    - condition to stop the approach.
    - Time for resting phase
    - speed of retracting phase.

Additionally we can wonder which of the two trap should be set in motion to
perform the indentation protocol.


To select the range of parameter we will use we should take into account a few
considerations.

    - The system is dynamic and polymerising, we should perform an indentation
      experiment sufficiently fast for the properties of the system not to
      change during the probing.

    - Ideally we would like to repeat the indentation a few times without the
      properties of the system to change to much, in order to get enough statistic.A

    - The system is viscoelastic, the speed at which we indent will determine
      wether the dominant effect we see is due to the elastic behavior, or
      viscous behavior.

As we like to effect many approach-retraction cycle to test the reproducibility
of the indentation, it is important to keep the bead in the trap. As
experimentally we found that force higher to 15-20 pN would lead to bead
escaping the trap we need to choose the experiment parameter in order to avoid
going over theses values. One possibility would be to fix the approach stopping
condition using a force feedback with a given threshold, unfortunately, the
increase of force if often too quick for our system, and using force feedback
revel to be an unsuccessful methods, thus falling back to an stopping condition
at a fixed distance between bead center.

We choose to indent at a speed of 10 µm/s with a resting phase of 3s and a
retraction to initial position at the same speed than the approach. Knowing
that the initial distance between beads is between 15µm and 20µm, this lead to
a duration of one approach-resting-retraction of 6 to 10 seconds allowing a few
repetition of indent. 

As for the condition, it was chosen on a per-cycle basis at the liberty of the
experimenter, indeed as we will see in the result section, the growing on the
dense gel on the bead surface is dependant both on time and biochemical
condition. Practically, the minimal approach distance was set to 8-9 µm, an
approach cycle done, and then minimal approach distance decrease stepwise by
0.5 micron until the peak force near 15 pN, then approach cycle were repeated
without decreasing the minimal approach distance. :num:`Fig #bead-move`.

.. _bead-move:

.. figure:: /figs/beed_move.png
    :alt: indent experiement
    :width: 50%

    Schematic of indentation experiment. On the left is the actin-bead, covered
    with actin, in the static trap, on the right the probe-bead in the mobile
    trap. At the brining of experiment (A) the probe bead is situated far from
    the actin bead. During the approach phase (I) the moving trap approach
    toward the static trap at 10µm/sec until it reached the minimal approach
    distance (B). The moving trap stay at the minimal approach distance for
    3sec (II), which constitute the relaxation phase.C) The actin gel are
    relaxed, the distance between bead is smaller than on B. III) the moving
    trap retract at 10 µm/sec back to its initial position.





.. fitting
3D fitting
**********

