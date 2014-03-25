
.. Part


Background
##########


.. todo::

    Misc To say

        - Even in mitosis for big cell, actin is needed to assemble chromosomes :cite:`Lenart2005`
        - Rapid change in actin structure :cite:`Vasilev2012`, timing is also important (exposition to inomycine disrupt cortex functionality)
        - F-actin network capable of supporting mechanical load :cite:`Feric2013` 
        - Presence of f-Actin mesh work mesh size ~0.5µm :cite:`Feric2013` 
        - This actin network can wistand repetitive compression :cite:`Feric2013` 
        - F actin network might be linked to the lamin (a kind of IF) cortex around the nucleus :cite:`Feric2013` 
        - Such a network would only need to sustain a pressure on the order od 0.01 PA :cite:`Feric2013`,
          and is essential to fight against gravity



Introduction
************

Cells are the basic component of living organism, understanding their
individual behavior and the way they function is a key step into understanding
how they interact with their environment and other organism. One of the key
component to most of organism is Actin, a protein which is highly conserved
across the species and play a important role in cell mechanics, from cell
migration to cell differentiation and division. It plays also a non negligible role
in most mechanical properties of the cell and its interactions with the
environment. In particular actin is the main component of the actin cortex :
the part of the cell cytoskeleton responsible for cell mechanical properties.
The properties of this actin cortex is drive by the mechanics of the properties
of its main component : a dynamic actin network. Understanding this actin
network is hence a key piece to learn how the actin cortex behave. 

The properties of an actin network highly depend on it's structure. The
structure itself depends on many parameters that influence how the network is
formed. Network structure and formation can be not only influence by its
physical and chemical environments but also by the variation of this
parameters with time and space.

Cells are complex systems that adapt their shape, mechanical properties and
biochemical conditions permanently. The spacial repartition of theses
properties is also variable as the cell regulate the concentration of proteins
all across its body. To well study the effect of each components independently,
it is crucial to study actin network in a controlled environment.

Biomimetic systems allow to respond to most of these concern, they provide a
well controlled environment where biochemical condition can be well controlled
both in space and time. Theses systems keep their biological relevance, as they
can mimic *in vivo* phenomenon. Biomimetic systems are also well adapted to the
tools available and the approach from a physics point of view. The optical trap
will allow us to study local mechanical properties of actin  network  with a
high time resolution which could allow to get insight into the variation of
theses properties as a function of time. 


During my PhD, my work has mainly be to study the mechanics of branched actin
network polymerizing on optically trapped polystyrene beads. Such network was
studied before :cite:`Kawska2012`  but have suspected to be highly inhomogeneous,
the use of optical trap allowed to probe mechanics of part of the network
unaccessible before.


.. todo::

    - time resolution
    - network dynamics
    - Move to liposome, 
    - study in OOCyte : 
    - Basically from purely biiomimetic to real cells









.. :cite:`...`  

.. include:: cells.rst
.. include:: roleofactin.rst

In vitro reconstituted actin networks
*************************************

.. todo::

     - bead assay
       - when it was designed
       - mimic listeria motility 

       - nucleation on the surface by Arp2/3 NPF, both mimicking the
         nucleation at the membrane outside of bacteria (listeria) and inside
         cell. 

     - liposomes (GUV): 
       - Giant unilamellar Vesicle

     - controlled biochemical condition 
     - bottom up approach  

Liposomes
^^^^^^^^^

A more advance system to reproduce a cell are Giant Unilamelar Vesicules
(GUV) also referred to as liposomes. Liposomes are a lipid bilayer closed on
itself into a spherical shape. Those represent a perfect first step into
recreating the condition as, like a cell, it is a closed system, that
separate its inside from its outside using lipids. 


Actin networks as viscoelastic material
***************************************

To study the mechanical properties of an actin network it is important to
describe the condition in which we study it to select the adequate models.

We have seen previously that while polymerising, G-actin form F-actin filament
with a characteristic called the persistence length (:math:`l_p`) which
represent the length after which the bending of filament becomes
non-negligible. For actin filament, the persistence length is in the order of
10 µm. This mean that for scale much smaller, portion of actin filament can be
considered as completely rigid, like in cell cortex where meshwork have a
typical size smaller than 250 nm. In the other end, add length scale much
bigger than :math:`l_p`, filament can be considered as fully flexible. Even if
for typical cells, the length scale is rarely much bigger than the persistence
length of actin, `Xenopus` eggs can be as big as 1 mm, so hundreds fold the
persistence length.  In mouse oocyte that can go up to a 80µm  diameter – and
on we will do some analysis – are hence slightly less than an order of
magnitude bigger than the persistence length. Still For majority of cell, the
typical size we are interested in is about the persistence length of an actin
filament, making it neither purely rigid nor completely flexible. 

For the above reasons, solution of actin are often compared to semi-flexible
polymers, and models that predict comportment of actin network often take
foundation on polymers physics :cite:`Morse1998` :cite:`Morse1998a`. Still, if
theses models rely on local microscopic parameter, experimental methods only
have access to bulk properties of the studies material, and it is from theses
properties, and through the models that we can deduce possible values for the
microscopic models.

Elastics Modulus
================

The elastics Modulus are probably the one that seem to be the easiest to
understand. They are characteristic of the material that will describe how a
material will deform non permanently  when applied a force. The stiffer
something is the higher its elastics modulus will be. There are two specific
elastic modulus we will be interested in in the rest of this manuscript,
`Young's Modulus` and `sheer modulus`. The first one describe more specially
how material will react to it's compression or extension, While the second one
describe how a material resist  sheering. in isotropic and homogeneous
material, the Young modulus (noted E) and the sheer models (G) are linked
together by the Poisson ratio (:math:`\nu`, with that we will see later by the
following relation.

.. math::
    
    G = \frac{E}{2(1+\nu)}


Hence at fixed Poisson ratio, and as :math:`\nu` is usually around a value of
:math:`0.5`, it is common to use G and E interchangeably and to just referee to
it as "elastic modulus". Both G and E units are homogeneous to :math:`N/m^2`,
so :math:`Pa` It is interesting to have an idea of the oder of magnitude of a
few usual materials. Aluminum will have an elastic modulus :math:`G_{Al}\simeq
70~GPa` while rubber will be more in the order of :math:`G_{rubber}\simeq
0.1~GPa`. The elastic modulus of muscle is in the order of :math:`G_{muscle}
\sim 10~kPa` and brain tissues around :math:`G_{braaiiin} \sim
0.1~\text{to}~1~kPa`.


For a  more accurate definition of the Young moduli, it is the ratio between
the stress along the direction of the deformation by the relative elongation. 
It is then proportional to the force by unit of surface applied divided by the relative elongation:

.. math:: 
    
    E &= \frac{\sigma}{\epsilon} \\
      & = \frac{   F/S }{   \Delta L / L_0        }


.. figure:: /figs/youngm.png
    :width: 70%
    :alt: Definition of young modulus
    
    Schematic of Young Modulus definition. F, force applied to sample, S
    surface of cross section when uncompressed, :math:`L_0`, length when no load
    applied. For both compression and extension, in the regime of small
    deformation, the relative change of length is proportional to the applied
    force. Here, the material can be seen to expand/contract in the direction
    orthogonal to the direction of application of the force, in the case of an
    incompressible material (:math:`\nu \neq 0.5`) this con be seen as the
    conservation of volume of the material.

The sheer modulus is it defined by :

.. math::

   G &= \frac{\tau_{xy}}{\gamma{xy}} \\
      & = \frac{   F/S }{   \Delta x / l        }

.. todo::

    Scheme for sheer modulus, shoudl we merge it with one where we explain
    Morse Paper with actin filament going throughthe cross section

Poisson Ratio
=============

We have just seen that the sheer modulus is linked to the Young modulus using
the Poisson ratio.  The Poisson ration is another characteristic of a material
that define how much a material will compress/expand in a direction
orthogonal to its elongation.

Typically, if one want to have volume conservation of material, one have to
take a Poisson ratio of `0.5`.  A Poisson ratio lower that this value, will
correspond to material expanding less than incompressible materials, with a
critical value being 0, where the material only expand or contract in the
direction of the main stress.  
On the other end, material with a Poisson ratio superior than 0.5 would show a
bigger deformation in the orthogonal direction than with a simply
incompressible material. 

.. todo::

some value for tissues. Existence of  negative PR
    material we put everything in G, make it complex define the real and imaginary
    part as G' g'' 


Viscosity
=========

Like elasticity, viscosity is something tangible we are used to work with in
everyday life, the more viscous a material is the more difficult it is to move
something in it at high speed. And indeed, viscosity is the pendant of Elastic
modulus but when considering force induced by speed instead of displacement.
The force exerted by the gradient a velocity, on a surface `S` or orthogonal to
direction :math:`\vec z` will be written :

.. math::

    F = \eta \frac{\partial v}{\partial z}

Where :math:`\eta` is the viscosity, and is expressed in :math:`Pa.s`. We will
also note that viscosity is often written :math:`\mu`, and can
also while dividing by the fluid density (:math:`\rho`)  then being :math:`\nu = {\eta}/{\rho}`.

At room temperature water have a viscosity of around 1 mPa.s, an honey have a viscosity of around 10 Pa.s


.. todo::

    Relatively short, compare to E/G but for speed, value of viscosity for
    different fluid ?  Quick reynolds equation ? In the condition we are interested
    in we are at extremely low reynolds, so no intertia involved ?

Viscoelastic
============

Typically, no material are purely elastic or purely viscous. When glacier can
seem purely solid at the time scale of a few days, observation on longer time
scale ranging from month to years will convince you that ice is not only a
solid but can also flow. Of course water in its solid form is not the only
material which is both solid and viscous. For this reason models have been and
are still developed, The Kelvin-Voight and Maxwell models are two and the
simpler one. A thought experiment to represent both is to put a spring and a
dash pot in parallel or series.  The resulting model will have a viscoelastic
behavior. 


.. figure:: /figs/MKV.png
    :width: 70%    

    Maxwell model schematic on the right and Kelvin-Voight model on the right.
    Both are a simple approach to express the properties of a viscoelastic
    model. The response to a creep compliance will deffer in both case. Maxwell
    model will mostly behave like  a fluid with viscosity :math:`\eta` after a
    long time, where the Kelvin-Voight model will mostly reflect the elastic
    component at constant stress exerted. (Schematic in Public Domain, adapted
    from Wikimedia).

The idea for more complex models is the same, any material can be seen like an
(infinite) combination of spring for elasticity, and dash-pot, for viscosity
associated which each other.

The generalised model can then be described using a unique parameter, we extend
the Young and sheer modulus  with a imaginary part capturing the effect of
viscosity. In addition to an imaginary part, we can introduce a dependency of G
with a pulsation (:math:`\omega`) when working in the frequency plane.

The real and imaginary part of :math:`G^*` are respectively called storage (:math:`G'`) and loss (:math:`G''`) modulus.
We can then write the following :
   
.. math::
    G^*(\omega) = G' (\omega) + i.G''(\omega)


The star denoting the complex character of `G` is often dropped, as well as the explicit dependency with :math:`\omega`.


The viscoelastic properties of a material are then fully characterized if one
get the full expression for the storage and loss modulus as a function of the
frequences



Frequency dependent value
=========================

 - Classical example of non Newtonian fluid (?), depend on frequency.
 - decompose in pulsation, then miracle :math:`i\omega \simeq \frac{\partial}{\partial t}` 
 - maxwell voight model, spring + dash pot

Active and Passive microrheology 
********************************

Optical tweezer
***************

Optical tweezer, or optical trap are a technique that allow to trap object near
the focal plane of microscope at the point where a high power laser is focused.
It is a versatile technique that allow to trap both fabricated object and part
of living cell an apply force up to a few tenth of pico newtons and detect
displacement of a few hundreds of nanometers.

To understand that light can trap an object, you should keep in mind that
despite having no mass, light carry momentum, and as for any massive object,
changing the trajectory require applying a force and this object. According to
newton third law, if you apply a force on an object, the object exerted the
opposite force. This will lead to object with higher refractive index being
attracted by toward higher light intensity. In a parallel laser beam, with a Gaussian
intensity profile, this will lead to  the object being attracted toward the
center of the beam. 

In addition to the lateral trapping, if the laser beam is focuses, this lead to
another weaker intensity gradient along the direction of propagation of the
beam, the intensity being at its highest at the laser waist. 

A focused laser inside a laser into the microscope's objective then act as a
three dimensional potential that keeps particle like hold in a tweezer. Usually
the trapping in the observation plane is strong, while the stiffness of the
trap in the direction of illumination is weak.

It should be noted that if trapped particles are hold strongly near the laser
focus, this does prevent the laser from exerting force on surrounding
particles, usually slowly attracting floating object passing in the converging
beam of light toward the plane of observation. The light also having a non
negligible radiation  pressure, object in the second half cone of diverging
light beyond the observation plane are often repel away from the trap.


.. figure:: /figs/ot1.png
    :alt: schematic of setup plus one
    :width: 90%

    Deflected light by a transparent bead change the momentum of light, so the
    light is exerting a force on the bead. The bead will be attracted toward
    the high intensity.  For a focused laser beam, the bead will be attracted
    near the focus of the laser.


In addition to allowing the object, to be hold in place, optical trap have the
advantaged of allowing the high frequency measurement of the force exerted on a
object as a function of time, though careful calibration of the trap is
necessary, and different methods can be used to do such calibration
:cite:`Jahnel2011`, :cite:`Vermeulen2006`. Indeed, as we saw previously, when
the trapped particle is not in the trap center it though exert a force on the
light beam, though slightly deflecting the light beam. Using optics and lenses
correctly placed on the Fourier plane of the sample, it is hence possible to
translate this change of orientation of the light  beam into a displacement of
a light spot onto a photo detector with hight sensitivity to displacement.

One of the quality of optical trap is that it often allow the multiplication of
the number of trap. A simple method allowing the obtainment of two trap is to
split the incoming light into two orthogonally polarized independent beam.
Instead of sharing the laser power between the different trap using
polarisation, one can use what is known as time sharing. By switching the laser
rapidly between traps at a much faster time scale than the relevant time scale
of the experiment, one is able to virtually achieve multiple traps on the same
sample.

In our case, the rapid switching is achieved using Accousto Optic Deflector
(aka AODs).  ADO consists of a crystal in which propagate a high frequency
sound-wave. The passing of the sound wave generate local change in the
refractive index of the material which then act as a diffracting grating. In
the right condition, the trapping laser passing through the same crystal will
then be deflected by generated grating.

In practice, rapidly controlling the frequency and amplitude of the generated
wave into the crystal, allow direct adjustment of laser position of the trap
position. Using AOD also have the advantage of allowing control not only of
number and position of multiple traps, but also the individual power allocated
to each trap and though stiffness of relevant trap.

.. _ots:

.. figure:: /figs/setup-plus-1.png
    :alt: schematic of setup plus one
    :width: 90%

    A schematic of used setup. The following element can be distinguished. An
    1064nm Laser will be used for trapping, it first pass through two AODs that
    well respectively be responsible from moving the position of the trap in
    the X ad Y direction.  The first couple of lenses between AODs are
    responsible from having both AOD conjugated.  The second pair of lens will
    allow to steer the beam and make sure that the AODs are  conjugated with
    the back-focal plane of the first objective, putting then in the Fourier
    plane of the sample. Thus a change of angle of the light beam induce by the
    AOD in reflected into the objective by a change of position of the trap.
    The trapping light is collected by a second objective, converging on a
    Quadrant photodiode (QPD) conjugated with the back focal plane of the
    collecting objective. By construction QPD and AODs should be conjugated, so
    deviation of the light beam induced by one of the AODs is not supposed to
    induce any change of position of the laser spot on the QPD. Additional
    dichroics mirror allow to use bright field and epifluorescence at the same
    time than using optical tweezer.


Membrane Physics 
*****************


.. myosis

Myosis (to move away)
*********************

.. todo::
    - Asymetric division of oocyte, 
    - from diploid, to haploid,
      - spindle usually in mitosis pulled by microtubule

