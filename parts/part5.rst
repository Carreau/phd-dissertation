Activity in oocyte cytoplasm
############################
.. 1

Introduction
************
.. 2

Mouse oocyte are big spherical cell with a diameter in the order of 80 µm.  It
ha been shown that the spindle positioning during meiotic division of oocyte is
dependant of an actin meshwork present in the cell :cite:`Schuh2008`.  This
actin meshwork is regulated by endogenous vesicle which dynamic is myosin-Vb
dependant :cite:`Holubcova2013`. In a collaboration with Marie-Hélène Verhlac
and Maria Almonacid in Collège de France, we designed a way to  measure
cytoplasmic activity in mouse oocyte.


:num:`Figure #oocytewt` shows a mouse
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

OOcytes
*******
.. 2

As oocyte meshwork in oocyte is controlled by the activity of formins than
drive actin polymerisation and Myosins Vb that controlled the dynamism of the
vesicle in the meshwork, we decided to develop the analysis in 3 type oocytes.
Wild types oocyte, oocyte preleved on Formin 2 invalidated female that lack the
actin meshwork and oocytes injected  with the dominant-negative tail of Myosin
Vb (:num:`Fig #fig3oo`)

.. _fig3oo:
.. figure:: /figs/3-oocytes.png
    :width: 100%

    Bright field image microscopy of the 3 kinds of oocyte (Credit to Maria
    Almonacid, Collège de France). WT) Image of Wild Type OOcyte, Scalebar is
    20µm. Fmn2-/-) Oocytes extracted from females with invalidated Formin 2,
    theses oocytes lack the actin meshwork. MyosinVb Tails) Oocyte injected
    with a Myosin Vb dominant negative tail have a less actin vesicle
    population.


Measure of activity
*******************
.. 2

The diffusion of actin positive vesicle ta can be seen during oocyte meiosis is
less important in Formin -/- and MyosinVb-tails oocytes than in Wild type.
While particle tracking with the vesicle present in oocyte is possible, it is a
complex process especially with the diffusion of vesicle outside the focal
plane of the microscope. In order to measure the activity we thus decided to
investigate the variations of the bright field images in mouse oocyte.

We can compute the difference between  region of interest (ROI) of images as a
function of time to see how fast the bright field image changes. We can compare
the result for wild type (:num:`Fig #decay-wt`), Formin Knockout (:num:`Fig
#decay-fmn2`) and MyosinVb dominant negative tail (:num:`Fig #decay-myo`).


.. _decay-wt:
.. figure:: /figs/decay-wt.png
    :width: 70%

    Bright field images of Wild type mouse oocyte at t=0, t=1m et t=174m as
    well at the difference between t=1m, t=174m and initial image. Blue
    indicate that the later image is brighter that the original one and red
    indicate that it is darker.  For wild type oocyte, we can see that the
    scale difference between images is similar for a :math:`\Delta t` of 1
    minute and 174 minute. Region show is the same as indicated in :num:`figure #fig3oo`.

.. _decay-myo:
.. figure:: /figs/decay-myo.png
    :width: 70%


    Bright field images of MyoVb tails mouse oocyte at t=0, t=1m et t=174m as
    well at the difference between t=1m, t=174m and initial image. Blue
    indicate that the later image is brighter that the original one and red
    indicate that it is darker.  We can see that the difference between images
    is much stronger after several hours (174min) than after a minute, unlike
    in :num:`Figure #decay-wt`. Region show is the same as indicated in :num:`figure #fig3oo`.

.. _decay_fmn2:
.. figure:: /figs/decay-fmn2.png
    :width: 70%

    Bright field images of Fmn2-/- mouse oocyte at t=0, t=1m et t=174m as well
    at the difference between t=1m, t=174m and initial image. Blue indicate
    that the later image is brighter that the original one and red indicate
    that it is darker.  We can see that the difference between images is much
    stronger after several hours (174min) than after a minute, unlike
    in :num:`Figure #decay-wt`. Region show is the same as indicated in :num:`figure #fig3oo`.



A quantitative measurement of the difference of the images is the
autocorrelation of these thought time. The correlation of two images :math:`x`
and :math:`y` of same dimension is defined as :


.. math::

    r_{xy}=\frac{\sum\limits_{i=1}^n (x_i-\bar{x})(y_i-\bar{y})}{(n-1) s_x s_y}

    
In which :math:`x_i` and :math:`y_i` are luminosity values of each of the
:math:`n` pixels in :math:`\bar{x},\bar{y}` correspond to average values over
the images, :math:`s_x` and :math:`s_y` are the standard deviation of the
luminosity values.

.. figure:: /figs/corrtime.png
    :width: 80%





