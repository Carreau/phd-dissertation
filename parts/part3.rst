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


.. todo::

    Correct Figure, Bead diameter removed or not

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
    a subsample of around 1 every 1000 points of acquired data. Shaded region
    represent area where the two polystyrene bead would interpenetrate.


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



Experimental observation
************************
.. 3

Using the bead system, we are able to reconstruct actin cortices `in vitro` and

we are able to investigate mechanical properties inaccessible to other
microscopy techniques like TIRF. Beyond the visible actin cortex we can detect
the presence of a actin structure that have mechanical effects far beyond the
thickness that has been measured for the biomimetically reconstructed actin
cortices (less than the µm). :num:`Fig #cloud-repelling` show qualitatively
that the actin cloud growing on actin beads is able to repel free floating
probe beads before they reach the visible reconstituted cortex. 


To quantify the distance at which the probe bead are affect by the actin-cloud
we measure the experimental noise by looking at the fluctuation of trapped probe bead.

During the indentation we defined :math:`d_0` as the distance at which the
average force felt by the probe bead is higher than the experimental noise.

 
 
.. _cloud-repelling: 

.. figure:: /figs/cloud-repelling.png
    :width: 100%

    Chronophotography representing the displacement back and forth of a trap
    actin bead in a solution with probe bead. During this experiment, the actin
    bead is keep static in the optical trap while the stage is moved. Up until
    frame 70, the stage is moved down in the Y direction (South), then up
    again. The 11 first frame show an average of the frame indicated as
    suptitle of each. frame 12 show a maximum projection of the all movie.
    Scale bar is 5 micrometers.


.. figure:: /figs/d0_violin.png
    :width: 80%

    Repartition of the bead-center distance at which the actin cloud exert a
    force higher than the noise (:math:`d_0`) on probe bead, as a function of
    capping protein. Red line represent position of bead surface (4.34 µm) and
    purple line represent bead surface+1µm (upper bound for the in vitro
    reformed actin cortex). We see in this graph that for symmetry breaking
    condition (CP 10 nM and 30 nM) the distance at which the actin cloud apply
    force on the probe bead is large compare to the thickness of the actin
    cortex. The distance at which the probe bead is able to detect the presence
    of the actin cloud decrease with the increase concentration in capping
    protein that restrict  actin filament growth. The condition in the absence
    of capping protein are a particular case as no dense actin network do for
    on the surface of the actin bead. The structure of the actin network on the
    actin bead can then be really different for this value.

Approach phase modeling
=======================
.. 3

To extract mechanical properties using the three phase of the indentation I
decided to model each part independently. In particular, I decided to fit
force-distance curve of the approach phase using a power law with 3 fit
parameters :math:`\alpha, \beta, \delta`:

.. math::

    F(d) = \beta \times \left(d-\delta\right)^\alpha

In which :math:`F` represent the force exerted on the probe bead, and :math:`d`
is the distance between bead center. The powerlaw exponent :math:`\alpha` is
expected to be negative as the force decreases with the distance :math:`d`, and
characterize how fast the steepness of the curve force increase as the two
beads approaches. The prefactor :math:`\beta` act as a scaling factor of the
force. The offset parameter :math:`\delta` shifts the curve on the distance
axis. The model has the particularity that the force on the probe bead tends to
:math:`+\infty` when the distance :math:`d` get close to :math:`\delta`. 

The offset distance :math:`\delta` practically describe the distance at which
the optical trap are not able to indent the network anymore. In the case of
hard sphere the value of :math:`\alpha` would tend toward :math:`-\infty`
leading to a infinite force increase at the contact between the two hard-sphere
of same diameter and a value of :math:`\delta` equal to the diameter of the
hard sphere. 

The optical tweezer we use are in the order can apply force in the order of 20
pN, and the bead we use expos a surface of roughly :math:`(2µm)^2`. Before
entering non-linear regime and escaping the trap, the probe bead can move up to
1µm off from the trap center. For a material of typical size in the order of
tens of µm,  this lead to a maximum Young's Modulus of the indented material in
the order of 100 Pa. Any material with a Stiffness much higher than 100 Pa can
be considered as infinitively rigid.

In our experiments, the polystyrene beads have a average diameter
of 4.34 µm, thus we expect :math:`\delta` to be higher than the bead diameter.

While there is a certain variation for individual diameter, data giving a
:math:`\delta` value smaller than bead diameter will be considered as
non-physical.

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

    Power law model fitted on approach phase data for one experiment in the presence
    of [CP]=10nM, with the particular values found for the fit parameters.  The
    vertical line represent the point at which the model diverges and the force
    goes to infinity, that is to say :math:`\delta`. The shaded region
    correspond to the distance at which the two bead would interpenetrates.


The approach phase data can be corrected for the distance offset :math:`\delta`
and plot in a log-log scale allowing for a better appreciation of the fit
result. The corrected distance is noted with  `c` indices :math:`d_c = d-
\delta` 




.. _force-distance-log-log:
.. figure:: /figs/force-distance-fit-loglog.png
    :width: 80%

    Force on actin bead as a function of bead distance minus distance offset
    :math:`\delta` plotted on a log-log scale. black line represent the power
    law model with  correction of the offset distance. Same data as :num:`Fig
    #force-distance` but showing only approach phase. 


Data with :math:`\delta`
values lower than 4.34 µm (21 out of 127) are considered as unphysical and
removed from further analysis.

As expected we find a negative values for :math:`alpha`, but surprisingly the
value of alpha does not vary significantly across the amount of capping protein
and stay close to -1, with a mean value of -1.10, and a standard deviation of
0.38. The distribution of power law exponent can be seen on :num:`Fig #power-law-exponent`

.. _power-law-exponent:
.. figure:: /figs/alpha_violin.png
    :width: 90%

    Violin plot showing the repartition of power law exponent with the
    concentration of capping protein.


Due to the scale invariance of the inverse power law we find above we, all the
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
    :math:`d_c/d_{c,min} < 10` (red cross), fitted slope is :math:`-1.06`. 
    As an eye guide, slope of `-1` and `-1.5` have been represented. 
 


The rescaled data confirm an average power law exponent of :math:`\sim -1`, the
breakdown of the average exponent beyond :math:`d_c/d_{c,min}=10` can be
explained by the statistical effect of having less data for long distance.


:math:`\alpha, \beta` and :math:`\gamma` 


.. todo:: 
    Zero of force is determined by average force on large distance. // bead <Left Mouse>


Variation of parameters with Capping Protein
============================================
.. 3

At the chosen concentration of Arp2/3 the bead system can show symmetry
breaking in the correct range of concentration of capping protein. In absence
of capping protein the dense dendritic network does not form on the surface. At
low concentration it seem not able to generate enough stress to rupture, and at
too high concentration (>35nM) the visible gel is thin and do not break
symmetry either. I then investigated the variation of each of the fit
parameters for concentrating of capping protein ranging from 0 to 50 nM.


We have already seen previously that the powerlaw exponent factor didn't had a
significant variation with the amount of capping protein in solution (:num:`Fig
#power-law-exponent`). The two other parameter that can be investigated are the
prefactor :math:`\beta`. At for the same value of :math:`\alpha` and
:math:`\delta`, the higher :math:`\beta` is the stronger the interacting
between the two beads for the same distance between bead center. We can see on
:num:`Figure #beta-violin`) that the average value for the prefactor decrease
with increase of capping protein concentration. 

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
the compression of the material between the two probe bead between two surface
that are the projected surfaces of the bead on the direction of compression.
The thickness of the compressed material is taken as being the distance between
bead center corrected by the distance offset |delta|.

The stress exerted onto the material projected onto the bead surface or radius :math:`R` can be written : 

.. math::
    
    \sigma = \frac{F}{\pi R^2}

For small defmation the local strain of the material :math:`u` can be written as a function of the
corrected bead position |dc| and the considered location along the axis between the two bead center `x` : 

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
properties of the uncompressed actin cloud with position. The geometry of hte
system and the fluorescence signal suggest a decrease of the density of the
actin cloud with the distance to the actin-bead center. All reported values
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
sparse entangle actin network, and confirm the idea that the actin-cloud the
optical-tweezer indent experiment has a fundamentally different structure that
the dense dendritic network that what can be seen on the actin bead surface
using fluorescence.

.. _E0-violin:
.. figure:: /figs/E0_violin.png
    :width: 80% 

    Young Modulus Prefactor as a function of capping protein. Similar to the
    graph of |beta| on :num:`Fig #beta-violin` as |E0| is proportionnal to
    |alpha|, which is alway close to -1 and |beta| .


To further understand the observed powerlaw we can model the actin cloud 

Interpretation 
==============
.. 3

The data collected and the results of data analysis lead to the conclusion that
on the surface of the actin bead is polymerized a dense actin gel of elasticity
close to ~1kPa, and which act as the scale of force of the optical tweezer can
apply to an infinitely rigid material that cannot be indented. Beyond this
dense gel a soft actin cloud with an effective Elastic modulus up to thousand
time softer  is present and extend on distance that are several time bigger
than the thickness of the reconstituted actin cortex. The structure structure
of this actin cloud is expected to be quite different from the dendritic gel
and could be mostly constituted of loosely entangle actin filaments. 

To investigate further this hypothesis, and the mechanical properties of the
network that should arise from a :math:`\alpha = -1` power law, we model the
deformation of the actin cloud by the theory of semi-flexible entangled polymer
network (:cite:`Isambert1996`, :cite:`MacKintosh1995`, :cite:`Morse1998a`).


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


.. _eq-A:
.. math::

    E(d_c)=\frac{ (1+\nu).14.k_BT}{5L_p^{1/5}}\times \rho(d_c)^{7/5}


The scaling exponent of |E| in `Eq #eq-A` with |dc| should match the exponent
of the experimentally found power law |alpha|. Thus the density can be
expressed in the following form : 

.. _eq-rho:
.. math::

    \rho(d_c)=\rho_0(d_c/d_0)^{5/7\times\alpha}

By the definition of :math:`\rho` in :cite:`Morse1998a` which is
the filament contour length per unit volume, we can determine the 
mesh-size :math:`\xi_0` of the undeformed network (average value) of :math:`\xi_0 = 1/√\rho_0`


By identifying to the phenomenological model we can thus express the Elastic
modulus as a function of the distance and the mesh size as a function of the
fit parameters and  characteristic scales of the system.


.. math::
         E(d_c)     &=  \frac{(1+\nu).14.k_BT}{5L_p^{1/5}\xi_0^{14/5} \left.d_0\right.^{\alpha}}\times \left.d_c\right.^{\alpha}.\\
                    &=  E_0' \times \left.d_c\right.^{\alpha}


.. math::
        \xi_0=\left(-\frac{({2-\frac{5}{7}\alpha)}.k_BT\pi R^2}{5\alpha \beta L_p^{\frac{1}{5}}\left.d_0\right.^{\alpha}}\right)^{\frac{5}{14}}



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

