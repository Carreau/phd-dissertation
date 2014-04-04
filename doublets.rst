.. _doublets:

==================
Liposomes doublets
==================


So the doublets are stuck liposome, 
and stuff like model :

We assume that :math:`S(P)` is the signal we get from real polymerised actin on
liposome doublet, and :math:`Noise(P)` is the signal noise that come from
different sources. To reconstruct the doublet parameter, which are center of
both liposomes, considerd as sphere, we need to find the two center and two
radius of the twho portion of sphere. 

Later theory do not depend on the six parameter that are given by the positoin
of the two centers, btit as we do not control the orientation and exact position 
of the liposome doublets during the experiements, we have to  count them as adjustabke parameter.





.. math::

    R = \int_{P\in\Omega}M(P).\left[S(P)+Noise(P)\right]d\Omega

    R = \int_{P\in\Omega}M(P).S(P)+ \int_{P\in\Omega}M(P).Noise(P)d\Omega

We cannot determine :math:`\int_{P\in\Omega}M(P).Noise(P)d\Omega`, but we can assume that the noise is uniforme and that

.. math:: 
    
    \int_{P\in\Omega}M(P).Noise(P)d\Omega = \int_{P\in\Omega}M(P).\left<Noise(P)\right>d\Omega

    \int_{P\in\Omega}M(P).Noise(P)d\Omega = \left<Noise(P)\right>.\int_{P\in\Omega}M(P)d\Omega

If we assume :math:`Noise(P)` uniform. 

Id we denote 

.. math::

    \int_{P\in\Omega}M(P)d\Omega = V_\Omega(M)

    \text{and}\quad \left<Noise(P)\right> = \mu

Then we can define :math:`R_n=R/V_\Omega(M)` by:

.. math::

    R_n = \frac{\int_{P\in\Omega}M(P).S(P)}{V_\Omega(M)} + \mu


As we will try to maximise the overlap between :math:`M` and :math:`S`, µ will
not interviene in the maximisation of :math:`R_n`. It is convenient to get rid
of the noise in the maximisation process, as it can varie from experiement to
experiements.

.. math::

    \mathcal{R} = \int_{P\in\Omega}M(P)S(P)




@We decided to build the setup both to be extensible and to able to combine on the same
microscope several imaging techniques, as well as the capacity tu use Optical trapping.

From the Imaging point of view, the final goal of the setup would be to be able
to acquire on the same sample, images from bright field, epifluorescence,
spinning disk and phase contrast. 

Optical trapping should provide both a strong fixed trap, as well as multiple
time shared optical trap, with force mesurement on each of thoses traps thanks
to position sensible detector on the back focal plane of the condensor.

In addition, we should be able to add a pused UV laser to make laser ablation
on living cells.

Optical trapping Requirement
----------------------------

The initial ~design~ for the optical trapping was to have at least one
non-mobile trap and one mobile trap that could be controlled  that could b used
at the same in the same plane in the observed samble.


