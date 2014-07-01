.. Actin Cloud:

Actin Cloud
###########
.. 1

Introduction 
*************
.. 2


We have seen that the actin cytoskeleton play a major role in
cellular mechanics in many domains. It is necessary for force generation, and a
key component to cell motility. It has also be extensively studied both in
cells and biomimetic systems. 

Actin can form a variety of network in cell, ranging from dense branched network
at the leading Edge of the lamelipodia to bundled parallel structure forming
the filopodia.  Reconstruction of actin network have been done in biomimetic
systems using purified component :cite:`...`, and many properties of these network have
been measured.

It has been determined that the actin cortex is  a mechanical support for the
plasma membrane and that it extend over a few hundreds of nanometers :cite:`...` . Many
cells processes also hint for actin structure connected to this cortex that are
key elements to organelle and chromosome positioning :cite:`...`. 

In this part of the manuscript we investigate how a sparse actin structure can
emanate from the actin cortex, and what its properties are. Using the
:ref:`bead-motility <bead-motility-assay>` biomimetic system to reconstitute the actin cortex and its
dendritic structure, we show that from the cortex emanate a network of
filaments that have mechanical effect sufficient to move cells organelles  up
to tens of micrometers from the actin cortex.

The branched structure of the actin cortex underneath the plasma membrane of
cells hint for a structure governed by Arp2/3. How Arp2/3 and CP can be used to
form a biomimetic actin cortex has been widely studied. In :cite:`Kawska2012`, both in
vitro measurement on reconstituted actin cortex on bead as well as simulation
investigate the effect of cross linking and Capping Protein on the formed gel. It can be
seen both experimentally and in simulation that a network of filament escape from
what is defined as the actin cortex. The effect of these long filaments is not
taken into account in the in-silica system where measurement is restricted to
filament shorter than 10 µm. Only the effect of dense entangled actin network
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
magnetic beads and actin stabilized with phalloidin. Though they do not
investigate the sparse and softer actin network that originate from he visible
part.


Using :ref:`time-shared optical tweezer <time_shared_ot>` we are able to probe
the mechanics of this soft actin structure at time scale shorter than characteristic time of actin
polymerisation and forces in the pN range. We show that beyond the dense dendritic network
mimicking the actin cortex which as been measured to have :ref:`Elastic Modulus
<elastic_modulus>` in the order of kPa :cite:`Pujol2012` the soft actin cloud
we probe is much softer with stiffness three order of magnitude smaller.
This might explain why such a structure as not previously been seen by less
sensitive techniques than optical tweezer we use. The size of this actin cloud and its ability
to sustain forces suggest that in cell the actin cortex is not sharply
delimited and that structure escaping from it have a role in organelle
positioning.


How does the external part of the gel which is below the half fluorescent intensity behave ? What are its mechanical properties ?  How does it change through time ? 
if the gel is elastic or 


.. figure:: /figs/intensity_profile_25nM_Arp_20nM_CP_09min.pdf
    :width: 100%

    Upper Left : Epifluorescence image of polystyrene bead with a growing actin
    gel in presence of 25 nM of Arp2/3 and 25 nM of Capping Protein scale bar
    is 5 µm.  Upper Right : Normalized intensity profile of fluorescence image
    with thickness of the gel shown with dashed line as defined in
    :cite:`Kawska2012` : Distance between maximum intensity and half-maximum
    intensity.  Lower Left: Epifluorescence image of log(intensity).

.. figure:: /figs/intensity_profile_25nM_Arp_0nM_CP_30min.pdf
    :width: 100%

    Upper Left : Epifluorescence image of polystyrene bead with a growing actin
    gel in presence of 25 nM of Arp2/3 and absence of Capping Protein scale bar
    is 5 µm.  Upper Right : Normalized intensity profile of fluorescence image
    with thickness of the gel shown with dashed line as defined in
    :cite:`Kawska2012` : Distance between maximum intensity and half-maximum
    intensity.  Lower Left: Epifluorescence image of log(intensity). In the
    absence of Capping Protein the growth of filament is not prevented away
    from the bead surface

.. todo: scheme of experimental setup.

Actin-Bead System
*****************
.. 2

To reproduce the actin cortex and study the mechanics of actin structure
emanating from it :ref:`we prepare polystyrene bead <bead_preparation>` of 4.3 µm
diameter coated with a nucleation promoting factor. Theses bead are placed in
the :ref:`ATP mix Buffer <atp_mix_buffer>` in presence of 25µm of Arp2/3 complex,
4µm of monomeric actin 20% fluorescent 12 µM of Profilin and a varying amount
of Capping Protein. :ref:`Cf Material and Methods <m_et_m>`. These beads are
referred to as actin-bead.

These condition are chosen in order to grow a dense network on the surface of
actin-bead as in :cite:`Kawska2012`. We place ourself at 25nM ATP and a varying
amount of Capping Protein concentrating in order to cover condition where the
dense gel that form on the actin-bead is able to accumulate sufficient stress
to lead to symmetry breaking (CP between 15  and 35 nM ). We also investigate
condition where the amount of Capping Protein is to low (< 15nM) or to high
(>35 nM) to permit symmetry breaking.

.. figure:: /figs/kawska-phase-diagram.png
    :width: 90%

    Phase diagram showing the concentrating of Arp2/3 and Capping Protein
    necessary for symmetry breaking (inside dotted line) on 4,5 µm beads both
    `in vitro` and `in silico`. Inverted fluorescent images an and simulation
    are represented. Adapted from :cite:`Kawska2012`



We select a bead diameter of 4.3 µm in order to get a characteristic symmetry
breaking time of 20 to 40 minutes.
A smaller bead radius imply a
faster increase of stress and a shorter symmetry breaking time. 
The choice of 4.3µm allow enough time to proceed with the
experiments before symmetry breaking occurs. 

All measured on actin bead were made on an actively growing actin network which
was not stabilized unlike in :cite:`Pujol2012`, and before symmetry breaking
occur for capping concentration in the range 15 to 35 nM.

Probe Bead System
*****************
.. 2

To indent the network formed on actin-bead we used polystyrene bead passivated
with BSA. These bead are referred to as probe-bead.  The size of probe-bead have to be chosen
to be the same of actin-bead in order to achieve optical trapping of both actin
and probe-bead in the same observation plane. In the case of bead with different diameter, due to the trapping in two different Z-planes, the forced exerted
between the two bead during the indentation process has a non-negligible
component along the z-axis which is the axis with the weaker trapping stiffness
leading to bead escaping the traps.



Experimental description
************************
.. 2

To probe the actin network we trap an actin-bead with a growing
actin-network and a probe-bead using time-shared optical trap :ref:`...`,  and measure force
on the actin-bead using a QPD placed in the back focal plane of the condenser :ref:`...`.

To avoid systematic error of force measurement on displacing trap, all the
force recording are  made on the static bead. In our case on the
actin bead.


The indentation is a three step process :num:`Fig #figindent-time` we describe hereafter and in :ref:`material and methods`

    - Approach phase at constant velocity 10µm/sec unless precised otherwise
    - Resting or relaxation phase of 3 second during which both trap are static
    - Retraction phase in which the probe trap move toward its initial position at 10µm/sec.


Approach Phase
==============
.. 3
 
Durring the approach phase, probe-trap approaches at constant speed (10 µm/s), as seen in
:num:`Fig #figindent-time` for :math:`t < t_1`. During the approach the actin bead
will repel the probe bead due the actin network growing on it. The force felt
by the actin bead will progressively increase as the probe bead approach
eventually reaching the maximum as the probe-trap reach its closest position
from the actin trap. Note that during this process as both bead fell the force
exerted in-between them they move away from their respective traps center. The trap
stiffness of :math:`>20 pN/µm` and the maximum for measured of :math:`~20 pN`
insure the displacement of the beads in the trap are small compared to the
distance between the two beads. Hence in the following we consider that the probe-bead speed is equivqlent to the trap spped of 10µm/sec.


Relaxation Phase
================
.. 3

After the approach phase is a 3 seconds resting (or relaxation)  phase during which the probe
and actin-trap remain static. The relaxation phase start at :math:`t_1` and
finish at :math:`t_3` Num figure here`...`. The duration of the relaxation phase is long enough to
allow the relaxation of the actin cloud to happen at the timescale of the experiement, and sufficiently short for
the actin polymerisation not to change the properties of the network during one indentation cycle as well as
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
    acquired data. We can see on the second graph that the bead displacement on their respective trap is small compared to the dissplacement of the trap and justify the approximation of a probe bead speed equal to the probe trap speed.


Retraction part
===============
.. 3


After the three seconds of the retraction phase, the probe trap return to it's
initial position at 10 µm/s (:math:`t > t_2`). During this phase, the force
exerted between the two beads decrease, becomes negative, reach a minimum, and
eventually reaching zero asymptotically as the probe bead recover its initial
position.

This can be seen on :num:`Figure #figindent-time` right part. Negative forces
represent forces that tends to push the two beads to ward each other.


Reconstitution of Force-distance-curve
======================================
.. 3

From the position of he trap with time and the signal measured by the QPD the
position of bead in the trap as well as the forced exerted on each bead can be
calculated. We can then recover the distance between beads center as a function
for time.  The force-distance curve curve representing the force exerted by the
probe bead on the actin bead as a function of the distance can be computed and
show in :num:`Fig #force-distance` where we can still distinguish the three
phase of the indentation cycle. 



.. _force-distance:
.. figure:: /figs/force-distance.png
    :width: 100%

    Force exerted on the actin bead as a function of the distance between the
    two beads center. Color and data are the same as in :num:`Fig
    #figindent-time`. The probe bead start from the far right, and get closer
    while the force increases (green upper part of the curve), reach a
    maximum, and enter the relaxation phase (orange part) where the force
    between the probe and actin bead decrease, while the distance  also slightly
    decrease. During the retraction part (Blue) the force decrease, reaches
    negative value while the bead return to its initial position. Shown data is
    a subsample of 1 every 1000 points of acquired data. Shaded region
    represent area where the two polystyrene bead would interpenetrates.


Repetitive indent
=================
.. 3

To check for reproducibility and non-plastic deformation of the network after
indentation, the indentation cycle can be repeated several time at a few seconds
intervals. As the network is constantly growing during the measurement, this
also allow to check for the change of network properties due to actin
polymerisation.


.. _reproc-time:

.. figure:: /figs/reproc-time.png
    :width: 100%

    Force exerted on actin bead as a function of time for ten repetitive
    indent at a few seconds of interval. In one of the cycle a sticking event
    can be seen in the retraction phase 6 seconds after the beginning of the
    cycle. Tis shows hi reproducibility of indentation curves.


.. _reproc:

.. figure:: /figs/reproc.png
    :width: 80%

    Figure showing the reproducibility of indentation process on a bead with
    25nM Arp2/3 and 10nM CP Subset of data from :num:`Fig #reproc-time` shown
    with different color to represent evolution of indentation curve with time.
    Time is relative to first indentation. Shaded area represent zone where the
    two beads would interpenetrates.

Effect of approach speed
========================
.. 3

:cite:`Gardel2003` suggest that for frequency higher than 0.1 Hz, 
force due to the viscous behavior  of actin network can be in the same order 
than the elastic component.  We checked the effect
of the approach speed on the force measurement. We check in :num:`Fig
#many-speed` how the indentation speed affect the measurement by varying the
approach speed from 10 to 30 µm/s onthe same actin bead.


.. _many-speed:

.. figure:: /figs/many_speed.png
    :width: 80%

    Aproach phase of repetitive indent at multiple speed on the same actin-bead. The approach phase in the differents conditions qre indentical, hinting for a negligible effect of the viscosity  in the actin cloud at the speed considered.



Experimental observation
************************
.. 3

Using the bead system, we are able to reconstruct actin cortices `in vitro` and
we are able to investigate mechanical properties inaccessible to other
microscopy techniques like TIRF. Beyond the visible actin cortex we can detect
the presence of a actin structure that have mechanical effects far beyond the
thickness that has been measured for the biomimetically reconstructed actin
cortices (less than the µm). :num:`Figure #cloud-repelling` show qualitatively
that the actin cloud growing on actin beads is able to repel free floating
probe beads before they reach the visible reconstituted cortex. 

.. todo::

    add the video online ?


To quantify the distance at which the probe bead are affected by the actin-cloud
we measure the experimental noise by looking at the fluctuation of trapped probe bead.

During the indentation we defined :math:`d_0` as the distance at which the
average force felt by the probe bead is higher than the experimental noise. THe
experimental noise is measured by looking at the fluctuation of the probe bead
in its trap before the indentation cycle starts.

The repartition of :math:`d_0` with the concentration in capping protein is
plotted on :num:`Figure #d0-violin`.

 
 
.. _cloud-repelling: 

.. figure:: /figs/cloud-repelling.png
    :width: 100%

    Chronophotography representing the displacement back and forth of a trapped
    actin bead in a solution with probe bead. During this experiment, the actin
    bead is kept static in the optical trap while the stage is moved. Up until
    frame 70, the stage is moved down in the Y direction (South), then up
    again. The 11 first pictures show an average of the frame indicated as
    suptitle of each. Pictures 12 show a maximum projection of the all movie.
    Scale bar is 5 micrometers. Total movie duration is 21 seconds.


.. _d0-violin:
.. figure:: /figs/d0_violin.png
    :width: 80%

    Repartition of the bead-center distance at which the actin cloud exert a
    force higher than the noise (:math:`d_0`) on probe bead, as a function of
    capping protein. Shaded region represent position of bead surface (4.34 µm)
    and purple line represent bead surface+1µm (upper bound for the in vitro
    reformed actin cortex measured in :cite:`Kawska2012`). We see in this graph that for symmetry breaking
    condition (CP 10 nM and 30 nM) the distance at which the actin cloud apply
    force on the probe bead is large compare to the thickness of the actin
    cortex. The distance at which the probe bead is able to detect the presence
    of the actin cloud decrease with the increase concentration in Capping
    Protein that restrict  actin filament growth. The condition in the absence
    of Capping Protein are a particular case as no dense actin network forms
    on the surface of the actin bead. 

Approach phase modeling
=======================
.. 3

To extract mechanical properties using the three phase of the indentation we
decided to model each part (approach, relaxation and retraction) independently.
In particular, we fit force-distance curve of the approach phase using a power
law with 3 fit parameters :math:`\alpha, \beta, \delta`:

.. math::

    F(d) = \beta \times \left(d-\delta\right)^\alpha

In which :math:`F` represent the force exerted on the probe bead, and :math:`d`
is the distance between bead center. The powerlaw exponent :math:`\alpha` is
expected to be negative as the force decreases with the distance :math:`d`, and
characterize how fast the steepness of the curve force increase as the two
beads approaches. The prefactor :math:`\beta` act as a scaling factor of the
force. The offset parameter :math:`\delta` shifts the curve on the distance
axis. The model has the particularity that the force on the probe bead tends to
:math:`+\infty` when the distance :math:`d` get  to :math:`\delta`. THe force
is undefined for value of :math:`d< \delta` The offset distance :math:`\delta`
practically describe the distance at which the optical trap are not able to
indent the network anymore. 

In the case of hard sphere the value of :math:`\alpha` would tend toward
:math:`-\infty` leading to a infinite force increase at the contact between the
two hard-sphere of same diameter and a value of :math:`\delta` equal to the
diameter of the hard sphere.  In this case :math:`F(d>\delta)=0` and
:math:`F(d<\delta)=\infty`

The optical tweezer we use can apply forces up to 20pN, and the bead we use
exposes a surface of roughly :math:`(2\mu{}m)^2`. Before entering non-linear
regime and escaping the trap, the probe bead can move up to 1µm from its
trap center. For a material of typical size in the order of tens of µm,  this
lead to a maximum Young's Modulus of the indented material in the order of 100
Pa. Any material with a stiffness much higher than 100 Pa can be considered as
infinitively rigid.


The elasticity of dense actin gels around polystyrene beads has been measured
in :cite:`Pujol2012` and found to be in the order of kPa. It then shouldn't be
surprising  not to be able to probe the mechanics of the dense gel on the
surface of the bead and found a value of :math:`\delta` higher than 4.34 µm.

The model can be fitted using-least squares independently on each experimental
approach phase. An example of such a model adjusted is shown on figure
:num:`Fig #force-distance-fit` and quality of fit can can be measure by the
coefficient of determination :math:`R^2` which as a media value of `0.97`
across all fits.

.. _force-distance-fit:
.. figure:: /figs/force-distance-fit.png
    :width: 100%

    Power law model fitted on approach phase data for one experiment in the
    presence of [CP]=10nM, with the particular values found for the fit
    parameters.  The vertical line represent the point at which the model
    diverges and the force goes to infinity, that is to say :math:`\delta`. The
    shaded region correspond to the distance at which the two bead would
    interpenetrates. Relaxation (orange) and retraction (blue) data are shown
    but not fitted.


The approach phase data can be corrected for the distance offset :math:`\delta`
and plot in a log-log scale allowing for a better appreciation of the fit
result. The corrected distance is noted with  `c` indices :math:`d_c = d-
\delta`. In the model the force tends to infinity at :math:`d_c = 0`.




.. _force-distance-log-log:
.. figure:: /figs/force-distance-fit-loglog.png
    :width: 80%

    Force on actin bead  during approach phase as a function of bead distance
    minus distance offset :math:`\delta` plotted on a log-log scale. black line
    represent the power law model with  correction of the offset distance. Same
    data as :num:`Fig #force-distance` but showing only approach phase. 


In our experiments, the polystyrene beads have a average diameter of 4.34 µm,
thus we expect :math:`\delta` to be higher than the bead diameter.  Data with
:math:`\delta` values lower than 4.34 µm (21 out of 127) are considered as
unphysical and removed from further analysis.

As expected we find a negative values for :math:`\alpha`. Surprisingly the
value of alpha does not vary significantly across the amount of capping protein
and stay close to -1, with a mean value of -1.10, and a standard deviation of
0.38. The distribution of power law exponent can be seen on :num:`Fig #power-law-exponent`

.. _power-law-exponent:
.. figure:: /figs/alpha_violin.png
    :width: 90%

    Right : Violin plot showing the repartition of power law exponent with the
    concentration of Capping Protein. Left distribution of power law exponent
    :math:`\alpha` regardless of the concentration in Capping Protein. Value of
    exponent lies close to `-1`.


Due to the scale invariance of the inverse power law found above,  all the
approach phases data can be rescaled into a single master-curve. This is done
by dividing the force by the maximum force :math:`F_{max}` reached during the
approach and rescaling the distance by the minimum approach distance from which
:math:`\delta` is subtracted. 

.. figure:: /figs/rescaled_powerlaw.png
    :width: 80%

    Representation of rescale approach data on a log-log scale.  Red and green
    cross correspond to average values. Blue area correspond to average +/-
    standard deviation for each average bin. Red dot in the upper right corner
    correspond to the point (1,1) with respect to which all data has been
    rescaled.
    
    Blue dashed line correspond to fit to the average data for
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
breaking in the correct range of concentration of Capping Protein. In absence
of Capping Protein the dense dendritic network does not form on the surface. At
low concentration it seem not able to generate enough stress to rupture, and at
too high concentration (>35nM) the visible gel is thin and do not break
symmetry either. We then investigated the variation of each of the fit
parameters for concentrating of Capping Protein ranging from 0 to 50 nM.


We have already seen previously that the powerlaw exponent factor |alpha| didn't had 
variation with the amount of Capping Protein in solution (:num:`Fig
#power-law-exponent`). The two other parameter that can be investigated are the
prefactor :math:`\beta`. For the same value of :math:`\alpha` and
:math:`\delta`, the higher :math:`\beta` is the stronger the interacting
between the two beads for the same distance |dc|. We can see on
:num:`Figure #beta-violin`) that the average value for the prefactor decrease
with increase of Capping Protein concentration. 

.. _beta-violin:
.. figure:: /figs/beta_violin.png
    :width: 80% 

    Violin plot showing the repartition of prefactor with the quantity of
    Capping Protein. Decrease of prefactor with increasing amount of Capping
    Protein indicate a lower force between the probe bead and the actin bead
    for the same corrected distance between bead centers 

The last parameter of our model is :math:`\delta`, distance at which the force
diverges.   It can be seen in :num:`Figure #delta-violin` that at the exception
of absence of capping protein, the distance at which the model diverge get
closer to the diameter of the polystyrene bead as the concentration of capping
protein in the medium increases. It interesting to see that the distance offset
is the closer from the bead diameter in the absence of capping protein, when no
biomimetic actin cortices forms.  

.. _delta-violin:
.. figure:: /figs/delta_violin.png
    :width: 80% 

    Violin plot showing the variation of the offset distance :math:`\delta`
    with the quantity of capping protein. The shaded region represent the
    non-physical region which would correspond to a diverging force beyond the
    contact of the two polystyrene bead. Experimental data with :math:`\delta`
    value in this regions have been excluded from further analysis.


Determination of Young Modulus
==============================
.. 3


.. |E| replace:: :math:`E`

.. |dc| replace:: :math:`d_c`

.. |delta| replace:: :math:`\delta`
.. |alpha| replace:: :math:`\alpha`
.. |beta| replace:: :math:`\beta`

.. |E0| replace:: :math:`E_0`

To determine the mechanical properties of he gel between the actin and the
probe bead, we model it as a purely elastic material. The viscous effect are
neglected in the approach part as the approach at different speed show now
clear effect on the approach curves (Cf :num:`Figure #many-speed`). We consider
the compression of the material between the two probe bead. Surface of the
compressed material correspond to projected surfaces of the bead along the
direction of compression (:math:`\pi R^2`).  The thickness of the compressed
material is taken as being the distance between bead center corrected by the
distance offset |delta| as any material below delta can be considered as
infinitively rigid for the optical tweezer.

The stress exerted onto the material projected onto the bead surface or radius
:math:`R` can be written : 

.. math::
    
    \sigma = \frac{F}{\pi R^2}

For small deformation the local strain of the material :math:`u` can be written
as a function of the corrected bead position |dc| and the considered location
along the axis between the two bead center `x` : 

.. math::

    u(x)= \frac{d_c-x}{d_c}


We can express the local differential strain around the position |dc| of the
bead : :math:`\partial u = -\partial x/d_c` in which the minus sign reflect the
choice of the coordinate system: a decrease in :math:`x` with a positive
Young's modulus |E| should lead to an increase of the exerted force. The local felt young modulus when the probe bead has been approached from its initial position to the distance |dc| is then  

.. _eq-E:
.. math::

    E(d_c) = \left.\frac{\partial\sigma}{\partial u}\right|_{d_c}

By injecting the expression of :math:`u` and :math:`\sigma` this lead to :

.. math:: 

    E(d_c) &= -\frac{d_c}{\pi R^2}\times \Big(\frac{dF}{dx}\Big) \Big|_{x=d_c}\\
         &= E_0 d_c^\alpha

In which the value of |E0| can be expressed as function of the power law exponent |alpha| and the prefactor |beta| :

.. math::
    
    E_0 = - \frac{\alpha\beta}{\pi R^2}

Experimentally, the probed young modulus correspond to the average mechanical
properties of the actin cloud between the surface of the actin bead and the
surface of the probe bead and do not reflect the variation of the mechanical
properties of the uncompressed actin cloud with position. The geometry of the
system and the fluorescence signal suggest a decrease of the density of the
actin cloud with the distance from the actin-bead center. All values
reported later represent estimation of elasticity of an effective young
modulus. The Effective young modulus values found are 3 orders of magnitude
smaller than know elasticity of dendritic gel formed on bead that are in the
order of kPa :cite:`Marcy2004`. 

This difference in elasticity might explain why this actin cloud as not been
seen mechanically before in other measurement like micro pipettes aspiration,
micro needle deformation or Atomic Force Microscopy indentation that have
sensitivity in the order of nN while the forces exerted by this actin network 
are in the order of the pN.

Nonetheless, :cite:`Gardel2003` show that such low moduli can be obtain using
sparse entangle actin network, and confirm the idea that the actin-cloud seen
with the optical-tweezer indent experiment has a fundamentally different
structure that the dense dendritic network that what can be seen on the actin
bead surface using fluorescence.

.. _E0-violin:
.. figure:: /figs/E0_violin.png
    :width: 80% 

    Young Modulus Prefactor as a function of capping protein show a decrease of
    average young modulus with an increase of Capping Protein concentration.
    Similar to the graph of |beta| on :num:`Fig #beta-violin` as |E0| is
    proportionnal to |alpha|, which is alway close to -1 and |beta| . 



Mechanical properties
=====================
.. 3


To investigate the mechanical properties of the network that should arise from
a :math:`\alpha = -1` power law, we model the deformation of the actin cloud by
the theory of semi-flexible entangled polymer network (:cite:`Isambert1996`,
:cite:`MacKintosh1995`, :cite:`Morse1998a`).


The Young's modulus of semiflexible filaments in a 3D environment can be
expressed as a function of filament contour length density :math:`\rho` and the
entanglement length :math:`L_e` as :cite:`Morse1998b`:

.. math::
    
    E= \frac{2.(1+\nu).7.k_BT \rho}{5L_e}

.. |nu| replace:: :math:`\nu`

In which |nu| is the Poisson ratio and allow the conversion from shear to
elastic modulus. Previous study have investigated the non-linear stiffening of
such actin network for large deformation :cite:`Semmrich2008` and found that in
our condition, the linear description of theses networks holds to describe the
actin-cloud.

Using :cite:`Morse1998a` allow us to express the entanglement length as a
function of other parameters : :math:`L_e\approx L_p^{1/5} \rho^{-2/5}`. We can
reduce the expression of the young modulus to a function of the following
parameters : 

    - The Poisson Ratio |nu|, 
    - The persistence lenght of actin filaments :math:`L_p`
    - The mesh size of the network :math:`\xi_0`
    - The "size" of the cloud, for which we use the distance at which the force
      is first significant :math:`d_0`

We need also the consideration that for a general compressible material, the
only variable that can change during compression is the density :math:`\rho`
which could be made to depend on the corrected distance :math:`\rho \to
\rho(d_c)`

Thus leading to :


.. math::
    :label: eqa

    E(d_c)=\frac{ (1+\nu).14.k_BT}{5L_p^{1/5}}\times \rho(d_c)^{7/5}


The scaling exponent of |E| in `Eq #eqa` with |dc| should match the exponent
of the experimentally found power law |alpha|. Thus the density can be
expressed in the following form : 

.. math::
    :label: eq-rho

    \rho(d_c)=\rho_0(d_c/d_0)^{5/7\times\alpha}

By the definition of :math:`\rho` in :cite:`Morse1998a` which is
the filament contour length per unit volume, we can determine the 
mesh-size :math:`\xi_0` of the undeformed network: 

.. math::
    \xi_0 = 1/\sqrt\rho_0


By identifying to the phenomenological model we can thus express the Elastic
modulus as a function of the distance and the mesh size as a function of the
fit parameters and  characteristic scales of the system.


.. math::
    :label: eqb
    
    E(d_c)     &=  \frac{(1+\nu).14.k_BT}{5L_p^{1/5}\xi_0^{14/5} \left.d_0\right.^{\alpha}}\times \left.d_c\right.^{\alpha}.\\
                    &=  E_0' \times \left.d_c\right.^{\alpha}

In which :math:`E_0'` can be identified as |E0| in :eq:`eqa` to extract the
closed form solution for the meshsize :math:`\xi_0` :

.. math::
        \xi_0=\left(-\frac{({2-\frac{5}{7}\alpha)}.k_BT\pi R^2}{5\alpha \beta L_p^{\frac{1}{5}}\left.d_0\right.^{\alpha}}\right)^{\frac{5}{14}}


The found mesh size is in the order of 0.3 to 0.4 µm which is consistent which
what has been found  previously :cite:`Morse1998`. The variation of the
meshsize can be seen on :num:`Fig #xi-violin` and does not seem to have a
correlation with the concentration of capping protein. 


.. _xi-violin:
.. figure:: /figs/xi_violin.png
    :width: 80%

    meshsize vs capping.


Despite the fact that the  mesh size is directly related to the offset distance
correction |delta|, a strong correlation can be seen between the two on
:num:`Fig #dxcf`.  This can be explain despite the fact that |delta|
seem correlated with the Concentration in capping protein through the
non-appearance of time in our data analysis.  We will see in a later point that
the value measured for |delta| might be influenced by the time of measurement.


.. _dxcf:
.. figure:: /figs/delta-xi-corr.png
    :width: 80%

    Correlation of the meshsize :math:`\xi_0` with the distance offset |delta|,
    with marginal distribution as histogram on the side and on the top.  Shaded
    regions represent confidence interval at 95%.

:num:`Figure #dxf` shows the relation between the mesh size and the offset
distance |delta| independently for each concentration of Capping Protein.

.. _dxf:
.. figure:: /figs/delta-xi-facets.png
    :width: 80%

    Same figure as :num:`Fig #dxcf` for each concentration of capping protein,
    with linear regression and confidence intervals at 95%

From :eq:`eqa` and :eq:`eqb` by identifying the prefactor it is also possible
to extract the Poisson ratio (|nu|) of the compressed material : 
    
.. math::
    :label: nu=f(alpha)

    \nu =\frac 1 2 \times \left( \frac 5 7.\alpha +1\right)


The Poisson ratio depend only on the powerlaw exponent and thus varies little
with the amount of Capping Protein concentration.  We found value of the
Poisson ratio that are between 0.07 and 0.16 corresponding compressible
foam-like material that do not expand highly in the direction orthogonal to the
compression axis. Previous study of bulk actin network find a Poisson ration of
0.5 (incompressible material) for actin concentration of 21.5 µM. The lower
value we find which are closer to Poisson ratio of polymer network can be
explain by the five fold decrease of actin concentration that we use here (4µM)
and the different structure of the actin cloud we measure here.

Interpretation
==============
.. 3

The results of data analysis lead to the interpretation that on the surface of
the actin bead is polymerized a dense actin gel of elasticity close to ~1kPa,
and which act as the scale of force of the optical tweezer can apply to an
infinitely rigid material that cannot be indented. Beyond this dense gel a soft
actin cloud with an effective Elastic modulus up to thousand time softer  is
present and extend on distance that are several time bigger than the thickness
of the reconstituted actin cortex (:num:`Fig #fig-interpretation`). The
structure of this actin cloud is expected to be quite different from the
dendritic gel and be mostly constituted of loosely entangle actin filaments. 

In this model, the offset distance |delta| correspond to the limit of the dense
dendritic actin network mimicking the actin cortex that grows on actin bead
and which elastic modulus make impenetrable by the optical tweezer we use. The
value of delta we found are coherent with the measured thickness :math:`e
\simeq \delta - 2.R_{bead}` of the  biomimetic actin cortex as measured by
epifluorescence in :cite:`Kawska2012` in the range of 1 to 2 µm. The decrease
of |delta| with Capping Protein is also coherent with the decrease of gel
thickness. The value of |delta| close to the bead radius also correspond to the
absence of formation of biomimetic cortices in the absence of Capping Protein.

The filament composing the loosely actin cloud emanates directly from the actin
cortex in which the nucleation of actin polymerisation started at the surface
of the bead. Eventually a few filaments can escape from the networks and are
capped by the Capping Protein only later with the growing extremity a several
micrometers from the bead surface. 

.. _fig-interpretation:
.. figure:: /figs/interp-delta.png
    :width: 60%

    Schematic of actin cloud. Left:  The Actin bead triggers actin
    polymerisation. Right Probe Bead. On the surface of the actin bead a dense
    and dendritic network forms a biomimetic actin cortex with an elastic
    modulus close to the kPa (Dark Green). From this actin cortex emanate a
    softer actin structure : The actin cloud . The actin cloud is  loosely
    entangled network formed by the filaments escaping from the bead actin
    cortex and extend on several micrometers. The actin cloud have an average
    elastic modulus which is several order of magnitude softer than the actin
    cortex. From the point of view of the probe bead in optical tweezer, the
    system (actin-bead+actin cortex) behave as a hard-sphere of radius
    :math:`\delta-R`


The thickness of the actin cortex :math:`e` as measured in :cite:`Kawska2012`
increase with time during the polymerisation of actin. We can predict that the
offset distance |delta| should increase with time, except in the absence of
Capping Protein where no actin cortices forms.This can be verified on
:num:`figure #time-delta-corr` that show the evolution of |delta| as a function
of polymerisation time. 

.. _time-delta-corr:
.. figure:: /figs/time-delta-corr.png
    :width: 80%

    Distance offset |delta| as a function of time (min) since mix of actin, Atp
    and beads. Linear fit with confidence interval at 95% (light shaded area)
    and bead surface (dark shaded area). Sample in the absence of Capping are
    not taken into account in the regression (Pink +). The increase of |delta|
    with time is coherent with the measured increase of the gel thickness
    :math:`e` as measured in :cite:`Kawska2012`


Relaxation phase
****************
.. 2

The approach phase of the indentation cycle has been modeled with a purely
elastic mode. However, the force distance plot show a significant dissipation
marked by an hysteresis :num:`Fig #force-distance`. The repetitive indent cycle giving the same
force-distance curves (:num:`Fig #reproc`) allow plastic deformation 
to be excluded. We can reject the hypothesis of ruptures of the
actin meshwork or breakage near the entanglement points.

The theory that allowed us to understand the link between the phenomenological
model and the mechanical properties of the network also propose a relation to
explain the relaxation of the network. 

In this model :cite:`Morse1998a`, the elastic modulus  |E| is function of time
and can be written as :math:`E(t) = E\times \chi(t)` with 

.. math ::
    :label: chi

    \chi(t)=\sum_{n, odd} \frac{8}{n^2 \pi^2}exp\left(- \frac{n^2\pi^2 t}{ \tau_{rep}} \right)

.. |Drep| replace:: :math:`D_{rep}`
.. |tau| replace:: :math:`\tau_{rep}`

In which :math:`\tau_{rep} = \frac{l_f^2}{D_{rep}}` is a single fit parameter
that depends on diffusion constant for filament reptation |Drep| and the
filaments length :math:`l_f`. In this form, :math:`\chi` is a sum of
exponential decay with well defined characteristic timescale and amplitudes
that decreases as :math:`1/n^2`. To fit this model to the data of the
relaxation phase, we can limit ourselves to the first 40 terms of the sum as
any of the subsequents terms represent timescales we cannot reach with out
experimental resolution. 

It should be noted that  the value of :math:`\chi(t=0)` is 1 and should be
treated particularly in order to insure continuity of the force applied on the
actin-bead in the model.

Using this sum of exponential decays is coherent with the common findings of
power-law found in the shear modulus of both in vivo and in vitro actin
networks as well as the relaxation behavior found in cells :cite:`...`.

In order to determine :math:`\tau_{rep}`, the Young modulus determined on the
approach phase is use and the model is fitted against the relaxation data.  A
result of such a fit can be seen on :num:`Fig #fit-3-phases`. The value of
|tau| are highly variable and the fit can be difficult when the relaxation is
slow or in the order of the measured noise. Variation of |tau| with the
concentration in Capping Protein can be seen on :num:`figure #tau-violin`, and
one example of fit on the :num:`figure #fit-3-phases`

.. _fit-3-phases:
.. figure:: /figs/3phases.png
    :width: 80%

    Force as a function of time as well as fit for the 3 phases, approach,
    relaxation and retraction.

.. _tau-violin:
.. figure:: /figs/tau_violin.png
    :width: 80%

    Violin plot showing the repartition of |tau| as a function of capping
    protein. Outlier (|tau| negative or greater than tens of minutes removed)




We can see here that the polymer model introduced in :cite:`Morse1998a` allow
to completely fit the succession of approach and relaxation phases.  To check if
the fit parameters give realistic value, we can estimate the diffusion constant
for filament reptation |Drep|. 

.. math:: 

    D_{rep} &= \frac{k_bT}{\gamma l_f} \\


In which :math:`\gamma\approx {2\pi\eta_s}/{ln(\xi_0/d_f)}` is the friction
coefficient per unit length. :math:`\gamma` depends on the solvent viscosity
:math:`\eta_s`, the mesh-size :math:`\xi_0` and the filament diameter
:math:`d_f` (:math:`~7nm` for actin).  We use :math:`\eta_s=10^{-3} Pa\times s`
for water and a mesh size in the order of 400nm as determined previously
(:num:`Fig #tau-violin`). Using |tau| given by the fit, this lead to filaments
length ranging from 3 to 8 µm.


Retraction Phase
================
.. 3

During the retraction phase the force decreases, becomes negative after a
retraction of 3 to 4 µm, and show a slow  return to 0 at large distance.
Sticking event can be seen when the force becomes abruptly negative before
relaxing as fast. :num:`Figure #sticking-event` show such a sticking even
happening during an indentation cycle.

.. _sticking-event:
.. figure:: /figs/sticking-event.png
    :width: 80%

    A sticking event at `d=15µm` where the force can be seen decreasing rapidly
    up to -18 pN before quickly returning to its normal value. A second smaller
    sticking even is present at `d=12µm` Sticking even appear roughly 20% of
    the experiments.

We assume that the sticking even are characteristic to non-specific interaction
between the probe bead and the actin cloud.  In the case when no sticking even
is present, we can suppose a partial closing of the actin cloud beyond the
probe bead during the relaxation phase and can model the retraction curve as a
transition between the damped-approach curve and a penetration of the probe
bead through the closing actin cloud.

Durring the approach phase the force exerted on the actin-bead is
:math:`F(d)=\beta(d-\delta)^\alpha`. During the relaxation phase the force
decrease from :math:`F(t_1)` to :math:`F(t_2)` with the relation :

.. math::

    \frac{F(t_2)}{F(t_1)} = \chi(t_2-t_1)

We can write that the force exerted on the actin-bead during the retraction can
be written as a sum of the force felt during the approach, damped during the
relaxation (:math:`F_{da}`), plus a force due to the closing of the actin
network behind the bead :math:`F_{closing}`.

.. math::

    F_{ret}(d) &= F_{da}(d) + F_{closing}(d)\\
    F_{ret}(d) &= \chi(t_2-t_1).\beta(d-\delta)^\alpha+ F_{closing}(d)

:math:`F_{closing}` can be computed using the fit parameter |alpha|, |beta|, |delta| and :math:`tau_{rep}` (`Fig #retract-powerlaw`).

On a bi logarithmic scale and at long distance :math:`F_{closing}` also seem to
follow a power low (:math:`F_{plaw}`)  and when no sticking even are present.

.. _retract-powerlaw:
.. figure:: /figs/retract-powerlaw.png
    :width: 100%

    Left : Retraction phase with approach phase fit damped by
    :math:`\chi(t_2-t1)` in green. Blue area under the curve is plotted on a
    log-log scale on the right, follow a powerlaw.


:math:`F_{ret}(d)` seem though to follow :math:`F_{da}` for :math:`d
\simeq{D_{bead}}` and :math:`F_{da}+F_{plaw}` for :math:`d > 10µm`.  The
typical size of the bead being :math:`D_{bead}` we expect the transition from
one regime to the other to be done on a length scale of :math:`D_{bead}` Thus
we use a smoothing function which is a convolution between the projected bead
area and a linear ramp function which can be seen on :num:`figure #interp`

.. _interp:
.. figure:: /figs/interpolation.png
    :width: 90%

    Interpolation function used to smooth the transition from :math:`F_{da}` to
    :math:`F_{da}+F_{plaw}` 


The complete retraction force can be seen on :num:`figure #fit-3-phases` and is equal to 

.. math::

    F_{ret}(d) &= F_{da}(d)\times(1-S(d)) + F_{plad}(d)\times S(d)\\


Where :math:`S(d)` is the interpolation function for a bead of 4.34 µm
diameter. We can see that the model fit correctly the retraction and especially
the position and value of the minimum of the retraction function without
fitting parameter when we use the diameter of the probe bead as a typical scale
for the transition when changing direction.

Discussion
**********
.. 2


The actin cytoskeleton play an important role in many cellular functions.  The
actin cortex, just beneath the cell membrane is not only a crucial structure in
cell motility and mechanical properties, it is also a essential component in
cell division :cite:`Chaigne2013a` and the positioning of spindle. Other actin
structures, that spawn from the nucleus to the cell membrane are responsible
for cells organelles positioning like in plants where nucleus is moved away
from light :cite:`Iwabuchi2010`, or push the nucleus away during nurses cell
maturation :cite:`Huelsmann2013`. The mechanical link from the outside of the
cell to the nucleus using actin bundle has already been show in
:cite:`Jaalouk2009`. We show here that these actin structure should not be the
only one take into account to explain organelles positioning.


Our experiments show that from biomimetically reconstituted actin cortex formed
on beads emanates a sparse and soft actin cloud capable of staining forces of
tens of pico newtons, enough to hold organelles in place. Using polymer physics
description we are able to model the behavior of such an actin cloud and
measure many of its mechanical properties. This soft actin cloud provide a
actin scaffold capable of deforming non-plastically. At time scale of few
seconds if behaves mostly elastically with an elastic modulus of a few Pascal.
The Poisson ratio of the actin cloud varies from 0.05 to 0.1 hinting for a
sparse structure of loosely entangle filaments forming a meshwork with a
typical mes size of 300 to 400 nm. 

The filament at the origin of this loosely entangled network would emanate from
the dense actin cortex that can be seen and simulated on actin-beads
:cite:`Kawska2012` and the evolution of parameters of this actin cloud are
coherent with the preceding studies on biomimetically reconstituted actin
cortices. Recently the role of actin network with similar properties as the
actin cloud have been described in cells such as `Xenopus` Oocyte
:cite:`Feric2013`. Poisson ratio of different actin network in have been
measured in bulk to be higher :cite:`Gardel2003` that what found here, but
cannot explain the low or even negative Poisson ratio that can be found in
pluripotent cells :cite:`Pagliara2014`. 


The actin cloud provide a novel structure that should be studied further to
understand the positioning of organelles in cells and which role this sparse
actin structure plays in the formation of other actin network inside cells.

In particular microrheology experiments could be performed on the growing actin
cloud in order to further  characterize frequency dependence of the mechanical
properties  of the actin cloud. The effect of cross linking and network
branching is crucial for the happening of symmetry breaking on bead system, and
would likely play a role in the structure of the actin cloud. A confined
geometry and direct polymerisation on membrane, or the effect of myosin motors
might allow to alter the properties of the actin cloud.

All these could be mechanism used by the cell to use the actin cloud in order
to efficiently form structures it need in order to achieve its function.
Further studies of the actin cloud on biomimetic or `in vivo` system is
challenging, but would lead to a better understanding of the mechanics of the
cells and its control.






.. .. can reorganize in parallel structure \cite{reymann_nucleation_2010}
.. 
.. .. network in cell anchored to cortical actin network. \cite{schuh_new_2008,
..     chaigne_soft_2013, iwabuchi_actin_2010, lenart_contractile_2005}
.. 
.. 
.. :cite:`Schuh2008` show that a sparse actin network contracted by
.. ..           myosin that like the cortex to the spindle is necessary for its
.. ..           migration
.. 
.. ..         - :cite:`Schuh2008` show that a sparse actin network contracted by
.. ..           myosin that like the cortex to the spindle is necessary for its
.. ..           migration.
.. 
.. - Organelles are supported by .. gravity thing :cite:`Feric2013`
.. 
.. 
.. Rough explanation beta/delta/cp
.. 
.. INfinite cappingfilamanet immedaitely capped.
.. 
.. Important psitionning of nucleus :cite:`Huelsmann2013` mechanics link from
.. external  environemt bundle intergrins cite{jaalouk_mechanotransduction_2009}
.. 
.. Actin network emanating can sutain forces up to 10 pN sufficient for draging
.. organelss inside cell
.. 
.. can allow a constantly polymerizing cortical network to push throughout the
.. inside of a cell and exert sufficient forces to move organelles and chromosomes
.. \cite{kumaran_chromatin_2008}
.. 
.. 
.. Indeed, networks observed inside cells are generally anchored to cortical actin
.. network \cite{schuh_new_2008, chaigne_soft_2013, iwabuchi_actin_2010,
.. lenart_contractile_2005}
.. 
.. 
.. We here reproduce a system that show how from a dense branched actin network
.. can emanate an actin cloud structure with mechanical force sufficient to move
.. organelles. This actin-cloud by the way it is form is linked to actin cortex
.. and provide a scafold to build larger structure linked together.
.. 
..  - should do microrheology
..    - measure average properties
..  - inquery the amount of branching. 
..  - better understand the retraction part. 
..  - How woudl this differ in the inside geometry.
..    - Astonishingly it is the same -1 law that is found for flexible polymers :cite:`pincus witten`
..  - how would this sparse actin network react in the addition of myosin ? bunddling ? firning parallel structure in lamelipodia ? 
..  - 
.. 
.. Conclusion
.. **********
.. .. 2
.. 
.. The actin cortex can be reproduced `in vitro` on polystyrene beads. It is
.. polymerized by the activation  of the Arp2/3 complex on the surface of
.. polystyrene beads. Near the surface of the gel forms a dense dendritic actin
.. network with Elastic modulus of kPa. This gel can be seen by fluorescence when
.. using fluorescent actin.
.. 
.. The transition from his dense network mimicking actin cortex to the solution
.. medium is not sharp. On beads system there is a large transition zone of
.. several micrometers through a soft actin structure that we call the
.. actin-cloud.  We determined the mechanical properties of these actin clouds and
.. determines their viscoelastic properties.  The actin cloud are very soft in
.. comparison to the dense gel with young modulus several order of magnitude lower
.. (pa). Nonetheless these actin cloud are capable of supporting force sufficient
.. to move cells organelles, and do not deform plastically.  
.. 
.. The properties of these actin cloud are well explained by polymer theory of
.. loosely entangle actin network and the predicted viscoelastic properties are in
.. agreement with our measurement. Values founds are also in agreement with bulk
.. measurement with measurement of properties of actin gel measurement in gels,
.. but also suggest that lower Poisson ratio can be observed in the actin
.. structure.
.. 
.. The mechanical effect of the actin cloud can thus not be ignored in cellular
.. context. It provides the correct range of force and spawn over a sufficient
.. distance to position organelles, and could be used to position many cellular
.. structure. The actin cloud also provide a sparse actin structure that could be
.. easily remodeled by other actors of the cell to form already known structures.
.. 
.. 
.. .. Doublets:
.. 
.. Doublets
.. ********
.. 
.. .. Oocytes:
.. 
.. Oocytes
.. *******

:cite:`Lenart 2014 ?? starfish (read  it first)`

.. figure:: /figs/actin-cloud.png
    :width: 40%

    The "actin cloud" from which polymerize actin filament branched by Arp2/3 and capped by CP
    — Congratulatin for your HDR – 
    
