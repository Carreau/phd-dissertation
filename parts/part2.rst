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

cf :cite:`Foley`


Bead Coating
************

Carboxylated polystyrene beads (Polysciences, Philadelphia, PA) of 4.34 ± 0.239
μm (Standard deviation) diameter were used from for actin and probe-beads.

Probe-beads: polystyrene beads are incubated for 20 min at 20°C under agitation
with 10 mg/ml BSA at room temperature for 30 minutes in the working buffer (pH
7.4, 10 mM Hepes, 100 mM KCl, 1 mM MgCl2, 0.1 mM CaCl2, 1.8 mM ATP and 1 mg/ml
BSA) and stored a few days at 4°C.

Actin-beads: polystyrene beads are first
incubated for 20 min at 20°C under agitation with 2 μM pVCA and stored in
working buffer (as above) for the day.

Equal amount of each beads are then are placed in the polymerization mix, which is a solution of 4 μM G-actin, 12 μM profilin, 25 nM
of Arp2/3 complex and various concentration of CP (0 to 50 nM) in the working
buffer. 15 μL of this mix is sealed between coverslips.


.. Bead Motility
Bead Motility
*************

Indentation experiment
**********************

To determine the mechanical properties of an actin gel growing on bead as used
in motility assay, I used an indentation assay close to what can be done using
Atomic Force Microscopy. In this part I will describe the different choice I
made for the experiments parameters and the reason behind them. 

The indentation assay consist in using a passivated bead as a probe.
Approaching this probe from the sample with known trajectory, and speed while
recording the force exerted on the sample allow to get the force displacement
graph which is characteristic from the material.

Description of protocol
^^^^^^^^^^^^^^^^^^^^^^^

The indentation experiment is done as follow. 
In the actin polymerisation buffer, two population of beads are mixed: 

    - Bead covered with an activator of nucleation of actin polymerisation (hereafter referred to as "actin-beads"
    - Passivated bead (refer hereafter as probe bead)

Once mixed together in the polymerisation buffer the actin-bead grows an actin
network. Using actin monomers solution mixed with a small amount of fluorescent
actin make the actin network visible using epi-fluorescence. Thus the actin
bead can be differentiated from the probe bead from simple observation.  Using
bright field microscopy both kind of beads can bee seen whereas only actin bead
are visible when observing in the fluorescent wavelength of actin.

As described in section [...] the experimental setup used is equipped with time
shared optical trap thus allowing to get multiple optical trap at the same time
in the sample.  To perform the indentation experiment two traps need to be
placed in the sample in each of which one of the two kind of bead need to be
trapped.

To avoid initial interaction between the probe bead and the actin
bead before the beginning of the experiment the initial distance of the trap
should be placed sufficiently far away from each other, usually a distance of
roughly 20µm was used. Both trap were usually set to their maximum trap stiffness.

Once trap are in position one bead of each kind is trapped. And moved into the
experimental chamber to check that they are both freely floating in the medium
and to place them away of any other bead that could interfere with the
measurement during the experiments.

Then the probe bead will be approached at constant speed toward the actin-bead,
eventually indenting the actin network while the exerted forced recorded on the
actin bead increase.

The probe bead will then be stopped close to the actin bead for a few seconds
letting some time to the network to relax, and usually accompanied with a
decrease of force on the actin bead. 

The probe bead then retract to it's initial position at the same speed it was
approached.

The sequence can then be repeated a few time on the same bead couple.


It should be noted that this system have several particularly: The measurement
are effectuated on a dynamic system, while the actin network on the actin bead
is polymerising. It has been show previously that only  in the right conditions
of Arp2/3 and CP concentration :cite:`kawska2012` a dense gel is formed around
the bead and is both able to generate and accumulate enough stress for a
certain time until symmetry is broken. As it is such condition that are mostly
relevant I choose to do experiment only near theses condition. 

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
different size lead to impossibility of achieving high indentation force, and
the lost of one of the bead while performing the experiment.

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

For those reason we decided to use identical beads for actin growth and as
probe bead. Only the surface treatment would differ to prevent actin
polymerisation and sticking on probe bead.

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
bead was to use fluorescently labeled actin (Alexa 488, green). A thin layer of
actin network forming quickly on the surface covered with an activator of actin
nucleation using epifluorescence the experimenter can quickly distinguish both
kind.  Bright field can be used when discriminating the beads is no longer
necessary.

It should be noted that long  exposition to fluorescence need to be avoided as
an over exposition of fluorescent actin to UV light seem to deteriorate the
network and can lead to earlier symmetry breaking, or degradation of the actin
network.

In our particular case, because of the use of one accousto optic deflector for
each of the direction, we decided to always perform the experiments with the
two trap aligned along the X axis to avoid the phenomenon of ghost trap due to
the slight delay in position switching between the two AODs. The alternative
would have lead to a decrease the apparent maximal trap stiffness achievable
for each of the tweezer.

We then dispose of two traps, that are aligned along the X axis, at initial
position they are separated from a sufficient distance for the probe bead to
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
actin been and the chamber. In such a case the rest of the experiment was not
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

Additionally we can investigate which of the two trap should be set in motion
to perform the indentation protocol. We settled on having the probe bead in
motion for avoid potential variability in drag effect due the grown actin
network.


To select the range of parameter we will use we should take into account a few
considerations.

    - The system is dynamic and polymerising, we should perform an indentation
      experiment sufficiently fast for the properties of the system not to
      change during the probing.

    - Ideally we would like to repeat the indentation a few times without the
      properties of the system to change to much, in order to get enough
      statistic.

    - The system is viscoelastic, the speed at which we indent will determine
      Wether the dominant effect we see is due to the elastic behavior, or
      viscous behavior.

In order to be able to repeat the approach-retraction cycle, it is important to
keep the bead in the trap. With the trap stiffness achievable by the optical
tweezer used, we found that force higher to 15-20 pN would lead to bead
escaping the trap.

One possibility to avoid loosing bead from the trap would be stop approaching
the bead using a force feedback and a threshold.  Unfortunately, the increase
of force is too quick for our system, and using force feedback revel to be an
unsuccessful methods.  We then decided to manually set the end of approach
condition at a fixed distance between bead center.

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
    :alt: indent experiment
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


From the position of the trap as a function of time, and the position on each
bead in their respective trap, we can deduce the position of the bead with
respect to each other. Knowing the that maximum force that will be exerted on
our sample is in the order of 10 to 15 pN, an that the stiffness of our traps
exceed the 100pN/µm, we can deduce that, bead center will not move from the
trap center from more than 100nm, otherwise they will escape the trap and the 
full indentation cycle will not finish.

The initial distance between bead center is of 20µm, and experimentally
distance between bead surface always stayed more than 10 times this
displacement. On first order we can then consider that the distance between
bead center is the distance between the trap. In the rest of the manuscript,
unless specified otherwise, we use the two interchangeably, nonetheless the
displacement of the bead in their respective trap was taken into account in the data analysis.

Measurement of force on Sample
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have seen in previous section that the distance between bead was controlled. To get the force-distance graph, we still need to record the force exerted between the two beads. 

For this finality, a QPD is placed on the back focal plane of the light
collecting objective. The displacement of the light collected on this QPD is
proportional to the displacement of the trapped sample. Thus by knowing the
trap stiffness, and calibrating the photodiode one can measure the force
exerted the sample. The photodiode being sufficiently fast, using time-shared
optical trap, one could even measure the forced exerted on the sample in each
of the traps, as long as the timescale at which the photodiode respond is
faster than the characteristic at which the time-shared trap are switching.

This allowed us to record the forced exerted both on the actin bead in the
static trap, and on the probe bead on the mobile trap. As the two beads, except
their interaction between each other are floating free in the medium, both
force measurement should give the same values. 

Though, due to non uniformity of efficiency of AOD on the sample and delicate
optical conjugation of the QPD with the back focal plane of the objective, the
force measurement on a mobile trap is highly biased by the movement of the trap
and lead to unreliable signal. Hence the force between exerted thought the
network between the two beads was always measured by the recording on the actin
bead which trap stays static.



.. fitting
3D fitting
**********

In the third system I studied, liposomes doublets, determining the  geometrical
parameter necessary to get information on the biological was extremely
experimenter dependant when analysing the data.  

As the doublets we study are free floating in solution, and we observe their
evolution thought time, their rotation in space made their study particularly
challenging.  Indeed that traditional microscopy only give access to specific
image on a particular plane.  Thus we decided to use confocal microscopy to
reconstitute the doublets in 3D. Even though tradition contact angle
measurement technique as used in :cite:`Maitre2012b` require image that contain
equatorial plan of both liposomes.

As liposomes have a spherical shape, and that by using fluorescent component we
can label part of the system,  we decided to develop our own numerical method
to reconstitute the geometrical parameters.


.. figure:: /figs/doublets-parameters.png
    :alt: doublets parameters

    Liposomes doublets parameters in (one of) the equatorial planes.  Each of
    The two liposomes `A` and `B` are separated by the interface `i` also
    spherical.  The center of each of the three different spherical membrane
    portion are noted :math:`C_x`.  On the upper left part of the schema are
    represented the tangent to the three membranes at the contact point. We use
    :math:`\theta` as the contact angle that can be subdivided into
    :math:`\theta_1` and :math:`\theta_2`  angle between the tangent at one
    liposomes and the tangent at the interface. The position of the Two
    doublets center in X,Y,Z as well as the two liposomes radius represent the
    height parameters we are interested in.

We should note that the system get one supplementary degree of freedom or
parameter characterising its internal geometry which is the radius of the inner
interface. We do not discuss adding this fit parameter to the model.

Finding a single liposome
^^^^^^^^^^^^^^^^^^^^^^^^^

To understand how the fitting of doublets works we will focus on doing the same
process on a single liposomes in a 2D plane with three parameter : position in
the center in X and Y,as well as radius. The principle can be extended to
adjust for extra dimensions (Z, time, wavelenght) and parameter (thickness of
cortex, asymmetry). 

Experimentally liposomes are observed using fluorescently labeled component, in
particular we used a GFP labeled actin and streptavidine that will be imaged
using a inverted microscope. In the observation plane, the liposomes formed
using fluorescently labeled streptavidine will form a bright ring of given
thickness.  When imaging the actin shell — assuming the actin shell is of
homogeneous thickness around the liposomes — will also manifest as a fluorescent ring.

    In the case where the membrane is marked, the radius of liposome will be
    the median radius of the ring. 

    In the case of actin shell, when the thickness of the actin shell is bigger
    compared the resolution limit of our method, then the liposome radius
    should be taken as the inner radius of the ring


.. figure:: /figs/modl-2d-doublet.png
    :alt: liposome Model

    Left : A simulation of liposome fluorescent of an uniform shell or
    membrane. 
    Middle: Same Image Adding gaussian noise to simulate a plane from
    a confocal Z-stack. 
    Right: Fluorescently labelled Liposome in fluorescent External Buffer 
    and non fluorescent medium.



.. figure:: /figs/corrfun-noise-.png
    :alt: liposome Model
















