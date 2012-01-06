.. _davisbicycle:

==========================
Davis Instrumented Bicycle
==========================

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

Preface
=======

At the beginning of 2009 I was in Delft working with Jodi and Arend on much of
the work explained in the previous Chapters. I was still also in contact with
Mont and Luke back in Davis. Before I'd come to Delft, Luke had mentioned the
possibilties of applying for an NSF grant to fund the remainder of our PhD
research. Mont doesn't have big track record in grant funding for his lab and
we'd spent the first few years taking teaching assistance positions which ate
up most of our available research time outside of classes. I fortunately got
the Fulbright grant which gave me a year to focus on research and Jodi's PhD
budget helped fund the research costs and some of my conference trips. At the
beginning of December 2008 Luke sent me an email with a renewed interest in
applying for the NSF grant and Mont seemed to be on board. Mont also talked
with Ron and got him interested. We spent the next two months writing our grant
proposal primarily using video conferencing and collaborative word processing
to get it done. The basic idea was to pair Ron's manual control expertise with
our bicycle dyanmics expertise to study the dynamics, control and handling
qualities of bicycles with the theoretical constructs supported by extension
experimentation. Our work paid off and we recieved the grant, albiet at a
smaller income than asked for so we had to cut back some of the scope (which
was probably already too large!). This set us up for a two year study where
we'd develop a manunal control model, verify it and the basic bicycle dynamics
with an instrumented bicycle and a robotic bicycle and finally do some work on
handling qualities predictions.

When I got back to Davis in September 2009 we started gearing up for the grant
work that would start come October 1st. I had to get my qualifying exam done
in October and I also signed up for a Spanish class (which wasn't necessarily a
good idea for the grant's sake). This gave a little slow start, as neither Luke
or I realized that the scope of what we had to do didn't really allow any more
time for classes. We got moving though and started to plan out the bicycle(s)
we wre going to build. Our proposal 

Introduction
============

This chapter details the design and implementation of an instrumented bicycle
capable of accuratley measuring much of the necessary kinematics and kinetics
associated with controlling the bicycle.

The bicycle's primary design criteria were as follows

#. Sized for our intended riders
#. Accurately measure the rider's applied steer torque
#. Accurately measure the three dimensional rates and orientations of the
bicylce frame and fork.
#. Accurately measure the rear wheel rotational rate relative to the bicycle
frame.
#. Restrict the rider's biomechanical movement to more closely meet the Whipple
model rigid rider assumption. This also requires the bicycle to be self
propelled, as no rider leg movemnt is allowed.
#. Measure a lateral disturbance force

Secondary

#. Measure the rider's restricted upper body motion
#. Measure the reaction forces between the rider and bicycle

We had very succesful results measuring the complete kinematic configuration of
the bicycle and rider with the motion capture techniques, but I no longer had
access to a system as good as the one at Vrije, especially not if we intended
to capture the motion of the system on the ground as opposed the small space
afforded by the treadmill. With this in mind, we decided to expand the
on board measurement techniques used in the Delft Instrumented bicycle. The
downside was inaccurate location tracking of the system. Being that this
wouldn't be detrimental to system identification, we moved forward.

Bicycle frame
=============

The bicycle frame is a large Surly 1 x 1 model. It is designed as a single
speed off road bicycle for 26in wheels with fat tires. The frame is constructed
from butted cromoly steel tubing. It has both front and rear v-brake and disc
brake mounts. We choose it primarily because it was steel and had disc brake
mounts which were going to be used for wheel speed encoder mounts. It was also
a good size for the intended riders.

Propulsion
==========

To allow teh bicycle to be propelled forward without requiring the rider to
pedal, we opted for a bicycle electric hub motor. Amped Bikes donated a direct
drive kit for our use and we purchased a light 36 volt lithium ion battery as a
substitute for the heavy lead acid batteries which came with the kit. The kit
had a motor controller with a rudmentary "cruise control". I desired the cruise
control to allow the rider to set the speed of the experiment and then focus
their attention to lateral control as opposed to throttle control. This worked
well for the experiments performed on the floor, but was more difficult on the
treadmill as matching the cruise control to the speed of the treadmill proved
difficult. So sort of feedback control could alleviate the difficulties.

Orientations, Rates and Accelerations
=====================================

The Whipple bicycle model at constant speed fundamentally has two important
states of the lateral dynamics: roll and steer (as defined in Chapter
:ref:`eom`). Ideally one would like to measure the angular orientation, rate
and accelerations of both the rear frame and the front frame. Sensors that
allow indpendent and accurate measurements off each are potentially ideal, to
avoid having to estimate measurements.

Steer angle is easy to measure with either some form of potentiometers or
encoders and has been accurately measured on many bicycle and motorcycle
systems. Same goes for the roll and steer rates, which can be measured directly
with rate gyro or encoders. The angular accelerations aren't directly
measurable, but after-the-fact numerical differentiation with filtering is
often acceptable. The linear acceleration of point on the body is directly
measurment with accelemeters, and the angular accelerations can be computed if
the acceretaion and location of poitns are measured. The roll angle is the most
tricky measurement. Integration of the roll rate measurment is an option, but
difinite initial conditions and some way to account for the drift is required,
and not trivial. The roll angle can be estimated from other measurments and if
a bicycle model is assumed accurate estimations can be computed with estimation
techniques such as a Kalman filter. This also poses some problems depending on
how you'd want to use the data. If you want the *actual* roll angle of the
physical rear frame, assuming a bicycle model and using a Kalman filter is not
the way to go as you've built in the assumptions of the bicycle model into you
estimation technique.

.. list-table:: Table of maximal measured values found in all experimental data
   taken in Chapter :ref:`motioncapture`. The ranges were determined from 95
   percentiles, the accuracy as a percentage of the range and the bandwith as
   95 percentile of the power in the signal.
   :header-rows: 1

   * - Measurement
     - Range
     - Accuracy
     - Bandwidth
   * - Roll Angle
     - :math:`\pm 8` deg
     - 0.2 deg
     - 45 hz
   * - Roll Rate
     - :math:`\pm 30` deg/s
     - 0.6 deg/s
     - 40 hz
   * - Roll Acceleration
     - :math:`\pm 100 \frac{\textrm{deg}}{\textrm{s}}`
     - :math:`2 \frac{\textrm{deg}}{\textrm{s}}`
     - 25 hz
   * - Steer Angle
     - :math:`\pm 65` deg
     - 1 deg
     - 45 hz
   * - Steer Rate
     - :math:`\pm 150` deg
     - 1.5 deg/s
     - 35 hz
   * - Steer Acceleration
     - :math:`\pm 600 \frac{\textrm{deg}}{\textrm{s}}`
     - :math:`12 \frac{\textrm{deg}}{\textrm{s}}`
     - 30 hz

The class of sensors that are called Inertial Measurement Units (IMU) or
Attitude heading reference systems (AHRS) have become more affordable and small
enough to be very appropriate for measurements such as ours due to the advent
of MEMs technology and very small rate gyros and accelerometers. An IMU can
potentially be rigidly affixed to each body of the system to give complete
kinematic details of the motion.

Inertial Measurement Units
   An inertial measurement unit typically measures the body fixed the angular rate
   and acceleration of rigid body and point respecitvely.
Attitude Heading Reference System
   An attitude heading reference system measures what an IMU does but also oftern
   includes earth magnetic field measuresments and or gps combined with an
   estimation algorithm to provide orientation and/or location estimations along
   with the other measurements.

Many of these were in our budget range so we scouted the companies to see what
was offered.

.. todo:: Add a small version of the IMU selection spreadsheet

We chose the VN-100 development board from a relatively new company called
VectorNav due to price, on board orientation calculations and the potential
ease of collecting data via a typical RS232 serial line. We'd place a single
VN-100 on the bicycle frame to measure the angular orientations and rates along
with the acceleration a point the frame. The VN-100 relied on additional
magentometer readings and an on-board proprietary Kalman filter for computing
the orientation.

The VN-100 would be used in tandem with sensors to measure the front frame
motion. I went with a similar design and setup as the Delft intrsumented
bicycye: a pontentiometer for relative steering angle measurement and a single
axis rate gyro for the body fixed angular rate about the steer axis.

.. list-table::

   * - Sensor
     - Measurements
   * - VN-100
     - Rear frame angular rates and acceleration of a point (estimations of
       orientation)
   * - Single axis rate gyro (Silicon Sensing CRS03-04)
     - Bodyfixed angular rate about the steer axis
   * - Rotory potentiometer (SP22F)
     - Relative steer angle

- rate gyro was super expensive for little gain
- i couldn't ingtegrate the vn-100 into the rest of the DAQ
- VN-100 sucked at giving orientation

Steer Angle
~~~~~~~~~~~

I adopted the same steering angle measurement device that I use on the Delft
instrumented bicycle, with some minor improvements such as better tension
adjustablity and switching to a screw mount potentiometer.

.. todo:: add the

The VN-100 turned out to be a poor choice for our application in mutliple ways.
The second of which I'll talk about in a later section. The first is that the
orientation estimations were very poor. I wanted *at least* accurate estimate
of the roll angle of the bicycle. The VN-100 repdeatly did not provide this.
VectorNav worked with me and tried offer various methods of tuning the VN-100
with state covariance weightings for the Kalman filter and also to tune out any
static magenetic fields from the bicycle frame. The highly likely issues were
associated with both the wheel rotationing and teh front frame rotation all
relative to the rear frame, with could cause varying distrubances in the
magnetic field. The hub motor definitely affecting the magnetometer readings
and these may have been too great to tune out. I also realized that going with
a proprietary estimator is a bad idead, especially when one has a good idea of
the dynamics of the rigid body that the sensor is attached to. In our case if
the Kalman filter was programmable, we could taylor it with the a bicycle model
to improve the orientaion estimation significantly. Also if the VN-100 could
accept input signals, the filter could be tuned well too. After countless hours
trying to tune their proprietary filter I gave and went to the roll angle
measurement design that I should have done in the beginning.

.. todo:: cite Boniolo for roll angle estimation, talk about Danique's work,
   cite other people that handle this problem too.

Roll angle trailer
~~~~~~~~~~~~~~~~~~

I designed a simple trailer to that was pulled behind the bicycle to measure
roll angle with a potentiometer, much in the way the steer angle was measured.
The trailer needed to be light such that it didn't adversly affect the lateral
dynamics and to give a good estimate of the roll angle. The trailer had two
caster polyurethane wheels (roller blade wheels) attached to a frame which
attached via a revolute joint aligned with the roll axis to a yoke that
attached at the axle of the rear wheel.

.. todo:: Make nice figure or photo of the trailer.

Lateral Force
=============

Strain Gauge Amplification
==========================

Seat Post
=========

Foot Pegs
=========

Rider rigidification
====================

Data aquisition
===============

Time sychronization
===================

DAQ Software
============

Steer Torque
============

Literature Review
-----------------

There are very few published studies that measure or attempt to measure steer
torque on a bicycle or lightweight single track vehicle. There are a more
analytical studies that attempt to predict steer torques. The following lists
some that I have read.

Steer torque from models
~~~~~~~~~~~~~~~~~~~~~~~~

[Limebeer2006]_
  Limebeer and Sharp show a graph of steer torque for the benchmark bicycle model
  on page 47 for step inputs of steer torque that range from -0.5 to 2.5 Nm for
  extreme roll and steer angles.

[Sharp2007]_
  Robin Sharp uses a multi-degree of freedom motorcycle model and an LQR
  controller with preview to control a motorcycle moving at 30 m/s through a 4
  meter lane change and a 250 meter S-turn. For the lane change he gets torques
  ranging from about -20 Nm to 55 Nm for a more aggressive control and -4 to 6 Nm
  for less aggressive control. The S-turn gives torques from -40 Nm to 70 Nm with
  a sharp peak in torque in the middle of the S-turn.

[Sharp2007a]_
  Robin Sharp uses the benchmark bicycle model and an LQR controller with preview
  to follow a randomly generated path that has about 2 meter lateral deviations.
  The bicycle is traveling at 10 m/s and the steer torque ranges from about -15
  to 15 Nm. Medium control reduces the torques to under +/- 10 Nm. Straight line
  to circle path maneuvers show torques ranging from -0.5 to 0.5 Nm for loose
  controls and -2.5 to 2.5 for medium controls.

[Sharp2008a]_
  Robin Sharp used the benchmark bicycle model and an LQR controller with preview
  to make a bicycle track a 4 meter lane change at 6 m/s. During this manuever,
  the steer toque ranged from about -1 to 1 Nm. He also showed a very fine steer
  torque variation in the range of 0 to 0.0025 Nm about 10 meters before the
  start of the lane change.

[Peterson2009]_
  Peterson and Hubbard show the steady turning required steering torques for the
  benchmark bicycle on page 7. The torques for lean angles from 0 to 10 degrees
  and steer from 0 to 45 degrees are under 3 Nm.

Steer Torque From Experiments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[Cain2010]_
  Stephen Cain built an instrumented bicycle with a steer torque measuring device
  and studied steady turns.

[Weir1979a]_
  Weir et al. designed an instrumented motorcycle with a torque sensor. The range
  was +/- 70 Nm with 1% accuracy and\>10 Hz dynamic range. The crosstalk due to
  the other moments on the steer were removed with by utilizing two thrust
  bearings. It included stops to prevent sensor overload protection and weighed
  14 Newtons. They comment that the handlebars are significantly rigid for their
  purposes. It was a modular design set up for multiple motorcycles. They
  comment on the range being too large for small amplitude inputs used in
  steady turning and straight running and that more sensitivity would be
  needed to measure these accurately. Weir used this to measure steer torques
  for two motorcycles at various speeds (\>10 m/s) for steady turning and lane
  change maneuvers. The steady turning produced torques in the range of -10 to
  30 Nm and the lane change produced -20 to 55 Nm.

.. todo:: http://biosport.ucdavis.edu/research-projects/bicycle/instrumented-bicycle/steer-torque-measurement/weirSteerTorque.png

[Lorenzo1997]_
  David de Lorenzo instrumeted a bike to measure pedal forces, handlebar forces,
  hub forces to measure the in-plane structural loads. He took the bike to the
  trails and had 7 riders do a downhill section. The hand reactions were measured
  with a handlerbar sensitive to x (pointing forward and parallel to the ground)
  and z (pointing upwards, perpendicular to the ground) axis forces on both the
  left and right sides of the handlebar. Net torque about any vector in the fork
  plane of symmetry can be calculated from these. Figure 3d shows a plot of
  steering torque with maximums around 7 Nm. The stem extension torque
  (representing the torque from pushin down and up on the handlebars) reaches 15
  Nm. The calibration information leads me to believe that the crosstalk from the
  all of the forces and moments on the handlebars gives a very low accuracy for
  the reported torques, probably in the +/- 1 to 3 Nm range.

[Biral2003]_
  Biral et al. designed a custom steer torque measurement system using a
  cantilever beam. They don't specifically discuss the cross talk, but do mention
  that they use a half-bridge strain gauge. This design seems that it could be
  susceptible to cross talk from the forces applied to the handlebars by the
  rider. But they also report experimental values for torque that match model
  predictions very well. The measure torques from -20 to 20 Nm for a slalom
  maneuver at 13 m/s.

.. todo:: Biral's Steer Torque Design

[Astrom2005]_
  Åström et al. shows a steer torque measurement system constructed for the UCSB
  instrumented bicycle but with little extra information. They use a linear force
  transducer of some sort mounted on the handlebars.

.. todo:: UCSB Steer Torque Measurement

[Cheng2003]_
  This is a report about a design project at UCSB to develop and implement a
  steer torque measurement device (same one shown the Åström paper). He gives a
  pretty bad anedoctal introduction to bicycle dynamics, but the experiments and
  measurements seem to be one of a kind. They did some basic experiments by
  attaching a torque wrench to a bicycle and made left at right turns at speeds
  from 0 to 13 m/s (0 to 30mph). The torques were under 5Nm except for the 13 m/s
  trial which read about 20 Nm. They designed a pretty nice compac torque
  measurement setup by mounting the handlebars on bearings and using a linear
  force transducer to connect the handlbars to the steer tube which reduced the
  effects of other moments and forces acting on the steer tube. The use of
  bearings and rodends may be questionable as there is bearing friction and slop.
  Furthermore, downward forces on the handlebars could possibly still be
  transmitted to the load cell. The design does allow one to choose the lever arm
  for the load cell, thus giving some choice to amplify the force signal. They
  set it up to measure from 0 to 84 Nm with a Model SM Series S-type load cell
  from Interface with a 670 Newton range. They used a transducer amplifier also
  for signal conditioning. There are several sections on calibration, with some
  description of the use of pulleys and cables to apply a torque to the
  handlebars. They measured the torque during two different manuever types: a
  sharp turn at various angles and steady turns on various diameter circles both
  at 10mph (4.5 meters/second). The rider maintained constant speed through
  visual feedback of a speedometer. He talks of very noisy measurements and
  filters the noise by some type of moving average. He does not identify an
  countersteering. He claims the rider turns the handle bars right to initiate a
  right turn. There seems to be no counter-torque in the data for turns. For the
  sharp turns the highest reported torque is about 10 Nm, for the steady turning
  he reports the highest average torque as 1 Nm.

Design
------

Initial Design Ideas
~~~~~~~~~~~~~~~~~~~~

We are planning on measuring the steer torque the rider applies to control a
bicycle. This will be used for human control model identification and for use
in the necessary feedback loops required control the riderless bicycle.
Measuring the steer torque is not trivial. This is because various models
predict torques ranging in the 0-2 Nm (0-1.5 ft lbs) range with signal
variations and reversals requiring +/- 0.01 Nm (0.01 ft lbs) in measurement
accuracy. The range and accuracy are easily measured with modern torque
sensors, but the fact that large moments can be applied to the fork and
handlebars by the ground and/or rider introduces the problem of crosstalk. The
forces and moments applied to the fork will corrupt the relatively small torque
measurements as they can be hundreds of times larger in magnitude. With this in
mind, we are trying to come up with a way to isolate the torque measurement to
eliminate or minimize the crosstalk and get good, noiseless, accurate readings.
The following are some basic designs we are working with:

Åström Design
  This is a sketch of what was designed for the UCSB instrumented bicycle and
  presented in a `2005 paper by Karl Åström et al`.
  It uses an off-the-shelf axial load cell mounted between a floating handlebar
  and a bar extending from the steer tube. This seems to be a good design, but
  it would be nice to eliminate the handlebar bearings and the rod ends.

.. todo:: Astrom Design

Landman Design
  My professor, `Drew Landman
  <http://eng.odu.edu/aerospace/aefaculty/dlandman.shtml>`_ , from Virginia who I
  worked with designed force balances for wind tunnel testing at the `LFST
  <http://www.nasa.gov/vision/earth/improvingflight/fst_overview.html>`_
  suggested a `redesign that eliminates the bearings and replaces them with
  flexures` .

Weir Design
  David Weir designed a motorcycle steer torque measurement system in his `1979
  technical repor` t that also floats the handlebars
  on bearings but uses an off-the-shelf torque sensor instead. The sketch shows
  the basic concept. The handlebars are floating on bearings and the torque
  sensor connects the handlebars to the steer tube. He claimed that the design
  lacked low range resolution. Motorcycles can experience torques that are as
  high as 50 Nm according to some models.

.. todo:: Weir Design

Internal Stem Design
  This is a design that we came up with when preparing our abstract on the topic.
  It is fundamentally the same as the Åström design but includes flexure elements
  instead of rod ends and is a bit smaller in scale.

.. todo:: Internal Stem Design

.. todo:: steerTorque.png

Double Steer Design
  This design separates the handlebar and stem's rotation axis from the steer
  tube and fork's rotation axis much the way many long wheel base recumbents or
  bakfiets are designed. The load cell is then place on the connecting rod. This
  design is is prone to slop in the steer mechanism.

.. todo:: Double Steer Design

Bearing-less design
  Luke came up with this design and was able to eliminate the need for bearings.
  Two arms are clamped to the steer tube and a load cell is placed between the
  arms. The difference in this is that not all of the torque is transferred
  through the load cell, but maybe enough is that we can measure it.

.. todo:: Bearing-less Design

Forces on the steer tube
~~~~~~~~~~~~~~~~~~~~~~~~

Ideally, we'd like to slap a strain gauge on the steer tube to measure the
shear strain and get a good torque reading but this isn't so easily done. The
bicycle steer tube has various other forces acting on it. For the most basic
case a the ground contact force at the front wheel puts the fork into bending
and compression. Likewise the person can apply forces to the handlbars which
also put the steer tube into bending and compression. It turns out that the
moments in the steer tube can be as high as 200 times the steer torques we are
trying to measure.

.. todo:: Basic Bicycle Forces

There are ways to apply strain gauges to a bar in torsion that would
theorectically cancel all of the axial and bending strain components. Both
bending moments and axial forces only create strain in the axial direction and
shear and torsion create strain in the direction normal to axial. The following
comes from Beckwith and Margoni's Mechanical Measurements and shows two
possible strain gage bridge configurations that can reduce or eliminate strains
not due to torsion.

.. todo:: Strain Bridge Configuration for Torsion

L seems to be a good choice for the steer torque measurement, but in reality it
is impossible to align strain gages perfectly. This can introduce
cross-sensitivity or cross talk. If the cross talk strains due to the bending
moments are only 1% of the of the total strain due to the moments, that can
still corrupt the steer torque measurement. With this in mind we decided to
look into what the forces in the steer tube actually look like.

We modeled the fork as a basic beam supported by the headset bearings (points
C and D) and the forces/moments due to the ground reaction force and force
applied to the handlebars were calculated.

.. todo:: Fork Modeled as a Beam

The following graphs show what the shear and bending moment diagrams for
various loadings look like both from the side and the front of the bike.

.. todo:: mvdiagram01.png
.. todo:: mvdiagram02.png
.. todo:: mvdiagram03.png
.. todo:: mvdiagram04.png
.. todo:: mvdiagram05.png
.. todo:: mvdiagram06.png

These graphs show that the bending moments and shear stresses can be of much
larger magnitude than the steer torques, so cross talk is a major concern.
These graphs also show that it if no loads are placed on the handlebars the
entire portion of the steer tube/stem above the headset has no bending moments
and no shear stress. This is the ideal place for a torque sensor, if we can
eliminate the transfer of forces applied to the handlebars to the steer tube.

This leads us to a design idea that isolates the steer torque sensor from the
handlebar and fork forces. The basic design idea is sketched below. It includes
a separate "headset" for the handlebars that take up any handlebar forces. The
handlebar is connected to the steer torque sensor via a zero backlash universal
joint so no moments can be transferred to the sensor. The steer motor will need
to be mounted above the u-joint so torques from the rider or the motor can be
measured. We are looking at a `Futek <http://www.futek.com/>`_ Reaction Torque
sensor that has a max torque of either `6 Nm
<http://www.futek.com/product.aspx?stock=FSH02594>`_ or `12 Nm
<http://www.futek.com/product.aspx?stock=FSH02595>`_ but are unsure what the
best range and accuracy for these measurements are since there seems to be no
public data from bicycle steer torque measurements.


.. todo:: Torque Measurement Design

Torque Wrench Experiments
~~~~~~~~~~~~~~~~~~~~~~~~~

Following Cheng's lead, we decided to do some experiments with a accurate
torque wrench to see get an idea of maximum torques. We made a little
attachment to the steer tube that allowed easy connection of various torque
wrenches. A helmet camera was mounted such that it could view the torque
wrench, handlebars and speedometer relative to the bicycle frame. The torque
wrench had a range from 0 to 8.5 Nm and a +/- 2% accuracy of full scale (+/-
0.17 Nm). The speed was maintained by an electric hub motor (i.e. no pedaling).

.. todo:: Torque wrench mount

.. todo:: Torque wrench face

.. todo:: Torque camera

The `data file` includes the run
number that corresponds to the video number, the rider's estimate of the speed
after the run in miles per hour, the maximum reading from the torque needle
after the run in inch-lbs, the rider's name, the maneuver, the minimum speed
seen on the video footage in miles per hour, the maximum speed seen on the
video footage in miles per hour, the maximum torque seen on the video footage
in inch-lbs, the minimum torque seen on the video footage in newton-meters, and
the rotation sense for each run (+ for clockwise [right turn] and - for counter
clockwise [left turn]) . There were seven different maneuvers: straight into
tracking a half circle (radius = 6 meters and 10 meters), tracking a straight
line, straight to a 2 meter lane change, slalom with 3 meter spacing, steady
circle tracking (radius = 5 and 10 meters). All of the videos and data can be
downloaded `here
<http://www.archive.org/details/BicycleSteerTorqueExperiment01>`_ . The results
( `R code` ), are shown in the
following graphs:

.. todo:: torqueHist.png

.. todo:: torqueSpeed.png

.. todo:: Circle5.png

.. todo:: Circle10.png

.. todo:: HalfCircle6.png

.. todo:: HalfCircle10.png

.. todo:: LaneChange.png

.. todo:: LineTrack.png

.. todo:: Slalom.png

The primary goal was to determine the maximum torques we will see for the types
of maneuvers we are interested in. The histograms shows that we never recorded
any torques higher than 5 Nm. The following shows the max and min torque values
for different maneuvers:

ManeuverMax Torque

Min Torque

Steady Circle (r = 10m)

3.4

-2.4

Steady Circle (r = 5m)

2.4

-2.2

Half Circle (r = 10m)

3.8

-3.2

Half Circle (r = 6m)

3.4

-5.0

Lane Change (2m)

2.9

-2.6

Line Tracking

2.6

-3.4

Slalom

4.5

-4.8

There seems to be little to no speed dependency on the max and min torque values.

Final Steer Assembly Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: Final Steer Torque Measurement Design

Steer Dynamics
--------------

The final design was setup to eliminate measuring anything but the torque in
the steer tube along the steer axis, but this measured torque, :math:`T_M`,
does not equal the input torque typically used for out bicycle models, (i.e.
:math:`T_\delta`).  But there is a relationship from :math:`T_M` to
:math:`T_\delta` that requires one to know, at a minimum[#]_ the friction in
the lower and upper bearings (this is potentially both viscous and coulomb) and
the inertia of the handlebar/fork assembly above and below the torque sensor at
a minimum.

We measure the torque in the steering column, :math:`T_M`, from a sensor that
is mounted between both the handlebars and fork steer tube and two sets of
bearings: the headset and the slip clutch bearings. We are interested in
knowing the torque applied about the steer axis by the rider's contact forces
to the handlebars, :math:`T_\delta`. It turns out that this is a function of
much of the data measured on the bicycle.

A free body diagram can be drawn of the upper portion of the handlebar/fork
assembly, where the lower portion is cut at the steer torque sensor. The
torques acting on the handlebar about the steer axis are the measured torque,
:math:`T_M`, the rider applied steer torque, :math:`T_\delta`, and the
friction from the upper bearing set which can be described by coulomb,
:math:`T_F`, and viscous friction, :math:`T_V`.

The coulomb friction can be described as a piecewise function:

.. math::
   :label: coulomb

   T_F = F\operatorname{sgn}(\dot\delta) = \left\{
   \begin{array}{rl}
     F & \textrm{if $\dot{\delta}>0$}\\
     0 & \textrm{if $\dot{\delta}=0$}\\
     -F & \textrm{if $\dot{\delta}<0$}\\
   \end{array}
   \right.

and viscous friction as a function linear in the steer rate:

.. math::
   :label: viscous

   T_V = c\dot{\delta}

where :math:`F` is the coulomb friction force and :math:`c` is the viscous
damping coefficient.

We measure the angular rate of the bicycle frame, :math:`B`, with three rate
gyros:

.. math::
   :label: framerate

   ^N\bar{\omega}^B = w_{b1}\hat{b}_1 + w_{b2}\hat{b}_2 + w_{b3}\hat{b}_3

The handlebar, :math:`H`, is connected to the bicycle frame, :math:`B`, by a
revolute joint that rotates through the steering angle, :math:`\delta`, and we
measure the angular rate of the handlebar about the steer axis directly with a
rate gyro. The angular rate of the handlebar can be written as follows:

.. math::
   :label: handlebarrate

   ^N\bar{\omega}^H = (w_{b1}\cos(\delta) + w_{b2}\sin(\delta))\hat{h}_1
   + (-w_{b1}\sin(\delta) + w_{b2}\cos(\delta))\hat{h}_2 + w_{h3}\hat{h}_3

The steer rate, :math:`\dot{\delta}`, can be computed by subtracting the
angular rate of the bicycle frame about the steer axis from the angular rate of
the handlebar/fork about the steer axis.

.. math::
   :label: steerrate

   \dot{\delta} = w_{h3} - w_{b3}

We measure the acceleration of a point, :math:`v`, on the bicycle frame.

.. math::
   :label: accelerationOfV

   ^N\bar{a}^v = a_{v1}\hat{b}_1 + a_{v2}\hat{b}_2 + a_{v3}\hat{b}_3

We also know the location of a point on the steer axis, :math:`s`, relative to point
:math:`v`.

.. math::
   :label: locationOfV

   \bar{r}^{s/v} = d_{s1}\hat{b}_1 + d_{s3}\hat{b}_3

The location of the center of mass of the handlebar, :math:`h_o`, is also known
relative to point :math:`s`.

.. math::
   :label: locationOfHo

   \bar{r}^{h_o/s} = d\hat{h}_1

:math:`^N\bar{a}^{h_o}` can be calculated using the two point thereom for
acceleration [Kane1985]_ twice staring at the point :math:`v`:

.. math::
   ^N\bar{a}^s = ^N\bar{a}^v + ^N\dot{\bar{\omega}}^B\times\bar{r}^{s/v} +
   ^N\bar{\omega}^B\times(^N\bar{\omega}^B\times\bar{r}^{s/v})

.. math::
   ^N\bar{a}^{h_o} = ^N\bar{a}^s + ^N\dot{\bar{\omega}}^H\times\bar{r}^{h_o/s} +
   ^N\bar{\omega}^H\times(^N\bar{\omega}^H\times\bar{r}^{h_o/s})

The angular momentum of the handlebar about its center of mass is:

.. math:: ^N\bar{H}^{H/h_o} = I^{H/h_o} \cdot ^N\bar{\omega}^H

where :math:`I^{H/h_o}` is the inertia dyadic with reference to the center of mass
which exhibits symmetry about the :math:`13`-plane.

The dynamic equations of motion of the handlebar can be written as the sum of
the torques on the handlebar about point :math:`s` is equal to the derivative
of the angular momentum of :math:`H` in :math:`N` about :math:`h_o` plus the
cross product of the vector from :math:`s` to :math:`h_o` with the mass times
the acceleration of :math:`h_o` in :math:`N`:

.. math::
   \sum \bar{T}^{H/s} = ^N\dot{\bar{H}}^{H/h_o} + \bar{r}^{h_o/s} \times m_H ^N\bar{a}^{ho}

The only torques applied to the handlebar that we are interested in act about the steer axis.

.. math:: \sum T^{H/s}_3 = T_\delta - T_F - T_M - T_V

Looking at only the 3 component of the equation of motion gives the following
relationship:

.. math::
   T_\delta - F\operatorname{sgn}({\dot{\delta}}) - T_M - c(w_{h3} - w_{b3}) = (^N\dot{\bar{H}}^{H/h_o} + ^s\bar{r}^h_o \times m_H
   ^N\bar{a}^s) \cdot \hat{h}_3

And :math:`T_\delta` can be solved for:

.. todo:: the following equation is giving errors in the latex document

.. math::

   \begin{align}
   T_{\delta} = &
   I_{H33} \dot{w}_{h3} + \\\notag
   & (I_{H11} (w_{b1}\cos(\delta) +
   w_{b2}\sin(\delta)) +
   I_{H31} w_{h3}) (-w_{b1}\sin(\delta) +
   w_{b2}\cos(\delta)) + \\\notag
   & I_{H22} (- w_{b1} \sin(\delta) +
   w_{b2}\cos(\delta))
   (w_{b1}\cos(\delta) +
   w_{b2}\sin(\delta)) + \\\notag
   & I_{H31} (- (- w_{b3} + w_{h3}) w_{b1}
   \sin(\delta) +
   (-w_{b3} + w_{h3})
   w_{b2}\cos(\delta) +
   \sin(\delta)\dot{w}_{b2} +
   \cos(\delta)\dot{w}_{b1}) +\\\notag
   & d m_H (d (-w_{b1}\sin(\delta) + w_{b2}
   \cos(\delta))(w_{b1}\cos(\delta) +
   w_{b2}\sin(\delta)) +
   d \dot{w}_{h3}) - \\\notag
   & d m_H (- d_{s1} w_{b2}^{2} + d_{s2}
   \dot{w}_{b2} - (d_{s1}
   w_{b3} - d_{s2}
   w_{b1}) w_{b3} +
   a_{v1})
   \sin(\delta) +\\\notag
   & d m_H(d_{s1} w_{b1}w_{b2} +
   d_{s1} \dot{w}_{b3} +
   d_{s2} w_{b2} w_{b3} - d_{s2} \dot{w}_{b1} +
   a_{v2})\cos(\delta) - \\\notag
   & c (- w_{b3} + w_{h3}) + T_F + T_s
   \end{align}

Experiments
~~~~~~~~~~~

The first thing we did was to try to characterize the friction in the bearings.
We did this by mounting the bicycle frame such that the steer axis was
vertical, the wheel was off the ground, and the bicycle frame was made very
rigid. Secondly, we attached two springs to the handlebars such that the force
from the springs acted on a lever arm relative to the steer axis. This allowed
us to perturb the handlebars and let the vibrations damp out. We recorded data
from the steer potentiometer, steer rate gyro and the torque sensor during
these perturbations. For now, we simply used the steer angle signals to
estimate both the viscous and coulomb friction from the two bearing sets.


.. [#] The elasticity of the steer column may also be a factor.
