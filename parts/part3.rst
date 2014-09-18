.. Actin Cloud:

Mechanical properties of a far reaching actin cloud
###################################################
.. 1

Introduction 
*************
.. 2

We have seen that the actin cytoskeleton plays a major role in
cellular mechanics. It is necessary for force generation, and a
key component for cell motility. It has also be extensively studied both in
cells and biomimetic systems. 

Actin can form a variety of networks in cells, ranging from dense branched
networks at the leading edge of the lamellipodia to bundled parallel structures
forming the filopodia.  Reconstruction of the actin network has been achieved in
biomimetic systems using purified components :cite:`Plastino2005`,
:cite:`Loisel1999`, :cite:`Bernheim-Groswasser2002`,  :cite:`Pontani2009`, and
many properties of these network have been measured.

It has been determined that the actin cortex provides mechanical support for the
plasma membrane and that it extends over a few hundreds of nanometers. Many
cellular processes hint for actin structures connected to this cortex to be
key elements in organelle and chromosome positioning. 

In this part of the manuscript we investigate how a sparse actin structure can
emanate from the actin cortex, and we explore its properties. Using the
:ref:`bead-motility <bead-motility-assay>` biomimetic system to reconstitute
the actin cortex and its dendritic structure, we show that a sparse network of
actin filaments emanating from the cortex has a mechanical effect sufficient to
displace objects on the size of cells organelles at distances up to tens of micrometers
away from the actin cortex.

The branched structure of the actin cortex underneath the plasma membrane of
cells hints for a structure governed by Arp2/3. How Arp2/3 and CP can be used
to form a biomimetic actin cortex has been widely studied. In
:cite:`Kawska2012`, both `in vitro` measurements on reconstituted actin cortices
on beads as well as simulations investigate the effect of cross-linking and
Capping Protein on the formed actin gel. It can be seen both experimentally and in
simulation that a network of filaments escape from what is defined as the actin
cortex (:num:`Fig #fig-bead-tirf`). The effect of these long filaments is not taken into account in the
`in-silico` system where the analysis is restricted to filaments shorter than 10
µm. Only the effect of dense entangled actin networks generated from primers
randomly placed  on the bead surface participate in the increase of tension and
contribute to symmetry breaking.

.. _fig-bead-tirf:
.. figure:: /figs/Bead-tirf-fluo-sim.png
    :width: 70%

    Upper Left : Fluorescence image of an actin bead with a growing actin
    cortex. Escaping filaments form the actin cloud that can only hardly  be
    seen in fluorescence. Scale bar is 2 µm. Lower Left: Total Internal Reflexion (TIRF) image
    of actin polymerising on an actin bead. Escaping filaments are directly
    visible. The gray circle represents the size of the bead.  Right :
    Representation of the actin growth simulation with delimitation between the
    entangled branched actin network and escaping filaments.  Adapted from
    :cite:`Kawska2012`.


The limit of the dense network visible in epifluorescence is defined in
:cite:`Kawska2012` by the position of the half-maximum fluorescent intensity (:num:`Fig #fig-intensity-profile`).
The properties of these networks are measured by :cite:`Pujol2012` using
magnetic beads and actin stabilized with phalloidin. Though they do not
investigate the sparse and softer actin network that originate from the visible
part.


Using :ref:`time-shared optical tweezer <time_shared_ot>` we are able to probe
the mechanics of this soft actin structure at time scale shorter than the
characteristic time of actin polymerisation and forces in the pN range. We show
that beyond the dense dendritic network mimicking the actin cortex which as
been measured to have an :ref:`elastic modulus <elastic_modulus>` in the order of
kPa :cite:`Pujol2012` the soft actin cloud is much softer with
a stiffness in the Pa regime.  This might explain why such a
structure has not previously been seen by less sensitive techniques than optical
tweezers. The size of this actin cloud and its ability to sustain forces
suggest that in cells the actin cortex is not sharply delimited and that
structures escaping from it may have a role in organelle positioning.


The questions we address in this part of the manuscript are :  How does the far
extends the soft part of the gel? What are its precise mechanical properties?  How does it change
over time?  Is the actin cloud elastic or viscous?

.. _fig-intensity-profile:
.. figure:: /figs/intensity_profile_xnM_Arp_xnM_CP_xmin.*
    :width: 80%

    A) Epifluorescence image of polystyrene bead with a growing actin gel in
    presence of 25 nM of Arp2/3 and 25 nM of Capping Protein. Scale bar is 5
    µm.  B) Normalized intensity profile of fluorescence image with thickness
    of the gel shown with dashed line as defined in :cite:`Kawska2012` :
    Distance between maximum intensity and half-maximum intensity.  C)
    Epifluorescence image of log(intensity). D,E,F) Same as A,B,C, in absence
    of Capping Protein

Actin-Bead System
*****************
.. 2

To reproduce the actin cortex and study the mechanics of actin structures
emanating from it :ref:`we prepare polystyrene beads <bead_preparation>` of 4.3
µm diameter coated with a nucleation promoting factor. Theses beads are placed
in the :ref:`ATP mix buffer <atp_mix_buffer>` in presence of 25nm of Arp2/3
complex, 4µm of monomeric actin (20% fluorescently labeled) 12 µM profilin and
a variable amount of Capping Protein. :ref:`see Material and Methods <m_et_m>`.
These beads are referred to as actin-beads.

These condition are chosen in order to grow a dense network on the surface of
actin-bead as in :cite:`Kawska2012`. We place ourself at 25nM ATP and a varying
amount of Capping Protein concentration in order to cover condition where the
dense gel that forms on the actin-bead is able to accumulate sufficient stress
to lead to symmetry breaking (CP between 15  and 35 nM, see part :ref:`Bead Motility Assay <bead-motility-assay>`). We also investigate
conditions where the amount of Capping Protein is too low (< 15nM) or too high
(>35 nM) to permit symmetry breaking.

.. .. _fig-phase-diagram:

We select a bead diameter of 4.3 µm in order to get a characteristic symmetry
breaking time of 20 to 40 minutes.
A smaller bead radius imply a
faster increase of stress and a shorter symmetry breaking time. 
The choice of 4.3µm provides sufficient time to proceed with the
experiments before symmetry breaking occurs. 

All measurements were made on an actively growing actin network which
was not stabilized and before symmetry breaking
occur for Capping Protein concentration in the range 15 to 35 nM :cite:`Kawska2012`.

Probe Bead System
*****************
.. 2

Beside the actin-bead, the experiment requires a polystyrene bead passivated
with BSA. These beads are referred to as probe-beads.  The size of the
probe-bead was chosen to be the same as the actin-bead, which ensure optical
trapping of both beads in the same observation plane. In the case of beads with
different diameters, the axial forces on the beads are different. This axial
displacement of the two beads during the indentation process leads to a
component along the z-axis which  eventually pushes one bead out of the trap.




Experimental description
************************
.. 2

To probe the actin network we trap an actin-bead with a growing actin-network
and a probe-bead using time-shared :ref:`optical trap <time_shared_ot>`,  and
measure the forces on the actin-bead using a QPD placed in the back focal plane of
the condenser (:ref:`material and methods <m_et_m>`).

To avoid systematic errors of force measurements on the moving trap, all force
recordings used for analysis are made on the static bead, which is in our case the actin bead.


The indentation is a three step process (:num:`Fig #figindent-time`):

    - Approach phase at constant velocity 10µm/sec unless specified otherwise
    - Relaxation phase of 3 second during which both traps remain static
    - Retraction phase in which the probe trap move towards its initial position at 10µm/sec.


Approach Phase
==============
.. 3
 
During the approach phase, the probe-trap approaches the actin-trap at constant speed (10 µm/s), as shown in
:num:`figure #figindent-time` for times :math:`t < t_1`. During this approach the actin bead
will repel the probe bead due to the actin network growing on it. The force felt
by the actin bead will progressively increase during the probe bead approach,
eventually reaching the maximum as the probe-trap reaches its closest position
to the actin trap. Note that during this process 
the force between the beads pushes  the beads out of the respective trap center. 
The displacement of the beads in the trap remains small compared to the
distance between the two beads. Hence in the following we consider that the probe-bead speed is equivalent to the trap approach speed of 10µm/sec.


Relaxation Phase
================
.. 3

After the approach , the trap remain static for a 3 seconds relaxation phase 
. The relaxation phase start at :math:`t_1` and
finish at :math:`t_3` as shown on :num:`figure #figindent-time`. The duration of the relaxation phase is sufficient to allow the partial
relaxation of the actin cloud  but remain sufficiently short compared to
the actin polymerisation speed hence the polymerisation is not expected to 
change the properties of the network during indentation cycle as well as
during repetitive indentation (:num:`Figure #reproc`)

While the actin network relaxes, the forces between the two beads will slowly
decrease thus leading to the beads getting closer to their trap center and
closer to each other. The decrease in distance during the relaxation phase is
small compared to the distance between beads. The decrease of force as well as
the minimal change in distance between the two bead can be seen on :num:`Fig #figindent-time`
in the middle part.

.. _figindent-time:

.. figure:: /figs/force_time.*
    :width: 70%
    
    Upper graph : Force as a function of time on the actin-beads.  Lower graph
    : distance between beads (distance between traps + displacement of beads
    from the trap center) as a function of time. First part of each graph
    (green curve, yellow back) represents the approach phase. Middle part
    (orange on white) corresponds to the relaxation phase, and right part (blue on pale
    yellow) is the retraction.  Shown data is a subsample of around 1 of every
    1000 points acquired. We can see on the second graph that the bead
    displacement on their respective trap is small compared to the
    displacement of the trap and justify the approximation of a probe bead
    speed equal to the probe trap speed.


Retraction part
===============
.. 3


After the three seconds of the retraction phase, the probe trap returns to it's
initial position at 10 µm/s (:math:`t > t_2`). During this phase, the force
exerted between the two beads decreases, becomes negative, reaches a minimum, and
eventually returns to zero as the probe bead recover its initial
position (shown on :num:`Figure #figindent-time` right part). Negative forces
represent forces that tends to push the two beads towards each other.


Reconstitution of Force-distance-curve
======================================
.. 3

From the position of he trap with time and the signal measured by the QPD the
position of bead in the trap as well as the force exerted on each bead can be
calculated. We can then recover the distance between bead centers as a function
of time.  The force-distance curve representing the force exerted by the
probe bead on the actin bead as a function of the distance can be computed and is
show in :num:`figure #force-distance` where we can still distinguish the three
phase of the indentation cycle, also marked by the color of the data. 



.. _force-distance:
.. figure:: /figs/force-distance.*
    :width: 80%

    Force exerted on the actin bead as a function of the distance between the
    two bead centers. Color and data are the same as in :num:`Fig #figindent-time`. 
    The probe bead starts from the far right, and gets closer
    while the force increases (green upper part of the curve), reaches a
    maximum, and enters the relaxation phase (orange part) where the force
    between the probe and actin bead decrease, while the distance  also
    slightly decreases. During the retraction part (blue) the force rapidly
    decreases and  reaches negative values while the bead returns to its initial
    position. Shown data is a subsample of 1 every 1000 points of acquired
    data. Shaded region represent areas where the two polystyrene beads would
    interpenetrates.


Repetitive indent
=================
.. 3

To check for reproducibility and non-plastic deformation of the network after
indentation, the indentation cycle can be repeated several times at a few seconds
interval. As the network is constantly growing during the measurement, this
repeat also allows to check for possible change of network properties due to actin
polymerisation. The force distance plot is shown in :num:`Figure #reproc` :num:`, #reproc-time`.


.. _reproc-time:
.. figure:: /figs/reproc-time.*
    :width: 100%

    Upper graph : Force exerted on actin bead as a function of time for ten
    repetitive indents. In one of the cycles a sticking event can be seen in the
    retraction phase 6 seconds after the beginning of the cycle. Lower graph:
    Distance as a function of time for  ten repetitive indents. The ten curves
    can only hardly be distinguished from one another, which shows the
    reproducibility of indentation curves.


.. _reproc:
.. figure:: /figs/reproc.*
    :width: 80%

    Figure showing the reproducibility of indentation process on a bead with
    25nM Arp2/3 and 10nM CP Subset of data from :num:`Fig #reproc-time` shown
    with different color to represent the evolution of the indentation curve
    over time.  Time is relative to first indentation. Shaded area represent
    zone where the two beads would interpenetrates.

Effect of approach speed
========================
.. 3

:cite:`Gardel2003` suggest that for frequencies higher than 0.1 Hz, force due to
the viscous behavior  of actin network can be in the same order as the elastic
component. To test if such an relaxation effect is important we measured the effect of the
approach speed on the force measurements. :num:`Fig #many-speed` presents the
indentation speed affect the measurement by varying the approach speed from 10
to 30 µm/s on the same actin bead.


.. _many-speed:

.. figure:: /figs/many_speed.*
    :width: 60%

    Approach phase of repetitive indents at multiple speed on the same
    actin-bead. The approach phase in the different conditions are similar,
    hinting for a negligible effect of the viscosity  in the actin cloud at the
    speed considered.


Experimental observations
*************************
.. 3

Using the bead system, we are able to reconstruct actin cortices `in vitro` and
to investigate the mechanical properties inaccessible to other microscopy
techniques like TIRF. Beyond the visible actin cortex we can detect the
presence of an actin structure that has mechanical effects starting at
distances of :math:`> 10\mu{}m`, hence far beyond the thickness of the actin cortex (~1µm). 
:num:`Figure #cloud-repelling` presents a video showing qualitatively that the actin cloud growing
on actin beads is able to repel free floating probe beads before they reach the
visible reconstituted cortex. 

.. todo:

    add the video online ?


To quantify the distance at which the probe beads are first affected by the actin-cloud
we measure the experimental noise by looking at the fluctuations of the trapped probe bead.

During the indentation we defined :math:`d_0` as the distance at which the
average force felt by the probe bead is higher than the experimental noise.
Typically the standard deviation is 2pN. 

The repartition of :math:`d_0` with the concentration of Capping Protein is
plotted in :num:`figure #d0-violin`.

 
 
.. _cloud-repelling: 

.. figure:: /figs/cloud-repelling.png
    :width: 85%

    Chronophotography representing the displacement a trapped actin bead in a
    solution with probe bead. During this experiment, the actin bead is kept
    static in the optical trap (marked by the cross) while the stage is moved.
    Scale bar is 5 micrometers. Total movie duration is 21 seconds.


.. _d0-violin:
.. figure:: /figs/d0_violin.*
    :width: 65%

    Repartition of the bead-center distance at which the actin cloud exert a
    force higher than the noise (:math:`d_0`) on the probe bead, as a function of
    Capping Protein. Shaded region represent the position of the bead surface
    (4.34 µm) and the red line represent the bead surface+1µm (upper bound for
    the in vitro
    Capping Protein concentration. The shaded region represents the position of
    the bead surface (4.34 µm) and the red line represents the bead surface+1µm
    (upper bound for the in vitro
    reformed actin cortex measured in :cite:`Kawska2012`). We see in this graph that for symmetry breaking
    conditions (CP 10 nM and 30 nM) the distance at which the actin cloud starts to apply
    forces on the probe bead is large compare to the thickness of the actin
    cortex. The distance at which the probe bead is able to detect the presence
    of the actin cloud decreases when increasing the concentration of Capping
    Protein that restricts  actin filament growth. The condition in the absence
    of Capping Protein are a particular case as no dense actin network forms
    on the surface of the actin bead. 

Approach phase modeling
=======================
.. 3

To extract mechanical properties using the three phases of the experiment we
decided to model each part (approach, relaxation and retraction) independently.
In particular, we fit force-distance curve of the approach phase using a power
law with 3 fit parameters :math:`\alpha, \beta, \delta`:

.. math::
    :label: eqa31

    F(d) = \beta \times \left(d-\delta\right)^\alpha

In which :math:`F` represent the force exerted on the probe bead, and :math:`d`
is the distance between bead centers. The powerlaw exponent :math:`\alpha` is
expected to be negative as the force decreases with the distance :math:`d`, and
characterizes how fast the force increase as the two
beads approaches each other. The prefactor :math:`\beta` acts as a scaling factor of the
force. The offset parameter :math:`\delta` shifts the curve on the distance
axis. This phenomenological model has the particularity that the force on the probe bead tends to
:math:`+\infty` when the distance :math:`d` get  to :math:`\delta`. The force
is undefined for values of :math:`d< \delta`. Hence, the offset distance :math:`\delta`
practically describe the distance at which the optical trap is not able to
indent the network anymore. 

In the case of a hard sphere the value of :math:`\alpha` would tend towards
:math:`-\infty` leading to a infinite force increase at the contact between the
two hard-spheres of same diameter and a value of :math:`\delta` equal to the
diameter of the hard sphere.  In this case :math:`F(d>\delta)=0` and
:math:`F(d<\delta)=\infty`

The optical tweezer we use can apply forces up to 20pN, and the beads we use
have a diameter of 4.34µm , hence we determine a cross-sectional surface of surface of roughly :math:`14.7\mu{}m^2`. Before 
escaping the trap, the probe bead can move up to 1µm from its
trap center. To estimate the maximal stiffness that can be measured, we approximate that we can 
provide a clear measure of deformation in the order of 1/10 of µm,  this
leads to a maximum detectable Young's modulus of :

.. math::
    :label: eqa32a

    E_{max} &\sim \frac{F_{max}L_{0,max}}{A_0.\Delta L} \\
            &\sim \frac{50.10^{-12} \times 1.10^{-5} }{  (\pi\times 2.17\times 10^{-6})^2 \times 1.10^{-7}              }\\ 
            & \sim 300 Pa

Any material with a stiffness much higher than 300 Pa can be considered as
infinitely rigid.


The elasticity of dense actin gels around polystyrene beads has been measured
in :cite:`Pujol2012` and found to be in the order of kPa.  Therefore the
optical tweezers are not able to probe the mechanics of the dense gel on the
surface of the bead. The value of :math:`\delta`  is expected to be :math:`> 4.34 \mu{}m` as it include partially the dense actin gel.

The model can be fitted independently on each experimental
approach phase. An example of such a fit is shown in
:num:`figure #force-distance-fit` and the quality of fit can be measure by the
coefficient :math:`R^2` which has a media value of `0.97`
across all fits.

.. _force-distance-fit:
.. figure:: /figs/force-distance-fit.*
    :width: 100%

    Power law model fitted on the approach phase data for one experiment in the
    presence of [CP]=10nM, with the particular values found for the fit
    parameters.  The vertical line represent the point at which the model
    diverges and the force goes to infinity, that is to say :math:`\delta`. The
    shaded region corresponds to the distance at which the two beads would
    interpenetrates. Relaxation (orange) and retraction (blue) data are not fitted.


The approach phase data can be corrected for the distance offset :math:`\delta`
and plot in a log-log scale allowing for a better appreciation of the fit
result (:num:`Fig #force-distance-log-log`). The corrected distance is noted with  `c` indices :math:`d_c = d-
\delta`. In the model the force tends to infinity at :math:`d_c = 0`.




.. _force-distance-log-log:
.. figure:: /figs/force-distance-fit-loglog.*
    :width: 80%

    Force on the actin bead  during the approach phase as a function of bead distance
    minus distance offset :math:`\delta` plotted on a log-log scale. Black line
    represents the power law model with  correction of the offset distance. Same
    data as :num:`Fig #force-distance` but showing only approach phase. 


In our experiments, the polystyrene beads have an average diameter of 4.34 µm,
thus we expect :math:`\delta` to be higher than the bead diameter since the beads cannot interpenetrates.  Data with
:math:`\delta` values lower than 4.34 µm (21 out of 127) are considered as
unphysical and were removed from further analysis.

As expected we find negative values for :math:`\alpha`. Surprisingly the value
of alpha does not vary significantly when comparing experiments with different
amount of Capping Protein and stay close to -1, with a mean value of -1.10, and
a standard deviation of 0.38. The distribution of the power law exponent can be
seen on :num:`figure #power-law-exponent`

.. _power-law-exponent:
.. figure:: /figs/alpha_violin.*
    :width: 60%

    Right : Violin plot showing the repartition of power law exponents with the
    concentration of Capping Protein. Left: distribution of power law exponent
    :math:`\alpha` regardless of the concentration in Capping Protein. Value of
    exponent lies close to `-1`.


Due to the scale invariance of the inverse power law found above,  all the
approach phases data can be rescaled into a single master-curve (:num:`Fig #fig-rescale-powerlaw`). This is done
by dividing the force by the maximum force :math:`F_{max}` reached during the
approach and rescaling the distance by the minimum approach distance from which
:math:`\delta` is subtracted. 

.. _fig-rescale-powerlaw:
.. figure:: /figs/rescaled_powerlaw.*
    :width: 70%

    Representation of rescale approach data on a log-log scale.  Red and green
    crosses correspond to average values. Blue area corresponds to average +/-
    standard deviation for each average bin. Red dot in the upper right corner
    corresponds to the point (1,1) with respect to which all data has been
    rescaled.
    
    Blue dashed line shows a powerlaw fit of the average data for
    :math:`d_c/d_{c,min} < 10` (red cross), fitted slope is :math:`-1.06` . 
    As an eye guide, slope of `-1` and `-1.5` have been represented. 
 


The rescaled data confirm an average power law exponent of :math:`\sim -1`, the
breakdown of the average exponent beyond :math:`d_c/d_{c,min}=10` can be
explained by the statistical effect of having less data for long distance.




.. todo:
    Zero of force is determined by average force on large distance. // bead <Left Mouse>


Variation of parameters with Capping Protein
============================================
.. 3

At the chosen concentration of Arp2/3 the bead system can show symmetry
breaking in the correct range of concentration of Capping Protein of 10 to 30
µM. In absence of Capping Protein the dense dendritic network does not form on
the surface :cite:`Kawska2012`. At low Capping Protein concentrations (:math:`<10 \mu{}M`) it seem not to be able to generate enough stress to
rupture, and at too high concentration (>35nM) the visible gel is thin and do
not break symmetry either. We then investigated the variation of each of the
fit parameters for concentrating of Capping Protein ranging from 0 to 50 nM.


We have already seen previously that the powerlaw exponent factor |alpha|
didn't vary with the amount of Capping Protein in solution (:num:`Fig #power-law-exponent`). 
The two other parameters investigated are the prefactor
:math:`\beta`. For the same value of :math:`\alpha` and :math:`\delta`, the
higher :math:`\beta` is the stronger the interaction between the two beads for
the same distance |dc|. We can see on :num:`figure #beta-violin` that the
average value for the prefactor decreases with increasing Capping Protein
concentration. 

.. _beta-violin:
.. figure:: /figs/beta_violin.*
    :width: 80% 

    Violin plot showing the repartition of the prefactor with the quantity of
    Capping Protein. Decrease of prefactor with increasing amount of Capping
    Protein indicates a lower force between the probe bead and the actin bead
    for the same corrected distance between bead centers. 

The last parameter of our model is :math:`\delta`, the distance at which the force
diverges.   It can be seen in :num:`Figure #delta-violin` that with the exception
of zero Capping Protein, the distance at which the model diverges gets
closer to the diameter of the polystyrene bead as the concentration of Capping
Proteins in the medium increases. It is interesting to see that the distance offset
|delta| is very close from the bead diameter in the absence of Capping Protein, when no
biomimetic actin cortices forms.  

.. _delta-violin:
.. figure:: /figs/delta_violin.*
    :width: 80% 

    Violin plot showing the variation of the offset distance :math:`\delta`
    with the Capping Protein concentration. The shaded area represents the
    non-physical region which would correspond to a diverging force beyond the
    contact of the two polystyrene beads. Experimental data with :math:`\delta`
    value in this regions have been excluded from further analysis.


Determination of Young's Modulus
================================
.. 3


.. |E| replace:: :math:`E`

.. |dc| replace:: :math:`d_c`

.. |delta| replace:: :math:`\delta`
.. |alpha| replace:: :math:`\alpha`
.. |beta| replace:: :math:`\beta`

.. |E0| replace:: :math:`E_0`

To determine the mechanical properties of the gel between the actin and the
probe bead, we model it as a purely elastic material. The viscous effects are
neglected in the approach part as the approach at different speed show no
clear effect on the approach curves (:num:`Figure #many-speed`). We consider
the compression of the material between the two beads. The surface of the
compressed material is approximated by the projected surfaces of the bead along the
direction of compression (:math:`\pi R^2`).  The thickness of the compressed
material is taken as being the distance between bead centers corrected by the
distance offset |delta| as any material below delta can be considered as
infinitively rigid for the optical tweezer.

The stress exerted onto the material projected onto the bead surface or radius
:math:`R` can be written : 

.. math::
    :label: eqa32
    
    \sigma = \frac{F}{\pi R^2}

For small deformation the local strain of the material :math:`u` can be written
as a function of the corrected bead position |dc| and the considered location
along the axis between the two bead center :math:`x` : 

.. math::
    :label: eqa33

    u(x)= \frac{d_c-x}{d_c}


We can express the local differential strain around the position |dc| of the
bead : :math:`\partial u = -\partial x/ \partial d_c` in which the minus sign
reflect the choice of the coordinate system: a decrease in :math:`x` with a
positive Young's modulus |E| should lead to an increase of the exerted force.
The locally felt Young's modulus 
at the distance |dc| is then  

.. _eq-E:
.. math::
    :label: eqa34

    E(d_c) = \left.\frac{\partial\sigma}{\partial u}\right|_{d_c}

By injecting the expression of :math:`u` and :math:`\sigma` this lead to :

.. math:: 
    :label: eqa35

    E(d_c) &= -\frac{d_c}{\pi R^2}\times \Big(\frac{dF}{dx}\Big) \Big|_{x=d_c}\\
         &= E_0 d_c^\alpha

In which the value of |E0| can be expressed as function of the power law exponent |alpha| and the prefactor |beta| :

.. math::
    :label: eqa36
    
    E_0 = - \frac{\alpha\beta}{\pi R^2}

Experimentally, the probed Young's modulus corresponds to the average mechanical
properties of the actin cloud between the surface of the actin bead and the
surface of the probe bead and do not reflect the variation of the mechanical
properties of the uncompressed actin cloud with position.
Physically :math:`E_0` correspond to the Young's modulus as a corrected distance of :math:`d_c = 1 \mu{}m` 
(See :num:`Fig #ev`)
The geometry of the
system and the fluorescence signal suggest a decrease of the density of the
actin cloud with the distance from the actin-bead center. All values
reported later represent estimation of elasticity of an effective Young's
modulus. The value of this effective Young's modulus are 3 orders of magnitude
smaller than the known elasticity of dendritic gels formed on beads that has been measured to be in the
order of kPa :cite:`Marcy2004`. 

This difference in elasticity might explain why the mechanical actions of this actin cloud as not been
seen before in other measurement like micro-pipette aspiration,
micro needle deformation or Atomic Force Microscopy indentation that have
sensitivities in the order of nN while the forces exerted by this actin cloud 
are in the order of pN.

Nonetheless, :cite:`Gardel2003` show that such low moduli can be obtain using
sparse entangle actin network, and confirm the idea that the actin-cloud seen
with the optical-tweezer indent experiments has a fundamentally different
structure than the dense dendritic network on the actin
bead surface.

.. _ev:
.. figure:: /figs/E0_violin.*
    :width: 80% 

    Young's Modulus prefactor as a function of Capping Protein show a decrease of
    average Young's modulus with an increase of Capping Protein concentration.


Mechanical properties
=====================
.. 3


To investigate the mechanical properties of the network that should arise from
a :math:`\alpha = -1` power law, we model the deformation of the actin cloud by
the theory of semi-flexible entangled polymer networks (:cite:`Isambert1996`,
:cite:`MacKintosh1995`, :cite:`Morse1998a`).


The Young's modulus of semi-flexible filaments in a 3D environment can be
expressed as a function of filament contour length density :math:`\rho` and the
entanglement length :math:`L_e` as :cite:`Morse1998b`:

.. math::
    :label: eqa37
    
    E= \frac{2.(1+\nu).7.k_BT \rho}{5L_e}

.. |nu| replace:: :math:`\nu`

In which |nu| is the Poisson ratio that allows the conversion from shear to
elastic modulus. Previous studies have investigated the non-linear stiffening of
such actin network for large deformation :cite:`Semmrich2008` and found that in
our condition, the linear description of theses networks holds to describe the
actin-cloud.

Similar to :cite:`Morse1998a` we express the entanglement length as a
function of persistence length and filament density: :math:`L_e\approx L_p^{1/5} \rho^{-2/5}`. We can
reduce the expression of the Young's modulus to a function of the following
parameters : 

    - The Poisson Ratio |nu|, 
    - The persistence length of actin filaments :math:`L_p`
    - The mesh size of the network :math:`\xi_0^2 = \rho_0`
    - The "size" of the cloud, for which we use the distance at which the force
      is first significant :math:`d_0`

We need also to consider that for a general compressible material, the
only variable that changes during compression is the density :math:`\rho`
which can be expressed as a function of the corrected distance :math:`\rho \to
\rho(d_c)`

Thus leading to :


.. math::
    :label: eqa

    E(d_c)=\frac{ (1+\nu).14.k_BT}{5L_p^{1/5}}\times \rho(d_c)^{7/5}


The scaling exponent of |E| in equation :eq:`eqa` with |dc| should match the exponent
of the experimentally found power law |alpha|. Thus the density can be
expressed in the following form : 

.. math::
    :label: eq-rho

    \rho(d_c)=\rho_0(d_c/d_0)^{5/7\times\alpha}

By the definition of :math:`\rho` in :cite:`Morse1998a` which is
the filament contour length per unit volume, we can determine the 
mesh-size :math:`\xi_0` of the undeformed network: 

.. math::
    :label: eqa38

    \xi_0 = 1/\sqrt\rho_0


By comparing this to the phenomenological fit we can express the elastic
modulus as a function of the distance and the mesh size, as a function of the
fit parameters and characteristic scales of the system.


.. math::
    :label: eqb
    
    E(d_c)     &=  \frac{(1+\nu).14.k_BT}{5L_p^{1/5}\xi_0^{14/5} \left.d_0\right.^{\alpha}}\times \left.d_c\right.^{\alpha}.\\
                    &=  E_0' \times \left.d_c\right.^{\alpha}

In which :math:`E_0'` can be identified as |E0| in :eq:`eqa` to extract the
closed form solution for the mesh size :math:`\xi_0` :

.. math::
    :label: eqa39

    \xi_0=\left(-\frac{({2-\frac{5}{7}\alpha)}.k_BT\pi R^2}{5\alpha \beta L_p^{\frac{1}{5}}\left.d_0\right.^{\alpha}}\right)^{\frac{5}{14}}


The found mesh size is in the order of 0.3 to 0.4 µm which is consistent with previous findings 
:`Morse1998b`. The variation of the
mesh size can be seen on :num:`figure #xi-violin` and does not seem to have a
correlation with the concentration of Capping Protein. 


.. _xi-violin:
.. figure:: /figs/xi_violin.*
    :width: 80%

    Meshsize vs Capping plot.

We explore the correlation between the mesh size and |delta| by plotting  the mesh size again the distance offset |delta| (:num:`Fig #dxcf`).
:num:`Figure #dxf` shows the relation between the mesh size and the offset
distance |delta| independently for each concentration of Capping Protein.

.. Despite the fact that the  mesh size is directly related to the offset distance
.. correction |delta|, a strong correlation can be seen between the two on
.. .  This can be explain despite the fact that |delta|
.. seem correlated with the Concentration in capping protein through the
.. non-appearance of time in our data analysis.  We will see in a later point that
.. the value measured for |delta| might be influenced by the time of measurement.


.. _dxcf:
.. figure:: /figs/delta-xi-corr.*
    :width: 100%

    Correlation of the meshsize :math:`\xi_0` with the distance offset |delta|,
    with marginal distribution as histogram on the side and on the top.  Shaded
    regions represent confidence interval at 95%.


.. _dxf:
.. figure:: /figs/delta-xi-facets.*
    :width: 100%

    Same figure as :num:`Fig #dxcf` for each concentration of Capping Protein,
    with linear regression and confidence intervals at 95%.

From :eq:`eqa` and :eq:`eqb` by identifying the prefactor it is also possible
to extract the Poisson ratio (|nu|) of the compressed material : 
    
.. math::
    :label: nu=f(alpha)

    \nu =\frac 1 2 \times \left( \frac 5 7.\alpha +1\right)


The Poisson ratio depends only on the powerlaw exponent and thus varies little
with the amount of Capping Protein concentration.  We found value of the
Poisson ratio that are between 0.1 and 0.2 corresponding to compressible
foam-like materials that do not expand highly in the direction orthogonal to
the compression axis. Previous study of bulk actin network find a Poisson
ration of 0.5 (incompressible material) for actin concentration of 21.5 µM.  We
suspect that the low actin concentration used in our experiments (4µM) is the
reason for the low Poisson Poisson Ratio. Also the local structure of filaments
emanating from the  bead may explain the large compressibility of our actin
cloud.

.. The lower
.. value we find which are closer to Poisson ratio of polymer network can be
.. explain by the five fold decrease of actin concentration that we use here (4µM)
.. and the different structure of the actin cloud we measure here.

Interpretation
==============
.. 3

The results of our data analysis lead to the interpretation that 
a dense actin gel of elasticity close to ~1kPa is polymerized
on the surface of the actin bead. This stiff gel
cannot be indented by the optical tweezer. Beyond this dense gel a soft
actin cloud with an effective elastic modulus of 1 Pa and below is
present and extends on distances that are several times bigger than the thickness
of the reconstituted actin cortex (:num:`Fig #fig-interpretation`). The
structure of this actin cloud is expected to be quite different from the
dendritic gel and be mostly constituted of loosely entangle actin filaments. 

In this model, the offset distance |delta| correspond to the limit of the dense
dendritic actin network mimicking the actin cortex that grows on actin beads. 
The high elastic modulus of this gel makes it impenetrable by the small forces generated by the optical tweezer we use. The
value of |delta| we found are coherent with the measured thickness :math:`e
\simeq \delta - 2.R_{bead}` of the  biomimetic actin cortex as measured by
epifluorescence in :cite:`Kawska2012` and found to be in the range of 1 to 2 µm. The decrease
of |delta| with Capping Protein is also coherent with the decrease of gel
thickness. 

.. The value of |delta| close to the bead radius also correspond to the
.. absence of formation of biomimetic cortices in the absence of Capping Protein.

The filaments composing the actin cloud emanate directly from the actin
cortex in which the nucleation of actin polymerisation started at the surface
of the bead. Eventually, a few filaments can escape from the network and are
capped by the Capping Protein only when the growing extremity is already several
micrometers from the bead surface. 

.. _fig-interpretation:
.. figure:: /figs/interp-delta.*
    :width: 90%

    A ) Schematic of an actin cloud. Left:  The actin bead triggers actin
    polymerisation. Right Probe Bead. On the surface of the actin bead a dense
    and dendritic network forms a biomimetic actin cortex with an elastic
    modulus close to the kPa (Dark Green). From this actin cortex emanates a
    softer actin structure : The actin cloud . The actin cloud is a loosely
    entangled network formed by the filaments escaping from the bead's actin
    cortex and extending over several micrometers. The actin cloud has an average
    elastic modulus which is several order of magnitude softer than the actin
    cortex. B ) From the point of view of the probe bead in optical tweezer, the
    system (actin-bead+actin cortex) behave as a hard-sphere of radius
    :math:`\delta-R`


The thickness of the actin cortex :math:`e` as measured in :cite:`Kawska2012`
increases with time during the polymerisation of actin. We can predict that the
offset distance |delta| should increase with time, except in the absence of
Capping Protein where no actin cortices form. This can be verified on
:num:`figure #time-delta-corr` that shows the evolution of |delta| as a function
of polymerisation time. 

.. _time-delta-corr:
.. figure:: /figs/time-delta-corr.*
    :width: 90%

    Distance offset |delta| as a function of time (min) since mix of actin, ATP
    and beads. Linear fit with confidence interval at 95% (light shaded area)
    and bead surface (dark shaded area). Samples taken in the absence of Capping
    Protein are not taken into account in the regression (Pink +). The increase
    of |delta| with time is coherent with the measured increase of the gel
    thickness :math:`e` as measured in :cite:`Kawska2012`


Relaxation phase
****************
.. 2

The approach phase of the indentation cycle has been modeled with a purely
elastic mode. However, the force distance plot shows a significant dissipation
marked by an hysteresis :num:`Fig #force-distance`. The repetitive indent cycle giving the same
force-distance curves (:num:`Fig #reproc`) allow to exclude a plastic deformation. 
We can hence reject the hypothesis of ruptures of the
actin meshwork or breakage near the entanglement points.

The theory of entangled filaments networks that allowed us to understand the link between the phenomenological
model and the mechanical properties of the network also proposes a relation to
explain the relaxation of the network. 

In this model :cite:`Morse1998a`, the visco elastic modulus  |E| is a function of time
and can be written as :math:`E(t) = E\times \chi(t)` with 

.. math::
    :label: chi

    \chi(t)=\sum_{n, odd} \frac{8}{n^2 \pi^2}exp\left(- \frac{n^2\pi^2 t}{ \tau_{rep}} \right)

.. |Drep| replace:: :math:`D_{rep}`
.. |tau| replace:: :math:`\tau_{rep}`

In which :math:`\tau_{rep} = \frac{l_f^2}{D_{rep}}` is a single fit parameter
that depends on diffusion constant for filament reptation |Drep| and the
filaments length :math:`l_f`. In this form, :math:`\chi` is a sum of
exponential decays with well defined characteristic timescales and amplitudes
that decrease as :math:`1/n^2`. To fit this model to the data of the
relaxation phase, we can limit ourselves to the first 40 terms of the sum as
any of the subsequents terms represent timescales we cannot reach with our
experimental resolution. 

It should be noted that the value of :math:`\chi(t=0)` is 1 and should be
treated particularly in order to insure continuity of the force applied on the
actin-bead in the model.

Using this sum of exponential decays is coherent with the common findings of
power-laws found in the frequency-dependant shear modulus of both `in vivo` and `in vitro` actin
networks as well as the relaxation behavior found in cells.

In order to determine :math:`\tau_{rep}`, the Young's modulus determined in the
approach phase is used and the model is fitted against the relaxation data.  A
result of such a fit can be seen on :num:`figure #fit-3-phases`. The value of
|tau| are highly variable and the fit can be difficult when the relaxation is
slow or in the order of the measured noise. Variation of |tau| with the
concentration in Capping Protein can be seen on :num:`figure #tau-violin`, and
one example of fit on the :num:`figure #fit-3-phases`

.. _fit-3-phases:
.. figure:: /figs/3phases.*
    :width: 80%

    Force as a function of time as well as fit for the 3 phases, approach,
    relaxation and retraction.

.. _tau-violin:
.. figure:: /figs/tau_violin.*
    :width: 80%

    Violin plot showing the repartition of |tau| as a function of capping
    protein. Outlier (|tau| negative or greater than tens of minutes removed)




We can see here that the polymer model introduced in :cite:`Morse1998a` allows
to completely fit the succession of approach and relaxation phases.  To check if
the fit parameters give realistic value, we can estimate the diffusion constant
for filament reptation |Drep|. 

.. math:: 
    :label: eqa3-10

    D_{rep} &= \frac{k_bT}{\gamma l_f} \\


In which :math:`\gamma\approx {2\pi\eta_s}/{ln(\xi_0/d_f)}` is the friction
coefficient per unit length. :math:`\gamma` depends on the solvent viscosity
:math:`\eta_s`, the mesh-size :math:`\xi_0` and the filament diameter
:math:`d_f` (:math:`~7nm` for actin).  We use :math:`\eta_s=10^{-3} Pa\times s`
for water and a mesh size in the order of 400nm as determined from the approach phase
(:num:`Fig #tau-violin`). Using |tau| given by the fit, this lead to filaments
length ranging from 3 to 8 µm, which is consistent with TIRF experiments and simulation as done in :cite:`Kawska2012`.


Retraction Phase
================
.. 3

During the retraction phase the force decreases, becomes negative after a
retraction of 3 to 4 µm, and show a slow  return to 0 at large distance.
Sticking events can be seen when the force becomes abruptly negative before
relaxing as fast. :num:`Figure #sticking-event` shows such a sticking even
happening during an indentation cycle.

.. _sticking-event:
.. figure:: /figs/sticking-event.*
    :width: 80%

    A sticking event at :math:`d=15\mu{}m` where the force can be seen decreasing rapidly
    up to -18 pN before quickly returning to its normal value. A second smaller
    sticking even is present at :math:`d=12\mu{}m` Sticking even appear roughly 20% of
    the experiments.

We assume that the sticking events are characteristic to non-specific interaction
between the probe bead and the actin cloud.  In the case when no sticking event
is present, we assume partial closing of the actin cloud beyond the
probe bead during the relaxation phase and model the retraction curve as a
transition between the damped-approach curve and a penetration of the probe
bead through the closing actin cloud.

During the approach phase the force exerted on the actin-bead is
:math:`F(d)=\beta(d-\delta)^\alpha`. During the relaxation phase the force
decrease from :math:`F(t_1)` to :math:`F(t_2)` with the relation :

.. math::
    :label: eqa311

    \frac{F(t_2)}{F(t_1)} = \chi(t_2-t_1)

We can write that the force exerted on the actin-bead during the retraction can
be written as a sum of the force felt during the approach, damped during the
relaxation (:math:`F_{da}`), plus a force due to the closing of the actin
network behind the bead :math:`F_{closing}`.

.. math::
    :label: eqa312

    F_{ret}(d) &= F_{da}(d) + F_{closing}(d)\\
    F_{ret}(d) &= \chi(t_2-t_1).\beta(d-\delta)^\alpha+ F_{closing}(d)

:math:`F_{closing}` is computed using the fit parameter |alpha|, |beta|, |delta| and :math:`\tau_{rep}` (:num:`Fig #retract-powerlaw`).

On a double logarithmic scale and at long distance :math:`F_{closing}` also seem to
follow a power law (:math:`F_{plaw}`), when no sticking events are present.

.. _retract-powerlaw:
.. figure:: /figs/retract-powerlaw.*
    :width: 100%

    Left : Retraction phase with approach phase fit damped by
    :math:`\chi(t_2-t1)` in green. Blue area under the curve is plotted on a
    log-log scale on the right, follow a powerlaw.


:math:`F_{ret}(d)` seems though to follow the force felt during the approach phase, damped by :math:`\chi(t)` (:math:`F_{da}`) for :math:`d
\simeq{D_{bead}}` and :math:`F_{da}+F_{plaw}` for :math:`d > 10\mu{}m`.  The
typical size of the bead being :math:`D_{bead}` we expect the transition from
one regime to the other to be done on a length scale of :math:`D_{bead}` Thus
we use a smoothing function which is a convolution between the projected bead
area and a linear ramp function which can be seen on :num:`figure #interp`

.. _interp:
.. figure:: /figs/interpolation.*
    :width: 90%

    Interpolation function used to smooth the transition from :math:`F_{da}` to
    :math:`F_{da}+F_{plaw}` 


The complete retraction force can be seen on :num:`figure #fit-3-phases` and is equal to 

.. math::
    :label: eqa314

    F_{ret}(d) &= F_{da}(d)\times(1-S(d)) + F_{plad}(d)\times S(d)\\


Where :math:`S(d)` is the interpolation function for a bead of 4.34 µm
diameter. We can see that the model represents correctly the retraction and especially
the position and value of the minimum of the retraction function without
fitting parameters when we use the diameter of the probe bead as a typical scale
for the transition when changing direction.

Discussion
**********
.. 2


The actin cytoskeleton plays an important role in many cellular functions.  The
actin cortex, just beneath the cell membrane is not only a crucial structure
for cell motility and the mechanical properties of the cell, it is also an essential
component in cell division and the positioning of the spindle.
Other actin structures, that spawn from the nucleus to the cell membrane are
responsible for cell organelle positioning like in plants where the nucleus is found
towards the anticlinal wall of the cell :cite:`Iwabuchi2010`, or during
nurse cell maturation where the nucleus is pushed away from the dumping channel:cite:`Huelsmann2013`. The mechanical link from the
outside of the cells to the nucleus using actin bundles has already been show previously
:cite:`Jaalouk2009`. We show here that these actin structure should not be the
only one taken into account to explain organelles positioning.


Our experiments show the existence of a sparse and stiff actin cloud emanating
from a biomimetically reconstituted actin cortex.  This actin cloud is capable
of staining forces of tens of pico Newtons, enough to hold organelles in place. Using polymer physics
we are able to model the behavior of such an actin cloud and
measure many of its mechanical properties. It provides an
actin scaffold capable of deforming non-plastically. At time scale of few
seconds if behaves mostly elastically with an elastic module of a few Pascal.
The Poisson ratio of the actin cloud varies from 0.1 to 0.2 hinting for a
sparse structure of loosely entangle filaments forming a meshwork with a
typical mesh size of 300 to 400 nm. 

The filaments at the origin of this loosely entangled network would emanate from
the dense actin cortex that can be seen and simulated on actin-beads
:cite:`Kawska2012` and the evolution of parameters of this actin cloud are
coherent with the preceding studies on biomimetically reconstituted actin
cortices. Recently, the role of actin networks with similar properties as the
actin cloud have been described in cells such as `Xenopus` Oocyte
:cite:`Feric2013`. Poisson ratios of actin networks have been
measured in bulk to be higher :cite:`Gardel2003` but are not inconsistent with our measurement at lower actin concentration.

.. that what found here, but
.. cannot explain the low or even negative Poisson ratio that can be found in
.. pluripotent cells :cite:`Pagliara2014`. 


The actin cloud provides a novel structure that should be studied further to
understand the positioning of organelles in cells and to study which role this sparse
actin structure plays in the formation of other actin networks inside cells.

In particular microrheology experiments could be performed on the growing actin
cloud in order to further characterize the frequency dependence of the mechanical
properties  of the actin cloud. The effect of cross linking and network
branching is crucial for the occurrence of symmetry breaking on bead systems, and
would likely play a role in the structure of the actin cloud. A confined
geometry and direct polymerisation on membrane, or the effect of myosin motors
might allow to alter the properties of the actin cloud.

All these could be cellular mechanisms to use the actin cloud in order
to efficiently form structures needed for its function.
Further studies of the actin cloud on biomimetic or `in vivo` system are
challenging, but would lead to a better understanding of the mechanics of the
cells and its control.

A Paper based on this study has been accepted for publication in Biophysical
Journal and is added for information as appendix of this manuscript.
