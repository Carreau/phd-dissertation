Liposomes Doublets
##################
.. 1


Introduction 
*************
.. Todo::
    check text
    change figure

We have seen that in cells actin is a key component to form structure like the
actin cortex in order to transmit forces. In order to drive shape changes,
cells regulate the  sub-micrometer thick actin cortex that lies beneath the
membrane :cite:`Clarke2013`. The actin cortex drives cell shape changes
:cite:`Salbreux2012b` and the presence of myosin lay a fundamental role in the
change of tension of the acto-myosin cortex :cite:`Tinevez2009`. Cortical
tension can be measured on cells to vary between 50 and 4000 pN/µm depending on
actin and myosin activity.  The change of cell cortical tension can also be
modulated by cell-cell adhesion :cite:`Maitre2012` which have impact on cell
sorting. 

Such acto-myosin cortices have been reconstructed on cell-sized liposomes
:cite:`Carvalho2013a` which showed that attachment of the actin cortex to the
membrane had a crucial role in the behavior or contractile acto-myosin network. 

In this study, I worked with Kévin Carvalho and Joël Lemière in order to extend the
system developed in :cite:`Carvalho2013a` to monitor the cortical tension
increased of a biomimetic actin cortex formed on liposomes. I was principally
involved in analysing 3D data acquire using Spinning disk microscope and
develop a novel in order to fit a model of the liposome to get an precise and
unbiased measure of the geometrical parameter.

To determine the role of cortical tension in cells, :cite:`Maitre2012` use cell
doublets. Here we form a liposome doublets around which we produce an actin
cortex `in vitro`. The shape change of these liposomes doublets allow us to
monitor thought time in a non-invasive way the increase of cortical tension.
We develop a methods for  precise monitoring of the doublets deformation
in order to determine accurately the increase of tension induced by the
injection of myosin motor on a preformed actin cortex.


Experimental description
************************
.. 2

.. image of peeling crunching ? 

Formation of liposomes doublets
===============================
.. 3

Liposomes are obtain by electro formation (cf :ref:`Material and methods
<electroformation>`) from a mix of EPC and PEG-biotin lipids. The presence of
streptavidin in the working buffer allow liposomes to naturally stick together
to form doublets after 15 minutes (:num:`Fig #fig1a`).


.. _fig1a:
.. figure:: /figs/Fig_01-A.png
    :width: 70%

    Cell-sized liposome doublets. Doublets are indicated by white arrows in
    the field of view of a phase contrast microscope.



Formation of actin cortex on doublets
=====================================
.. 3

Formation of the actin network on doublets are done as in
:cite:`Carvalho2013a`. Actin filament  stabilized by phalloidin with
biotinylated monomers are linked to the PEG-Biotin lipid of the membrane
through streptavidin present in solution (:num:`Fig #fig1b`). The presence of
streptavidin also cross links the filament. Such network has already been
characterized in :cite:`Carvalho2013a`.  Note that actin monomers being added
after the formation of liposome, the interface between the two liposomes that
compose the doublets are free of actin (:num:`Fig #fig1c`, :num:`#fds`). As the actin added
is fluorescent, this can be checked by epifluorescence as the interface appears
dark compared to the rest of the doublet.

.. scheme equilibrium tension contact angle.

.. _fds:
.. figure:: /figs/doublets-schema.png
    :alt: Formation doublet schema
    :width: 90%

    Formation of doublets: 1) In the presence of streptavidin, single liposome
    (a) aggregate into doublets (B). The addition of biotinylated actin
    filament stabilized with phalloidin (2) form liposomes doublets covered
    with a micrometer-sized actin network (C). The interface between the two
    liposome is a double lipid bilayer free of actin filaments.

.. _fig1b:
.. figure:: /figs/Fig_01-B.png
    :width: 50%

    Schematic of the stabilized actin cortex at the membrane (proteins not to scale).

Visualisation of the interface
==============================
.. 3


.. _fig1c:
.. figure:: /figs/Fig_01-C.png
    :width: 50%

    i) Macrofluidics chamber designed to exchange the outside buffer. Doublets
    are visualized in the middle horizontal channel of the H shape chamber to
    avoid movement during the buffer exchange. Spinning disk images of the
    doublet before i) or after iii) myosin II injection. One liposome contains
    SRB (red) to visualize the interface of the doublet, actin cortex is
    labeled in green. Scale bar 5µm.




To visualise the interface between liposomes, and avoid the use of fluorescent
lipids that may affect the membrane mechanics :cite:`Sandre1999` the inside
buffer of half the liposomes are labeled with 0.9 µm of sulphorhodamin B
eventually leading to half of the doublets being fluorescent (:num:`Fig #fig1c` i and iii).

Geometrical parameters
======================
.. 3

To study the doublets geometry we model each liposome as well as the interface
between them as two spherical caps with their respective center, and radius, as
show in :num:`figure #fig-notations-doublets`. 

.. _fig-notations-doublets:
.. figure:: /figs/notations-doublets.png
    :width: 80%

    Notation of parameters for doublets, |R1|, |R2|, |Ri| are respectively the
    radius of the liposome 1, the liposome 2 and the interface. |d| is the
    distance between liposome center. |theta1|, |theta2| are the angle between
    the tangent to the liposome surface and the tangent to the interface at the
    contact line. The total contact angle |theta| is the sum of |theta1| and |theta2|

The center position in 3D (X,Y,Z) and radius (R) of the spherical caps
completely determine the problem, though it is interesting to look at other
parameters of the doublets which are :

    - the total volume of the liposome doublets `V`
    - the contact angle between the two liposomes
    - Each of the "half"-contact angle which are the angle between the
      interface and each of the liposome :math:`\theta_1,\theta_2`
    - The distance between liposomes center.

The model have a rotational symmetry along the axis that passes through the
center of the three liposomes, we thus consider only one of the equatorial
plane when referring to the model. Unless otherwise specified, all component
outside of such a plane are null.

Experimental Observations
*************************
.. 2


Effect of myosin injection
==========================
.. 3


We images liposomes doublets placed in an open chamber either in phase contrast
and epifluorescence, or spinning disk microscopy in the red  (sulphorhodamin)
and green (actin) channel.

.. todo: brokenref

Myosin II that form :ref:`bipolars filaments <myoII>` is slowly injected into
the chamber, and trigger a shape change (:num:`Fig #doublets-contraction`) of the doublets in a matter of minutes.

.. _doublets-contraction:
.. figure:: /figs/doublet-contract.png
    :width: 40%

    Doublets contraction showing green channel (actin): Left doublets before
    myosin II injection. Right: doublets during contraction due to myosin II.
    Scalebar is 5 µm 

.. |theta| replace:: :math:`\theta`
.. |theta1| replace:: :math:`\theta_1`
.. |theta2| replace:: :math:`\theta_2`

The distance between liposome center decreases as the total angle :math:`\theta
= \theta_1+\theta_2` increases. The contact angle and other parameter of the
doblets are obtained by fitting spherical caps onto the 2D epifluorescence
images or 3D confocal stack as :ref:`described later <full3dfit>`.  In the absence of myosin, the
contact angle |theta| is measured to be :math:`\theta = 64 \pm 16 ^{\circ}` whereas in
the presence of myosin II (200 nM) we find a value of :math:`\theta = 86 \pm 21
^{\circ}`. Measured of contact angle after myosin injection are done before the cortex
ruptures as characterized in :cite:`Carvalho2013a` .

Angle related to tension
========================
.. 3

.. |tau1| replace:: :math:`\tau_1`
.. |tau2| replace:: :math:`\tau_2`
.. |taui| replace:: :math:`\tau_i`
.. |taut| replace:: :math:`\tau_t`
.. |W| replace:: :math:`W`
.. |V| replace:: :math:`V`
.. |d| replace:: :math:`d`
.. |R1| replace:: :math:`R_1`
.. |R2| replace:: :math:`R_2`
.. |Ri| replace:: :math:`R_i`

Each liposome have its respective tension |tau1|, and |tau2|.  In the absence
of the biomimetic acto-myosin cortex these tensions correspond only to the
tension of the liposomes membranes. The interface between the two liposome is
formed of a double lipid bilayer, and it tension is due to two contribution.
The tension of the lipids bilayer themselves, is noted |taui|, and the
adhesion energy per surface unit |W| due to the biotin-streptavidin-biotin link
between the two lipid bilayers. The total tension at the interface can thus be
written :math:`\tau_t = \tau_i -W`.


As the movement of the contact line during the contraction in in the order of
µm/min we can consider the contact line between the liposomes and the interface
to be  at equilibrium, we can thus apply Young's equation over time. This allow
to relate the tension of each of the lipid layers and the angle
between them at each instant of the contraction. We can in particular project
the result of this equation onto the direction of the contact surface
tangent : 

.. Math::
    :label: young-tangent

    \tau_1 - W = \tau_1.cos(\theta_1) + \tau_2.cos(\theta_2)

And on the direction perpendicular to it :

.. math::
    :label: young-perpendicular

     \tau_1.sin(\theta_1) = \tau_2.sin(\theta_2)


These equation link the tensions to the contact angles both before, during and
after the contraction. Value that relate to before contraction phase will
be suffixed by  `0` indices. Thus, for example :math:`\tau_{i,0}` refer to the
tension of the interface before the addition of myosin, and |taui| refer to the
tension of the interface at any instant of the contraction.

Contact angle dispersion
========================
.. 3
    

The value of the contact angle |theta| varies across sample both before
and after the  addition of myosin II. It reflect an initial variation of tension in
:math:`\tau_{i,0}`, :math:`\tau_{1,0}`, and :math:`\tau_{2,0}`. This could be
due to a difference in the tension acquired during liposome preparation, to a
variation of adhesion energy between liposome, or effect of tension build-up
during the formation of the actin shell. As the dispersion in contact angle is
in the same order as the increase in angle with the addition of myosin, a
statistical analysis of the contact angle before and during contraction is
difficult. Thus to avoid this effect of dispersion, we follow the evolution of
:math:`\theta` on the same doublet during time.


Tension of actin-shell
======================
.. 3

In order to investigate the increase of tension due to the acto-myosin network
on liposome, we first characterise the increase due to the sole actin-shell in
the absence of myosin. By photo bleaching the actin (:num:`Fig #fig2a`) we compare the shape of the
same doublets in the presence and absence of the actin-shell. The total contact
angle change by :math:`3.4 \pm 2.0 degree` after disruption (:num:`Fig #fig2b`) of the actin network.
Thus we conclude that the effect of the actin-shell is small and negligible
compared to the effect we see with myosin. 

.. _fig2a:
.. figure:: /figs/Fig_02-A.png
    :width: 80%

    Image of the same doublet coated with fluorescent actin before i) ii) and
    after iii) iv) actin cortex disruption. The actin cortex is visualized by
    epifluorescence ii) iv) and the doublet by phase contrast i) iii). Scale
    bar 5µm.

.. _fig2b:
.. figure:: /figs/Fig_02-B.png
    :width: 80%

    Measurement of the contact angle between the two liposomes as a function of
    their volume, before (black) and after (white) disruption of the stabilized
    actin cortex. 


.. _3d-obs:
3D observation
**************
.. 2

Three dimensional imaging of the doublets are necessary to get the correct
contact angle, especially when doublets are of different radii. In our
experiments, liposomes composing a doublets had a ratio :math:`R_1 / R_2 \in
[1.15:1.82]`, and to measure the contact angle the epifluorescence plane have
to be one of the equatorial plane of the doublets, leading to a under
estimation of the contact angle. 

The interface between the two liposomes is a portion of sphere with a curvature
:math:`C_i= \frac{1}{R_i}` much smaller than :math:`\frac{1}{R_1}` and
:math:`\frac{1}{R_2}`. The determination of the radius :math:`R_i` was
difficult as the difference in the position of the interface both before and
after myosin injection differed from flat surface by only a few pixels in most
of the cases.

.. todo: image with flat interface after contraction.

Also there is no important dissymmetry  of the liposome composing the doublets.
In theses conditions we assume that |theta1| and |theta2| are equal in our
system with our optical resolution.

.. _confocal-stack:
.. figure:: /figs/light_table.png
    :width: 90%

    Confocal stack of an liposome doublets, actin channel, 3D reconstruction in
    :num:`Figure #fig3a`. Note that there is no actin at the interface between
    the liposomes.
 

.. _fig3a:
.. figure:: /figs/Fig_03-A.png
    :width: 80%

    3D reconstruction of a doublet surrounded by actin. The absence of actin on
    the interface can be seen more easily on :num:`figure #confocal-stack`  

3D Spinning disk images  (:num:`Fig #confocal-stack` with 3D reconstruction
:num:`Fig #fig3a`) are recorded for an accurate determination of the different
parameters of the doublet over time: the contact angle |theta| (:num:`Fig #fig3b`) , the
volume of the doublet |V| (:num:`Fig #fig3d`), the distance between trap
centers :math:`d` (:num:`Fig #fig3c`). All theses parameters are obtain by
fitting spherical 3D caps on the 3D stack as explained :ref:`in later parts`. 

.. _fig3b:
.. figure:: /figs/Fig_03-B.png
    :width: 80%

    Evolution of the contact angle compare to the initial one as a function of
    time. Each doublet is represented by a different line color. 
    Same color code for same doublets as in figure :num:`#fig3c`, :num:`#fig3d`
    and :num:`#fig3e`. Note that the blue dashed line corresponds to the
    evolution of geometrical parameters of the same doublet, analyzed even
    after actin cortex rupture. It recovers its initial parameter values.

.. _fig3c:
.. figure:: /figs/Fig_03-C.png
    :width: 80%

    Evolution of the distance between the two liposomes center over time.
    Same color code for same doublets as in figure :num:`#fig3b`, :num:`#fig3d`
    and :num:`#fig3e`. Note that the blue dashed line corresponds to the
    evolution of geometrical parameters of the same doublet, analyzed even
    after actin cortex rupture. It recovers its initial parameter values.

.. _fig3d:
.. figure:: /figs/Fig_03-D.png
    :width: 80%

    Evolution of the volume ratio over time.
    Same color code for same doublets as in figure :num:`#fig3b`, :num:`#fig3c`
    and :num:`#fig3e`. Note that the blue dashed line corresponds to the
    evolution of geometrical parameters of the same doublet, analyzed even
    after actin cortex rupture. It recovers its initial parameter values.


During contraction triggered by myosin injection, we observe that the contact
angle |theta| increases while the distance between liposomes center |d|
decreases. During this process the volume remain constant within a 10% error, which is consistent with cells doublets experiments done by :cite:`Maitre2012a`.

Discussion 
***********
.. 2

Cortical tension is homogeneous for single doublet
==================================================
.. 3

The use of equation :eq:`young-perpendicular` with :math:`\theta_1 = \theta_2 = \theta
/2` leads to the equality of tension on both side of the doublet during all the
experiments.We can then write :math:`\tau_1 = \tau_2 = \tau`. This result is
consistent with the fact that actin is distributed continuously all around the
liposome doublet. Hence, myosin II minifilaments pull on a continuous shell. In
these conditions equation :eq:`young-tangeant` simplifies to :

.. math:: 
    :label: eq3

    \tau_i - W = 2.\tau(t).cos(\theta(t)/2)


Where :math:`\tau(t)` and :math:`\theta(t)` are the tension and the angle at
the time t after myosin injection. A reasonable assumption is that
:math:`\tau_i-W` may depend on a variability of the initial adhesion between
liposomes. Since myosin does not operate at the interface between liposome as
it is free from actin, it is also reasonable con consider the tension and
adhesion energy constant for a given doublets through time. That is to say
:math:`\tau_i-W = \tau_{i,0}-W_0`.
Therefore we obtain the expression of the tension :math:`\tau(t)` during the acto myosin contraction that reads : 

.. math::
    :label: eqtime

    \tau(t) &= \frac{ \tau_i - W }{2.cos(\theta/2)}\\
            &= \frac{ cst           }{2.cos(\theta/2)}


Hence we can evaluate the tension relative to its initial value over time :

.. math::

    \frac{ \tau(t) }{\tau_0} = \frac{cos(\theta_0/2)}{cos(\theta(t)/2)}


Relative increase in cortical tension
=====================================
.. 3


Interaction of myosin II filaments with a biomimetic actin cortex induces
tension build up. The cortical tension, normalized to its initial value,
increases and reaches a plateau where :math:`\tau(t) = \tau_{peeling}` (
:num:`Fig#fig3e`)with the same trend as |theta|.  Note that if the actomyosin shell
breaks and peels, the doublet recovers its initial shape (see dashed blue line
for :math:`d` and |theta| on  :num:`Fig #fig3b`, :num:`#fig3c`, :num:`#fig3d` ). The average relative tension is found to
be :math:`\tau_{peeling}/\tau_0 = 1.56 \pm 0.56` (n=5) in 3D and
:math:`\tau_{peeling}/\tau_0  = 1.25 \pm 0.15` (n=5) in epifluorescence, in
agreement with the underestimates of the contact angle in epifluorescence. 


.. _fig3e:
.. figure:: /figs/Fig_03-E.png
    :width: 80%

    Increase of the tension ratio between the tension :math:`\tau(t)`at time
    :math:`t` and the initial one :math:`\tau_0`. 
    Same color code for same doublets as in figure :num:`#fig3b`, :num:`#fig3c`
    and :num:`#fig3d`. Note that the blue dashed line corresponds to the
    evolution of geometrical parameters of the same doublet, analyzed even
    after actin cortex rupture. It recovers its initial parameter values.




Cortical tension increase in doublets and in cells
==================================================
.. 3

In cells, cortical tension can be as low as 50 pN/µm in fibroblast progenitor
cells :ref:`KRIEG NatCellBio 2008` and can go up to 4000 pN/µm for
dictyostelium :ref:`SCHWARZ 2000`. Surprisingly, when myosin activity is
affected, either by drugs or by genetic manipulation  the cortical tension only
decreases by a factor of about 2. Cells are also observed to round up during
division :ref:`KUNDA 2008` in which an  increase of tension by a factor of two
is sufficient.  Our `in vitro` reconstruction is able to capture this feature
in the change of cortical tension. Indeed, we observe a cortical tension of the
doublets increasing by a factor 1.1 to 2.4.



Different contributions for cortical tension
============================================
.. 3

.. todo: 2 missing citations

Cortical tension is the sum of the membrane tension and the tension due to the
acto myosin cortex. We question how the membrane contribute to cortical tension
and in our assay we show that it count for about 50% of the cortical tension.
In suspended fibroblast cells, membrane tension is estimated to be 10% of the
cortical tension :cite:`Tinevez2009`. When polymerisation of actin is
stimulated, the cortical tension is multiplied by a factor of 5 showing a
strong dependence also with actin dynamics :cite:`Tinevez2009`. Hence he
residual tension in cells might be due to actin dynamics which is absent in our
experiments. How actin contribute to cortical tension is still an open question
that need to be addressed in the cell geometry.  Whereas actin polymerisation
outside outside a liposome has been show to generate inward pressure
:cite:`[missing citation ...]`, how this can be translated to tension  is a different geometry is
not yet clear. `In vitro` assay are on their way to mimic actin dynamics in
cells :cite:`missing citation ...` and will allow to unveil the mechanism of tension build up by
actin dynamics, which  is the remaining module that need ti be understood. The
effect of myosin and the one of membrane being clarified in this study.


Conclusion 
===========
.. 3

We provide a biomimetic reconstitution of tension build up through acto-myosin contractility using liposome doublets. Cortical tension change is visualized in situ over time by analyzing doublet shape changes. This method allows us to directly quantify the relative increase in tension due to myosin, separately from the one due to actin dynamics. Understanding contraction of composite systems built brick by brick on the model of a cell tile the road for the reconstitution of complex systems like tissues.


.. _full3dfit:

3D fitting
**********
.. 2

The obtention of geometrical parameter of doublets is challenging, indeed in
classical phase contrast microscopy, or epifluorescence  the acquired images
only capture one of the plane of the doublets. This makes the experiment 
difficult as the observation plane have to be kept in the 
equatorial plane of the doublet.

In order to achieve good precision in the measure of the contact angle we
decided to use confocal microscopy and acquire evenly spaced stacks. From
theses stacks where reconstructed 3D structure of a doublet. From the 3D
structure of the doublets can be recovered its the geometrical parameters and
the contact angle can be calculated.

In order to determine the geometrical parameter of the doublets through time
time we modeled the doublets as two intersecting sphere simulated the 3D
obtained imaged and adjusted the parameter of the model to reflect the obtained
experimental data. 

I was responsible for developing a fast and precise methods to reliably and
automatically recover the geometrical parameter of the liposomes doublets
acquired using spinning disk microscopy. I will develop the principle of this
methods and the result on liposomes doublets in this parts.

Finding a single liposome
=========================
.. 3

In this part we show the principle that allowed us to determine the 8
geometrical parameter that characterise a doublet 2 centers (X,Y,Z) and 2 radii
(|R1| and |R2|). 


As the principle for finding the geometrical parameter does not differ with the
number of dimension.  The methods can apply with  more dimensions (deformed
ellipsoid liposome, or multi channel imaging), the principle stay the same in a
space with less dimentison, so  we will restrict ourself to a single liposome
on a 2D plane (X,Y position of center and R, radius)  instead of the eight of
the doublets.

Experimentally liposomes are observed using fluorescently labeled actin that
form an homogeneous micrometric actin shell. In the observation plane, the
liposome shows as a bright ring of given thickness (we will refer to as the
`ground truth` signal), on top of this image are various noises due to the
presence of fluorescent actin monomers in the buffer solution, electronic noise
from the camera CCD, or other. Eventually, the noise in the outside buffer due
to monomeric actin can be higher than inside which is fee of actin. 

The signal from a liposome and the addition of noise can be replicated
numerically as seen on  :num:`figure #fig-2d-sim`.


.. _fig-2d-sim:
.. figure:: /figs/modl-2D-doublet.png
    :alt: liposome Model

    Left : A simulation of liposome fluorescent of an uniform shell or membrane
    (`ground truth`).  Middle: Same Image Adding Gaussian noise. This simulate
    one plane from a confocal Z-stack.  Right: Simulation of Liposome with
    fluorescently labeled actin shell in fluorescent External Buffer and non
    fluorescent inside buffer.

The ground truth signal can be modeled numerically using several parameter of
the system (center and radius of liposome, point spread function of microscope,
...). 

To find the correct parameters of the doublets we will numerically correlate 
the acquired data with the numerical model and search for the value of the correlation that correspond to the real parameters, In which the correlation between the model and data can be written.

.. math::

    r_{xy}=\frac{\sum\limits_{i=1}^n (x_i-\bar{x})(y_i-\bar{y})}{(n-1) s_x s_y}

In which :math:`x_i` are luminosity values of each of the :math:`n` pixels in
the acquired data, :math:`y_i` are the luminosity of the pixels in the model
:math:`\bar{x},\bar{y}` correspond to average values over the images,
:math:`s_x` and :math:`s_y` are the standard deviation of the luminosity
values.

As the monomeric fluorescently labeled actin and electronic noise are dominant
in the acquired images, we can assume a uniform noise on top of the `ground
truth` signal. The correlation between the model and the noise is in average
uniform.

.. math::
    r_{noise,model(params)} = cst

And the correlation between the `ground truth` and the model is expected to be
maximal for the parameter of the model that  equal the real geometrical
parameters of the doublets.

.. math::

    \operatorname*{arg\,max}_p\left(r_{data,model(p)}\right)= \operatorname*{arg\,max}_p \left(r_{groundTruth,model(p)}\right)

Thus searching the value of the parameters that maximize the correlation
between the model and the data implies allow to find geometrical parameters we
are interested in.  
    


We can test the ability to do this numerically by generating data, adding noise
to it and try to recovering the parameter of the `ground truth`.

By looking at the value of the correlation between generated data and the model
as a function of parameters of the model, we can check that the correlation
value are maximal when the model center value correspond to the `ground truth` center value (Figure :num:`corr-fun-1`), and when the radius of the model liposome has the same radius in the model correspond to the radius in the generated data (Figure :num:`corr-fun-2`).



.. .. figure:: /figs/corrfun-noise-.png

.. _corr-fun-1:
.. figure:: /figs/double-c-_100-by-100-rc-40_0-noise-0_5-delta-4_0_.png 
    :alt: liposome Model
    :width: 60% 

    Value of the correlation as a function (arbitrary units) of two of the fit
    parameter. Radius of the liposome in the model is taken as
    equal to the value of the ground truth, and position of the center is
    varied on X and Y direction. The value of the correlation is maximal for
    the position of the center in the model that equal the one ground truth.  We
    can see local maxima on the 3D representation that are well below the value
    of the global maximum. The peak at the global maxima is sharp hinting  that 
    the search of the maxima need relatively good initial
    parameters (lower than ~1/10 of liposome radius). The sharpness of the peek
    point that the result of the fit parameters on experimental data should be
    robust.  
    
.. _corr-fun-2: 
.. figure:: /figs/c-R-_100-by-100-RC-40_0-noise-0_5-delta-4_0_.png 
    :width: 60% 

    Same as :num:`figure #corr-fun-1`  with Y position of the center taken
    as equal to the ground-truth, variating X position of the model and
    radius of the liposome. The graph show the same properties as before.



Using minimisation technique we can search the parameter space of the model an
maximise the correlation between the model and the experimental data. We then
recover the geometrical parameters of the liposomes. This can be done by
efficiently computing the value of the correlation only in a few hundreds of
points and get access to the  liposomes geometrical parameters, here position
and radius.



Fitting a doublet
=================
.. 3


The determination of contact angle on epifluorescence image or phase contrast
images are often underestimated as the imaged plan is not one of the doublets
equatorial plan. Moreover, most determination of contact angle on phase
contrast and epifluorescence images are done manually :cite:`Maitre2012b` and
are subject to experimenter biased as experimenter draw the tangent line at the
contact point between the liposomes. Thus we decided to do fitting of acquired
3D stack with confocal microscope. In our case we avoided the usage of
fluorescent lipids that could change the tension of the membrane.

As seen on :num:`Figure #fds`, the doublets are covered with a
thin micrometer-thick layer of fluorescent actin filament. It is such layer
that we imaged with confocal spinning disk. The contact angle is defined as the
angle between the lipid bilayer, when imaging the actin-layer this correspond
to the angle between the inner surface of the actin network on each liposome.

Thus in order to determine the geometrical parameter of the doublets we need to
model the actin shell. As the liposome in contact are two spherical caps the
uniform actin layer also form two spherical caps with a given thickness. The
total signal is thus the union of two spherical caps blurred by the point
spread function of the microscope. This can be seen on :num:`figure #mproj1`

.. _mproj1:
.. figure:: /figs/max_proj_340A.png
    :width: 80%

    Maximum projection along X,Y and Z of recorded stacks, green channel actin.
    One can see that the liposomes doublets are stuck to the surface of the
    observation chamber.

As the contraction of the doublets is rapid, and recorded 3D movies contains a
large number of frames, it is crucial to be able to compute the model and the
correlation in a reasonable time (less than the hour per images) in order to
achieve this, beyond calculating the model as efficiently as possible one can
replace the exact calculation of two spherical cap and the point spread
function of the microscope by the union and subtraction of sphere followed 3D
numerical Gaussian blur.

.. figure:: /figs/3dblur.png
    :width: 60% 

    Principe of numerically approximating the two spherical caps as the union
    and intersection of sphere, follow by a 3D numerical Gaussian blur. The
    speedup compared to the exact calculation of the fluorescent density allow
    to make fits on doublets in minutes instead of hours.

Though the use of numerical technique is not without artifact.  In the case of
discreet Z-stack sufficiently spaced the difference of radius between
fluorescent rings in subsequent stack can led to an "ring-artifact" (`Fig
#ring-artifact`) when using numerical Gaussian blur. In the case of a too
pronounced "ring-artifact" a "ghost" spheres can appear around each liposomes
which might lead the fitting process of the doublets to fall into a local
maximum of correlation, thus leading to wrong value of the geometrical
parameters.

.. _ring-artifact:
.. figure:: /figs/ring_artifact.png
    :width: 90%

    Left : One plane of the numerical model with exaggerated ring artifact due
    to an under sampling of the model in the Z-direction, stacks from "Far" Z
    leaks onto current Z-stack and form a ring.  Right : Same plane of the
    model with enough sampling plane in the Z-direction do not show the ring
    artifact. In this case we use a sampling equal to the number of slice than
    the recorded data. (X,Y in arbitrary units)
   

In our case we have a sufficient number of stacks so that the numerical model
with the same sample size as the data do not show the ring artefact and have
smooth transition near the position of the spherical cap. Though the ring
artifact can be eliminated by oversampling/interpolating the model before the
Numerical Gaussian blur and under sampling afterward to the correct number of
pixels.

The size of the
Gaussian blur can also be adjusted to be higher which will act as a regularisation
function for the value of the correlation between the model and the acquired
data (cf :num:`Figure #max-proj-model`), thus smoothing or eliminating local maxima, but reducing the precision in the position of the maxima.

.. _max-proj-model:
.. figure:: /figs/max_proj_model.png
    :width: 80%

    Maximum projection along X,Y and Z of numerical model, the "ring" effect
    can still slightly be seen near the pole of each liposome, but is not
    sufficient enough to have the minimisation process stick in a local minima. 


The value of the correlation between the model and the experimental recorded
data can be maximised using already available function, in particular we used
Nelder–Mead simplex as implemented in `scipy.optimise` python library. This
gaves us the 8 parameters of the doublets. Result of the fits are show in
:num:`figure #fig-fit-t0`.

.. _fig-fit-t0:
.. figure:: /figs/Doublet-402-A-Fit-t-0.png
    :width: 80%

    Maximum projection of confocal images in the X,Y and Z projection as well
    as the result of the fits shown as equatorial circles for the three
    direction of projection.


Using fast Cython code also allowed to also speed up fitting to a reasonable
time : one Z-stack of 3 millions pixels can be fitted in about 40 seconds. Thus
allowing the fitting of a full 3D movie of a doublets contraction to be done in
less than an hour for 30 to 40 frames.

To insure the fits where robust to doublets center displacement during
acquisition, the initial parameter of the fit where chosen manually for each
first frame of each sequences. The final fit parameter of each frame are reused
as initial fit parameter for the subsequent frame.

In order to test robustness of the fit, initial fit parameters where randomly
modified by an amount of +/- 1µm, and we checked that the final parameter did
not varied.

For a couple of parameter, the value of the correlation function can be plotted
to check for the regularity of the function and the absence of local maxima. :num:`Figure #gof2d` and :num:`figure #gof3d` show the


.. _gof2d:
.. figure:: /figs/gof-2d-doublets.png
    :width: 80%
    
    Correlation of the model and the data as a function of the center position
    of on of the model spherical cap along the X axis and the radius of this
    same spherical cap. Vertical axis in arbitrary unit.

.. _gof3d:
.. figure:: /figs/gof-3d-doublets.png
    :width: 80%

    3D representation of the data in :num:`figure #gof2d`, the shape of the
    function is the same as the simulation done with the `ground truth` in
    :num:`figure #corr-fun-1` :num:`and #corr-fun-2`



The correctness of the fit is also checked visually to check for error in the
procedure.  Fit was found to be alway accurate and coherent with manual
measurement of contact angle.  When red channel was also present and liposomes
contained sulphorhodamin, fits where also visually checked by using maximum
projection of the red channel.  Cf :num:`Fig #srhod`).

.. _srhod:
.. figure:: /figs/srhod_superimpose.png
    :width: 80%

    Maximum projection of the red channel (`sulphorhodamin`) and the fitted
    parameter for the doublet.
    

Discussion
==========
.. 3

In this part we show that by modeling the liposome doublet and using
fluorescently labeled actin we are able to develop a technique that
automatically and robustly determine the geometrical properties of the liposome
doublets.

We note that red fluorescent dye present in the inside buffer of the liposome
could be use conjointly to the green channel in order to improve the quality of
the fit, though  would require the extra parameters of the interface radius. As
the computation time needed to fit the doublets increase rapidly with the
number of parameter, this solution found out to be impractical.  Moreover, the
curvature of the interface being relatively small and the difference between
the curved interface and a plane being close to the optical resolution, we can
expect the fit to be relatively unstable.  The use of fluorescently labeled
lipids for the liposome membrane also suffers from the same issues of extra if
one want to recover the position of the interface.



Conclusion
==========
.. 3


We developed a robust and automated methods able to determine the geometrical
parameter of liposome doublets. This allowed us to determine robustly and
thought time the geometrical parameters of liposomes doublets without
experimenter measurement biases due to the selection of the illumination plane,
resolution of optics and luminosity scale.

We have seen that liposome doublets with reconstituted acto-myosin cortices are
a biomimetic system that allow to follow the change in cortical tension through
time. 3D fitting helped us quantify it by obtaining the contact angle. 

Observing the contraction of multiple liposomes doublets simultaneously and the
ability to automatically determine the geometrical parameters allows more
sample to be collected. Faster and more reliable data acquisition on actin
network contraction will allow a better understanding of the effect of actin
network `in vitro` which also pave the way to reconstitution of more complex system.
