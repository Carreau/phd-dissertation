Preamble
########
.. 1


During my PhD I decided to investigate the effect of actin network on the
mechanical properties of cells. Indeed, mechanical properties of cell are a key
parameter that has an crucial impact on cell and organism function. Being able
to detect changes, and understand the mechanism that govern them is a important
to be able to apprehend the behavior of cells, distinguish healthy from
malignant cell and tissues in order to control them.

During the last three years, I decided to focus on biomimetic system and
establish characteristic of actin network. Actin is a highly conserved
component across the living kingdom, and it plays a major role in cells
mechanics. By interacting with a number of other component of the cell, actin
is able to form a various number of network. It is on such network, and in
controlled condition that I decided to focus my research. 

Along this dissertation we will mainly focus on three system.

On the first one, we reconstitute an already observed actin network on a
biomimetic system, then show that from this network emanate a second sparse
actin network previously unseen, and characterize its mechanical properties. We
developed the idea that the effect of this second network cannot be neglected
in cell and investigate a few of the phenomenon it can be involved in.

As the effect of such a sparse actin has not been demonstrated we decided to
investigate the effect of another sparse actin network on a living cell. In
collaboration with College de France, we studied the mechanical properties
inside mouse Oocyte. We see in this system that the actin related protein can
have a hi impact on the structure and the mechanics both of the cell and the
actin network in it. 

As characterizing the dynamics of a network in a living cell is complex as we
only have few control on the biochemical condition, the third system has been
developed to allow to follow the modification of properties of actin network
with time without perturbing it. By covering a doublet of two liposomes by an
actin network and imaging it, we are able to deduce change in the network
properties only by looking at the change in geometry. 

.. todo:

    recap the organisation of the PhD

.. Part

Background
##########
.. 1


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
.. 2

Cells are the basic component of living organism, understanding their
individual behavior and the way they function is a key step into understanding
how they interact with their environment and other organism. One of the key
component to most of organism is actin, a protein which is highly conserved
across the species and play a important role in cell mechanics, from cell
migration to cell differentiation and division. It plays also a non negligible
role in most mechanical properties of the cell and its interactions with the
environment. Under the cell membrane is thin layer which properties control the
cell mechanical properties : the actin cortex. The properties of this actin
cortex is driven by the mechanics of the properties of its main component : a
dynamic actin network. Understanding this actin network is hence a key piece to
learn how the actin cortex behave. 

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
will allow us to study local mechanical properties of actin network with a
high time resolution which could allow to get insight into the variation of
theses properties as a function of time. 


During my PhD, my work has mainly be to study the mechanics of branched actin
network polymerizing on optically trapped polystyrene beads. Such network was
studied before :cite:`Kawska2012` but have suspected to be highly
inhomogeneous, the use of optical trap allowed to probe mechanics of part of
the network unaccessible before both because of their sensitivity and the
ability to get hi time resolution. I further moved toward studying actin
network on other biomimetic system constituted of liposomes, in order to better
understand the effect on actin cortex polymerisation on membrane tension and
characterize network dynamic through time. Finally I participated in a
collaboration in order to understand the implication such actin network in
living mouse Oocyte.


.. :cite:`...`  

.. include:: cells.rst
.. include:: roleofactin.rst

In vitro reconstituted actin networks
*************************************
.. 2

Living cells are complex organism, for which each function may require a number
of interacting proteins and components. To understand the action of each
individual component it is needed to isolate of modify their actin
independently.

In order to achieve the  precise tuning of each component independently two
approach are envisageable. An approach referred to  as "Top-Down" where
starting from the full system — in our case the cell — we will modify or remove
each of the component and study the global change of behavior. It is a complex
process that might be difficult to interpret as biological system have often
multiple pathways and feedback loop to regulate each of their process. With the
large number of component that constitute a living cell, it is also relatively
difficult to come up with the minimal system necessary to replicate a behavior.

The other approach, also referred to as the  bottom-up approach, require to
reconstitute the system  component by component until it replicate the expected
behavior. It is also a complex process, as there are a large of component to
chose from that can potentially be added to the reconstituted system, but often
lead to a wider range for the testable parameter as well as minimal number of
interacting component. This allow for a deeper understanding of the governing
principle of the system, and often permit access to a wider off accessible
conditions and individual tweaking of component.

In our lab we are mainly interested in the bottom-up approach and the use of
biomimetic system. We try to reconstitute biologically relevant behavior with
the minimal system constituted from pure protein components.

In particular in this manuscript we are interested in the mimicking the process
by which the listeria is able to hijack cellular mechanism, recruit proteins
responsible for actin polymerisation at the leading edge of the cell, and use
them to polymerize actin on its back. This is what allow the listeria to
propel itself fast enough (1.5 to 2 µm /sec) :cite:`Dabiri1990` to be able to
pass through cell membrane from one cell to the other.

The bead motility system is the minimal in-vitro system capable of replicating
the listeria motility.

Bead motility assay
===================
.. 3

Listeria  is 1.5 to 5 micrometer cylindrical bacteria that hijack cell
polymerisation machinery. It does so by the recruitment of single protein to
its read end : ActA. ActA activate the Arp2/3 complex. From the recruited
Arp2/3 will grow a dense branched and entangle actin network that will for a
comet behind the bacteria propelling the bacteria at the speed of actin comet
polymerisation. Listeria comets are composed of a wide range of protein, it has
though been shown :cite:`Loisel1999` that the number of required component can
be highly reduced.


The simpler system that can replicate the listeria motility is the bead
motility assay, it consist of a micrometer-sized bead covered with a nucleation
promoting factor that will activate Arp2/3 present in solution.  This NPF can
be ActA as in the case of listeria, but one can use other NPF like N-WASp or
pVCA as we will do in the rest of this manuscript. In the solution is also
present G-Actin, and Capping Protein to prevent the polymerisation from
happening away from the bead surface as well as the component necessary for
actin polymerisation (ATP, Salt...) 

Due to the presence of Capping Protein in solution and NPF on the surface of
the bead, the polymerisation of actin will happened only on the surface on the
bead forming a thin and dens actin gel capable of sustaining stress depending
on on the different protein concentration. Unlike in the case of listeria which
control on which if its side the nucleation process happens, this is not
controlled on bead motility assay. Though, in the right condition
:cite:`Kawska2012` the dense actin gel formed on the bead surface can
accumulate stress induce by polymerisation of inner layer until symmetry
breaking occurs. The gels ruptures on one of the side of he bead, leading to
the formation on a comet on the opposite side.

.. todo::
    Figure with symetry breaking grap scheme from Berlin Presentation, 

The further polymerisation of the actin network on the surface of the bead will
make the comet grow, propelling the bead forward. This is what make the bead
system a biomimetic system replicating the listeria motion.

It should be noted that during the evolution of this system, two phases can be
distinguished. In the first phase, the system present a spherical symmetry with
an homogeneous actin  network around the bead. The gel is growing from the
surface and is accumulating stress due to the polymerisation of inner layers.

If the gel is able of accumulating sufficient stress, and the polymerisation to
produce enough,  the symmetry breaking event happens, and the system enters in
a second phase with the formation of a comet. 

The condition that lead to symmetry breaking are investigated in
:cite:`Kawska2012`. In the absence of capping, the actin polymerisation seem
not to be restricted enough on near the surface of the bead, and the formed
network is not able to generate or sustain enough stress to achieve symmetry
breaking. At high capping concentration, the growth of the gel is too impaired
to also permit symmetry breaking. The concentration of Arp2/3 is also critical
as Arp form branched network, and these branched network are primordial for the
ability to sustain stress.


.. _phase-diag:

.. figure:: /figs/symmetry-breaking-phase-diagram.png
    :alt: Symetry breaking phase diagram
    :width: 70% 

    Phase diagram showing symmetry breaking in bead motility assay as a
    function of concentration of Arp2/3 and Capping Protein. Symmetry breaking
    only occurs inside the area delimited by dashed line. Experiments are
    displayed as inverted fluorescence image. Adapted from :cite:`Kawska2012`

In the rest of this manuscript we use the bead motility system bu only consider
it during the first phase, where the symmetry breaking has not yet occurred, or
in condition where it should not occur. In particular we will investigate
condition at 25 Nm Arp2/3 and concentration of Capping Protein varying from 0
to 50 nM. This correspond in :num:`Fig #phase-diag` to both condition where no
symmetry breaking can occurs, but also to condition to which symmetry occurs
happens with the highest probability. This first phase where the gel is still
homogeneous around the bead has already been studied in :cite:`Pujol2012`, who
measure the stiffness of the thin actin gels that form near the surface of the
bead.We focus on fixed system where we will do further study on still
polymerising system.


.. todo:

     - bead assay
       - when it was designed
       - mimic listeria motility 

       - nucleation on the surface by Arp2/3 NPF, both mimicking the
         nucleation at the membrane outside of bacteria (listeria) and inside
         cell. 
     - controlled biochemical condition 
     - bottom up approach  

.. todo::
     - liposomes (UV): 
       - Giant unilamellar Vesicle


Liposomes
=========
.. 3

Bead are a model biomimetic system that replicate the polymerisation mechanism
that happened on the leading edge of the cell. Because of their composition and
rigidity phenomenon observed on bead cannot reproduce all the interaction and
process that take place on cell membrane. Cells are finite compartment with a
limited amount of actin that act on the dynamic of polymerisation.  The fact
that cell size is in the order of the persistence length of actin filament
also play a role on the structure of actin network . Indeed at these scale as a
single filament can never reach the length at which is can be considers a fully
flexible.

Liposomes are one of the biomimetic system that are capable of capturing these
interaction between cell membrane. Liposomes are lipid bilayers that imprison
an aqueous compartment and exhibit many extra characteristic similar to cells.
The inside of liposomes can act as a biochemical reactor of limited size with
the lipid bilayer actin as a separation with the outside, like the cell
membrane. The composition of the lipid layer can be varied in order to reflect
the composition of cell membrane. In particular it is possible to attach
protein to the liposomes membrane. Finally the size of the liposomes can be
varied, leading to actin network of size and shape similar to those found in
cells.


It is possible to mimic the cell actin cortex using liposomes, and especially
its contractility. A crosslinked actin network, can be formed and attached to
the outer leaflet of liposomes, and contractility can be trigged by injecting
molecular motors. The behavior of the system will depend on the attachment
between the reconstituted actin cortex and liposomes membrane.  Week attachment
lead to a favorable rupture of the actin cortex during the increase of tension,
implying a symmetry breaking as in bead system.  In the case of strong
attachment the liposomes actin cortex will accumulate tension until it has
enough force to crush the supporting lipid layer thus collapsing the liposomes
:cite:`Carvalho2013`. This system also allow the observation of the system
through time giving extra insight into the dynamic of actin network.



.. todo::
    figure peeling crushing. 

    
Membrane Physics 
****************
.. 2

Cells and their liposomes biomimetic counterpart are constituted of lipid bilayers with physical properties. Understanding the mechanics of these membranes is crucial to understand the behavior of the system.


Actin networks as viscoelastic material
***************************************
.. 2


To study the mechanical properties of an actin network it is important to
describe the condition in which we study it to select the adequate models.

We have seen previously that while polymerising, G-actin assemble into F-actin
filaments. The stiffness of filament can be measured by a characteristic number
called the persistence length (:math:`l_p`) which represent the length after
which the bending of filament becomes non-negligible. For actin filaments, the
persistence length is in the order of 10 µm :cite:`Isambert1996`. This means
that for scales much smaller, the actin filament can be considered as rigid,
like in cell cortex where meshwork have a typical size smaller than 250 nm. In
the other extreme, at length scale much bigger than :math:`l_p`, filaments can
be considered as flexible. Even if for typical cells, the length scale is
rarely much bigger than the persistence length of actin, `Xenopus` eggs can be
as big as 1 mm, so hundreds fold the persistence length. In mouse oocyte that
can go up to a 80µm diameter – and on which we will do some analysis – actin
filaments are hence about an order of magnitude bigger than the persistence
length. Still for the majority of cells, the typical size we are interested in
is about the persistence length of an actin filament, making it neither purely
rigid nor completely flexible.

For the above reasons, solution of actin are often compared to semi-flexible
polymers, and models that predict comportment of actin network often take
foundation on polymers physics :cite:`Morse1998` :cite:`Morse1998a` . Still, if
theses models rely on local microscopic parameter, experimental methods only
have access to bulk properties of the studies material, and it is from theses
properties, and through the models that we can deduce possible values for the
microscopic models. :cite:`Isambert` :cite:`MacKintosh`

.. todo::
    Fix Above citations

.. todo:: 
    Typically the persistence length is the length at which thermal fluctuation becomes  ...  `<\theta(0)\Theta(l)>` = exp(-l/lp)

Elastics Modulus
================
.. 3

The elastics modulus are probably the one that seem to be the easiest to
understand. They are characteristic of the material that will describe how a
material will deform non permanently  when applied a force. The stiffer
something is the higher its elastics modulus will be. There are two specific
elastic modulus we will be interested in in the rest of this manuscript,
`Young's Modulus` and `shear modulus`. The first one describe more specially
how material will react to it's compression or extension, while the second
describe how a material resists  shearing. In isotropic and homogeneous
material, the Young modulus (noted E) and the shear models (G) are linked
together through the Poisson ratio (:math:`\nu`) by the
following relation:

.. math::
    
    G = \frac{E}{2(1+\nu)}


Hence at fixed Poisson ratio, and as :math:`\nu` is usually around a value of
:math:`0.5`, it is common to use G and E interchangeably and to just referee to
it as "elastic modulus". Both G and E units are homogeneous to :math:`N/m^2`,
so :math:`Pa` It is interesting to have an idea of the oder of magnitude of a
few usual materials. Aluminum will have an elastic modulus :math:`G_{Al}\simeq
70~GPa` while rubber will be more in the order of :math:`G_{rubber}\simeq
0.1~GPa`. The elastic modulus of muscle cell is in the order of :math:`G_{muscle}
\sim 10~kPa` and brain tissues around :math:`G_{brain} \sim
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

The shear modulus is it defined by :

.. math::

   G &= \frac{\tau_{xy}}{\gamma{xy}} \\
      & = \frac{   F/S }{   \Delta x / l        }

.. todo::

    Scheme for shear modulus, should we merge it with one where we explain
    Morse Paper with actin filament going through the cross section

Poisson Ratio
=============
.. 3

We have just seen that the shear modulus is linked to the Young modulus using
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
.. 3

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
.. 3

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
.. 3

 - Classical example of non Newtonian fluid (?), depend on frequency.
 - decompose in pulsation, then miracle :math:`i\omega \simeq \frac{\partial}{\partial t}` 
 - maxwell voight model, spring + dash pot

Active and Passive microrheology 
*********************************
.. 2

Optical tweezer
***************
.. 2

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

Determination of force and displacement on bead
===============================================
.. 3

Using optical tweezer to not only hold a particle in position, but also get
quantitative measurement of its displacement and force exerted require
calibrated probe. The use of polystyrene beads is one of the artificial probe
that can be use to achieve such a goal.

The use of polystyrene bead has multiple advantages, the first being that one
can obtain mono-dispersed bead leading to reproducible and predictable trap
stiffness. Secondly the theory :cite:`Mie scattering` can predict the shape of
the potential felt by such a bead in a Gaussian beam.

.. figure:: /figs/bead_potential.png
    :width: 100%
    :alt: potential felt by a bead and force felt.

    Left : scheme representing the potential felt by a bead along one axis,
    near the minimum of the potential it can be approximated as an harmonic
    potential, which correspond to a constant stiffness. Right: Deflection of
    the light by an off centered bead in the trap. Also proportional to the
    displacement of the spot on the QPD. With correct calibration of the trap
    the displacement is also proportional the force exerted on the bead.
    
The second advantage being that beads can be functionalised, allowing specific
interaction to be controlled, both in vitro and in vivo. Of course, the
calibration is essential for the correct measurement of mechanical property of
different system, and the choice of the bead diameter have impact both on
biological side and in the physics of the measurement. In particular, the
linear regime for the  displacement-deflection can only be seen for beads that have a
diameter which is not too close from the beam waist diameter. In such case a
flattening on the curve prevent precise measurement.


.. figure:: /figs/todo.png
    :width: 80%
    :alt: flattening of the displacement/deflection curve

    Simulation of flattening of the curve near the center of the trap by
    deriving the sum of two gaussians. One cannot make a linear approximation
    near the center.


    
    



.. myosis

Myosis (to move away)
*********************
.. 2

.. todo::
    - Asymetric division of oocyte, 
    - from diploid, to haploid,
      - spindle usually in mitosis pulled by microtubule

