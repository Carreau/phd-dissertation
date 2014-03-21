
.. Part
Background
##########


.. todo::
    Misc To say
    ***********

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
migration to cell differentiation and division. It plays also a non negligible
in most mechanical properties of the cell and how it interacts with its
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
    Scheme for sheer modulus, shoudl we merge it with one where we explain Morse Paper with actin filament going throughthe cross section

Poisson Ratio
=============

Active and Passive microrheology 
********************************

Optical tweezer
***************

Membrane Physics 
*****************


.. myosis

Myosis (to move away)
*********************

.. todo::
    - Asymetric division of oocyte, 
    - from diploid, to haploid,
      - spindle usually in mitosis pulled by microtubule

