Liposomes Doublets
##################
.. 1


Introduction 
*************
.. 2

We have seen that in cells actin is a key component to form structure like the
actin cortex in order to transmit forces. In order to drive shape changes,
cells regulate the  sub-micrometer thick actin cortex that lies beneath the
membrane :cite:`Clarke`2013`. The actin cortex drives cell shape changes
:cite:`Salbreux2012b` and the presence of myosin lay a fundamental role in the
change of tension of the acto-myosin cortex :cite:`Tinevez2009`. Cortical
tension can be measured on cells to vary between 50 and 4000 pN/µm depending on
actin and myosin activity.  The change of cell cortical tension can also be
modulated by cell-cell adhesion :cite:`Maitre2012` which have impact on cell
sorting. 

Such acto-myosin cortices have been reconstructed on cell-sized liposomes
:cite:`Carvalho2013a` which showed that attachment of the actin cortex to the
membrane had a crucial role in the behavior or contractile acto-myosin network. 

In this study, I worked with K. Carvalho and J.Lemière in order to extend the
system developed in :cite:`Carvalho2013a` to monitor the cortical tension
increased of a biomimetic actin cortex formed on liposomes.

To determine the role of cortical tension in cells, :cite:`Maitre2012` use cell
doublets. Here we form a liposome doublets around which we produce an actin
cortex `in vitro`. The shape change of these liposomes doublets allow us to
monitor thought time in a non-invasive way the increase of cortical tension.
We develop a methods for  precise monitoring of the doublets deformation
in order to determine accurately the increase of tension induced by the
injection of myosin motor on a preformed actin cortex.

.. image of peeling crunching ? 

Formation of liposomes doublets
*******************************
.. 2

Liposomes are obtain by electro formation (cf :ref`m_et_m`) from a mix of EPC
and PEG-biotin lipids. The presence of streptavidin in the working buffer
allow liposomes to naturally stick together to form doublets.

.. image  picture of liposome doublets.

Formation of actin cortex on doublets
*************************************
.. 2

Formation of the actin network on doublets are done as in
:cite:`Carvalho2013a`. Actin filament  stabilized by phalloidin with
biotinilated monomers are liked to the PEG-Biotin lipid of the membrane through
streptavidine present in solution. The presence of streptavidin also cross
links the filament. Such network has already been characterized in
;cite:`Carvalho2013a`.  Note that actin monomers being added after the
formation of liposome, the interface between the two liposomes that compose the
doublets are free of actin. As the actin added is fluorescent, this can be
checked by epifluorescence as the interface appears dark compared to the rest
of the doublet.

.. _figDoubletsSchema:

.. figure:: /figs/doublets-schema.png
    :alt: Formation doublet schema
    :width: 90%

    Formation of doublets: 1) In the presence of streptavidin, single liposome
    (a) aggregate into doublets (B). The addition of biotinylated actin
    filament stabilized with phalloidin (2) form liposomes doublets covered
    with a micrometer-sized actin network (C). The interface between the two
    liposome is a double lipid bilayer free of actin filaments.


To visualise the interface between liposomes, and avoid the use of fluorescent
lipids that may affect the membrane mechanics :cite:`Sandre1999` the inside
buffer of half the liposomes are labeled with 0.9 µm of sulphonamide B
eventually leading to half of the doublets being fluorescent.

Geometrical parameters
**********************
.. 2

To study the doublets geometry we model each liposome as well as the interface
between them as two spherical caps with their respective center, and radius, as show in `figure #fig-notation-doublets`. 

.. _fig-notations-doublets:
.. figure:: /figs/notations-doublets.png
    :width: 80%

    Notation of parameters for doublets

The center (X,Y,Z) and radius (R) of the three spherical caps completely determine the problem, though it is interesting to look at other related parameters which are :

    - the total volume of the liposome doublets `V`
    - the contact angle between the two liposomes
    - Each of the "half"-contact angle which are the angle between the
      interface and each of the liposome :math:`\theta_1,\theta_2`
    - The distance between liposomes center.

The model have a rotational symmetry along the axis that passes through the
center of the three liposomes, we thus consider only one of the equatorial
plane when referring to the model. Unless otherwise specified, all component
onside of such a plane are null.

Effect of myosin injection
**************************
.. 2


We images liposomes doublets placed in an open chamber either in phase contrast
and epifluorescence, or spinning disk microscopy in the red  (sulphorhodamine)
and green (actin) channel.

Myosin II that form bipolar filaments :ref:`Chapter 1` is slowly injected into
the chamber, and trigger a shape change of the doublets in a matter of minutes.

.. figure:: /figs/doublet-contract.png
    :width: 40%

    Doublets contraction showing green channel (actin): Left doublets before
    Myosin II injection. Right: doublets during contraction due to Myosin II.
    Scalebar is 5 µm 

.. |theta| replace:: :math:`\theta`
.. |theta1| replace:: :math:`\theta_1`
.. |theta2| replace:: :math:`\theta_2`

The distance between liposome center decreases as the total angle :math:`\theta
= \theta_1+\theta_2` increases. The contact angle and other parameter of the
doblets are obtained by fitting spherical caps onto the 2D epifluorescence
images or 3D confocal stack as describe later.  In the absence of myosin, the
contact angle |theta| is measured to be :math:`\theta = 64 \pm 16 °` whereas in
the presence of Myosin II (200 nM) we find a value of :math:`\theta = 86 \pm 21
°`. Measured of contact angle after Myosin injection are done before the cortex
ruptures as characterized in :cite:`Carvalho2013a` .

Angle related to tension
************************
.. 2

.. |tau1| replace:: :math:`\tau_1`
.. |tau2| replace:: :math:`\tau_2`
.. |taui| replace:: :math:`\tau_i`
.. |taut| replace:: :math:`\tau_t`
.. |W| replace:: :math:`W`

Each liposome have its respective tension |tau1|, and |tau2|.  In the absence
of the biomimetic acto-myosin cortex these tensions correspond only to the
tension of the liposomes membranes. The interface between the two liposome is
formed of a double lipid bilayer, and it tension is due to two contribution.
The tension of the lipids bilayer themselves, we will note |taui|, and the
adhesion energy per surface unit |W| due to the biotin-streptavidin-biotin link
between the two lipid bilayers. The total tension at the interface can thus be
written :math:`\tau_t = \tau_i -W`.


As the movement of the contact line during the contraction in in the order of
µm/min we can consider the contact line between the liposomes and the interface
to be  at equilibrium, we can thus apply Young's equation over time. This allow
is allow to relate the tension of each of the lipid layers and the angle
between them at each instant of the contraction. We can in particular project
the result of this equation onto the direction of of the contact surface
tangent : 

.. Math::
    :label: young-tangent

    \tau_1 - W = \tau_1.cos(\theta_1) + \tau_2.cos(\theta_2)

And on the direction perpendicular to it :

.. math::
    :label: young-perpendicular

     \tau_1.sin(\theta_1) = \tau_2.sin(\theta-2)


These equation link the tensions to the contact angles both before, during and
after the contraction. Value that relate to the before contraction phase will
be suffixed by  `0` indices. Thus, for example :math:`\tau_i,0` refer to the
tension of the interface before the addition of myosin, and |taui| refer to the
tension of the interface at any instant of the contraction.

Contact angle dispersion
************************
.. 2
    

The value of the contact angle |theta| varies across sample both before
addition of myosin II. It reflect an initial variation of tension in
:math:`\tau_{i,0}`, :math:`\tau_{1,0}`, and :math:`\tau_{2,0}`. This could be
due to a difference in the tension acquired during liposome preparation, to a
variation of adhesion energy between liposome, or effect of tension build-up
during the formation of the actin shell. As the dispersion in contact angle is
in the same order as the increase in angle with the addition of myosin, a
statistical analysis of the contact angle before and during contraction is
difficult. Thus to avoid this effect of dispersion, we follow the evolution of
:math:`\theta` on the same doublet during time.






