Active cytoplasm movement in mouse oocytes
############################
.. 1

Introduction
************
.. 2

Mouse oocyte are big spherical cells with a diameter of about 80 µm.  Previous work has shown
that the spindle positioning during meiotic cell division in oocytes depends 
on an actin meshwork that is present in the cell's cytoplasm :cite:`Schuh2008`.  This
actin meshwork is regulated by formin that is localized to endogenous vesicles. 
Additionally, these vesicles recruit the myosin-Vb motor protein, that are know do drive the active movement
of the vesicles in the cytoplasm :cite:`Holubcova2013`. In a collaborative project with the group of Marie-Hélène Verhlac
and her Postdoc Maria Almonacid at the Collège de France, we designed a way to measure
cytoplasmic activity in mouse oocyte.


In :num:`Figure #oocytewt` a typical mouse
oocyte is presented where the nucleus can be seen to be positioned at the center of the cell.
Current questions in this system relate to the mechanical processes during miosis such as the chromosome migration, 
the assymetric cell division and the positioning of organelles by the dynamic remodelling of the actin network. 
While our team did active and passive microrheology measurements on teh timescales or 10 seconds, I developped a 
method that is suitable for longer timescales in the order of minutes, that are more relevant for the process of miosis. 
.. todo:

    Maybe mention that actin is important in this positioning.

.. _oocytewt:

.. figure:: figs/oocyte-wild-type.png     
    :alt: "Bright field image of an oocyte"
    :width: 60%

    (YOU NEED A SCALE BAR!) Bright field image of a mouse oocyte before meiosis. The cell diameter is about
    80µm. The nucleus is positioned at the center of the oocyte during Meiosis I by the
    help of the actin network. The positioning is a crucial factor for the
    normal division of the oocyte. The oocytes are a good reference system as they provide a clean spherical
    symmetry and due to their size give a good spatial differences between the cortex and the cytosole which helps 
    in measuring spatial variations of mechanical properties and vesicel movement.  Image Credit to Maria Almonacid from
    Collège de France.

Oocytes
*******
.. 2

The cytosolic actin meshwork in oocyte is controlled by the activity of formins (Fmn2) that
nucleate actin polymerisation and by the activity of the vesicle bound molecular motor protein myosins Vb that 
controlls the dynamic movement of the
vesicles in the actin meshwork. Hence it is of interest to study oocytes that have formin and myosin Vb deficites. 
In particular, we focused on three types: 1) Wild types oocyte, 2) oocytes prepared from Formin 2 invalidated female 
(Fnm2-/-) that lack the
actin meshwork and 3) oocytes injected  with the dominant-negative tail of Myosin
Vb (:num:`Fig #fig3oo`)

.. _fig3oo:
.. figure:: figs/3-oocytes.png
    :width: 100%

    Bright field image microscopy of the 3 kinds of oocyte (Credit to Maria
    Almonacid, Collège de France). WT) Image of Wild Type Oocyte, Scalebar is
    20µm. Fmn2-/-) Oocytes extracted from females with invalidated Formin 2,
    theses oocytes lack the actin meshwork. MyosinVb Tails) Oocyte injected
    with a Myosin Vb dominant negative tail have a less actin vesicle
    population. The white square gives an example of the region that is used for the analysis presented in this chapter. 


Measure of activity
*******************
.. 2

The diffusive like motion of actin positive vesicles that can be observed during oocyte meiosis is
reduced in Fmn2-/- and MyosinVb-tails oocytes when compared to the wild type.
While the use of particle tracking algorithms to measure vesicle motion in oocyte is possible, it remains a
complex process especially as the vesicles may move outside the focal
plane of the microscope. As a simple appraoch to measure the vesicle activity we decided to
investigate the temporal variations of the bright field images in mouse oocyte.

We can compute the time dependent difference between predefined region of interest (ROI) in an image
series to see how fast the bright field images change. We can compare
the result for wild type (:num:`Fig #decay-wt`), Formin Knockout (:num:`Fig
#decay-fmn2`) and MyosinVb dominant negative tail (:num:`Fig #decay-myo`).

(PUT THE 3 IMAGES TOGETHER IN 3 DIFFERENT PANELS. THEN DESCRIBE THE DIFFERENCE. WOULD IT NOT BE BETTER TO ALWAYS USE THE SAME SCALE ON THE COLORBAR?)
.. _decay-wt:
.. figure:: figs/decay-wt.png
    :width: 70%

    Bright field images of Wild type mouse oocyte at t=0, t=1min et t=174min as
    well at the difference between t=1min, t=174min and initial image. Blue
    indicate that the later image is brighter that the original one and red
    indicate that it is darker.  For wild type oocyte, we can see that the
    scale difference between images is similar for a :math:`\Delta t` of 1
    minute and 174 minute. Region show is the same as indicated in :num:`figure #fig3oo`.

.. _decay-myo:
.. figure:: figs/decay-myo.png
    :width: 70%


    Bright field images of MyoVb tails mouse oocyte at t=0, t=1m et t=174m as
    well at the difference between t=1m, t=174m and initial image. Blue
    indicate that the later image is brighter that the original one and red
    indicate that it is darker.  We can see that the difference between images
    is much stronger after several hours (174min) than after a minute, unlike
    in :num:`Figure #decay-wt`. Region show is the same as indicated in :num:`figure #fig3oo`.

.. _decay_fmn2:
.. figure:: figs/decay-fmn2.png
    :width: 70%

    Bright field images of Fmn2-/- mouse oocyte at t=0, t=1m et t=174m as well
    at the difference between t=1m, t=174m and initial image. Blue indicate
    that the later image is brighter that the original one and red indicate
    that it is darker.  We can see that the difference between images is much
    stronger after several hours (174min) than after a minute, unlike
    in :num:`Figure #decay-wt`. Region show is the same as indicated in :num:`figure #fig3oo`.

(I AM NOT SURE WHAT EXACTLY YOU WANT TO SHOW. YOU SAY THAT THE CHANGE IS STRONGER IN FMN2-/- and MYOVb, WHICH SUGGESTS THAT THEY MORE ACTIVE?)

A quantitative measurement of the difference of the images is the
autocorrelation of these thought time. The correlation of two images :math:`A`
and :math:`B` of same dimension is defined as :


.. math::

    r_{AB}=\frac{\sum\limits_{i=1}^n (A_i-\bar{A})(B_i-\bar{B})}{(n-1) s_A s_B}

    
In which :math:`A_i` and :math:`B_i` are luminosity values of each of the
:math:`n` pixels in :math:`\bar{A},\bar{B}` correspond to average values over
the images, :math:`s_A` and :math:`s_B` are the standard deviations of the
luminosity values.


We can compare the decrease of correlation over time depending on the type of
oocyte. In order to extract a single value that represent the activity, 
we can phenomenologically fit the correlation as a decaying exponential with an offset :

.. math:: 
    :label: edecay

    r(t) = (1-off).e^{(-t/\tau)}+off


In which :math:`t` is time, and :math:`\tau` is a characteristic time representing the
correlation decay. The offset  :math:`off` represent the value of the
correlation at infinite time to take into account artifact in the chosen region
of interest, and defects in the image that will not decorrelate over time. 

:num:`Figure  #fig-exp-decay` gives typical examples of the result of the measured autocorrelation over time, and a
single exponential decay fit. 

.. _fig-exp-decay:
.. figure:: figs/corrtime.png
    :width: 65%

    Decreasing autocorrelation of images internsity (solid line) over time, with
    exponential decay fit (dotted lines) as in :eq:`edecay`. The characteristic decay time of the fit 
    :math:`\tau` in the legend. We can see in the plot that the
    correlation of the images decrease much faster in wild type oocyte (red
    curves, :math:`\tau \sim minute`) in compared to Fmn2-/- (blue lines
    :math:`\tau > hour`) that lack the actin meshwork, or to dominant negative myosin Vb
    tails (green :math:`\tau > hour`). While the fit quality is not impressively good, the 
    overall change in the timescales is well captured. 



The results show that the values of the characteristic time increases with when we disrupt the
actin network or the  source of its dynamism by inactivating Myosin Vb. We can
then use the inverse of :math:`\tau` as an indicator of activity.


Once we have define the activity of a region of the cytoplasm of the cell, we
can repeat the measurement on different areas of the cytoplasm. This allows to
reproduce a map of the activity in the cell as a function of the position (
:num:`Fig #fig-activity-map`.

.. _fig-activity-map:
.. figure:: figs/CellAct-WT.png
    :width: 80%

    Activity for different region of  10 by 10 pixels of a wild type oocyte.
    Value of :math:`1/\tau` plotted as color square overlaying the
    analysed bright field image. Scale
    bar is 20 µm. We can see that the activity is near the nucleus is lower
    (blue) than in the middle of the cytoplasm. 

The measure of the correlation characteristic decay time can also be done on a
time sliding widows. This allows for the determination of activity of a
particular area of the cytoplasm with time.


Conclusion
**********
.. 2


In this part we developed a methods that allow to determine the cytoplasmic
activity. This method also allows to determine the variation of this cytoplasmic
activity over space and time. This methods is the study of oocyte as it allows
to probe timescale from the second to the hour which is in the order of the
relevant timescale for oocyte maturation of a few hours. It is also
complementary to techniques like micro rheology that have difficulties probing
timescale beyond tens of seconds due to thermal drift and cell movements, but
reach much shorter timescale.

The use of this technique is currently under investigation at Collège de France
by Marie-Hélène Verhlac and Maria Almonacid. It is used to measure the activity
of actin network in oocyte and determine their effect on the meiosis of mouse
oocyte.

