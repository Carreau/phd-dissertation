.. Actin Cloud:

Mechanical properties of a far reaching actin cloud
###################################################
.. 1

Introduction 
*************
.. 2

We have seen that the actin cytoskeleton plays a major role in
cellular mechanics.Essential for force generation, it is a
key component for cell motility. It has also been extensively studied both in
cells and biomimetic systems. 

Actin can form a variety of cells networks, ranging from dense branched
networks at the lamellipodia leading edge to bundled parallel structures
forming the filopodia.  The actin network reconstruction has been achieved in
biomimetic systems using purified components :cite:`Plastino2005`,
:cite:`Loisel1999`, :cite:`Bernheim-Groswasser2002`,  :cite:`Pontani2009`, and
many properties of these networks have been measured.

It has been determined that the actin cortex provides mechanical support for the
plasma membrane and that it extends over a few hundreds of nanometers.Many
cellular processes hint that actin structures connected to this cortex, are
key elements in organelle and chromosome positioning.

In this part of the manuscript, we will investigate how a sparse actin structure can
emanate from the actin cortex, and explore its properties. Through the use of the
:ref:`bead-motility <bead-motility-assay>` biomimetic system aiming at reconstituting
the actin cortex and its dendritic structure, we will show that a sparse actin filaments network 
emanating from the cortex has a mechanical effect, sufficient to
displace objects of cells organelles size at distances up to tens of micrometers
away from the actin cortex. 

The actin cortex branched structure underneath the plasma membrane of
cells implies a structure governed by Arp2/3. To what extend can Arp2/3 and CP be used
to form a biomimetic actin cortex has already been widely studied. In
:cite:`Kawska2012`, both `in vitro` measurements on reconstituted actin cortices
on beads and simulations investigate the effect of cross-linking and
Capping Protein on the formed actin gel. It can be observed both experimentally and in
simulation that a filaments network escapes from what is defined as the actin
cortex (:num:`Figure #fig-bead-tirf`). The effect of these long filaments is not taken into account in the
`in-silico` system, where the analysis is restricted to filaments shorter than 10
µm. The effect of dense entangled actin networks generated from
randomly placed primers on the bead surface only participates in the tension increase and
contributes to symmetry breaking.

.. _fig-bead-tirf:
.. figure:: /figs/Bead-tirf-fluo-sim.png
    :width: 70%

    Upper Left : Fluorescence image of an actin bead with a growing actin
    cortex. Escaping filaments form the actin cloud that can  hardly  be seen
    in fluorescence. Scale bar is 2 µm. Lower Left: Total Internal Reflexion
    (TIRF) image of actin polymerising on an actin bead. Escaping filaments can
    directly be observed. The gray circle represents the bead size.  Right :
    Representation of the actin growth simulation with delimitation between the
    entangled branched actin network and escaping filaments.  Adapted from
    :cite:`Kawska2012`.


The limit of the dense network, visible in epifluorescence, is defined in
:cite:`Kawska2012` by the position of the half-maximum fluorescent intensity (:num:`Figure #fig-intensity-profile`).
The networks properties are measured by :cite:`Pujol2012` using
magnetic beads and phalloidin-stabilized actin. Though, they do not
investigate the sparse and softer actin networks that originate from the visible
part.


Using :ref:`time-shared optical tweezer <time_shared_ot>` we are able to probe
the mechanics of this soft actin structure at a timescale shorter than the
characteristic time of actin polymerisation and forces in the pN range. We will show
that beyond the dense dendritic network mimicking the actin cortex, which has
been measured to have an :ref:`elastic modulus <elastic_modulus>` in the order of
kPa :cite:`Pujol2012`, the soft actin cloud is much softer with
a stiffness in the Pa regime.  This might explain why such a
structure has not previously been observed with less sensitive techniques than optical
tweezers. The size of this actin cloud and its ability to sustain forces
suggest that in cells, the actin cortex is not sharply delimited and that
structures escaping from it may play a role in organelle positioning.


Hereunder are the questions we address in this part of the manuscript : 
How far does the soft part of the gel extend ? What are its precise mechanical properties?  How does it change
over time?  Is the actin cloud elastic or viscous?

.. _fig-intensity-profile:
.. figure:: /figs/intensity_profile_xnM_Arp_xnM_CP_xmin.*
    :width: 80%

    A) Epifluorescence image of polystyrene bead with a growing actin gel in
    presence of 25 nM of Arp2/3 and 25 nM of Capping Protein. Scale bar is 5
    µm.  B) Normalized intensity profile of fluorescence image with gel thickness
    shown with dashed line as defined in :cite:`Kawska2012` :
    Distance between maximum intensity and half-maximum intensity.  C)
    Epifluorescence image of log(intensity). D,E,F) Same as A,B,C, in absence
    of Capping Protein

Actin-Bead System
*****************
.. 2

Reproducing the actin cortex and studying the mechanics of actin structures
emanating from it :ref:`required 4.3 µm diameter polystyrene beads <bead_preparation>`
coated with a nucleation promoting factor. Theses beads were placed
in the :ref:`ATP mix buffer <atp_mix_buffer>` in presence of 25nm of Arp2/3
complex, 4µm of monomeric actin (20% fluorescently labeled), 12 µM profilin and
a variable amount of Capping Protein. :ref:`see Material and Methods <m_et_m>`.
These beads are referred to as actin-beads.

These conditions were chosen in order to grow a dense network on the actin-bead surface as in :cite:`Kawska2012`. We determined at an amount of 25nM ATP and a varying
amount of Capping Protein concentration in order to cover conditions where the
dense gel formed on the actin-bead was able to accumulate sufficient stress
to lead to symmetry breaking (CP between 15  and 35 nM, see part :ref:`Bead Motility Assay <bead-motility-assay>`). We also investigated
conditions where the amount of Capping Protein was too low (< 15nM) or too high
(>35 nM) to permit symmetry breaking.

.. .. _fig-phase-diagram:

We selected a 4.3 µm bead diameter in order to get a characteristic symmetry
breaking time of 20 to 40 minutes.
A smaller bead radius implies a
faster increase of stress and a shorter symmetry breaking time. 
Chosing 4.3µm provides sufficient time to proceed with the
experiments before symmetry breaking occurs. 

All measurements were made on an actively growing actin network which
was not stabilized before symmetry breaking
occurred for Capping Protein concentration in the range 15 to 35 nM :cite:`Kawska2012`.

Probe Bead System
*****************
.. 2

Beside actin-bead, the experiment required a polystyrene bead passivated
with BSA. These beads are referred to as probe-beads.  The probe-bead size, similar to the actin-bead’s, ensured the optical
trapping of both beads in the same observation plane. In the case of different beads diameters, the axial forces on the beads were different. This axial
displacement of the two beads during the indentation process led to a
component along the z-axis which  eventually pushed one bead out of the trap.




Experimental description
************************
.. 2

In order to probe the actin network, we trapped an actin-bead with a growing actin-network
and a probe-bead using time-shared :ref:`optical trap <time_shared_ot>`,  and
measured the forces on the actin-bead, using a QPD placed in the back focal plane of
the condenser (:ref:`material and methods <m_et_m>`).

Moreover, all force
recordings used for analysis were made on the static bead, in our case the actin bead, to avoid systematic errors of force measurements on the moving trap.


The indentation is a three step process (:num:`Figure #figindent-time`):

    - An approach phase at constant velocity 10µm/sec unless specified otherwise
    - A 3 second relaxation phase during which both traps remain static
    - A retraction phase  during which the probe trap returns to its initial position at 10µm/sec.


Approach Phase
==============
.. 3
 
During the approach phase, the probe-trap will approach the actin-trap at constant speed (10 µm/s), as shown in
:num:`figure #figindent-time` for times :math:`t < t_1`, and the actin-bead
will repel the probe-bead, due to the actin network growing on it. The force undergone
by the actin-bead will progressively increase during the probe-bead approach,
eventually reaching the maximum as the probe-trap reaches its nearest position
to the actin-trap. It should be noted that during this process, 
the force between the beads pushes  them out of their respective trap centers.   
The beads displacement in the trap remains negligible compared to the
distance between the two beads. Hence, in the following we will consider that the probe-bead speed is equivalent to the trap approach speed of 10µm/sec.


Relaxation Phase
================
.. 3

After the approach, the trap remains static for a 3 seconds relaxation phase 
. The relaxation phase starts at :math:`t_1` and
finishes at :math:`t_3` as shown on :num:`figure #figindent-time`. The duration of the relaxation phase is sufficient to allow the actin cloud  partial
relaxation but remains sufficiently short compared to
the actin polymerisation speed. Hence, the polymerisation is not expected to 
change the network properties during indentation cycle and repetitive indentation (:num:`Figure #reproc`)

While the actin network relaxes, the forces between the two beads will slowly
decrease, thus leading to the beads getting closer to their trap center and
to each other. There is a slight decrease in distance during the relaxation phase, compared to the distance between beads. The force decrease as well as
the minimal change in distance between the two beads can be observed on :num:`Figure #figindent-time`
in the middle part.

.. _figindent-time:

.. figure:: /figs/force_time.*
    :width: 70%
    
    Upper graph : Force as a function of time on the actin-beads.  Lower graph
    : distance between beads (distance between traps + beads
    displacement from the trap center) as a function of time. The first part of each graph
    (green curve, yellow back) represents the approach phase. The middle part
    (orange on white) corresponds to the relaxation phase, and the right part (blue on pale
    yellow) is the retraction. The observed data is a subsample of around 1 out of every
    1000 acquired points. We can see on the second graph that the beads
    displacement on their respective traps is negligible compared to the
    trap displacement and justifies the approximation of a probe-bead
    speed equivalent to the probe-trap speed.


Retraction part
===============
.. 3


After the three seconds of the retraction phase, the probe-trap returns to 
its  initial position at 10 µm/s (:math:`t > t_2`). During this phase, the force
exerted between the two beads decreases, becomes negative, reaches a minimum, and
eventually returns to zero as the probe-bead recovers its initial
position (shown on :num:`Figure #figindent-time` right part). Negative forces
represent the forces that tend attract the two beads towards each other.


Reconstitution of Force-distance-curve
======================================

The beads position in the trap as well as the force exerted on each bead can be
calculated from the position of the trap over time ( and the signal measured by the QPD. We can then recover the distance between bead centers as a function
of time.  The force-distance curve representing the force exerted by the
probe-bead on the actin-bead as a function of the distance can be computed and is
shown in :num:`figure #force-distance` where we can still distinguish the three
phases of the indentation cycle, also marked by the color used for the data. 



.. _force-distance:
.. figure:: /figs/force-distance.*
    :width: 80%

    Force exerted on the actin-bead as a function of the distance between the
    two bead centers. Colors and data are the same as in :num:`Figure #figindent-time`. 
    The probe-bead starts from the far right, and gets closer
    while the force increases (green upper part of the curve), reaches a
    maximum, and enters the relaxation phase (orange part), where the force
    between both probe-beads and actin-bead decreases, while the distance  also
    slightly decreases. During the retraction part (blue), the force rapidly
    decreases and  reaches negative values as   the bead returns to its initial
    position. The observed data is a subsample of 1 in every 1000 points of acquired
    data. Shaded regions represent areas where the two polystyrene beads should 
    interpenetrate.


Repetitive indent
=================
.. 3

The indentation cycle can be repeated several times every few seconds, to check for reproducibility and non-plastic deformation of the network after
indentation. As the network is constantly growing during the measurement, this
repeat also allows to check for possible changes of the network properties, due to actin
polymerisation. The force-distance plot is shown in :num:`figure #reproc` :num:`, #reproc-time`.


.. _reproc-time:
.. figure:: /figs/reproc-time.*
    :width: 100%

    Upper graph : Force exerted on actin-bead as a function of time for ten
    repetitive indents. In one of the cycles, a sticking event can be dentified in the
    retraction phase, 6 seconds after the beginning of the cycle. Lower graph:
    Distance as a function of time for  ten repetitive indents. The ten curves
    can hardly be distinguished from one another, which shows the
    reproducibility of indentation curves.


.. _reproc:
.. figure:: /figs/reproc.*
    :width: 80%

    Figure showing the indentation process reproducibility on a bead with
    25nM Arp2/3 and 10nM CP Subset of data from :num:`Figure #reproc-time` highlighted
    with different colors to represent the evolution of the indentation curve
    over time.  Time is relative to the first indentation. Shaded areas represent
    zones where the two beads should  interpenetrates.

Effect of approach speed
========================
.. 3

:cite:`Gardel2003` suggests that, for frequencies higher than 0.1 Hz, the force due to
the actin network viscous behavior can be in the same order as the one due to the elastic
component . In order to test whether such a relaxation effect is important, we measured the effect of the
approach speed on the force measurements. :num:`Figure #many-speed` presents the
indentation speed affecting the measurement by varying the approach speed from 10
to 30 µm/s on the same actin-bead.


.. _many-speed:

.. figure:: /figs/many_speed.*
    :width: 60%

    Approach phase of repetitive indents at multiple speeds on the same
    actin-bead. The approach phase in the different conditions is similar,
    hinting at  a negligible effect of the viscosity  in the actin cloud at the
    considered speed.


Experimental observations
*************************
.. 3

Through the use of the bead system, we are able to reconstruct actin cortices `in vitro` and
to investigate the mechanical properties inaccessible to other microscopy
techniques like TIRF. Beyond the visible actin cortex, we can detect the
presence of an actin structure with mechanical effects starting at
distances of :math:`> 10\mu{}m`, hence far beyond the thickness of the actin cortex (~1µm). 
:num:`Figure #cloud-repelling` presents a video qualitatively showing that the actin cloud growing
on actin-beads is able to repel free floating probe-beads, before they reach the
visible reconstituted cortex. 


In order to quantify the distance at which the probe-beads start to be affected by the actin-cloud,
we measured the experimental noise by studying the fluctuations of the trapped probe-bead.

During the indentation, we defined :math:`d_0` as the distance at which the
average force received by the probe-bead is higher than the experimental noise.
Typically the standard deviation is 2pN. 

The repartition of :math:`d_0` with the concentration of Capping Protein is
plotted in :num:`figure #d0-violin`.

 
 
.. _cloud-repelling: 

.. figure:: /figs/cloud-repelling.png
    :width: 85%

    Chronophotography representing the displacement of a trapped actin bead in a
    solution including probe-beads. During this experiment, the actin bead is kept
    static in the optical trap (marked by the cross) while the stage is moved.
    Scale bar is 5 micrometers. The total movie duration is 21 seconds.


.. _d0-violin:
.. figure:: /figs/d0_violin.*
    :width: 65%

    Repartition of the bead-center distance at which the actin cloud exerts a
    force higher than the noise (:math:`d_0`) on the probe-bead, as a function of
    Capping Protein. The shaded region represents the bead surface position     (4.34 µm) and the red line represents the bead surface+1µm (upper bound for
    the in vitro
    Capping Protein concentration). The shaded region represents the bead surface position(4.34 µm) and the red line represents the bead surface+1µm
    (upper bound for the in vitro
    reformed actin cortex measured in :cite:`Kawska2012`). We can see in this graph that for symmetry breaking
    conditions (CP 10 nM and 30 nM, the distance at which the actin cloud starts to apply
    forces on the probe-bead is larger than the thickness of the actin
    cortex. The distance at which the probe-bead is able to detect the presence
    of the actin cloud decreases when increasing the concentration of the Capping
    Protein that restricts  the actin filament growth. The condition in the absence
    of Capping Protein is a particular case, as no dense actin network forms
    on the surface of the actin bead. 

Approach phase modeling
=======================
.. 3

We
decided to model each part (approach, relaxation and retraction) independently, to extract their mechanical properties, by using the three phases of the experiment.
In particular, we fitted the force-distance curve of the approach phase using a power
law with 3 fit parameters :math:`\alpha, \beta, \delta`:

.. math::
    :label: eqa31

    F(d) = \beta \times \left(d-\delta\right)^\alpha

in which :math:`F` represents the force exerted on the probe-bead, and :math:`d`
is the distance between bead centers. The power law exponent :math:`\alpha` is
expected to be negative as the force decreases with the distance :math:`d`, and
to characterize how fast the force increases as the two
beads approach each other. The prefactor :math:`\beta` acts as a scaling factor of the
force. The offset parameter :math:`\delta` shifts the curve on the distance
axis. This phenomenological model presents the particularity that the force on the probe bead tends to
:math:`+\infty` when the distance :math:`d` gets  to :math:`\delta`. The force
is undefined for values of :math:`d< \delta`. Hence, the offset distance :math:`\delta`
practically describes the distance at which the optical trap is no longer able to
indent the network. 

In the case of a hard sphere, the value of :math:`\alpha` would tend towards
:math:`-\infty` leading to a infinite force increase at the contact between the
two hard-spheres of same diameter, and a value of :math:`\delta` equal to the
diameter of the hard sphere.  In this case :math:`F(d>\delta)=0` and
:math:`F(d<\delta)=\infty`

The used optical tweezer being able to apply forces up to 20pN, and the beads
having a diameter of 4.34µm , we hence determined a cross-sectional surface of roughly :math:`14.7\mu{}m^2`. Before 
escaping the trap, the probe-bead did move up to 1µm from its
trap center. To estimate the maximal stiffness acchievable, we considered that we could
provide a clear measure of deformation in the order of 1/10 of µm,  this
leading to a maximum detectable Young's modulus of :

.. math::
    :label: eqa32a

    E_{max} &\sim \frac{F_{max}L_{0,max}}{A_0.\Delta L} \\
            &\sim \frac{50.10^{-12} \times 1.10^{-5} }{  (\pi\times 2.17\times 10^{-6})^2 \times 1.10^{-7}              }\\ 
            & \sim 300 Pa

Any material with a stiffness much higher than 300 Pa can be considered as
infinitely rigid.


The elasticity of dense actin gels around polystyrene beads has been measured
in :cite:`Pujol2012` and found to be in the order of kPa.  Therefore, the
optical tweezers are not able to probe the mechanics of the dense gel on the
bead surface. The value of :math:`\delta`  is expected to be :math:`> 4.34 \mu{}m` as it partially includes the dense actin gel.

The model can be fitted independently on each experimental
approach phase. An example of such a fit is shown in
:num:`figure #force-distance-fit` and the fit quality can be measured by the
coefficient :math:`R^2` which has a media value of `0.97`
across all fits.

.. _force-distance-fit:
.. figure:: /figs/force-distance-fit.*
    :width: 100%

    Power law model fitted on the approach phase data for one experiment in the
    presence of [CP]=10nM, with the particular values found for the fit
    parameters.  The vertical line represents the point where the model
    diverges and the force goes to infinity, that is to say :math:`\delta`. The
    shaded region corresponds to the distance at which the two beads should
    interpenetrate. Relaxation (orange) and retraction (blue) data are not fitted.


The approach phase data can be corrected for the distance offset :math:`\delta`
and plot in a log-log scale allowing for a better appreciation of the fit
result (:num:`Figure #force-distance-log-log`). The corrected distance is noted with  `c` indices :math:`d_c = d-
\delta`. In the model the force tends to infinity at :math:`d_c = 0`.




.. _force-distance-log-log:
.. figure:: /figs/force-distance-fit-loglog.*
    :width: 80%

    Force on the actin bead  during the approach phase as a function of bead distance
    minus distance offset :math:`\delta` plotted on a log-log scale. Black line
    represents the power law model with the offset distance correction. Same
    data as :num:`Figure #force-distance` but showing only the approach phase. 


In our experiments, the polystyrene beads have an average diameter of 4.34 µm,
thus we expect :math:`\delta` to be higher than the bead diameter, since the beads cannot interpenetrate.  Data with
:math:`\delta` values lower than 4.34 µm (21 out of 127) are considered as
unphysical and removed from further analysis.

As expected, we found negative values for :math:`\alpha`. Surprisingly, the value
of alpha does not vary significantly when comparing experiments with different
amounts of Capping Protein and remains close to -1, with a mean value of -1.10, and
a standard deviation of 0.38. The distribution of the power law exponent can be
seen on :num:`figure #power-law-exponent`

.. _power-law-exponent:
.. figure:: /figs/alpha_violin.*
    :width: 60%

    Right : Violin plot showing the repartition of power law exponents as a function of concentration in Capping Protein. Left: distribution of power law exponent
    :math:`\alpha` regardless of the concentration in Capping Protein. Value of
    exponent lies close to `-1`.


Due to the scale invariance of the inverse power law found above,  all the
approach phases data can be rescaled into a single master-curve (:num:`Figure #fig-rescale-powerlaw`). This is achieved
by dividing the force by the maximum force :math:`F_{max}` reached during the
approach, and rescaling the distance by the minimum approach distance from which
:math:`\delta` is subtracted. 

.. _fig-rescale-powerlaw:
.. figure:: /figs/rescaled_power law.*
    :width: 70%

    Representation of rescale approach data on a log-log scale.  Red and green
    crosses correspond to average values. Blue area corresponds to average +/-
    standard deviation for each average bin. Red dot in the upper right corner
    corresponds to the point (1,1) with respect to which all data have been
    rescaled.
    
    Blue dashed line shows a power law fit of the average data for
    :math:`d_c/d_{c,min} < 10` (red cross), fitted slope is :math:`-1.06` . 
    As an eye guide, the slopes of `-1` and `-1.5` have been represented. 
 


The rescaled data confirm an average power law exponent of :math:`\sim -1`, the
breakdown of the average exponent beyond :math:`d_c/d_{c,min}=10` can be
explained by the statistical effect due to a lack of data for long distance.




Variation of parameters with Capping Protein
============================================
.. 3

At the chosen concentration of Arp2/3, the bead system can show symmetry
breaking in the correct range of a Capping Protein concentration of 10 to 30
µM. In absence of Capping Protein, the dense dendritic network does not form on
the surface :cite:`Kawska2012`. At low Capping Protein concentrations (:math:`<10 \mu{}M`) it seems not able to generate enough stress to
rupture, and at too high concentrations (>35nM, the visible gel is thin and does
not break symmetry either. We then investigated the variation of each fit parameters for Capping Protein concentrating ranging from 0 to 50 nM.


We have already,  seen  that the power law exponent factor |alpha|
didn't vary with the amount of Capping Protein in solution (:num:`Figure #power-law-exponent`). 
The two other investigated parameters are the prefactor
:math:`\beta` and distance offset :math:`\delta` . For the same value of :math:`\alpha` and :math:`\delta`, the
higher :math:`\beta` is, the stronger the interaction between the two beads for
the same distance |dc|. We can see on :num:`figure #beta-violin` that the
average value for the prefactor decreases in accordance with the increasing of Capping Protein
concentration. 

.. _beta-violin:
.. figure:: /figs/beta_violin.*
    :width: 80% 

    Violin plot showing the repartition of the prefactor with the quantity of
    Capping Protein. The decrease of prefactor with an increasing amount of Capping
    Protein indicates a lower force between the probe-bead and the actin bead,
    for the same corrected distance between bead centers. 

The last parameter of our model is :math:`\delta`, the distance at which the force
diverges.   It can be seen in :num:`figure #delta-violin` that with the exception
of zero Capping Protein, the distance at which the model diverges gets
closer to the polystyrene bead diameter, as the concentration of Capping
Proteins in the medium increases. It is interesting to note that the distance offset
|delta| is very close from the bead diameter in the absence of Capping Protein, when no
biomimetic actin cortices forms.  

.. _delta-violin:
.. figure:: /figs/delta_violin.*
    :width: 80% 

    Violin plot showing the variation of the offset distance :math:`\delta`
    with the Capping Protein concentration. The shaded area represents the
    non-physical region which would correspond to a diverging force beyond the
    contact of the two polystyrene beads. Experimental data with :math:`\delta`
    value in this region have been excluded from further analysis.


Determination of Young's Modulus
================================
.. 3


.. |E| replace:: :math:`E`

.. |dc| replace:: :math:`d_c`

.. |delta| replace:: :math:`\delta`
.. |alpha| replace:: :math:`\alpha`
.. |beta| replace:: :math:`\beta`

.. |E0| replace:: :math:`E_0`

In order to determine the gel mechanical properties between the actin and the
probe bead, we modelled it as a purely elastic material. The viscous effects are
neglected in the approach part, as the approach at different speeds shows no
clear effect on the approach curves (:num:`Figure #many-speed`). We considered
the compression of the material between the two beads. The surface of the
compressed material is approximated by the bead projected surfaces of the bead along the
direction of compression (:math:`\pi R^2`).  The thickness of the compressed
material is regarded as the distance between bead centers corrected by the
distance offset |delta|, as any material below delta can be considered as
infinitively rigid for the optical tweezer.

The stress exerted onto the material projected onto the bead surface or radius
:math:`R` can be written : 

.. math::
    :label: eqa32
    
    \sigma = \frac{F}{\pi R^2}

For a minor deformation, the local strain of the material :math:`u` can be written
as a function of the corrected bead position |dc| and the considered location
along the axis between the two bead center as :math:`x` : 

.. math::
    :label: eqa33

    u(x)= \frac{d_c-x}{d_c}


We can express the local differential strain around the bead position |dc| : :math:`\partial u = -\partial x/ \partial d_c` in which the minus sign
reflects the choice of the coordinate system: a decrease in :math:`x` with a
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

in which the value of |E0| can be expressed as function of the power law exponent |alpha| and the prefactor |beta| :

.. math::
    :label: eqa36
    
    E_0 = - \frac{\alpha\beta}{\pi R^2}

Experimentally, the probed Young's modulus corresponds to the average mechanical
properties of the actin cloud between the actin bead surface and the
probe-bead surface and does not reflect the variation of the uncompressed actin cloud mechanical
properties with position.
Physically :math:`E_0` corresponds to the Young's modulus as a corrected distance of :math:`d_c = 1 \mu{}m` 
(See :num:`Figure #ev`)
The geometry of the
system and the fluorescence signal suggest a decrease of the actin cloud density according to the distance from the actin-bead center. All values
reported later represent an estimation of the effective Young’s modulus elasticity. The value of this effective Young's modulus is 3 orders of magnitude
smaller than the acknowledged elasticity of dendritic gels formed on beads, measured in the
order of kPa :cite:`Marcy2004`. 

This difference in elasticity might explain why the mechanical actions of this actin cloud have not been
confirmed before in other measurements, like micro-pipette aspiration,
micro needle deformation or Atomic Force Microscopy indentation that have
sensitivities in the order of nN, while the forces exerted by this actin cloud 
are in the order of pN.

Nonetheless, :cite:`Gardel2003` shows that such low moduli can be obtained using
sparse entangled actin networks, and confirms the idea that the actin-cloud seen
with the optical-tweezer indent experiments, has a fundamentally different
structure than the dense dendritic network on the actin
bead surface.

.. _ev:
.. figure:: /figs/E0_violin.*
    :width: 80% 

    Young's Modulus prefactor, as a function of Capping Protein, shows a decrease of the
    average Young's modulus with an increase of Capping Protein concentration.


Mechanical properties
=====================
.. 3


To investigate the mechanical properties of the network that should arise from
a :math:`\alpha = -1` power law, we modelled the actin cloud deformation by
the theory of semi-flexible entangled polymer networks (:cite:`Isambert1996`,
:cite:`MacKintosh1995`, :cite:`Morse1998a`).


The Young's modulus of semi-flexible filaments in a 3D environment can be
expressed as a function of the filament contour length density :math:`\rho` and the
entanglement length :math:`L_e` as :cite:`Morse1998b`:

.. math::
    :label: eqa37
    
    E= \frac{2.(1+\nu).7.k_BT \rho}{5L_e}

.. |nu| replace:: :math:`\nu`

In which |nu| is the Poisson’s ratio that allows the conversion from shear to
elastic modulus. Previous studies have investigated the non-linear stiffening of
such actin networks for large deformation :cite:`Semmrich2008` and found that in
our condition, the linear description of these networks holds to describe the
actin cloud.

As :cite:`Morse1998a` we expressed the entanglement length as a
function of persistence length and filament density: :math:`L_e\approx L_p^{1/5} \rho^{-2/5}`. We can
reduce the expression of the Young's modulus to a function of the following
parameters : 

    - The Poisson’s Ratio |nu|, 
    - The persistence length of actin filaments :math:`L_p`
    - The mesh size of the network :math:`\xi_0^2 = \rho_0`
    - The "size" of the cloud, for which we use the distance where the force
      is first significant :math:`d_0`

We also need to consider that for a general compressible material, the
only variable that changes during compression is the density :math:`\rho`
which can be expressed as a function of the corrected distance :math:`\rho \to
\rho(d_c)`

Thus leading to :


.. math::
    :label: eqa

    E(d_c)=\frac{ (1+\nu).14.k_BT}{5L_p^{1/5}}\times \rho(d_c)^{7/5}


The scaling exponent of |E| in equation :eq:`eqa` with |dc| should match the exponent
of the experimentally found power law |alpha|. Thus, the density can be
expressed in the following form : 

.. math::
    :label: eq-rho

    \rho(d_c)=\rho_0(d_c/d_0)^{5/7\times\alpha}

By defining :math:`\rho` in :cite:`Morse1998a`, which is
the filament contour length per unit volume, we can determine the 
mesh-size :math:`\xi_0` of the undeformed network: 

.. math::
    :label: eqa38

    \xi_0 = 1/\sqrt\rho_0


By comparing this to the phenomenological fit, we can express the elastic
modulus as a function of the distance, and the mesh size, as a function of the
fit parameters and the characteristic scales of the system.


.. math::
    :label: eqb
    
    E(d_c)     &=  \frac{(1+\nu).14.k_BT}{5L_p^{1/5}\xi_0^{14/5} \left.d_0\right.^{\alpha}}\times \left.d_c\right.^{\alpha}.\\
                    &=  E_0' \times \left.d_c\right.^{\alpha}

In which :math:`E_0'` can be identified as |E0| in :eq:`eqa` to extract the
closed form solution for the mesh size :math:`\xi_0` :

.. math::
    :label: eqa39

    \xi_0=\left(-\frac{({2-\frac{5}{7}\alpha)}.k_BT\pi R^2}{5\alpha \beta L_p^{\frac{1}{5}}\left.d_0\right.^{\alpha}}\right)^{\frac{5}{14}}


The found mesh size is in the order of 0.3 to 0.4 µm, which is consistent with previous findings 
:`Morse1998b`. The variation of the
mesh size can be seen on :num:`figure #xi-violin` and does not seem to have a
correlation with the Capping Protein concentration. 


.. _xi-violin:
.. figure:: /figs/xi_violin.*
    :width: 80%

    Meshsize vs Capping plot.

We explored the correlation between the mesh size and |delta| by plotting  the mesh size against the distance offset |delta| (:num:`Figure #dxcf`).
:num:`Figure #dxf` shows the relation between the mesh size and the offset
distance |delta| regardless of each Capping Protein concentration.


.. _dxcf:
.. figure:: /figs/delta-xi-corr.*
    :width: 100%

    Correlation of the meshsize :math:`\xi_0` with the distance offset |delta|,
    with marginal distribution as per histogram on the side and on the top.  Shaded
    regions represent confidence interval at 95%.


.. _dxf:
.. figure:: /figs/delta-xi-facets.*
    :width: 100%

    Same figure as :num: #dxcf` for each concentration of Capping Protein,
    with linear regression and confidence intervals at 95%.

From :eq:`eqa` and :eq:`eqb` by identifying the prefactor, it is also possible
to extract the Poisson’s ratio (|nu|) of the compressed material : 
    
.. math::
    :label: nu=f(alpha)

    \nu =\frac 1 2 \times \left( \frac 5 7.\alpha +1\right)


The Poisson’s ratio only depends on the power law exponent and thus slightly varies
with the amount of Capping Protein concentration.  We found a Poisson’s ratio value between 0.1 and 0.2, corresponding to compressible
foam-like materials that do not highly expand in the direction orthogonal to
the compression axis. A previous study of bulk actin network finds a Poisson’s
ration of 0.5 (incompressible material) for an actin concentration of 21.5 µM.  We
suspected that the low actin concentration used in our experiments (4µM) is the
reason for the low Poisson’s Ratio. The local structure of filaments
emanating from the  bead may also explain the large compressibility of our actin
cloud.


Interpretation
==============
.. 3

The results of our data analysis lead to the interpretation that 
a dense actin gel with an elasticity close to ~1kPa is polymerised
on the actin bead surface. This stiff gel
cannot be indented by the optical tweezer. Beyond this dense gel, a soft
actin cloud with an effective elastic modulus of 1 Pa and below is
present and extends on distances several times bigger than the thickness
of the reconstituted actin cortex (:num:`Figure #fig-interpretation`). The
structure of this actin cloud is expected to be quite different from the
dendritic gel and to be mostly constituted of loosely entangled actin filaments. 

In this model, the offset distance |delta| corresponds to the limit of the dense
dendritic actin network mimicking the actin cortex that grows on actin beads. 
The high elastic modulus of this gel makes it impenetrable for the small forces generated by the optical tweezer we use. The
values of |delta| we found are coherent with the measured thickness :math:`e
\simeq \delta - 2.R_{bead}` of the  biomimetic actin cortex, as measured by
epifluorescence in :cite:`Kawska2012` and found to be in the range of 1 to 2 µm. The decrease
of |delta| with Capping Protein is also coherent with the decrease of gel
thickness. 

.. The value of |delta| close to the bead radius also corresponds to the
.. absence of formation of biomimetic cortices, in the absence of Capping Protein.

The filaments composing the actin cloud directly emanate from the actin
cortex in which the actin polymerisation nucleation started at the bead surface
. Eventually, a few filaments can escape from the network and are
capped by the Capping Protein provided that the growing extremity is already several
micrometers from the bead surface. 

.. _fig-interpretation:
.. figure:: /figs/interp-delta.*
    :width: 90%

    A ) Schematic of an actin cloud. Left:  The actin bead triggers actin
    polymerisation. Right Probe Bead. On the actin bead surface, a dense
    and dendritic network forms a biomimetic actin cortex with an elastic
    modulus close to the kPa (Dark Green). From this actin cortex emanates a
    softer actin structure : the actin cloud . The actin cloud is a loosely
    entangled network formed by the filaments escaping from the bead's actin
    cortex and extending over several micrometers. The actin cloud has an average
    elastic modulus which is several orders of magnitude softer than the actin
    cortex. B ) From the probe-bead point of view in the optical tweezer, the
    system (actin-bead+actin cortex) behaves as a hard-sphere of radius
    :math:`\delta-R`


The actin cortex thickness, :math:`e` as measured in :cite:`Kawska2012`,
increases with time during the actin polymerisation. We can predict that the
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

The approach phase of the indentation cycle has been modelled with a purely
elastic mode. However, the force-distance plot shows a significant dissipation
marked by an hysteresis :num:`Figure #force-distance`. The repetitive indent cycle, giving the same
force-distance curves (:num:`Figure #reproc`), allows to exclude a plastic deformation. 
We can hence reject the hypothesis of ruptures of the
actin meshwork or breakage near the entanglement points.

The entangled filaments networks theory that allowed us to understand the link between the phenomenological
model and the mechanical properties of the network, also proposes a relation to
explain the network relaxation. 

In this model :cite:`Morse1998a`, the visco elastic modulus  |E| is a function of time
and can be written as :math:`E(t) = E\times \chi(t)` with 

.. math::
    :label: chi

    \chi(t)=\sum_{n, odd} \frac{8}{n^2 \pi^2}exp\left(- \frac{n^2\pi^2 t}{ \tau_{rep}} \right)

.. |Drep| replace:: :math:`D_{rep}`
.. |tau| replace:: :math:`\tau_{rep}`

In which :math:`\tau_{rep} = \frac{l_f^2}{D_{rep}}` is a single fit parameter
depending on diffusion constant for filament reptation |Drep| and the
filaments length :math:`l_f`. In this form, :math:`\chi` is a sum of
exponential decays with well defined characteristic timescales and amplitudes
that decrease as :math:`1/n^2`. To fit this model to the
relaxation phase data, we can limit ourselves to the first 40 terms of the sum, as
any of the subsequent terms represent timescales, we cannot reach with our
experimental resolution. 

It should be noted that the value of :math:`\chi(t=0)` is 1 and should be
treated particularly in order to ensure continuity of the force applied on the
actin-bead in the model.

Using this sum of exponential decays is coherent with the common conclusions of
power-laws found in the frequency-dependant shear modulus of both `in vivo` and `in vitro` actin
networks, as well as the relaxation behaviour found in cells.

In order to determine :math:`\tau_{rep}`, the Young's modulus established  in the
approach phase is used and the model is fitted against the relaxation data.  A
result of such a fit can be observed on :num:`figure #fit-3-phases`. The values of
|tau| are highly variable and the fit can be difficult when the relaxation is
slow or in the order of the measured noise. The variation of |tau| with the
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
to completely fit the succession of approach and relaxation phases.  In order to check whether
the fit parameters give realistic values, we can estimate the diffusion constant
for filament reptation |Drep|. 

.. math:: 
    :label: eqa3-10

    D_{rep} &= \frac{k_bT}{\gamma l_f} \\


In which :math:`\gamma\approx {2\pi\eta_s}/{ln(\xi_0/d_f)}` is the friction
coefficient per unit length. :math:`\gamma` depends on the solvent viscosity
:math:`\eta_s`, the mesh-size :math:`\xi_0` and the filament diameter
:math:`d_f` (:math:`~7nm` for actin).  We use :math:`\eta_s=10^{-3} Pa\times s`
for water and a mesh size in the order of 400nm as determined from the approach phase
(:num:`Figure #tau-violin`). Using |tau| given by the fit, this leads to filaments
length ranging from 3 to 8 µm, which is consistent with TIRF experiments and simulation as done in :cite:`Kawska2012`.


Retraction Phase
================
.. 3

During the retraction phase the force decreases, becomes negative after a
retraction of 3 to 4 µm, and shows a slow  return to 0 at large distance.
Sticking events can be observed when the force becomes abruptly negative before
relaxing as fast. :num:`Figure #sticking-event` shows such a sticking event
happening during an indentation cycle.

.. _sticking-event:
.. figure:: /figs/sticking-event.*
    :width: 80%

    A sticking event at :math:`d=15\mu{}m` where the rapidly decreasing force can be determined to go
    up to -18 pN, before quickly returning to its normal value. A second smaller
    sticking event is present at :math:`d=12\mu{}m`. Sticking events roughly appearing in 20% of
    the experiments.

We assume that the sticking events are characteristic of non-specific interactions
between the probe-bead and the actin cloud. If no sticking event
is present, we assume the partial closing of the actin cloud beyond the
probe-bead during the relaxation phase, and model the retraction curve as a
transition between the damped-approach curve and a penetration of the probe-bead through the closing actin cloud.

During the approach phase, the force exerted on the actin-bead is
:math:`F(d)=\beta(d-\delta)^\alpha`. During the relaxation phase, the force
decreases from :math:`F(t_1)` to :math:`F(t_2)` with the relation :

.. math::
    :label: eqa311

    \frac{F(t_2)}{F(t_1)} = \chi(t_2-t_1)

We can write that the force exerted on the actin-bead during the retraction  can be expressed as a sum of the force felt during the approach, damped during the
relaxation (:math:`F_{da}`), plus a force due to the closing of the actin
network behind the bead :math:`F_{closing}`.

.. math::
    :label: eqa312

    F_{ret}(d) &= F_{da}(d) + F_{closing}(d)\\
    F_{ret}(d) &= \chi(t_2-t_1).\beta(d-\delta)^\alpha+ F_{closing}(d)

:math:`F_{closing}` is computed using the fit parameter |alpha|, |beta|, |delta| and :math:`\tau_{rep}` (:num:`Figure #retract-powerlaw`).

On a double logarithmic scale and at long distance :math:`F_{closing}` also seems to
follow a power law (:math:`F_{plaw}`), when no sticking events are present.

.. _retract-powerlaw:
.. figure:: /figs/retract-powerlaw.*
    :width: 100%

    Left : Retraction phase, with approach phase fit damped by
    :math:`\chi(t_2-t1)` in green. Blue area under the curve is plotted on a
    log-log scale on the right, and follows a power law.


:math:`F_{ret}(d)` though, seems to follow the force felt during the approach phase,
damped by :math:`\chi(t)` (:math:`F_{da}`) for :math:`d\simeq{D_{bead}}` and
:math:`F_{da}+F_{plaw}` for :math:`d > 10\mu{}m`.  The
typical bead size being :math:`D_{bead}`, we expect the transition from
one regime to the other to be done on a length scale of :math:`D_{bead}`. Thus
we use a smoothing function which is a convolution between the projected bead
area and a linear ramp function one can observe on :num:`figure #interp`

.. _interp:
.. figure:: /figs/interpolation.*
    :width: 90%

    Interpolation function used to smooth the transition from :math:`F_{da}` to
    :math:`F_{da}+F_{plaw}` 


The complete retraction force can be seen on :num:`figure #fit-3-phases` and is equal to 

.. math::
    :label: eqa314

    F_{ret}(d) &= F_{da}(d)\times(1-S(d)) + F_{plad}(d)\times S(d)\\


where :math:`S(d)` is the interpolation function for a 4.34 µm
diameter bead. We can notice that the model correctly represents the retraction and especially
the position and value of the retraction function minimum without
fitting parameters, when using the probe-bead diameter as a typical scale
for the transition when changing direction.

Discussion
**********
.. 2


The actin cytoskeleton plays an important role in many cellular functions.  The
actin cortex, just beneath the cell membrane is not only a crucial structure
for both cell motility and cell mechanical properties, it is also an essential
component in cell division and spindle positioning.  Other actin structures,
that spawn from the nucleus to the cell membrane, are responsible for cell
organelle positioning, as is the case for plants, where the nucleus is found
towards the cell anticlinal wall :cite:`Iwabuchi2010`, or during nurse cell
maturation, where the nucleus is pushed away from the dumping
channel:cite:`Huelsmann2013`. The mechanical link from the outside of the cells
to the nucleus using actin bundles has already been shown :cite:`Jaalouk2009`.
We demonstrated here that these actin structures should not be the only ones
taken into account to explain organelles positioning.


Our experiments confirmed the existence of a sparse and stiff actin cloud emanating
from a biomimetically reconstituted actin cortex.  This actin cloud is capable
of staining forces of tens of pico Newtons, enough to hold organelles in place. By using polymer physics,
we are able to model the behaviour of such an actin cloud and
to measure many of its mechanical properties. It provides an
actin scaffold capable of deforming non-plastically. At time scales of few
seconds it behaves mostly elastically with an elastic module of a few Pascal.
The actin cloud Poisson’s ratio varies from 0.1 to 0.2, hinting at a
sparse structure of loosely entangled filaments, forming a meshwork with a
typical mesh size of 300 to 400 nm. 

The filaments at the origin of this loosely entangled network could emanate
from the dense actin cortex that can be seen and simulated on actin-beads
:cite:`Kawska2012` and the evolution of this actin cloud parameters are is
coherent with the preceding studies on biomimetically reconstituted actin
cortices. Recently, the role of actin networks with the same properties as an
actin cloud have been described in cells such as `Xenopus` Oocyte
:cite:`Feric2013`. The Poisson’s ratios of actin networks have been measured in
bulk to be higher :cite:`Gardel2003` but are not inconsistent with our
measurements at lower actin concentration.


The actin cloud provides a novel structure that should be studied further to
understand the positioning of organelles in cells, and to study the role this sparse
actin structure plays in the formation of other actin networks inside cells.

In particular, microrheology experiments could be performed on the growing actin
cloud in order to further characterise the frequency dependence of the actin cloud mechanical
properties. The effect of cross linking and network
branching is crucial for the occurrence of symmetry breaking on bead systems, and
probably plays a role in the actin cloud structure. A confined
geometry and direct polymerisation on membranes, or the effect of myosin motors
might alter the actin cloud properties.

All these, could be cellular mechanisms to use the actin cloud in order
to efficiently form the structures needed for its function.
Further studies of the actin cloud on biomimetic or `in vivo` systems are
challenging, but would lead to a better understanding of the cells mechanics
and its control.

A Paper based on this study has been accepted for publication in Biophysical
Journal and is added for information as appendix of this manuscript.

