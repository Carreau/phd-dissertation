.. role_of_actin

The Role And Composition Of Cytoskeleton
****************************************
.. 2


We have already introduced the cell cytoskeleton in a previous part,
:ref:`into_cyto`, we will describe its component and function ality more in
detail here.  The cytoskeleton of the cell as though three main function, it
connects the cell both physically and biochemically to the external
environment, generate and coordinate the forces that give the cell its shape
and allow it to move, it is also responsible for organising spatially  the cell
content :cite:`Fletcher2010`. The cytoskeleton is also in particular sensitive
to Spatial and temporal information that can affect cell fate and the assembly
of cytoskeletal structure. This can be seen for example with the bud scar of
budding yeast that persist after division. 

.. todo::
    trouver des ref pour ci de sous    

Composition of cell cytoskeleton
================================
.. 3


The cytoskeleton is mainly composed of three type of filaments.  The
microtubules, intermediate filament and actin filament, also known as
microfilaments.

.. Microtubules

Microtubules are the wider with a diameter of 20nm and :num:`Fig #fig-mt` the
stiffer of the three kinds of filament with a persistence length in the order
of millimeter, which is much longer than the size of the usual cell.
Microtubules are extensively studied :cite:`cite some reviews ...`.
Microtubules are formed by the polymerisation of an heterodimer of tubuline
that lead to the formation of polar (oriented) filament that can be walked on
by molecular motors. These molecular motors can be decomposed in two families –
kinesins and dyneins – depending on the end toward which the motor preferably
walk.  Microtubules are mostly known for their action during the cells mitosis
where they will form majority of the mitotic spindle that drive the segregation
of the chromosomes in two groups, each group ending in one of the daughter
cells. 

Microtubules have the characteristic of being highly dynamic by alternating
between two state of rapid growth after what is called a `rescue` , and a rapid
shrinkage after a `catastrophe`

.. _fig-mt:

.. figure:: /figs/microtubules-structure.jpg
    :alt: "Structures of Microtubules, schematic and electro microscopy"
    :width: 70%

    Structure of an heterodimer of tubuline and assembly into a microtubule.
    Electron microscopy of a single microtubule filament. From `Molecular
    Biology of the Cell`


.. Intermediate filament


Intermediate filaments are of medium diameter in the order of around 10nm, in
between actin and microtubules filament, hence their name.  Unlike microtubules
and actin filament, intermediate filaments are composed by several sub-families
of proteins and are non-polar.

Intermediate filament have an important role in the mechanical properties of
the cell due to the fact that they are particularly  resistant to stretching. 

Unlike actin and microtubules, they are thought to be passive, with mechanical
properties mainly deriving from how multiple filaments are linked together
laterally.

.. Actin


Actin, is the third component of the cytoskeleton, the one we will focus most
of our effort. Actin monomers polymerises into actin filament, the thinest of
the three kind that form the cytoskeleton. Actin is produced in the cell as a
globular protein of ~40 kDa that once associated with ATP or ADP polymerises
into helicoidal filament with a diameter between 7 and 9nm. The formed actin
filament are polar, which both extremity respectively called the plus (`+`) or
barbed end, and the minus (`-`) or pointed end. The polarity of the actin
filament is of importance as this give rise to a proved direction for most
processes that can happen on the filament.


The actin protein is highly conserved across species, and is know to directly
interact with hundreds of proteins :cite:`DosRemedios2003`. As hint before it
can in particular bind to ATP, that can hydrolyse into, ADP

Single undecorated filament will behave at the scale of the cell as
semi-flexible polymer with a persistence length in the order of 10 µm. When the
assemble into different structure and network, or associate with other proteins
and molecule the resulting mechanical and dynamic properties can be highly changed.

.. _fig-actin:

.. figure:: /figs/actin-structure.jpg     
    :alt: "Structures of actin, schematic and electro microscopy"
    :width: 70% 

    Structure of a single monomer of actin, and electron microscopy snapshot.
    — from Molecular Biology of the cell.


Dynamic of actin polymerisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. 4 

The assembly mechanism that allow to go from single monomers of actin (also
refer to as G-actin) to actin filament (also refer as F-actin)
need to be well understood to explain the different networks structures actin
filaments can create in presence of other proteins.

The polymerisation of ATP/ADP actin monomer to form an actin filament
need to go through the step of forming an actin proto-filament which
is constituted of at least 3 actin monomers. This will most of the
time be the kinetically limiting step. Once proto-filaments are
present in solution, single monomers can be freely added or removed on
both ends of the filament.  The process of forming these
proto-filament is called the nucleation and is the rate limiting factor
to form actin filament from actin monomers. To circumvent this
limitation experimentally one can use actin filament seed, or actin
nucleator to direct the polymerisation on cell as cell does.

We need to distinguish between the dynamics of polymerisation and
depolymerisation on both ends of the filament. Indeed it has been show that the
association and dissociation rate are differing between the pointed (-) and
barbed (+) end. The barbed end has a  higher dynamic that its pointed
counterpart which is the reason that give it its (+) name. The dynamics of
polymerisation  is higher both in he case of ATP and ADP, though the rate
constant of association and dissociation differ for both kind of filaments.

.. _fig-actin:

.. figure:: /figs/elongation-rate-constant.png     
    :alt: "Elongation rate constant of actin filament as measured by Pollard 2003"
    :width: 25%

    Association and dissociation rate of both ATP and ADP actin on pointed and
    barbed end as measured in :cite:`pollard2003`. The difference of
    equilibrium constant between the barbed end (bottom) in the presence of ATP
    allow filament treadmilling.




The equations that drive the polymerisation can be written as follow

.. math::

    \frac{dC_{barbed}}{dt} &= k_{+,{barbed}}.[monomers] - k_{-,{barbed}} \\
    \frac{dC_{pointed}}{dt} &= k_{+,{pointed}}.[monomers] - k_{-,{pointed}} \\

Where `barbed` and `pointed` designate respectively the barbed and pointed end,
and :math:`k_+` and :math:`k_-` are the polymerisation and de-polymerisation
rate.  The concentration in barbed and pointed end denoted by
:math:`C_{{barbed}/{pointed}}`. By assuming that the number of pointed end is
equal to the number of barbed end, one can derive the steady state which give
rise to the critical monomer concentration below which an actin filament cannot
grow: :math:`[monomers]_c`.

The rate constant of elongation of actin have been determined to also depend of
whether the monomer was bound to ADP or ATP :cite:`Pollard1986`. We should now
consider the fact that ATP-bound actin will hydrolyse to ADP-Pi then release
the inorganic phosphate, and thus with a rate which also depend on whether the
monomer is part of a filament or in solution. With the hydrolysis of ATP-bound
actin into ADP bound actin in the filament, this lead to an imbalance of actin
(de)-polymerisation on both ends, which leads to actin filament preferably
growing on the barbed end and preferably shrinking from the pointed end.

This will lead to a phenomenon known ad treadmilling where a single actin
monomer bound to an ATP molecule, will be incorporated at the `+` end of the
filament and progressively move toward the minus end, eventually hydrolysing it
ATP into ADP before detaching from the filament on the pointed end. During this
process the filament will grow / shrink until it reaches the stationary state
where its length would stay constant but the treadmilling continues.

Treadmilling require an imbalance in the global rate constant on the barbed and
pointed end and an energy source, in the case of actin this is provided by the
hydrolysis of ATP into ADP+Pi before releasing the inorganic phosphate, without
whom treadmilling would not occurs.

Practically this can be approximated by having only ATP monomers at the barbed
end of actin filament wile pointed end is constituted only of ADP monomers,
thus the critical concentration is lower at the  pointed end. The barbed end
have a higher critical concentration. The growth speed of the filament depend
on both end depends on the monomer concentration in solution and in between the
critical concentration of both ends exist a concentration at which the
polymerisation on (+) exactly compensate the depolymerisation on (-).



Actin network can be controlled by a host of actin binding proteins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. 4

Despite the already complex process that is actin polymerisation and the
numbers of parameter that we have already introduced, the formation of an actin
network is an even more complex process that involve many other components.
Especially, actin monomers and filament can interact with a high number of
proteins that will affect the previously introduced dynamics.  We will present
some categories of such protein in the following.

Formins
"""""""
.. 5

`Formins` are polymerase proteins that will increase the polymerisation rate
of actin filament by dimerizing and binding to the barbed end. It has the
particularity of being processive, meaning that it will stay bound to the
barbed and while catalysing the addition of new monomers. The processivity of
formins also permit the control of the localization of actin polymerisation
where formin proteins are present, like the tip of filopodia :cite:`Faix2006`
:cite:`Bornschlogl2013`. `Formin` posses domains rich in proline capable of
binding to profilin (`FH1`) which allow formin to elongate F-Actin using actin
monomers bounds to profilin :cite:`Pruyne2002` :cite:`Pring2003a`.


Actin depolymerization and severing
"""""""""""""""""""""""""""""""""""
.. 5

Like polymerisation that can be enhanced by some proteins, depolymerization can
also be speed up by divers proteins. ADF/Cofilin is a protein
which is able to speedup the depolymerization of actin either by increasing the
off rate at the pointed end :cite:`Carlier1997`, or by actively severing the
filament in different point, thus disassembling the formed network :cite:`McCullough2011`.

It should be noted that depolymerization can not only be  enhanced at the
pointed end, indeed formin is also able to accelerate the detachment of actin
monomers at the barbed end.

Capping Protein
"""""""""""""""
.. 5


To regulate polymerisation, cells also have the possibility to reduce or stop
the polymerisation. To achieve this, some proteins will bind to the growing end
of actin filament and prevent the addition of new monomers.  `Capping Protein`
(CP) being one particular example that will specifically bind to the barbed end
of a growing filament and  prevent here from growing. Capping proteins are
necessary to prevent polymerisation of actin in undesired area
and are essential for the structure and mechanical properties of actin gel
:cite:`Kawska2012`. `Gelsoline` is another example of capping protein, that
unlike CP can only attached to the barbed end of an actin filament after
severing it. Gelsoline is hence both a severing and a capping protein.

.. todo:: 
    refs look for a review

Cross-linkers
"""""""""""""
.. 5


We have seen that some proteins were able to attach to actin filaments. When
such a protein is able to attach to many filament at once, it can act as an
attachment point between the two filament, preventing them to move with respect
one to each other. Such proteins, are referred to as cross-linkers.

.. todo::
    ref to review

The amount of freedom in movement between the two filaments is dependant of the
used cross-linker. For example , α-actinin will allow rotation of the two
filament at their anchoring point whereas cross-linker like fascine will prefer
a parallel conformation of the filament and favor the formation of actin
bundles.

Stabilizing actin filaments
"""""""""""""""""""""""""""
.. 5



As actin network a dynamics construct that are changing shape and properties
with time, it is convenient to be able to stabilize those network. Tropomyosins
are proteins capable to bind on the side of actin filament to stabilize them.

The use of phalloidin, a toxin extracted from fungus, is also common as by
binding between F-actin subunits on the filament, it prevent it from
de polymerising.  Though, it is known that stabilizing actin filaments with
phalloidin will increase they persistence length which can change the
mechanical properties of the formed actin network.

Molecular Motor
"""""""""""""""
.. 5


A particular kind of protein that can bind to cytoskeleton filament are
molecular motors. Molecular motors are proteins that will consume energy source
in the form of ATP, hydrolyse it to change conformation and produce forces.

The motors that move along actin filaments are part of myosin superfamily, they
are both responsible for the transport of cargo along filament, cell motility,
division, and muscle contraction. They acquire their name from their discovery
in 1864 by Willy Kühne who extracted the first myosin II extract from muscle
cell :cite:`Hartman2012`.

The myosin super family is divided into subfamilies number with roman literals.
As of today we count more than 30 family of myosin :cite:`Berridge2012a`.
Muscle myosin are part of the myosin II family and are often referred to  as
conventional myosin for historical reason as being the first discovered. Non
muscle  myosin are also referred to as unconventional myosin or Non-muscle
myosin.

Myosin motors seem to be shared among all the living kingdom, hinting for an
early emerging of myosin in the evolution. All the myosin motors move on actin
filament toward the barbed end, with the exception of myosin VI which moves
toward the pointed end :cite:`Buss2008`.

Different subfamily of myosin are used for different function in cells, even in
subfamily each type of myosin can have specific function. For example,
conventional myosin found in muscle cell are use for large scale cell
contraction. In contrast, myosin V is known to transport cargo and is found to
be responsible for actin network dynamics and vesicle positioning
:cite:`Holubcova2013`. 


Myosin II
---------
.. 6

As stated before, the myosin II family both encompass conventional myosin ans
well as Non-muscle myosin II (NMII). Both have a similar structure.

All myosin II are dimers constituted of two heavy chains and light chains. The
heavy chain are held together by a coil-coiled alpha helix referred to as the
tail. On the other side of the protein sequence is a globular head, which is
responsible for ATP hydrolysis and is able to convert the energy from the
hydrolysis into mechanical force, it is also the part that will bind to th
actin filament. In between the tail en head is the neck domain that act as a
lever to transmit the force generated by the head to the tail. The length of
the neck influence the length of the movement done by the cargo at each step of
the myosin as well as the size of the step the myosin can effect. The two light
chains are situated in the neck region and are responsible for the myosin
activity regulation.

Myosin II dimers can align and assemble by the tail region, forming myosin
minifilaments. These minifilaments are bipolar, having numbers of myosin head
with the same orientation at each extremities.

Into the myosin II family, conventional myosin and NMII differentiate by the
size of the minifilaments they form. Muscle myosin will form minifilaments
aggregating around 200 dimers, where NMII minifilaments will be composed  only
of 10 to 20 minifilaments. The other characteristic of unconventional myosin
with muscle myosin is the mode of activation. Conventional myosin activation
will be regulated by the amount of $Ca^{2+}$ available, whereas its counterpart
is activated by th phosphorilation of the Myosin Light Chain (MLC).

Another parameter that discriminate muscle form cell myosin is their duty
ratio.  The duty ratio is define as the ratio of the time the myosin stays
attached to its actin filament over the typical time of a contraction cycle.
By noting :math:`\tau_{on}` and :math:`\tau_{off}` the time the myosin head
spent attached/detached from  the filament , the duty-ratio or duty-cycle can
be noted :

.. math::
    r = \frac{\tau_{on}}{\tau_{on}+\tau_{off}}

We will see in the following that the duty-ratio might have an important effect
on the processivity of the myosin.

Ti should be noted that as minifilaments can attach on actin filaments on both
ends, they can also act as a bridge that hold two points close to each other,
though having the properties of crosslinkers.

Myosin V
--------
.. 6

Myosin V is an unconventional myosin, unlike myosin II it does not aggregate
into minifilaments.  Though, myosin V has a similar structure to myosin II but
with a longer neck, this confer to myosin two the ability to realize longer
step on actin filament. Indeed, myosin V step is of 36nm, a length close to the
repeat length of actin filament this concede to myosin V motors to walk along
actin filament without having to rotate around it. At the end the tail domain
myosin V posses another globular domain capable of binding to its cargo, and
the variability of this region is what mostly define the difference between the
different type of myosin V.

Myosin V also have a high duty-ratio, this lead to dimers having almost always
one of the two head of the myosin to be bound to actin. This grant the myosin
five with the ability to walk in a processive manner toward the barbed end of
the actin filaments, both head successively binding 36 nm in front of the other
head.


.. todo:

    This need to be an expanded section with equal weight to ARP. Explain more
    about its function and give a figure _________ get inspired by Alberts.

    Important : Introduce minifilaments, make the difference between  head and
    tail, _______ introduce the duty ratio, and the difference between Muscle
    and Cell Myosin II.



.. figure:: /figs/figure-16-54a.jpg     
    :alt: "Schematic of a myosin II motor"
    :width: 70%

    A schematic of a dimer of myosin motors with the example of Myosin II.
    Each of the myosin monomer is colored in a
    different shade of green. From Right to Left, the myosin head, with the N
    terminal, is the part of the myosin that binds to the actin filaments. The
    neck region with the light chain act as a lever arm. Finally the tail,
    constituted with coiled-coil alpha-helix that aggregate to form minifilaments.
    Adapted from Molecular Biology of the cell.



Myosin cycle
------------
.. 6

We saw earlier that the duty ratio of myosin was the ratio of time the head of
the myosin spent attached to the actin filament. Indeed, myosin can generate
displacement through a cycle of ATP hydrolysis and attachment/detachment
described below for a Myosin II motor:

The cycle can be decomposed in 5 steps, last of which will be responsible for
the forced exerted on the myosin cargo.

    - The myosin start in the 'rigor' conformation where it is lightly bound to
      the actin filament.

    - An ATP molecule binds to the myosin head inducing the detachment of the
      myosin from the actin filament.

    - ATP molecule is hydrolysed into ADP+Pi, providing energy which is stored
      into a conformational change of the myosin which effect a recovery
      stroke. 

    - Inorganic phosphate is released as the myosin head attaches to the actin
      filament.

    - The actin-bound myosin change conformation, applying forces on it's
      cargo. This step is known as the power-stroke and is responsible for most
      of the applied force or displacement of the myosin. During the
      power-stroke the ADP bound to the myosin head is released, leading back
      to first step of the cycle.


The principle stay the same for all kinds of myosin. In the case of Myosin two
the duty-ratio is only of about 5%, which leave Myosin II detached from the
actin filament most of the time. A single dimer cannot then achieve
processivity.   Though the aggregation of myosin II dimers into minifilaments
of tens of dimers increase the effective attachment time of the minifilaments
to actin networks, and confer it processivity.

The bipolar nature of myosin II minifilaments also allow them to act as force
dipoles, each  of th extremity pulling the surrounding actin network or
filament toward the center of the minifilaments. This is the mechanism at the
origin of muscle contraction and can allow to build-up tension in actin network. 


.. Latrunculin
.. """""""""""
.. 
.. Another toxin that act on actin is latrunculin, secreted by sponges,it bind to
.. actin monomer preventing them to polymerise.  In presence of latrunculin, actin
.. filament can though only depolymerize.


Profilin
""""""""

Profilin is a protein that will bind to the barbed end of single monomers of
actin in solution.  By doing so it will first prevent the association of
monomers into dimers and trimmers, thus preventing the nucleation of actin
filament. It thus allows a better control of localisation of actin filament
both in vivo and in vitro in the presence of actin seeds of actin nucleator.

Profilin as for a long time been believed to be only a sequestering protein
that inhibit polymerisation :cite:`Yarmola2009`, though it has a more complex
behavior, and if it prevent polymerisation of actin filaments by the pointed
end, it can facilitate polymerisation. One of the cause of increase in
polymerisation speed by profilin is the fact it binds preferably to ADP-Actin
and increase the exchange rate of ADP into ATP. :cite:`probably something, look in Yarmola`.


Branching Agent
"""""""""""""""

We have seen previously that crosslinker were proteins capable on linking two
or more actin filament together by binding on their side. Another mechanism
involving binding on the side on actin filament is responsible for a closely
related network, the branching mechanism. 

The Arp2/3 complex is composed of seven subunits, two of which are highly
similar to actin, from Arp2 and Arp3 family for Actin Related Proteins,
giving the complex its name. Arp2/3 will bind on the side of a pre-existing
actin filament, hence initiating the growth a daughter filament with an angle of
70° to the mother filament. The newly created daughter filament pointed end
is terminated by the Arp2/3 complex that will stay attached to the mother
filament, thus increasing the number of available barbed end, without changing
the number of available pointed end. Cf Nature Review by Erin D. Goley and
Matthew D. Welch :cite:`Goley2006` for  a longer review about the Arp2/3
complex.

In cells, the Arp2/3 complex need to be activated by a Nucleation Promoting
Factor (NFP).  Among then are the  WASp protein (Wiskott-Aldrich Syndrome
protein) and its neural homologue N-WASP which are from the same family as
SCAR/WAVE :cite:`Machesky1999`.  All these activator of Arp2/3 have in common a WCA motif. The Wild
type protein need to be activated in order to activate Arp. The activation is
done by a change in conformation that expose the active region and provide the
first actin monomer necessary for the nucleation of the daughter filament.  To
circumvent the activation process activation process of these protein, we use a
reconstructed version of the protein that cut all region before the
poly-proline. The confer to pVCA the ability to be permanently active. This
region can also be replaced by streptavidine in order to selectively bind pVCA
to selected regions. Characterisation and more detailed description of pVCA can
be found in :cite:`Noguerra2012`.

Unlike Cells that are able to control the localisation of actin nucleation
process thanks to activation of WASP and its homologue, the in vitro control
of localisation of actin polymerisation is directly done by the localisation of
pVCA.

The network formed by Arp2/3 is called a dendritic network, and is in particular
found at the leading edge of the cell, and it is such a network is present in
the bead system we will study hereafter.

When first binding to the actin filament the Arp2/3 complex is initially inactive, it
needs the help of another protein to start the nucleation actin nucleation process.

.. todo:

    Very important : Talk about the activation of the Arp2/3 complex. Introduce
    the activator and pVCA. Why do we use this peptide.



.. _actin-cycle:

.. figure:: /figs/pollard2003-actin-cycle.jpg     
    :alt: "Actin recycling at the leading edge of a cell"
    :width: 70%

    Adapted from :cite:`Pollard2000`, scheme recapitulating the formation of a
    dendritic network at the leading edge of a cell were several of the
    function of above described protein can be seen. An actin nucleation
    promoting factor will activate Arp2/3 which will act both as nucleation
    factor and a branching agent. From an activated Arp2/3 will grow an actin
    filament pointing toward the membrane. Newly growing barbed ends can
    eventually be capped by capping proteins which will terminate their growth.
    Aging monomers in actin filament will slowly hydrolyse their ATP, eventually
    releasing the inorganic phosphate before detaching from the pointed end.
    Depolymerisation is helped by severing protein and Actin Depolymerisation
    Factor (ADF). ADP-actin monomer will bind to profilin will will increase the turn
    over rate to ATP-actin which will be reuse by the leading edge of the cell.

.. todo:: 
    Generally : The Protein you use need to be better introduced than others

The actin cortex
================
.. 3

The actin cortex is a thin layer — of between 200 to 500 nm —that can be found
just underneath the plasma membrane of a cell. The properties of the actin
cortex makes it a key component to diverse processes.  Its capacity to resit
to, and transmit forces is indispensable for locomotion of many cell by
allowing the retraction of the rear of the migrating cell and will be describe
in more detail in the next section. Its structure is also essential for the
cellular division as contractility is necessary to generate cortical tension
and achieve the separation of the two daughter cells.


The actin cortex is constituted of actin filaments that can be parallel or
orthogonal to the membrane as one can see using electron microscopy on cells
:cite:`Morone2006b`. 

.. figure:: /figs/Actin-Cortex-Moronne-2006.jpg
    :alt: "Electron microscope view of the actin cortex"
    :width: 70%

    Electro microscope view of the actin cortex in rat cell. The inset clearly
    show a periodicity of ~5nm in filaments characteristic of actin.  Scale
    bars are 100nm, inset 50 nm. Extracted from :cite:`Morone2006b`.

We saw through the but scar of budding yeast that the full cytoskeleton could
retain memory of past event. It is also the cse for simple actin network as
show in :cite:`Parekh2005` who described how actin-network growth can be
determined by network history, showing actin cortex could also act as a memory for cell.


Cell Motility
=============
.. 3

The way cells moves highly depend on their environment and the type of cells.
We can distinguish several Strategy of movement, mainly categorised into
amoeboid and mesenchymal movement. The type of motility involve for certain
cell can be characteristic of malignant tissue, and play a significant role in
the ability of the cells to invade nearby tissues. 


.. todo::
    Figure filopodia pushing



Lamelipodium based Motility
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. 4

We can ave a first look into the amoeboid mode of locomotion of cell, which is
also often referred to as crawling. To understand how a cell is able to crawl
to move itself we will in particular take the example of the lamelipodium.
Lamelipodia is a characteristic structure of cells moving on a 2D substrate. By
its nature, motion using lamelipodia in one of the easiest to study using
microscopy which might explain why it is one of the best know process on cell
displacement. Non the less, it does not diminish its importance in tissues
behavior as all epithelial cell can be considered as moving on a 2D substrate.
Beyond lamelipodia, structure that are responsible for cell motion are
filopodia and pseudopodia. They mainly differs from lamelipodia by their shape
and the organisation of the actin structure inside.
Lamelipodia-based motion can move a cell up to a few micrometers per minute.

The action necessary to move in an amoeboid way can be decomposed in three
steps. First the cell need to grow a protrusion. Growing this protrusion is
often governed by actin polymerisation just underneath the plasma membrane. The
lamelipodia is such a protrusion which is constituted by a 2D actin network
that polymerize at the leading edge of the cell. Second the cell's protrusion
need to attach to the surface. This is done through trans membrane proteins
that are bound to the actin cortex on the inside of the cell. The actin cortex
will act as a scaffold to transmit the force across the cellular to these
anchor point. Last part is traction in which the rest of the cell is pulled
toward the attached protrusion. The traction force is mediated through the
cytoskeleton and actin cortex while the contraction force themselves can origin
from actin network contraction and reorganisation due to myosin motors.

As we can see the cell cytoskeleton and the actin cortex in particular play a
fundamental role in the motion process of mesenchymal cells. While we can see
that wit the lamelipodia, the same conclusion can be drawn from pseudopodia and
filopodia. Indeed filopodia basically differ from lamelipodia by the fact that
they are unidimensional at the scale of the cell and are host of an actin
structure made of parallel  filaments and bundles. Pseudopod are the equivalent
of filopodia, except they are characteristic in motion in a 3D environment and
are constituted by an actin gel more than parallel filaments.  

Blebbing base Motility
^^^^^^^^^^^^^^^^^^^^^^
.. 4

The second mode of motility which is known as mesenchymal is more
characteristic of 3D displacement of cells. In this mode, the cells will also
form protrusions but will not rely on the traction to move its body. This
motility rely on blebs, that are blister-like protrusion that happened on the
cell surface. A bleb form on the surface of cell when the membrane detach from
the actin cytoskeleton underneath it, or if the cortex ruptures. The small
protrusion formed with quickly grows as it lacks the force supporting layer
that the actin cortex provide and fill with the cytosol. The actin cortex can
rapidly reform on the bleb slowing down its growth. In some cases, the
reformation of the actin cortex in the bleb and the rebuilding of the tension
inside the bleb is enough to reverse the bleb. Though, the content of the cell
can also drain itself into the bleb as it grows and while the main body of the
cell contract and empties, thus moving the cell from its old position to a new
one in the direction of the initial growth of the bleb.

The initial state of blebs as spherical protrusion almost only made of membrane
and filled with cytosol make them a perfect simple system to reconstitute and
model in vivo.

.. figure:: /figs/Bleb-nature-paluch.jpg
    :alt: "Motion through bleb mechanism"
    :width: 70% 

    Extracted from :cite:`Charras2008`


Organelle Positioning (actin cloud) 
====================================
.. 3

.. todo::

    Maybe  change the structure a bit, Say beside the  –––––, –––––– –––––– –––
    seen (sparse network) , additionally these seem to be –––––– in positioning.
    Then give examples


.. todo:: 
    remove this paragraph

We have previously seen that actin plays a major role in cell motility and
division. By opposition to the actin cortex which is thin and dense network
just under the membrane, we will interest here in different kind of structure
formed by actin that have an as important role in the cells life cycle.

In the same way that cells need to displace, or that components need to be
transported between parts of the cell, the positioning of organelles in cells
is crucial for development. The cell nucleus, essential to the cell replication
as it contains most of the genetic material needs to be protected. It has been
shown :cite:`Iwabuchi2010` that in plant cells, the nucleus is moved away from
high energy light that could damage its DNA with a mechanism that involve
actin. Wether the nucleus is actually sliding along actin bundles or anchored
to the filament while they are pull as not been addressed in for theses cells,
is has been shown that in fibroblast, nuclear positioning is directly coupled
to actin cable using TAN lines :cite:`Luxton2011`. Both of theses mechanism use
actin as a scaffold to transmit the forces generated by other process to the
targeted organelle. These other process are due to molecular motors in the
cases of plant cell, and retrograde flow in the second one. It is a natural
question to ask of whether or not, actin can have such effect by itself ?

A beginning of answer to this question can be hinted by looking at drosophila
nurses cell. Indeed, during the phase where nurses cell expel their content
into the oocyte, the nucleus have to be positioned not to obstruct the process.
It was observed:cite:`Huelsmann2013` that the force exerted by polymerizing
filament seem to be enough to displace the nucleus. More especially, while the
polymerisation occurs at anchored points in the membrane, the actin filaments
grows, moving the pointed end toward the nucleus, eventually pushing it away.

.. todo::
    
    - speak about necessity of a soft actin cortex for spindle positioning in
      oocyte ( Chaigne Sykes, Campillo) :cite:`Chaigne2013a`
    - :cite:`Azoury2011`  Symmetry Breaking in mouse Oocyte require transient F-Actin meshwork 
    - :cite:`Lenart2005` A contractile nuclear actin network drives chromosome congression in oocytes.


Nuclear positioning during meiosis
==================================


