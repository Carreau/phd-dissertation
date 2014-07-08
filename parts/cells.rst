.. Cells

 
Living Cells
************
.. 2


.. Description of cell
.. ~~~~~~~~~~~~~~~~~~~

.. todo:

    - spherical, cytokinetic ring, filopodia
    - how force effect actin
    - focal adhesion

    - organelle, 

      - nucleus/spindle positioning in division
      - from oocyte, diploid -> haploid



Cell are the basic building block of life, all living things are composed of
cells, from unicellular to multicellular organisms like us. Unicellular
organism must accomplish all the functions. At the other end,
multicellular organism cells differentiate in order to accomplish specialised
tasks often by regrouping into organs. Despite sharing the same genetic
material, each cell to accomplish a different task require different
mechanical properties of the cells. The variation of elasticity and other
mechanical properties of cells derive from the structure they are composed of.

.. todo:

    This paragraph is a little too repetitive try to boil it down to 1-3 simple
    phrases rethink what message you want transmit.

Cells are hence able to adapt to their environment and develop function and
behavior that will depend on time. A small change of timing and/or biochemical
conditions can highly injure the development of an organism : modification of
the actin network at the right time of the cell cycle prevents symmetric division
:cite:`Lenart2005`, :cite:`Vasilev2012`. Mechanical properties of the substrate can
govern the differentiation of cells : Soft substrate will favor brain-tissue
cell, where stiff substrates increase the appearance of muscle cells
:cite:`Engler2006`.

.. _albertcell:

.. Figure:: /figs/figure-1-30.jpg
    :alt: schematic of a cell
    :width: 90%

    Schematic of an eukariotic cell, adapted from :cite:`Alberts2008`. One can
    see the many component that constitute majority of cells.  Cell shape and
    size can highly vary, from quasi spherical with a typical size of ten
    micrometers to elongated neurones that can be tens of centimeters long.

Nonetheless, even with all theses different behavior and phenotypes, cells
have a common structure. The exterior of the cell is separated from the
inside by a plasma membrane. The interior of the cell is filled with the cytoplasm
which contain diverse structures known as organelles, genetic material, and
a large number of proteins that the cell uses to accomplish its functions. To
communicate with the outside, cells have a series of mechanism that allow signals
and cargo to go through the membrane. This communication can be chemical, but
mechanics is also known to participate in the process. To sense their
mechanical environment, cells use adhesion complexes to attach to the
substrate, and integrins as trans-membrane protein to transfer the force to the
cell cytoskeleton situated inside the cell. Chemical signals can either cross
the membrane through trans-membrane proteins, endocytosis and exocytosis are
ways for the cell to impart and export proteins and chemicals through its membrane. 





 


.. todo:
  - structure of Arp2/3 branched network is the same on beads comets than on
    lamelipode :cite:`Cameron2001` 
  - more than 150 protein have been found to bind with actin.
  - [x] Wave complex,
    - [x] Wasp, N-Wasp ( need to :cite:`Machesky1999` )
  - Some network need actin, some other do not. (Fletcher review 2010)
  - [x] Polymerase, (depolymerase severing), 
  - [x] crosslinker
    - [x] parallel like fascine
      - [x] rotate like alpha-actinin 
      - effect of cross linking distance :cite:`Morse20..`

.. todo:
  - interphase, cellule prepare for division
  - Mitosis : "DNA Segregating"
  - need to describe actin, 
    - depending on the length scale semi-flexible polymers.
  - polymerisation barbed end pointed end, (directed)
    - form microfilement
  - cytoskeleton is dynamic
  - formed under the plasma membrane
  - ratchet nechanisme
  - [x] use of Arp2/3 to branch
  - capping, protein,  formin (OOcyte)
  - [x]myosin, run on actin to barbed end/ processive/not processive.
    - stress fibres
  - [x] troppomyosine


Cell Organelles
===============
.. 3

.. todo:

    Maybe this should be before cytoskeleton. Here it is breaking the flow.
    Also you may ------ -- ti 12. when you introduce the cell

Inside the cytoplasm, cells have a number of structures with different and
specialised functions which are called organelles. The position and state of
organelles is of great importance for the cell to achieve its functions.
Probably the most known organelle is the cell nucleus of eukariotic cells that
contains the genetic material. Attached to the nucleus is the endoplasmic
reticulum  which is the organelle responsible form translating
RNA coming from the nucleus to functional proteins that will be delivered
across the cell after maturation in vesicles. Theses vesicles are
transported across the cell both by dyneins and kinesins — molecular motors —
that walk along microtubules originating from the centriole part of the
centrosome but also by myosin along actin filaments.  All of those processes
consume energy in  the form of ATP, generated within the mitocondria spread
across the cytoplasm. A schematic of the cell with some organelles can be seen
on :num:`Figure #albertcell`

The positioning of organelles is crucial for the life of an organism. During the
meiotic division of cell, for example, it has been seen that the positioning of
the nucleus at the center of the cell in mouse oocytes happens before its
migration closer to the cortex to expel the first polar body. Failure to do so
result in a incorrect amount of DNA in germinal cell that can lead to
infertility. 

It is already known that microtubules play a key role in organelle positioning.
Microtubules emanating from centrosome position at the two ends of the cell
during its division is used to fetch the correct chromosomes. Each
chromosome is pulled towards the centrosome which leads to each daughter
cell having the same amount of DNA.

Actin plays also an determinant role in organelle positioning process,
like in drosophila oocyte maturation where it positions the nurses cell away
from the dumping canal :cite:`Huelsmann2013`. In a later chapter (:ref:`Organelle
Positionning <organelle_positioning>`) we will develop a few keys points where
actin is indispensable in organelle positioning and how this relate to the
biomimetic actin networks we reconstitute. :num:`Figure #oocytewt` shows a mouse
oocyte where the nucleus can be seen positioned at the center of the cell.

.. todo:

    Maybe mention that actin is important in this positioning.

.. _oocytewt:

.. figure:: /figs/oocyte-wild-type.png     
    :alt: "Bright field image of an oocyte"
    :width: 60%

    Bright field image of a mouse oocyte before meiosis. Cell diameter is of
    80µm. The nucleus can be clearly seen at the center of the cell. The
    nucleus is positioned at the center of the oocyte during Meiosis I by the
    help of the actin network. The positioning is a crucial factor for the
    normal division of the oocyte.  Oocytes are a good reference system  by
    their symmetry and their sufficient size that help measuring spatial
    variation of mechanical properties.  Image Credit to Maria Almonacid from
    Collège de France.


.. _intro-cyto:

The Cytoskeleton
================
.. 3

The cytoskeleton, literally skeleton of the cell, is the structure which gives
it shape to a cell.  As for other multicellular animals that possesses
skeleton, its shape is often a hint on how a organism moves. As feet, fins and
wings are characteristics that will tell you whether a animal 
 prefer land, see or air, the cytoskeleton will tell you many
things a bout a cell. 

Unlike the (exo)-skeleton of animals which is rigid and
static, the cytoskeleton of cell is a  highly dynamic structure that keep
remodeling itself on a short time scale compared to the speed at which a cell
move. That's through this dynamics that the cytoskeleton can achieve its
functions.  As mammals skeletons are necessary to transmit force from one part
of the body to another, the cell cytoskeleton is responsible to not only
transmit the force the cell is exerting, but also to generate theses force.
Thats through its cytoskeleton that a cell can be connected to its environment,
both mechanically and biochemically.

We will consecrate a longer part to describe the cytoskeleton in the later part 
:ref:`role_of_actin`.

