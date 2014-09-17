.. _role_of_actin:

The Role And Composition Of The Cytoskeleton
********************************************
.. 2

We have already introduced the cell cytoskeleton in the previous part, and we will now
describe its components and functionality more in detail here.  The cytoskeleton
has three main functions, it connects the cell both physically
and biochemically to the external environment, generate and coordinate the
forces that give the cell its shape and allows it to move. It is also
responsible for organising spatially  the cell content :cite:`Fletcher2010`.
The cytoskeleton is also in particular sensitive to spatial and temporal
information that can affect cell fate and the assembly of the cytoskeletal
structure. This can be seen for example with the bud scar of budding yeast that
persists after division. 

Composition of the cell cytoskeleton
====================================
.. 3


The cytoskeleton is mainly composed of three types of filaments.  
Microtubules, intermediate filament and actin filament, also known as
microfilaments.

.. Microtubules

Microtubules are the widest structure with a diameter of 20nm (:num:`Fig #fig-mt`) 
and the
stiffest of the three kinds of filaments with a :ref:`persistence length <viscoelastic>` in the order
of millimeters, much longer than the size of the usual cell.
Microtubules are extensively studied :cite:`Valiron2001`.
Microtubules are formed by the polymerisation of a heterodimer of tubuline
that leads to the formation of polar (oriented) filaments that can be walked on
by molecular motors. These molecular motors can be decomposed in two families –
kinesins and dyneins – depending on the end towards which the motor preferably
walk.  Microtubules are mostly known for their action during mitosis
where they will form the majority of the mitotic spindle that drive the segregation
of the chromosomes in two groups, each group ending in one of the daughter
cells. 

Microtubules have the characteristic of being highly dynamic by alternating
between two states of rapid growth and a rapid shrinkage. The transition from
microtubule growth to shrinkage is called a `catastrophe`, the transition from
shrinkage to growth is called a `rescue`.

.. _fig-mt:

.. figure:: /figs/microtubules-structure.jpg
    :alt: "Structures of Microtubules, schematic and electro microscopy"
    :width: 70%

    Structure of an heterodimer of tubuline and assembly into a microtubule.
    Electron microscopy of a single microtubule filament. From :cite:`Alberts2008`.
    A) Structure of heterodimer of tubuline B)
    Heterodimers can assemble forming polar filaments. C) Filaments can
    assemble into  microtubules. D,E) Electron microscopy image of
    microtubules.


.. Intermediate filament

Intermediate filaments are of medium diameter in the order of around 10nm, in
between actin and microtubules filaments, hence their name.  Unlike microtubules
and actin filaments, intermediate filaments are composed by several sub-families
of proteins and are non-polar.

Intermediate filament have an important role in the mechanical properties of
cells due to the fact that they are particularly  resistant to stretching. 

Unlike actin and microtubules, they are thought to be passive, with mechanical
properties mainly deriving from how multiple filaments are linked together
laterally.

.. Actin


Actin, is the third component of the cytoskeleton, the one on which  we will
focus on most of our efforts. Actin monomers, also called `G-Actin` for globular actin can polymerise. 
By polymerizing actin monomers (G-actin) into actin filaments (`F-actin`), the
thinest of the three cytoskeletal components forms. Actin is produced in the
cell as a globular protein of ~40 kDa (:num:`Fig #fig-actin`) that once associated with ATP or ADP
polymerises into helicoidal filament with a diameter between 7 and 9nm. The
formed actin filaments are polar, where both extremities are respectively called the
plus (`+`) or barbed end, and the minus (`-`) or pointed end. The polarity of
the actin filament is of importance as this gives rise to a preferred direction
for most processes that can happen on the filaments.


The actin protein is highly conserved across species, and is know to directly
interact with hundreds of proteins :cite:`DosRemedios2003`. 

Single undecorated filaments will behave  as
semi-flexible polymers at the scale of the cell with a persistence length in the order of 10 µm :cite:`Isambert1995`. When they
assemble into different structures and networks, or associate with other proteins
and molecules the resulting mechanical and dynamic properties can be highly variable.

.. _fig-actin:

.. figure:: /figs/actin-structure.jpg     
    :alt: "Structures of actin, schematic and electro microscopy"
    :width: 70% 

    A) Structure of a single monomer of actin, and electron microscopy snapshot.
    — from :cite:`Alberts2008`.


Dynamics of actin polymerisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. 4 

The assembly mechanisms that allow to go from single monomers of actin (also
refer to as G-actin for globular actin) to actin filament (also refer as
F-actin) need to be well understood to explain the different network
structures created by actin filaments in the presence of other proteins.

The polymerisation of ATP/ADP actin monomers to form an actin filament need to
go through the step of forming an actin proto-filament which is constituted of
at least 3 actin monomers. This will most of the time be the kinetically
limiting step. Once proto-filaments are present in solution, single monomers
can be freely added or removed on both ends of the filament.  The process of
forming these proto-filaments is called nucleation and it is the rate limiting
factor to form actin filaments. To circumvent this
limitation experimentally one can use preformed actin filament seeds, or actin nucleators
to direct the polymerisation on the cell.

We need to distinguish between the dynamics of polymerisation and
depolymerisation on both ends of the filament. Indeed, it has been show that the
association and dissociation rates are differ between the pointed (-) and
barbed (+) end. The barbed end has  higher dynamics than its pointed
counterpart which is the reason for its (+) name. The dynamics of
polymerisation is higher both in he case of ATP and ADP, though the rate
constant of association and dissociation differ for both kind of filaments (:num:`Figure #fig-actin-pollard`)

.. _fig-actin-pollard:

.. figure:: /figs/elongation-rate-constant.png     
    :alt: "Elongation rate constant of actin filament as measured by Pollard 2003"
    :width: 25%

    Association and dissociation rate of both ATP and ADP actin on pointed and
    barbed end as measured in :cite:`Pollard1986` (scheme from :cite:`Pollard2003`).
    The difference of equilibrium constant between the barbed end (bottom) 
    and pointed end (top) in the presence of ATP allow filament treadmilling.




The equations that drive the polymerisation can be written as follow

.. math::
    :label: roa1

   \left. \frac{dn}{dt} \right|_{barbed}&= k_{+,{barbed}}.nGActin - k_{-,{barbed}} \\
   \left. \frac{dn}{dt}\right|_{pointed}&= k_{+,{pointed}}.nGActin - k_{-,{pointed}} \\

Where `barbed` and `pointed` designate respectively the barbed and pointed end,
$\frac{dn}{dt} \right|_{barbed|pointed}$ represent the variation of the number of actin 
monomers in the actin filament which is due to addition or removal at the barbed
(respectively the pointed) end.
The association rate constant :math:`k_+` and dissociation ate constant :math:`k_-` are the polymerisation and de-polymerisation
rate.  The concentration in barbed and pointed-end denoted by
:math:`C_{{barbed}/{pointed}}`. By assuming that the number of pointed ends is
equal to the number of barbed ends, one can derive the steady state which give
rise to the critical monomer concentration below which an actin filament cannot
grow: :math:`[GActin]_c`.

The rate constants of elongation of actin have been determined and depend on
whether the monomer is bound to ADP or ATP :cite:`Pollard1986`. We should
consider the fact that the  ATP bound to actin will hydrolyse to ADP-Pi before releasing
the inorganic phosphate. The hydrolysis and phosphate release rates also depend on whether the
monomer is part of a filament or in solution. The hydrolysis of ATP-bound
actin into ADP bound actin in the filament  leads to an imbalance of actin
(de)-polymerisation on both ends. The actin filaments preferably
grow from the barbed end and shrink preferably from the pointed end.

This will lead to a phenomenon known as treadmilling where a single actin
monomer bound to an ATP molecule, will be incorporated at the `+` end of the
filament and progressively migrate toward the `-` end, eventually hydrolysing its
ATP into ADP before detaching from the filament on the pointed end. During this
process the filament will grow / shrink until it reaches the stationary state
where its length would stay constant but the treadmilling continues.

Treadmilling requires an imbalance in the global rate constant on the barbed and
pointed end and an energy source, in the case of actin this is provided by the
hydrolysis of ATP into ADP+Pi before releasing the inorganic phosphate, without
which treadmilling would not occur.

Practically, this can be approximated by having only ATP monomers at the barbed
end of actin filaments while the pointed end is typically constituted only of
ADP monomers, thus the critical concentration is lower at the  pointed end
compared to the barbed end. The growth speed of the filament on both
ends depends on the monomer concentration in solution. In between the
critical concentration of both ends, there exists a concentration at which the
polymerisation on (+) exactly compensates the depolymerisation on (-).



Actin network can be controlled by a host of actin binding proteins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. 4

Despite the already complex process of actin polymerisation and the
number of parameters that we have already introduced, the formation of an actin
network is an even more complex process that involves many other components.
Especially, actin monomers and filaments can interact with a high number of
proteins that will affect the previously introduced dynamics.  We will present
some categories of such proteins in the following.

Formins
"""""""
.. 5

`Formins` are polymerase proteins that will increase the polymerisation rate
of actin filaments by dimerizing and binding to the barbed end. It has the
particularity of being processive, meaning that it will stay bound to the
barbed end while catalysing the addition of new monomers. The processivity of
formins also permits the control of the localization of actin polymerisation
where formin proteins are present, like the tip of filopodia :cite:`Faix2006`
:cite:`Bornschlogl2013`. `Formins` posses domains rich in proline, capable of
binding to profilin (`FH1`) which allows formin to elongate F-Actin using actin
monomers bounds to profilin :cite:`Pruyne2002` :cite:`Pring2003a`.



Capping Protein
"""""""""""""""
.. 5


To regulate polymerisation, cells also have the possibility to reduce or stop
the polymerisation. To achieve this, some proteins will bind to the growing end
of actin filaments and prevent the addition of new monomers.  `Capping Protein`
(CP) being one particular example that will specifically bind to the barbed end
of a growing filament and  prevent it from growing. Capping proteins are
necessary to prevent polymerisation of actin in undesired area
and are essential for the structure and mechanical properties of actin gel
:cite:`Kawska2012`. `Gelsoline` is another example of Capping Protein, that
unlike CP can only attached to the barbed end of an actin filament after
severing it. Gelsoline is hence both a severing and a Capping Protein.

.. todo:
    refs look for a review

Cross-linkers
"""""""""""""
.. 5


We have seen that some proteins were able to attach to actin filaments. When
such a protein is able to attach to many filament at once, it can act as an
attachment point between the two filament, preventing them to move with respect
one to each other. Such proteins, are referred to as cross-linkers.

.. todo:
    ref to review

The amount of freedom in movement between the two filaments depends on the
cross-linker used. For example , α-actinin will allow rotation of the two
filament at their anchoring point whereas cross-linkers like fascine will prefer
a parallel conformation of the filament and favor the formation of actin
bundles.

Cross-linkers are essential for the formation of elastic network as they allow
forces to be carried from one actin filament to the other. The quantity of
cross link of a network will often be a key parameter for the elastic properties.
The distance between the link points in the network (both cross links
and entanglement points) will give the typical network mesh-size which is used
to calculate the viscoelastic response of networks : :cite:`Morse1998a`.

Stabilizing actin filaments
"""""""""""""""""""""""""""
.. 5



As actin networks are dynamic constructs that are changing shape and properties
over time, it is convenient to be able to stabilize those networks. Tropomyosins
are proteins capable to bind on the side of actin filament to stabilize them.

The use of phalloidin, a toxin extracted from fungus (Amanita phalloides), binds 
between F-actin subunits on the filament, and hence  prevents it from
de-polymerising.  Though, it is known that stabilizing actin filaments with
phalloidin will increase their stiffness as measure by the persistence length which can change the
mechanical properties of the formed actin network.


.. Latrunculin
.. """""""""""
.. 
.. Another toxin that act on actin is latrunculin, secreted by sponges,it bind to
.. actin monomer preventing them to polymerise.  In presence of latrunculin, actin
.. filament can though only depolymerize.


Profilin
""""""""
.. 5

Profilin is a protein that will bind to the barbed end of single monomers of
actin in solution.  By doing so it will first prevent the association of
monomers into dimers and trimmers, thus preventing the nucleation of actin
filament. It thus allows a better control of localisation of actin filament
both in vivo and in vitro in the presence of actin seeds of actin nucleator.

Profilin was for a long time believed to be only a sequestering protein
that inhibit polymerisation :cite:`Yarmola2009`, though it has a more complex
behavior, and if it prevent polymerisation of actin filaments by the pointed
end, it can facilitate polymerisation. One of the cause of increase in
polymerisation speed by profilin is the fact it binds preferably to ADP-Actin
and increase the exchange rate of ADP into ATP. 

Branching Agent
"""""""""""""""
.. 5

A type of network found of the leading edge of cells lamellipodia is dendritic
network. It is characterised by tree-like structure of actin filaments in which
thanks to the Arp2/3 complex branching agent a mother actin filament will form a
daughter filament on its side.

We have seen previously that crosslinkers are proteins capable of linking two
or more actin filaments together by binding on their side. Another mechanism
involving binding on the side on actin filament is responsible for a closely
related network, the branching mechanism. 

The Arp2/3 complex is composed of seven subunits, two of which are highly
similar to actin, forming the Arp2 and Arp3 family for Actin Related Proteins,
giving the complex its name. Typically Arp2/3 will bind on the side of a pre-existing
actin filament, hence initiating the growth of a daughter filament with an angle of
70° to the mother filament. The newly created daughter filament pointed end
is terminated by the Arp2/3 complex that will stay attached to the mother
filament, thus increasing the number of available barbed end, without changing
the number of available pointed end. See Nature Review by Erin D. Goley and
Matthew D. Welch :cite:`Goley2006` for  a longer review about the Arp2/3
complex.

In cells, the Arp2/3 complex needs to be activated by a Nucleation Promoting
Factor (NFP).  Among them is the  WASp protein (Wiskott-Aldrich Syndrome
protein) and its neural homologue N-WASP which are from the same family as
SCAR/WAVE :cite:`Machesky1999`.  All these activators of Arp2/3 have in common a
WCA motif. The wild type protein need to be activated in order to activate Arp2/3.
The activation is done by a change in conformation that exposes the active
region and provides the first actin monomer necessary for nucleation of the
daughter filament (:num:`Figure #fig-pwa-deploy`).  To circumvent the activation process of
these proteins, we use a reconstructed version of the protein that cut all
region before the poly-proline. This confer to pVCA the ability to be
permanently active. This region can also be replaced by streptavidin in order
to selectively bind pVCA to selected regions. Characterisation and more
detailed description of pVCA can be found in :cite:`Noguera2012`.


.. _fig-pwa-deploy:
.. figure:: figs/pwa-deploy.png
    :width: 60%
    
    Organisation of Wasp domains. A change in conformation make the protein
    active, which allow the activation of the Arp2/3 complex and the nucleation
    of a daughter filament.  Adapted from :cite:`Goley2006`


Unlike Cells that are able to control the localisation of actin nucleation
processes thanks to activation of WASp and its homologue, the 'in vitro' control
of localisation of actin polymerisation is directly done by the localisation of
pVCA.

The network formed by Arp2/3 is called a dendritic network, and is in
particular found at the leading edge of the cell in the lamellipodia. It is
such a network that is present in the bead system we will study hereafter.

As for crosslinkers, dendritic networks are able to carry forces across single
actin filaments by the intermediary of Arp2/3. Two dendritic network of Arp2/3
can also entangle and allow forces to be carried across them
:cite:`Kawska2012`. 


.. _actin-cycle:

.. figure:: /figs/pollard2003-actin-cycle.jpg     
    :alt: "Actin recycling at the leading edge of a cell"
    :width: 70%

    Schematic recapitulating the formation of
    a dendritic network at the leading edge of a cell were several of the
    function of protein can be seen. An actin nucleation promoting factor
    (Active WASp,  blue rectangle at the membrane) will activate Arp2/3 (green
    blob) which will act both as nucleation factor and a branching agent. From
    an activated Arp2/3 will grow an actin filament pointing towards the
    membrane. Newly growing barbed ends, rich in ATP-actin (white circle) can
    eventually be capped by Capping Protein (light-blue pairs of circle) which
    will terminate their growth.  Aging monomers in actin filament will slowly
    hydrolyse their ATP (yellow and red circle), eventually releasing the
    inorganic phosphate before detaching from the pointed end.
    Depolymerisation is helped by severing protein (sharp triangle) and Actin
    Depolymerisation Factor (ADF). ADP-actin monomer will bind to profilin
    (Black dots) increasing the turn over rate to ATP-actin which will be reused
    by the leading edge of the cell. Adapted from :cite:`Pollard2000`.


A schematic that recapitulate the interaction of actin with other protein and
the formation of a dendritic network at the leading edge of the cell is
presented on :num:`figure #actin-cycle`.


Molecular Motor
"""""""""""""""
.. 5


A particular kind of protein that can bind to the cytoskeletal filaments are
molecular motors. Molecular motors are proteins that will consume energy 
in the form of ATP, hydrolyse it to change conformation and produce forces.

The motors that move along actin filaments are part of the myosin superfamily, they
are both responsible for the transport of cargo along filaments, cell motility,
division, and muscle contraction. They acquire their name from their discovery
in 1864 by Willy Kühne who extracted the first myosin II extract from muscle
cell :cite:`Hartman2012`.

The myosin super family is divided into subfamilies numbered with roman literals.
As of today we count more than 30 families of myosin :cite:`Berridge2012a`.
Muscle myosin is part of the myosin II family and is often referred to  as
conventional myosin for historical reason as being the first discovered.
Non-muscle  myosin are also referred to as unconventional myosin.

Myosin motors seem to be shared among the living domain, hinting for an
early emerging of myosin in the evolution. All the myosin motors move on actin
filaments toward the barbed end, with the exception of myosin VI which moves
towards the pointed end :cite:`Buss2008`.

Different subfamily of myosin are used for different function in cells. Even in
subfamilies each type of myosin can have specific functions. For example,
conventional myosin found in muscle cells are use for large scale cell
contraction. In contrast, myosin V is known to transport cargo and is found to
be responsible for actin network dynamics and vesicle positioning
:cite:`Holubcova2013`. 

.. _myoII:

Myosin II
---------
.. 6

As stated before, the myosin II family both encompass conventional myosin as
well as Non-muscle myosin II (NMII). Both have a similar structure (:num:`Fig #fig-myosin`).

All myosin IIs are dimers constituted of two heavy chains and light chains. The
heavy chains are held together by a coil-coiled alpha helix referred to as the
tail. On the other side of the protein sequence is a globular head, which is
responsible for ATP hydrolysis and is able to convert the energy from the
hydrolysis into mechanical force. It is also the part that will bind to the
actin filaments. In between the tail and head is the neck domain that acts as a
lever to transmit the force generated by the head to the tail. The length of
the neck influences the length of the movement done by the cargo at each step of
the myosin as well as the size of the step the myosin can effect. The two light
chains are situated in the neck region and are responsible for the myosin
activity regulation.

Myosin II dimers can align and assemble by the tail region, forming myosin
minifilaments. These minifilaments are bipolar, having numbers of myosin head
with the same orientation at each extremity.

In the myosin II family, conventional myosin and NMII differentiate by the
size of the minifilaments they form. Muscle myosin will form minifilaments
aggregating around 200 dimers, where NMII minifilaments will be composed  only
of 10 to 20 minifilaments. The other characteristic of unconventional myosin
with muscle myosin is the mode of activation. Conventional myosin activity is
regulated by the amount of :math:`Ca^{2+}` available, which frees the actin filaments to let the myosin motor bind. However, its
counterparts are typically activated by the phosphorilation of the Myosin Light Chain (MLC).

Another parameter that discriminates muscle from non-cell myosin is their duty
ratio.  The duty ratio is define as the ratio of the time the myosin stays
attached to an actin filament over the typical time of a contraction cycle.
By noting :math:`\tau_{on}` and :math:`\tau_{off}` the time the myosin head
spent attached/detached from  the filament, the duty-ratio or duty-cycle can
be noted :

.. math::
    :label: roa2

    r = \frac{\tau_{on}}{\tau_{on}+\tau_{off}}

We will see in the following that the duty-ratio might have an important effect
on the processivity of the myosin.

It should be noted that as minifilaments can attach to actin filaments on both
ends, they can also act as a bridge that holds two points close to each other,
though having the properties of crosslinkers.

Myosin V
--------
.. 6

Myosin V is an unconventional myosin. Unlike myosin II it does not aggregate
into minifilaments.  Though, myosin V has a similar structure to myosin II but
with a longer neck, this confers to myosin V the ability to realize longer
steps on actin filaments. Indeed, the myosin V step size is of 36nm, which is close to the
twisting length of actin filaments. This allows myosin V motors to walk along
actin filament without having to rotate around it with the helix they form. At the end the tail domain
myosin V posses another globular domain capable of binding to its cargo, and
the variability of this region is what mostly define the difference between the
different type of myosin V.

Myosin V also has a high duty-ratio, this leads to dimers having almost always
one of the two head of the myosin to be bound to actin. It grants to the myosin
V the ability to walk in a processive manner toward the barbed end of
the actin filaments, both head successively binding 36 nm in front of the other
head.


.. todo: MyoV OOcyte Maria ?

.. _fig-myosin:
.. figure:: /figs/figure-16-54a.jpg     
    :alt: "Schematic of a myosin II motor"
    :width: 70%

    Schematic of a dimer of myosin motors with the example of Myosin II.
    Each of the myosin monomer is colored in a
    different shade of green. From Right to Left, the myosin head, with the N
    terminal, is the part of the myosin that binds to the actin filaments. The
    neck region with the light chain act as a lever arm. Finally the tail,
    constituted with coiled-coil alpha-helix that aggregate to form minifilaments.
    Adapted from :cite:`Alberts2008`.



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
      into a conformational change of the myosin which effects a recovery
      stroke. 

    - Inorganic phosphate is released as the myosin head attaches to the actin
      filament.

    - The actin-bound myosin change conformation, applying forces on it's
      cargo. This step is known as the power-stroke and is responsible for most
      of the applied forces or displacements of the myosin. During the
      power-stroke the ADP bound to the myosin head is released, leading back
      to first step of the cycle.


This principle is the same for all kinds of myosins. In the case of Myosin II
the duty-ratio is only of about 5%, which leave Myosin II detached from the
actin filament most of the time. A single dimer cannot achieve
processivity.   The tail of myosin II can bundle itself with the tail of other
myosin II motors.  They from large bipolar thick filaments of hundreds of dimers.
As each myosin dimer attaches and detaches independently from the actin
network the effective attachment of of the filament increases with the number
of motors in the minifilaments. Indeed the probability of having at least one
motor attached increases with the number of motors. The constant attachment of
at least one myosin II head in minifilaments insure that the filament does not
displace with respect to the actin network when others myosin heads recover
from their power stroke and reattach, thus conferring processivity to myosin II
minifilaments. 


The bipolar nature of myosin II minifilaments also allow them to act as force
dipoles, each  of the extremity pulling the surrounding actin network or
filament towards the center of the minifilaments. This is the mechanism at the
origin of muscle contraction and can allow to build-up tension in actin network. 

The actin cortex
================
.. 3

The actin cortex is a thin layer of between 200 to 500 nm that can be found
just underneath the plasma membrane of a cell (:num:`Fig #fig-electro-cortex`) . The properties of the actin
cortex makes it a key component to diverse processes.  Its capacity to resit
to, and transmit forces is indispensable for locomotion of many cells by
allowing the retraction of the rear of the migrating cell and will be describe
in more detail in the next section. Its structure is also essential for the
cellular division as contractility is necessary to generate cortical tension
and achieve the separation of the two daughter cells.

.. todo::

    Sketch actin cortex


The actin cortex is constituted of actin filaments that can be parallel or
orthogonal to the membrane as one can see using electron microscopy on cells
:cite:`Morone2006b`. 

.. _fig-electro-cortex:
.. figure:: /figs/Actin-Cortex-Moronne-2006.jpg
    :alt: "Electron microscope view of the actin cortex"
    :width: 70%

    Electron microscope view of the actin cortex in rat cell. The inset 
    show a periodicity of ~5nm in filaments characteristic for actin.  Scale
    bars are 100nm, inset 50 nm. Extracted from :cite:`Morone2006b`.

We saw through the bud scar of budding yeast that the full cytoskeleton could
retain memory of past events. It is also the case for simple actin networks as
show in :cite:`Parekh2005` who describe how actin-network growth can be
determined by network history, showing actin cortex could also act as a memory
for cell.


Cell Motility
=============
.. 3

The way cells move highly depends on their environment and the cell type.
We can distinguish several strategies of movement, mainly categorised into
amoeboid and mesenchymal movement. The type of motility for certain
cells can be characteristic for malignant tissue, and plays a significant role in
the ability of the cells to invade nearby tissues. 


.. _fig-schafer:
.. figure:: /figs/Schafer2004.jpg
    :width: 60%

    Polymerisation at the leading edge of the cell. NPF situated on the
    membrane of the cell localize the polymerisation. The lamellipodium will be
    characterized by a dendritic network formed by Arp2/3. Parallel actin
    structures can form a growing protrusion called filopodium.  Adapted form
    :cite:`Schafer2004`

Lamellipodium based Motility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. 4

We can ave a first look into the mesenchymal mode of locomotion of cells, which is
also often referred to as crawling. To understand how a cell is able to crawl,
to move itself, we will in particular take the example of the lamellipodium.
The lamellipodium is a characteristic structure found in cells moving on a 2D substrate. By
its nature, motion using lamellipodia is one of the easiest to study using
microscopy which might explain why it is one of the best know process of cell
displacement. None the less, it does not diminish its importance in tissues
behavior as all epithelial cell can be considered as moving on a 2D substrate.
Beyond lamellipodia, further structures that are responsible for cell motion are
filopodia and pseudopodia. They mainly differ from lamellipodia by their shape
and the organisation of the actin structure inside (:num:`Fig #fig-schafer`). Lamellipodia-based motion
can move a cell up to a few micrometers per minute.

.. todo:

    Cite speed ? Ofer2011 ?

The action necessary to move in an mesenchymal way can be decomposed into three
steps. First the cell needs to grow a protrusion. Growing this protrusion is
typically governed by actin polymerisation just underneath the plasma membrane. The
lamellipodium is such a protrusion which is constituted by a 2D dendritic actin network
that polymerize at the leading edge. Second the cell's protrusion
need to attach to the surface. This is done through trans membrane proteins
that are bound to the actin cortex on the inside of the cell. The actin cortex
will act as a scaffold to transmit the force across the cellular to these
anchor points. The last part is the generation of traction in which the rest of the cell is pulled
toward the attached protrusion. The traction force is mediated through the
cytoskeleton and actin cortex while the contraction force themselves can origin
from actin network contraction and reorganisation due to myosin motors (:num:`Fig #fig-lam-principle`).

.. As we can see the cell cytoskeleton and the actin cortex in particular play a
.. fundamental role in the motion process of mesenchymal cells. What we can see
.. that with the lamellipodium, the same conclusion can be drawn from pseudopodia and
.. filopodia. Indeed filopodia basically differ from lamellipodia by the fact that
.. they are unidimensional at the scale of the cell and are host of an actin
.. structure made of parallel filaments and bundles. Pseudopods are the equivalent
.. of filopodia, except they are characteristic in motion in a 3D environment and
.. are constituted by an actin gel more than parallel filaments.

.. todo::

    Find review on lamellipodia


.. _fig_lam_principle:
.. figure:: figs/figure-16-86.jpg
    :width: 90%

    Schematic of Lamellipodium base motility. The lamellipodium grows at the
    leading edge of the cell and attach to a focal point. The actin cortex
    under tension contract and is capable to pull the rear of the cell. Adapted
    from :cite:`Alberts2008`.




Blebbing based Motility
^^^^^^^^^^^^^^^^^^^^^^^
.. 4

The second mode of motility which is known as amoeboid is more characteristic
of 3D displacement of cells. In this mode, the cell will also form protrusions
but will not rely on adhesion to move its body. This motility rely on blebs,
that are blister-like protrusion that appear on the cell surface. A bleb
forms on the surface of cell when the membrane detach from the actin
cytoskeleton underneath it, or when the cortex ruptures (:num:`Fig #fig-bleb`). The small protrusions
are formed, quickly grow as they lack the force supporting layer that the actin
cortex provides. While growing, the bleb fills with cytosol. The actin
cortex can rapidly reform on the bleb slowing down its growth. In some cases,
the reformation of the actin cortex in the bleb and the rebuilding of the
tension inside the bleb by myosins mediated contraction is enough to reverse
the bleb. Though, the content of the cell can also drain itself into the bleb
as it grows and while the main body of the cell contract and empties, thus
moving the cell from its old position to a new one in the direction of the
initial growth of the bleb.

At their initial state, blebs are simple membrane protrusions filled with
cytosol and empty of organelles. The stop of their growth is due to the
spontaneous formation of an actin cortex on the inner side of the bare
membrane.

By their relative simplicity to the rest of the cells, blebs are the perfect
system to be reconstituted `in vitro` in liposomes.


.. _fig-bleb:
.. figure:: /figs/Bleb-nature-paluch.jpg
    :alt: "Motion through bleb mechanism"
    :width: 40% 

    Formation of bleb can be done either by a) detachment of the membrane from
    the cytoskeleton, or b) by a rupture of the cytoskeleton. In both cases the
    inner pressure of the cell leads to the inflation of the membrane at the
    point of rupture/detachment. The acto-myosin cortex will rapidly re-polymerize on
    the inside of the bleb slowing down its growth until the expansion stops.
    Extracted from :cite:`Charras2008`


.. _organelle_positioning:

Organelle Positioning
=====================
.. 3

.. todo:

    Maybe  change the structure a bit, Say beside the cortex often actin structures
    seen (sparse network), additionally these seem to be –––––– in positioning.
    Then give examples


We have seen previously that organelle positioning plays an important role in
cell function.  Several mechanisms involving actin are at the origin of
structure positioning in cells. The positioning of organelles by actin can have
a wide impact from being necessary for the correct cell division, to
allowing locust eyes to adapt in the dark by repositioning mitocondrion
:cite:`Sturmer1995`.

We already know that the actin cortex is a necessary element in cell
motility. It also plays a determinant  role in organelle
positioning. It has been shown  :cite:`Chaigne2013a` that the correct range
of elasticity of the actin cortex during oocyte division is needed for proper spindle
positioning. The correct spatial position of this spindle is necessary to
perform a viable division of the cell.

The actin cortex is not the only actin structure in the cell, beyond the thin and 
dense layer just below the membrane lies a softer and sparser actin structure that has a 
crucial role in organelle positioning.

During cell division, there are several stages that require actin structures.
As shown previously :cite:`Azoury2011` the expulsion of polar body during
oocyte asymmetric division is  strongly dependent on the time evolution of a
sparse actin network that can be found in the cell. Actin structures are  also
required at a later stage to permit the correct capture of chromosomes by
microtubules and achieve correct haploid division.  :cite:`Schuh2008` also shows
that a similar sparse actin network contracted by myosins is necessary for 
spindle migration.

Especially in oocyte that are typically large, the effect of gravity is not
negligible. The presence of a sparse "actin scaffold" is discussed in
:cite:`Feric2013`, where it is found that an actin network is present to
balance the gravitational force.

In drosophila, nurses cell need to expel their content into oocytes. It has been
observed :cite:`Huelsmann2013` that during this phase, the nurse cells' nucleus
is pushed away from the dumping canal by single actin filaments polymerising
from the membrane and forming a soft and sparse actin network.

.. There are more than theses few studies that show the importance of sparse actin network
.. inside cells, but theses networks are not extensively studied. Especially the
.. transition from the thin and dense actin cortex near the membrane to the softer
.. and sparser actin inside the cytosol. 



.. - We just saw actin cortex, 

..       - it has been shown in :cite:`Chaigne2013a` that the elasticity of the
..         actin cortex  during oocyte division need to get the right value in
..         order to get spindle positioning. The correct spatial position of this
..         spindle is necessary to perform a viable division of the cell.

..     - Actin also play role in other part of Cellular division
.. 
..       - The structure and the time evolution of the actin network in mouse
..         oocyte is necessary for the correct symmetry breaking in oocyte and
..         expulsion of polar body :cite:`Azoury2011`
.. 
..       - Later actin is necessary for the de capture of Chromosomes in order to
..         achieve correct haploid division :cite:`Lenart2005`.

..     - Beyond division actin as a few other role in positioning organelles. 
.. 
..       - Positioning of the nucleus which contain genetic material, not only
..         during division, but in general, for example to protect the genetic
..         material. This is true in plants :cite:`Iwabuchi2010`, where it has
..         been show that nucleus is moved form toward the wall of the cell the
..         less exposed to high energy light that have high chance of damaging the
..         DNA with an actin-dependant mechanism. Tan Line :cite:`Luxton2011` is
..         another actin-related mechanism, that allow to transmit forces to the
..         nucleus in order to position it at the rear of cells before migration.
.. 
..    - Unlike, the cortex which is thin and dense soften and sparse actin
..      structure exist in cells and are crucial to organelles positioning.

..         - during the phase where nurses cell expel their content into the
..           oocyte, the nucleus have to be positioned not to obstruct the
..           process. It was observed :cite:`Huelsmann2013` that the force exerted
..           by polymerizing filament seem to be enough to displace the nucleus.
.. 
..         - :cite:`Schuh2008` show that a sparse actin network contracted by
..           myosin that like the cortex to the spindle is necessary for its
..           migration. 
.. 
..         - Organelles are supported by .. gravity thing :cite:`Feric2013`
.. 
..         - The passage from the thin an thick actin cortex to such sparser and
..           softer is not well studied, the capacity of such for to
..           generate/sustain forces neither.


.. todo:
    - Mitoncondria, ER (made to produce proteins), also serve in locust (Sturmer1995)

    - the passage from cortex to cytosol is not well studied
    - :cite:`Holubcova2013`. 


.. We have previously seen that actin plays a major role in cell motility and
.. division. By opposition to the actin cortex which is thin and dense network
.. just under the membrane, we will interest here in different kind of structure
.. formed by actin that have an as important role in the cells life cycle.

.. In the same way that cells need to displace, or that components need to be
.. transported between parts of the cell, the positioning of organelles in cells
.. is crucial for development. 
.. The cell nucleus, essential to the cell replication
.. as it contains most of the genetic material needs to be protected. It has been
.. shown :cite:`Iwabuchi2010` that in plant cells, the nucleus is moved away from
.. high energy light that could damage its DNA with a mechanism that involve
.. actin.
.. Wether the nucleus is actually sliding along actin bundles or anchored
.. to the filament while they are pull as not been addressed in for theses cells,
.. is has been shown that in fibroblast, nuclear positioning is directly coupled
.. to actin cable using TAN lines :cite:`Luxton2011`.
.. Both of theses mechanism use
.. actin as a scaffold to transmit the forces generated by other process to the
.. targeted organelle. These other process are due to molecular motors in the
.. cases of plant cell, and retrograde flow in the second one. It is a natural
.. question to ask of whether or not, actin can have such effect by itself ?
.. 
.. A beginning of answer to this question can be hinted by looking at drosophila
.. nurses cell. Indeed, during the phase where nurses cell expel their content
.. into the oocyte, the nucleus have to be positioned not to obstruct the process.
.. It was observed :cite:`Huelsmann2013` that the force exerted by polymerizing
.. filament seem to be enough to displace the nucleus. More especially, while the
.. polymerisation occurs at anchored points in the membrane, the actin filaments
.. grows, moving the pointed end toward the nucleus, eventually pushing it away.
.. 
.. 
.. The position of the organelles can have more unexpected effects. In particular,
.. some nocturnal locust adapt their vision depending on the light condition by
.. modifying the properties of a part of their eye called the omatidium. More
.. specially, the refractive index if each organelle being slightly different, the
.. reorganisation of the position on mitocondrion and endoplasmic reticulum inside
.. the cell has been show to be droved by actin polymerisation and responsible
.. from changed in optical properties in locust eye :cite:`Sturmer1995`.
.. 
.. 
.. Movement of organelles is also crucial for plant biology, indeed, genetic
.. material is sensitive to UV light, and protecting it is necessary for plant
.. survival. Iwabuchi et al. have show that actin is responsible for the migration
.. of the cell nucleus away from the part of the cell the more exposed to the
.. damaging light :cite:`Iwabuchi2010`.





