.. _systemidentification:

=====================
System Identification
=====================

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

Outline
=======

* Preface
* Introduction
* Literature review

  * Passive model identification
  * Rider control model identification

* Experimental Description
  * Answer question about whether bicycle dynamics are same on and off
    treadmill
* Data Description

  * Processing methods

* Parameter identification versus model identification

  * Identifiability

* Identification model structures

  * Black Box

    * Basic
    * State Space
    * Canonical Form

  * Grey Box

    * Structured State Space
    * Structured Canonical Form
    * Parameterized State Space

* Passive Model Identification

  * Black box ID

    * SISO (ARX, ARMAX, State Space)
    * System order

  * Grey box ID

    * Talk some about the identifiability of individual parameters.

  * Structured State Space ID

    * Coefficient plots

  * Canonical Form ID

    * Comparison of derived models with respect to rider and environment
    * Quality of models with respect to variance explained by the data

  * Comparison of identified models to first principle models

    * Structured state space per run
    * Regression results of general model
    * Benchmark canonical form identification for sets of runs

* Rider Controller identification

  * Grey box identification of the 7 parameter control model

    * Lateral deviation loop
    * Heading loop

  * Data set
  * System id process
  * Resulting parameters
  * Frequency response

    * Crossover frequencies

  * Compare to Ron's method

* Discussion of results
* Conclusion

Preface
=======

I started to think about system identification when I arrived at Delft and the
discussions began with Arend and Jodi. I hadn't much clue about the formal
field and theory of system identification. My first look at it was when Arend
presented me with a light introduction by Ljung, and I credit Arend and his
cohorts for the ideas. We talked about it here and there but never really put
together a solid experimental plan to do anything about it. Karl Astrom visited
us in Delft in late 2008 and we talked some with him about ideas. I mainly
recall him focusing on how to excite the system in a very controlled manner with
an oscillating mass on the bicycle. Some of these ideas propagated through Arend
to Peter and can be seen in the final sections of his thesis [Lange2011]_. Many
of these ideas influenced our NSF proposal and ultimately the final portion of
what I was to do for my dissertation work.

Once I had gotten back to Davis we now had the resources available from NSF
funding to make something happen. My goal had basically formalized into
creating a instrumented bicycle to be controlled by person that was capable of
measuring all of the kinematics and kinetics involved seen in regulated control
tasks. We also originally had hoped to be able to vary the dynamics of the
bicycle, but the reduced funding nixed that idea. It took some time into the
project to really understand what we may be able to accomplish with that but it
finally materialized into validating Ron's theoretic control model which is
discussed in Chapter :ref:`control` with data collected via the instrumented
bicycle. After our first experiments, over a year into the project timeline it
became apparent that simple tasks with measured lateral perturbations would
provide the best chance of us validating his model. Unfortunately, I had not
thought a great deal about how to provide and measure these lateral
perturbations but the manually excited perturbations seemed to to trick.

We ran a lot of preliminary system identification analyses on the first set of
trial data, but it quickly became apparent that we had little understanding in
the subject. The early analyses did give confidence that data was of good
enough quality to do something with, but our goal of identifying the parameter
of the controller were still far from our reach.

We performed the final set of experiments around August and September of 2011
to get a large sample of data for the final analyses. The NSF grant was to end
at the end of September and I still had to figure out how to analyze all of
the data, not to mention write up a ton of work for my dissertation. We ended
up extending the NSF grant another year (as seems to be typical with these
things). I look back to our original proposal and in hindsight the scope was
way too large (accurately predicted by Arend). We nixed the handling qualities
parts when the funding was lowered, but I now see that what we intended to do
really took another 6-12 months than we had intended.

The final analyses has forced me to figure out what system identification is all
about and I've learned a great deal rapidly and much on my own. At this stage
we weren't able to find any local experts on the subject to help us along but
I've gotten some great insight from both the single track vehicle dynamics
email list and in particular from personal communication with Karl Astrom. I
still feel very weak in the subject but it is more clear how difficult
identifying complex systems is, especially trying to identify physical
parameters.

As many doctoral students probably hope when starting their long trek to the
PhD, I hoped for some grand findings to arise from this work. But I've been
humbled a lot in that quest. I present here the work I've done with regards to
identifying the bicycle and rider system with what I think are pretty good
results, but I hope that it is more of guide for others to see some of the
difficulties in executing this kind of analyses with some ideas to better
structure it.

Introduction
============

The work presented in this Chapter is intended to be the icing on the cake that
takes into account all of the theory presented in the previous chapters and
evaluates it with a large set of data taken with the instrumented bicycle
described in Chapter :ref:`davisbicycle`. It is also the overarching
deliverable I was responsible for under the NSF grant. This chapter details
system identification of a bicycle and rider system. It is broken in two main
parts, the first's goal being to identify the passive bicycle rider system and
the second to identify the active portion, i.e. the rider's control system. The
literature review gives an introduction to other's efforts in both these
analyses with respect to single track vehicles.

Literature
==========

There is a rich history of bicycle and motorcycle mathematical model
development. This has been able to explain many of the more dynamically
fascinating phenomena from countersteering and stability to speedman’s wobble
and gyroscopic effects. But the amount of experimental validation of these
idealized models pales in comparison, with the motorcycle experimentation
outdistancing that done with bicycles.

Basic bicycle and motorcycle identification is typically done on data collected
by exciting the vehicle through either force/torque perturbations in roll or
steer. These experiments can be done when the bicycle is under closed loop
control or when the bicycle is stable, the former being a requirement for
speeds outside of the stable speed range. But, the mode excitation methods are
limited to the frequency band around that mode of motion. Manual excitation
under closed loop control gives better excitation bandwidth and a pairing with
modern system identification techniques can provide richer models.

Passive Vehicle and Rider Identification
----------------------------------------

Identification of the passive vehicle rider models are more numerous than the
controller identification. It is indeed a requirement to have a very good
vehicle model before attempting to identify the control system a human employs
while controlling the system. The bicycle and motorcycle are excellent choices
for manual control experiment design due to the fact that they are relatively
economical systems that require a broad range of human control skills to
stabilize and direct the vehicle, but they have the disadvantage that the first
principles models may not be very robust predictors of the motion due as a
simpler or more well studied system. The approaches to identifying the passive
model include mode excitation techniques to system identification under more
general inputs.

.. todo:: What about Dohring. He took measurements of a motorcycle and did
   something. Maybe I should review it. I forget his conclusions.

CALSPAN
~~~~~~~

The earliest comprehensive bicycle model validation began at CALSPAN in the
late 60’s . This included several revolutionary studies, in one of which they
made use of a rocket to apply know step torques to an uncontrolled riderless
bicycle. In another, simulations of slalom maneuvers were visually compared
with video footage.

.. todo:: read over notes for these papers, I'm sure there is a little more
   worth saying.

Eaton
~~~~~

David Eaton's work ([Eaton1973]_, [Eaton1973a]_, [Eaton1973b]_) may be the
closest example to the work presented in this chapter. He did his PhD work at
the University of Michigan under the Highway Safety Research Institute.  His
dissertation focused on the experimental validation of the motorcycle modeling
work of [Sharp1971]_ and the human controller modeling work of [Weir1972]_. He
did this with two sets of experiments 1) identification of the uncontrolled
dynamics of the motorcycle under perturbations and 2) identification of the
rider controller during roll stabilization tasks, the latter of which will be
discussed in the next section.

His initial experiments were aimed at validating and identifying the passive
motorcycle system. During these experiments, his subjects road a motorcycle
with their bodies rigidly braced to the frame and hands-free at speeds of 15,
30, and 45 mph (6.7, 13.4, and 20.1 m/s) along side a pace car which recorded
the output from roll angle, roll rate and steer angle sensors. The brace and
open loop response allowed rigid rider modeling assumptions to be used.
Weights were dropped from one side of the motorcycle to induce a step roll
torque and the rider used a single pulse in steering torque to the handlebars
to right the motorcycle in roll after the drop. These experiments were
impressively dangerous and would be hard pressed for approval by the
Institutional Review Board if done today, but well controlled for the typical
modeling assumptions. The resulting time histories of the measured system
outputs were compared to simulations of Sharp's model [Sharp1971]_ augmented
with a variety of tire models of Eaton's design. He found good agreement
between the experiments and the models for higher speeds, but felt that a more
robust tire model was needed to predict the wobble mode in slower speed runs.

The second set of experiments were more tame. The three riders simply balanced
the motorcycle on a straight path at two speeds, 15 mph and 30 mph, for a total
of 38 runs. He added a steer torque transducer bar above the handlebars. The
rider controlled the motorcycle with one hand and the rider applied torque was
recorded along with the other signals. No perturbations were necessary, as the
rider's natural control actions excited the system in a wide enough bandwidth.
From this data he was able to identify the motorcycle steer torque to roll
angle transfer function through the spectral densities of the measured signals
(by dividing the cross spectrum of the roll angle and steer torque signal by
the power spectrum of the steer torque). The identified transfer functions show
good agreement with the augmented Sharp motorcycle model at the 30 mph speeds,
less so for the 15 mph runs.

His generated frequency responses from the second experiments provided an
empirical model, while the simulation comparisons from the first experiments
were validation rather than identification.

Aoki
~~~~

[Aoki1979]_

.. todo:: James2002 cites this study. He does experiments with a motorcycle.

Weir, Zellner, Teper
~~~~~~~~~~~~~~~~~~~~

Weir, Zellner, and Teper performed an extensive experimental study on
motorcycle handling qualities for the U.S. National Highway Traffic Safety
Adminstration in the late 70's, [Weir1979a]_. This was a follow up to both the
CALSPAN studies and [Taguchi1975]_ both under or related to the same
administration. There is litte to no explicit system identification in the
study but some important elements are there. In terms of the passive model
identification they present steady state comparisons of their experimental data
to their models with varying degrees of qualitative agreement and generally
good ability to predict the conditions at which sign reversals in torque are
needed to maintain a steady turn. They also compare single lane change
simluations of a controlled vehicle to their measured data by visual
inspection. They unfortunately admit that adjusting the first principles models
to better fit their measured data was outside the scope of the project.  But
this gives some early examples of model evaluation with respect to good quality
data.

James
~~~~~

Stephen James published a study in 2002 [James2002]_ in which he attempted to
identify the linear dynamics of an off-road motorcycle. He measured steering
torque, steer angle, speed, roll rate and yaw rate while his subjects manually
exciting the vehicle through steer torque during runs at various speeds on a
straight single lane road. He made use of black box ARX SIMO identification
routines of 6th and 7th order (his and others motorcycles models are usually
10th+ order) to tease out the weave and wobble eigenvalues. He compares the
identified eigenvalues, eigenvectors and frequency responses to his motorcycle
model and claims good fits based on visual interpretation of the plots. The
agreement is questionable due to the lack of statistics in the model
comparisons and little validation of his first principles model which assumes a
rigid rider. The study does show that there is the possibility of
identification of multiple modes of motion with simple manual excitation of the
handlebars.

Biral et al.
~~~~~~~~~~~~

[Biral2003]_ performed a nice study to identify the motorcycle dynamics under
an oscillatory steer torque input. They measured steer torque, roll rate, steer
angle and yaw rate with an instrumented motorcycle. They performed slalom
maneuvers at speeds from 2 to 30 m/s at three sets of cone spacings in the
slalom course. The resulting time histories were close to ideal sinusoids. They
used curve fitting to find amplitude and phase relationships among the measured
signals. The results were plotted on Bode plots for comparison to the frequency
response of several first principles models. The models predict the
experimental data and their motorcycle model is shown to do a better job than
other models from literature. This claim is only based on visual inspection.  I
would say this technique and others like it are more of an ad hoc method of
system identification of the vehicle dynamics because they rely heavily on very
specific input and output characteristics, but never-the-less seems to be
effective. Making use of formal system identification techniques could
potentially give more reliable results and the ability to better characterize
the uncertainty in the predictions.

Kooijman
~~~~~~~~

Jodi Kooijman has worked on experimental validation of the benchmark bicycle
[Meijaard2007]_ linear equations of motion for a riderless bicycle
[Kooijman2006]_, [Kooijman2008]_, [Kooijman2009]_. His instrumented bicycle
measured the steer angle, forward speed, roll rate, and yaw rate. Due to the
fact that the bicycle can be stable at certain speeds he was able to launch the
bicycle in and around the stable speed range and perturb the bicycle with a
lateral unmeasured impulse and record the stable decay in the steer, roll and
yaw rates. The post perturbation time histories of the measured signals
provided nice decaying oscillations and curves could be fit to find both the
time constant and frequency of oscillation. These were then compared to the
predicted weave response based on the first principle model numerically
populated with measured physical parameters of the bicycle. He found good
prediction abilities of the weave mode between 4 and 6 m/s. The "goodness" of
fit were gaged by visual inspection with no uncertainty estimates in the models
or the results from the dynamic measurements. The method was not able to
predict the heavily damped caster mode nor the capsize mode. He also
demonstrated that the measured dynamics were the same when the experiments were
performed on a treadmill.

In [Kooijman2011]_, Jodi constructed a bicycle with very unusual physical
characteristics including negative trail and canceled angular momentum of the
wheels. He performed similar experiments as his Master's thesis work. They show
the comparison of a stable single experiment in which the yaw and roll rates
were measured and compared it to the predictions of the benchmark bicycle.

[Stevens2009]_ and [Escolana2011]_ both perform experiments similar to
Kooijman's with similar results, although Steven's results vary in the ability
of the model to predict the data for various configurations of his adjustable
bicycle.

These also fall into the ad hoc system identification techniques that take
advantage of very the stability at certain speeds and very specific output
characteristics. The variability in reproducibility in the studies from other
researchers should be noted.

Chen and Doa
~~~~~~~~~~~~

[Chen2010]_ develop a first principles non-linear bicycle model with a fuzzy
controller and use it to generate stable simulations for various speeds. He
then does an output error grey box identification on the resulting data with
respect to the non-zero and non-unity entries of the state, input and output
matrices (i.e.  just the entries of the acceleration equations). The
identification is done for a discrete number of speeds in the range 1 to 15
m/s. The eigenvalues are calculated of the resulting identified speed dependent
A matrices and the root loci plotted versus speed.

The resulting eigenvalues seem to behave like the benchmark bicycle but the
capsize mode is shown to go unstable briefly at a speed lower than the stable
speed range. They did not attempt to characterize or identify the process noise
even though they generated the data with a known model with known input noise.
Also their non-linear bicycle equations of motion [Chen2006]_ were never
validated against any other accepted models. Both of these can explain the
discrepancies in their identification. Their identification procedure does show
that it may be possible to get good estimates of a linear model of the vehicle
alone from noisy data regardless of the controller which stabilizes the
vehicle.

Doria
~~~~~

In [Doria2012]_ experiments are performed where a motorcycle rider excites the
steering with a pulse and lets the motorcycle oscillate while the rider keeps
his hands on the handlebars (as opposed to Eaton's hands-free experiments). The
resulting dynamical measurements are nice decaying sinusoidal-like motions of
which the authors fit ideal curves to the data. They identify the time
constants, frequency and phase information to construct the eigenvalues and
eigenvectors of the excited mode. The empirically derived eigenvectors show
some resemblance to the model's predictions.

Controller Identification
-------------------------

van Lunteren and Stassen
~~~~~~~~~~~~~~~~~~~~~~~~

At Delft University of Technology in the Man-Machines research group, Drs. van
Lunteren and Stassen began work in 1962 to identify the human controller for a
normal population of subjects and report on their work into the early 70's
([Lunteren1967]_, [Lunteren1969]_, [Stassen1969]_, [Lunteren1970]_,
[Lunteren1970a]_, [Lunteren1970b]_, [Luntern1973]_, [Stassen1973]_). They chose
a bicycle simulator as the plant because it was a common task that average
people could do and their studies could focus on a wider population of
individuals as compared to most previous work based around trained pilots. The
bicycle simulator did not capture all of the essential dynamics of a real
bicycle as it's operation was based on only the simplified roll dynamics of
Whipple's model, but nonetheless offered a similarly complex roll stabilization
control task as a normal bicycle would do. The simulator was controlled by both
the steering angle and the rider's lean angle, both of which are questionable
inputs as have been pointed out as early as [Roland1972]_.

They assumed the rider's control actions can be described by a PID controller
with time delays on each feedback variable and mention that this controller was
chosen instead of a McRuer style controller primarily due to limitations of
their computational equipment. The error in the roll angle is fed into two PID
controllers each with a time delay: one to output the corrective steer angle
and the other to output the corrective lean angle. They introduce a remnant
term for each control action and the external disturbances to the bicycle
model.

The identification goal was to find the six gains and two times delays in which
the controller performed as a human would. The preferred method was a real time
estimation routine due to the speed of computations and reasonable agreement
their correlation method. The results indicated that the subjects used no
integral control (i.e. only position and rate feedback). They could identify
within a bandwidth of about 2 Hz and noticed that when the system was
undisturbed their was a 0.5 Hz dominant frequency in the rider's control
actions. The rate feedback was more dominant in generating the lean control
input than it was for the steer control input. Also, they found the time delay
for lean to be larger than the steer time delay and postulate that the steer
action is a result of cerebral activity while the lean is more of reflex
pattern. Another finding resulting from analysis of Nyquist plots of different
rider's identified control actions showed that riders chose different control
actions. They attribute this to the roll stabilization being a sub-critical
task (i.e. a more difficult task may force different riders to adopt similar
control behavior). They also investigated the effects of drugs, such as
alcohol, to the riders control behavior. They found correlations from drug dose
to time delays and the error in the control actions. Their later studies
introduced better identification methods and they found discrepancies in the
identified time delays of the later work as compared to the newer work. For
example, the steer control time delay was originally found to be around 1.5
seconds and the improved methods found the delay to be around 0.7 seconds, and
the discrepancy attributed to the bias due to remnant in their early work. They
also introduced a visual tracking task into the simulator but had difficulties
in getting reliable transfer function identification as compared to the roll
stabilization transfer functions which improved in quality due to longer trials
of 35 minutes.

The methods developed in their studies are great and thorough examples of early
parameter identification in human control tasks. The simpler plant dynamics
were most likely beneficial at reducing the uncertainty in the identified
parameters, but the choice of angles as inputs instead forces of torques may
not be a realistic enough model of the human's actuation control response and
actuation.

Eaton
~~~~~

After feeling confident in his motorcycle identification results, Eaton made
use of the Wingrove-Edwards method in tandem with an impulse identification to
identify the human controller. The remnant element was large with respect to
the torque that was linearly correlated with the roll angle, but the human
control element was identified with a simple gain and time delay for most of
the high speed runs. The time delay identification of about 0.3 seconds was
very repeatable across all runs. Furthermore, he demonstrated that the
crossover model was evident in the resulting closed loop rider-motorcycle
transfer functions.

Eaton is one of very few who have identified the rider controller during actual
single track vehicle tests with confidence in the underlying passive
rider-vehicle model. This study has influenced the work in the Chapter in many
ways.

Doyle
~~~~~

A recently uncovered study on the manual control of a bicycle from a
psychologist's perspective has some very non-traditional techniques and
outlooks to the understanding of the control system employed while balancing a
bicycle [Doyle1987]_. Anthony Dolye's paper [Doyle1988]_ on his thesis topic
opens with "The old saw says that once learned it is never forgotten, but what
exactly is learned has been by no means clear." This reflection points to the
great complexity behind balancing a bicycle, such an easily gained skill. He
chooses to study the bicycle over a simpler task partially due to the fact that
the rider has little freedom in effective control strategies and partially
because it is a skill many people can do.

His goal was to determine how much of the rider's control actions can be
accounted for without involving higher cerebral functions. He mentions the Weir
and Zellner work and the fact that its focus is on  motorcycles at high speed,
and questions whether the control employed for their system is simply a
different version of the one employed on a bicycle at low speed or whether they
are different control methodologies all together.

He was aware of the inherent stability that bicycles can provide and constructs
an instrumented bicycle where the head angle, trail, and front wheel gyro
effects are eliminated so that "all steer movements are a result of the human's
control". He also mentions, but doesn't use, a body brace to eliminate
unnecessary body movements and he blindfolds his subjects so that their sensory
information is limited to proprioception and vestibular cues. He mentions the
arm and upper body movements and how it is difficult to tease out the
deliberate movements versus the passive dynamics of the body. With the
instrumented bicycle he conducts low speed steady turn and balancing tasks and
measures speed, roll rate and steer angle.

Along with the experimental data, he developed a bicycle and rider model with
accompanying controller. The bicycle derivation of the bicycle model is
questionable due to the non-traditional methods, but he does end up with a
model which behaves like a bicycle including speed dependent stability. He is
aware of the need to roll the bicycle frame in the direction of the desired
turn for directional control and how counter-steering plays a roll in this.
This concept leads to the primary inner loop being chosen as roll control and
his control structure resembles that of Weir's work in terms of sequential
loops. He cites the crossover model and is aware that humans can adjust their
gains as needed for good performance. The controller is traditional in most
senses and follows the patterns by McRuer, Weir, and Eaton but he adds in the
ability to add discrete pulses to the roll angle. He feeds back roll
acceleration and integrates it to get roll angular velocity. This is basically
a continuous PD control on roll rate. But his non-continuous addition to the
controller is based on a fuzzy logic-like rule "Make a pulse against the lean
whenever it gets bigger that 1.6 degrees."

.. todo:: how are the pulses applied?

It seems like he gets somewhat close matches to the experimental traces from
his control model simulations without the discrete pulses , but then adds in
pulses (single or multiple) to the steering so that the traces matches more
closely. His identification technique and criterion is focused around a
detailed examination of the patterns in the time histories in a very
qualitative way.

His results focus around the evidence for intermittent control and finds the
traditional gains to be inversely proportional to speed. He claims the
balancing part of the control system is done primarily in the lower cortex.

To me, Doyle's work emphasizes to the need for close collaboration between
psychologists and control engineers to formalize the theory for human balance.
His intermittent control theory may be valid, but due to the unusual model
development, simulation and analyses techniques it is hard to gage whether the
need for intermittent control was simply artifact of poor modeling. His insight
into the human control theory is very enlightening and his ways of wording
bring the theory outside of the traditional control framework for an expansion
in understanding.

Lange
~~~~~

Peter de Lange's recent Master thesis work [Lange2011]_ focused on identifying
the rider controller from the data that he helped us collect while interning at
our lab. He used the Whipple bicycle model, a simplified second order
representation of the human's nueromuscular dynamics (natural frequency 2.17
rad/s and damping ratio of 1.414) and a PID like controller with a 0.03 second
time delay. The controller structure had gains proportional to the integral of
the angle, the angle, the angular rate and the angular acceleration for roll
and steer. The control task was defined as simple roll stabilization (i.e.
track a roll angle of zero degrees), even though the data was collected during
heading and roll tracking tasks.

He used a four step process for identifying the rider controller 1) he
"removed" the human remnant by averaging the time histories over several single
perturbations, 2) he identified a very high order finite impulse response model
(only a function previous inputs) for the lateral force to steer angle SISO
pair (lateral perturbation force input and steer angle as output) 3) low pass
filtered the resulting responses, and 4) he identified the rider controller
parameters with a grey box model using the filtered FIR simulation results as
the base data. The grey box model was parameterized with eight gains and a time
delay. He was able to identify the gains, but the time delay always gave a
resulting unstable model, so he dropped it. Furthermore, all of the gains were
not necessary for a good model predictions so he eliminated the unnecessary
gains systematically to find the critical feedback elements. These turned out
to be the gains for roll angle, roll rate, steer rate and the integral of the
steer angle. The first three are as one may expect and he concludes that the
steer angle integral could be equated to yaw angle feedback since they are
proportional in the linear sense.

Peter's approach hinges on the averaging process in step one. The human remnant
is large relative to the measurements and averaging potentially removes data
that isn't necessarily noise. This averaging is atypical, as process noise
models are usually employed to account for these variations in the data. Using
a model such as ARMAX instead of the two step averaging and FIR model would
potentially allow one to identify the underlying linear model without removing
potentially valid data in the time history averaging process. Or all of the
steps could be combined into a state space grey box formulation with a process
noise model, for a more direct route to identifying the free parameters. But
these methods have their difficulties and will be described later in the
Chapter.

Conclusion
----------

The literature provides many examples of first principle models for both the
open loop vehicle-rider system dynamics and the rider's control, but often
proving that those models are good predictors of real physical phenomena is
difficult. These previous examples that I've presented have various
similarities influence to the methods I've chosen to use to identify the
vehicle and the rider.

Open loop identification
   The purpose of the open loop identification is to identify the passive
   vehicle and rider dynamics. This includes the force and kinematic
   relationships of the bicycle or motorcycle and if a rider is present the
   passive dynamics of the rider's body motion. Their are two basic approaches
   that have been used in literature.

   Mode Excitation
      This involves identifying particular modes of motion by forcing the
      system such that those modes are excited. The input to the vehicle is
      typically limited in bandwidth. The forcing can be generated manually
      from human control, by external perturbations, or by function of the
      maneuver. The techniques are best at identifying sustained oscillatory
      modes. Decaying oscillations are fit to the data and to extract time
      constants, frequency, and phase shift for various input-output
      combinations. These techniques generally give good repeatable results,
      but limited to identifying single modes and require many experiments to
      get a spread in frequency content and vehicle speed. These methods are
      also limited to identifying the open loop dynamics.
   Excitation
      Many modes of a model can be excited if proper inputs to the vehicle are
      chosen, giving the opportunity to identify more complete dynamic models.
      Frequency sweeps, white noise, and sum of sines are good candidates for a
      broad input spectrum. And it turns out that the remnant associated with
      human control and or deliberate random manual excitation can provide a
      wide bandwidth input spectrum as shown in [Eaton1973]_ and [James2002]_
      for adequate system identification of many modes including the higher
      frequency wobble mode. Modern system identification techniques can be
      used to find models and identify physical parameters.

Rider Control Identification (closed loop, active)
   Few have attempted to identify the rider as a control element in the bicycle
   or motorcycle system. The large array of potential control actions from a
   unconstrained rider is extremely difficult to measure, especially when both
   the forces and kinematics are key to proper identification. Typically,
   limits are put on how the rider can actuate the system and in some cases
   limits are put on the rider's ability to sense the system. This is somewhat
   critical so that the system is much more tractable. Similar to the open loop
   excitation techniques, a broad frequency spectrum provides better data to
   work for identification purposes.[Lange2011]_ has a good overview of
   excitation ideas.

   The open dynamics are in some sense much easier to model with first
   principles, as the theory is much more mature. On the other hand, the
   theoretical constructs of the control system of the human relatively in its
   infancy, so having the advantage of solid first principles is much weaker.
   Most researchers approaches have been modeled from the manual control work
   lead by authors such as Tustin and McRuer in the 50s and 60s. When mapped to
   the bicycle, the primary control loop is taken as roll stabilization and roll
   command authority. With the secondary loops being heading and tracking. Both
   sequential loop controller designs and the popular PID controllers have been
   used as a structure for gain and delay parameter identification in the
   control loops.

   Accurate parameter identification relies on strong characterization of the
   system process noise and in the case of a human rider, the process noise is
   often comparable in magnitude and frequency to the control actions
   themselves. Techniques that treat the controller as a quasi-linear structure
   where the noise is modeled as white and Gaussian and characterized by the
   portion of the output not linear correlated to the input (i.e. remnant) have
   been popular in past. [Eaton1973]_ took care to account for this and found
   that the crossover model was a good predictor of human control action. A
   proper treatment of the noise by other researchers is typically little to
   none and justly so as it is not necessarily easily dealt with large
   signal-to-noise ratios in the linear control framework. Modern system
   identification techniques offer some ability to model process noise with
   ARMAX types of implementations and state space formulations benefiting from
   the integration with Kalman filters. As will be discussed in the following
   sections, model identification works fairly well but parameter
   identification such as those for control gains becomes increasingly
   difficult with higher noise.

Experimental Design
===================

Our main experimental designs were focused around reasonable ways to excite the
rider/bicycle system with the goal of identifying the parameters of the rider
control system. I started by simply repeating some of the perturbation
experiments from Chapters :ref:`delftbicycle` and :ref:`motioncapture`, but
included and measured the lateral perturbation force and the steer torque which
were critical measurements for a realistic input/output relationships that the
previous studies lacked. We also attempted single lane change maneuvers because
we'd been using a lane change as our objective criteria in our simulations
[Hess2012]_ and they had been used successfully used in the literature. It
turned out that we were able to get reasonable results with preliminary system
identification with the lateral perturbation runs and did not pursue the lane
change maneuvers beyond the preliminary runs. The lane changes were especially
difficult on the narrow treadmill.

Riders
------

We chose three riders: Charlie, Jason, and Luke of similar age: 34, 28-29, 32,
mass: 79, 84 , 84 kg and bicycling ability although Luke has more technical
mountain biking skill other two riders. A wide range skills level was outside
the scope of the project and we preferred riders with good proficiency as it
has been shown that it increases repeatability of results in tasks such as
these [Weir1979a]_. The seat height and harness were set in the same position
for Charlie and Luke and in different positions for Jason. The inertia of the
rear frame was measured for both configurations (thus the "Rigidcl" and "Rigid"
bicycles) in Chapter :ref:`physicalparameters`.

Environments
------------

We performed the experiments in two different environments: on a treadmill and in
a large gymnasium for different reasons. You'll have to read the next
paragraphs to find out!

Treadmill
~~~~~~~~~

Dr. James Jones at the veterinary school at here at Davis graciously let us use
their horse treadmill (Graber Ag Kagra Mustang 2200) during their downtime. The
treadmill is 1 meter wider and 5 meters long and has a speed range from 0.5 m/s
to 17 m/s. This was only a third of the width treadmill at Vrije Universitiet
in Amsterdam, but after some practice runs we felt that narrow lane changes and
the lateral perturbations could be successfully performed. We used the
treadmill because the environment was very controllable, in particular with
regards to fixed constant speeds, and it offered the ability to do have very
long run durations within a broad speed range. Potentially both the side
railings and the belt side curbs added rider's lack of lateral movement space.

.. figure:: figures/systemidentification/treadmill.jpg
   :width: 4in

   Sideview of the horse treadmill while Luke was riding the bicycle.

Pavilion
~~~~~~~~

The bicycle ended up design such that all of the data collection equipment was
on board and was suitable for data collection in a free environment. After
lengthy bureaucratic negotiations, we were able to make use of the UCD pavilion
floor for the experiments. The floor was made of a stiff rubber and provided a
rectangular wind free space of about 100' by 180' (30 m by 55 m). We road
around the perimeter to build up speed and did our maneuvers on a straight
section about 100 feet (30 m) long. We were not able to travel at speeds higher
than about 7 m/s as the tires would slip in the final turn into the test
section (this primarily seem to be due to the dust on the floor). This in door
environment provided a wind free area which was more akin to the environment
bicyclists normally ride in.

.. figure:: figures/systemidentification/pavilion.jpg
   :width: 3in

   Overhead view of the pavilion floor during a perturbation run.

.. todo:: find out what the floor material is on the treadmill and in the pavilion

Maneuvers
---------

Our choice of maneuvers was primarily guided by our previous experiments and
the search for an optimal way to externally excite the system. We also made
sure to take sets of experiments that would act as a control without
deliberate disturbances. The following list details the meaning of the maneuver
labels in the dataset.

System Test
   This is a generic label for data collected during various system tests that
   should not be used for general analysis. This was primarily used to check
   that all sensors were working.
Balance
   The rider is instructed to simply balance the bicycle and keep a relatively
   straight heading. They were instructed to focus on a point of their choosing
   in the far distance. There was an open door in front of the treadmill which
   allowed the rider to look to a point outside across the street. In the
   pavilion, the rider looked into the rafters of the building or at the
   furthest wall. We may have given slightly different instructions to the
   riders and Charlie did not understand the instructions exactly during some
   of the earlier runs, but nonetheless these can be analyzed with a control
   model that only has the roll and heading loops closed and maybe even with
   only the roll loop closed. We had a line taped to the pavilion floor during
   these runs that was still in the periphery of the rider's vision. This may
   have affected their heading control.
Balance With Disturbance
   Same as 'Balance' except that a lateral force perturbation is applied just
   under the seat of the bicycle. The rider wore a face shield on the side of
   the perturber so no visual cues were available to predict the perturbation
   time. On the treadmill, we sample for 60 to 90 seconds with five to eleven
   perturbations per run. On the pavilion floor we were able to apply two to
   four perturbations per run due to the length of the track. In the early runs
   (< 204), the lateral force was applied only in the negative direction (to
   the left) and the perturber decided when to apply the perturbations. For the
   later runs (> 203), we applied a random sequence of positive and negative
   perturbations that was unknown to the rider. On the treadmill, the rider
   signaled when they felt stable and the perturbation was applied at a random
   time between 0 and 1 second based on a simple computer program. On the
   pavilion floor, we simply applied the perturbations as soon as the rider
   felt stable so that we could get in as many as possible during each run.
Track Straight Line
   The rider was instructed to focus on a straight line that was marked on the
   ground and he attempted to keep the front wheel on the line. The line of
   sight from the rider's eyes to the line on the ground was essentially
   tangent the top of the front wheel. In the pavilion, the line could be seen
   up to 100 feet ahead, so there was greater peripheral view of the line. On
   the treadmill, there was from 0.5 to 1.5 meters of preview line available.
Track Straight Line With Disturbance
   Same as "Track Straight Line" except that a lateral perturbation force is
   applied to the seat of the bicycle. This was done in the same fashion as
   described in "Balance With Disturbance".
Lane Change
   The rider attempted to track a line in similar fashion as the "Track
   Straight Line" maneuver except that the line was a single lane change. On
   the pavilion floor, the line was taped on the ground and the rider was
   instructed to do whatever felt best to stay on the line. They could use full
   preview looking ahead, focus on the front wheel and line, or a combination
   of both. We also tried some lane changes on the treadmill but the lack of
   preview of the line made it especially difficult. We were able to manage it
   by marking a count down on the belt so that the rider new when the lane
   change would arrive. The rider also new the direction of lane change before
   hand for all the scenarios.
Blind With Disturbance
   We did a run or two for each rider on the pavilion floor with the rider's
   eyes closed to attempt to completely open the heading loop. In hindsight,
   blind tests would be preferable when identifying the rider control system so
   that only inner roll stabilization loop need be analyzed.
Static Calibration
   We took a short duration sample of the sensors signals while no rider was on
   the bicycle and the bicycle was fixed as close to vertical in roll before
   each set of runs. The static accelerometer readings could theoretically give
   the roll and pitch angles of the bicycle frame and be used to account for
   the bias in the roll angle measurements.
   .. todo:: It would not be a bad idea to figure out the accelerometer
      readings when the frame is know to be vertical and at the nominal pitch
      angle. As this was never done.

.. figure:: figures/systemidentification/pavilion-lane-change.*

   The dimensions of the single lane change on the pavilion floor for runs
   115-139.

We only focus on the Balance and Track Straight Line maneuvers with and without
disturbances in the following analyses and they will be referred to as Heading
Tracking and Lateral Deviation Tracking from now on.

Heading Tracking
    The rider was instructed to simply balance the bicycle and keep a
    relatively constant heading while focusing their vision at a point
    in the far distance.

Lateral Deviation Tracking
    The rider was instructed to focus on a straight line that was marked
    on the ground and to attempt to keep the front wheel on the line.

Both tasks were performed with and without the application of a manually
applied lateral perturbation force just below the seat. The forces were
applied randomly in direction and time.

Data
====

The experimental data was collected on seven different days. The first few days
were mostly trials to test out the equipment, procedures and different
maneuvers. The data from the trial days is valid data and we ended up using it
in our analysis. The tires were pumped to 100 psi at the start of each day.

February 4 2011 Runs 103-109
   These were the first trials on the treadmill for preliminary testing. Only
   Jason rode. We performed lateral deviation tracking with disturbances. The
   bike fell over, broke and we had to cut it short.
February 28, 2011 Run 115-170
   These were the first trials in the pavilion. Jason was the only rider. We
   tried lane changes (115-139), lateral deviation tracking with disturbances
   (140-157), and a mixture of heading tracking and lateral deviation tracking
   with no disturbances (158-170). I noted that the slip clutch backlash seemed
   to be larger than the previous day with a guess of about 1 degree.
March 9, 2011 Runs 180-204
   This was the second go at the treadmill, still just testing out things.
   Jason was the only rider. We did heading and lateral deviation tracking with
   disturbances and some lane changes. The lane changes were 0.25 m wide left
   and right maneuvers back and forth among two lines on the treadmill at 2 m
   long segments. Countdown markers to give an idea when the lane change
   started were necessary due to the rider's limited preview distance. We did
   the highest speed during any subsequent trials at 9 m/s. The 9 m/s runs
   acquired a large amount of noise in the lateral force channel. The treadmill
   elevation was set at 0.1% grade.
August 30, 2011 Runs 235-291
   Jason and Luke rode and performed heading and lateral deviation tasks with
   and without perturbations at three speeds on the treadmill.
September 6, 2011 Runs 295-318
   Charlie performed heading and lateral deviation tasks with and without
   perturbations on the treadmill.
September 9, 2011 Runs 325-536
   Luke, Charlie and Jason performed heading and lateral deviation tracking
   tasks on the Pavilion floor with and without perturbations. Most of Luke and
   Charlie's runs were corrupt due to the time synchronization issues.
September 21, 2011 Runs 538-706
   Luke and Charlie repeated the runs from September 9th. And we added a couple
   of blind runs for each of them.

The metadata and raw time history data for each run and all sensor calibration
data were stored in individual Matlab mat files on the data acquisition
computer with my `BicycleDAQ <https://github.com/moorepants/BicycleDAQ>`_
software. The run files and calibration files are automatically numbered in
sequence with a five digit number; one sequence for runs and one for
calibrations. These mat files were then parsed and merged into a HDF5 database
for a uniform, organized and complete single database that could be accessed by
a number of programs and languages for fast data queries. I made use of
`PyTables <http://www.pytables.org>`_ for writing and reading from the
database. The software `BicycleDataProcessor
<http://github.com/moorepants/BicycleDataProcessor>`_ was designed as an
interface to the data in the database. In particular, it is able to load the raw
data from individual runs, process it, and present it for easy manipulation and
viewing.

The database is initially structured with three top level tables and nodes
containing the time histories of the sensors for each run. The run table has a
row for each run and the columns store each piece of metadata, including the
corruption coding described below. The signal table has a row for each raw and
processed signal type and the classification information for each. The
calibration table has a row for each calibration which provides information
about the sensor and the data collected in the calibration.

.. todo:: the descriptions of the collected data either need to be in an
   appendice or included with the BicycleDataProcessor documentation

.. todo:: Some of this belongs in the Davis Bicycle Chapter

We recorded a large set of meta data for each run to help with parsing during
analyses. We also video recorded all of the runs (minus a few video mishaps).
I coded each run based on the notes, data quality, and viewing the video for
potential or definite corrupted data with the following five codes.

Corrupt
   If the data is completely unusable due to time synchronization issues or
   other then this is set to true.
Warning
   Runs with a warning flag are questionable and potentially not usable.
Knee
   The rider's knees would sometimes de-clip from the frame during a
   perturbation. This potentially invalidates the rigid rider assumption. An
   array of 15 boolean values are stored for each run and each true value
   represents a perturbation where a knee came off.
Handlebar
   On the treadmill the bicycle handlebars occasionally connected with the side
   railings. Each perturbation during the run which this happen was recorded.
Trailer
   On the treadmill the roll trailer occasionally connected with the side of
   the treadmill. Each perturbation during the run which this happened was
   recorded.

We ultimately collected 600+ runs that were potentially usable for analysis.
Figure :ref:`figDataBarPlots` gives a breakdown of the runs by rider,
environment, maneuvers, and speed bins.

.. _figDataBarPlots:

.. figure:: figures/systemidentification/raw-data-bar-plot.*
   :width: 7in

   figDataBarPlot

   Four bar charts showing the number of runs that are potentially usable for
   model identification. These include runs from the treadmill and pavilion,
   one of the four primary maneuvers, and were not corrupt.

.. todo:: note how many runs were acutally usable

The processed data provides filtered signals that correspond to the coordinates
and speeds outlined in our models, Chapters :ref:`eom` and :ref:`extensions`.
We were even able to estimate the path of the wheel contact points on the
ground. The quality of the data is high with little to no missing data and
complete description of the dynamic state through time. Figures
:ref:`figTreadmillTimeHistory` and :ref:`figPavilionTimeHistory` give examples
of the processed data for the two environments.

.. _figTreadmillTimeHistory:

.. figure:: figures/systemidentification/time-history-treadmill.*
   :width: 7in

   figTreadmillTimeHistory

   The time histories of the computed signals for a typical treadmill run after
   processing and filtering. Only a portion of the 90 second run is shown for
   clarity.

.. _figPavilionTimeHistory:

.. figure:: figures/systemidentification/time-history-pavilion.*

   figPavilionTimeHistory

   The time histories of the computed signals for a typical pavilion run after
   processing and filtering.

System Identification
=====================

My primary goal in the following analyses of all the collected data is to
identify the manual control system employed the rider. I will approach this in
a similar fashion as [Eaton1973]_ and attempt to identify the open loop bicycle
and rider dynamics first and follow by with identification of the control
system.

This two part process was not originally thought to be needed and I started
with the identification of the control system assuming the Whipple model would
be adequate for the open loop dynamics. But my preliminary attempts at
identifying the controller with the Whipple model in place as the plant always
under-predicted the steer torque needed for a given measured trajectory. This
lead me into the exploration of the validity of the Whipple model.

There is actually very little experimental validation of the open loop dynamics
of the bicycle and rider with [Kooijman2006]_ being one of the better studies.
But his study was limited to a riderless bicycle in a narrow speed range where
the bicycle was stable. Taking the various first principles models like this
for granted is potentially dangerous. In our case, it resulted in erroneous
early estimations of the controller parameters. As pointed out by many, in
particular the motorcycle crowd, there is very good reason to question some of
assumptions such as knife edge, no side slip wheels especially under a rider's
weight. And secondly, the rider's biomechanics have much influence and coupling
to the bicycle than the motorcycle which must be accounted for.

After a model for the open system is derived I identify parameters to the
control structure described in [Hess2012]_ and in Chapter :ref:`control`. We've
shown that this control structure is robust for a range of speeds and lends
also itself to the dictates of the crossover model which is built upon strong
experimental evidence in human operator modeling. I make use of multi-input
multi-output grey box state space identification techniques to home in on the
optimal parameters for the measured data.

Before I proceed, it is important to note the difference in identifying a model
that best predicts the data versus identifying physical parameters in a model
structure that cause the data to best fit the measured data. In the first case,
it is somewhat easy to fit a model to input and output data. By increasing the
order of the model and thus the number of free parameters one can theoretically
fit every data point. This is most evident in the over-fitting of a linear
trend with that of a higher order polynomial. It still often takes human
intuition and reasoning to limit the order of the system to something that
represents the true relationships in the variables. But even in this case, the
individual meaning of the resulting identified parameters of black box system
may have little apparent connection to the known first principles laws we are
familiar with and believe in. In dynamics, we often want to know how well our
first principles models predict the measured motion and secondly we'd like the
ability to identify parameters, particular ones we uncertain of, in the first
principles models from measured data. Accurately identifying model parameters
is much more difficult task, as noise, both process and measurement, have to be
accounted for to get repeatable and accurate estimates of the parameters. I
have had good success with finding models that predict the data but little
success with explicit and accurate parameter identification in the following
analyses. There is great room for improvement in the parameter identification
if the noise issues are better managed.

Bicycle Model Validity
======================

The open loop dynamics of the bicycle-rider system can be described with many
models, see [Astrom2005]_, [Limebeer2006]_, and [Meijaard2007]_ for good
overviews. The benchmarked Whipple model [Meijaard2007]_ provides a somewhat
minimalistic model in a manageable analytic framework which is capable of
describing the essential dynamics such as speed dependent stability, steer and
roll coupling and non-minimal phase behavior. I use this model as the standard
base model to work from, as the fidelity of simpler models are generally not
adequate. The model is 4th order with roll angle, steer angle, roll rate and
steer rate typically selected as the independent states and with roll and steer
torque as inputs. I neglect the roll torque input and in its place extend the
model to include a lateral force acting at a point on the frame to provide a
new input, accurately modelling lateral perturbations, see Chapter
:ref:`extensions`. I also examine a second candidate model which adds inertial
effects of the rider's arms to the Whipple model, Chapter :ref:`extensions`.
This model was designed to more accurately account for the fact that the riders
were free to move their arms with the front frame of the bicycle. This model is
similar in fashion to the upright rider in [Schwab2010]_, but with slightly
different joint definitions. Constraints are chosen so that no additional
degrees of freedom are added, keeping the system both tractable and comparable
to the benchmarked Whipple model.

I estimated the physical parameters of the first principles models with the
techniques described in Chapter :ref:`physicalparameters`. The bicycle was
measured as described in to get accurate estimates of the parameters used in
the benchmark bicycle. Each rider's inertial properties were estimated using
Yeadon's [Yeadon1990]_ method which allowed easy extraction of body segment
parameters for more complicated rider biomechanic models such as the inclusion
of moving arms as described above. The parameter computation is handled with
two custom open source software packages [Dembia2011]_ and [Moore2011]_.

State Space Realization
-----------------------

During all of the experiments there are two measured external (or exogenous)
inputs: the steer torque and the lateral force. Both inputs are generated from
manually, the first from the rider and the second from the person applying the
pulsive perturbation. The outputs can be any subset of the measured kinematical
variables or combinations thereof. The problem can then be formulated as such:
given the inputs and outputs of the system and some system structure, what
model parameters give the best prediction of the output given the measured
input. This a classic system identification problem.

Method
~~~~~~

For this analysis, I limit the inputs to steer torque and lateral force and the
outputs to roll angle, steer angle, roll rate and steer rate. The ideal fourth
order system can be described with the following continuous state space
description

.. math::
   :label: eqConStateSpace

   \dot{x}(t) & =
   \mathbf{F}x(t) + \mathbf{G}u(t)\\
   \begin{bmatrix}
     \dot{\phi} \\
     \dot{\delta} \\
     \ddot{\phi} \\
     \ddot{\delta}
   \end{bmatrix}
   & =
   \begin{bmatrix}
     0 & 0 & 1 & 0\\
     0 & 0 & 0 & 1\\
     a_{\ddot{\phi}\phi} & a_{\ddot{\phi}\delta} &
     a_{\ddot{\phi}\dot{\phi}} & a_{\ddot{\phi}\dot{\delta}}\\
     a_{\ddot{\delta}\phi} & a_{\ddot{\delta}\delta} &
     a_{\ddot{\delta}\dot{\phi}} & a_{\ddot{\delta}\dot{\delta}}
   \end{bmatrix}
   \begin{bmatrix}
     \phi \\
     \delta \\
     \dot{\phi} \\
     \dot{\delta}
   \end{bmatrix}
   +
   \begin{bmatrix}
     0 & 0 \\
     0 & 0\\
     b_{\ddot{\phi}T_\delta} & b_{\ddot{\phi}F_{c_l}}\\
     b_{\ddot{\delta}T_\delta} & b_{\ddot{\delta}F_{c_l}}
   \end{bmatrix}
   \begin{bmatrix}
     T_\delta\\
     F_{c_l}
   \end{bmatrix}\\
   \eta(t) & = \mathbf{H}x(t)\\

where :math:`\mathbf{H}` is the identity matrix.

Assuming that this model structure can adequately capture the dynamics of
interest of the bicycle-rider system, our goal is to accurately identify the
unknown parameters :math:`\theta` which are made up of the unspecified entries
in the :math:`\mathbf{F}` and :math:`\mathbf{G}` matrices. To do this one needs
to recognize that this continuous formulation is not compatible with noisy
discrete data. The following difference equation can be assumed if we sample
the continuous system at :math:`t=kT`, :math:`k=1,2,\dots`, with :math:`T`
being the sample period and that assumption that  the variables are constant
over the sample period (i.e. zero order hold).

.. math::
   :label: eqDisStateSpace

   x(kT + T) & = \mathbf{A}(\theta)x(kT) + \mathbf{B}(\theta)u(kT) + w(kT)\\
   y(kT) & = \mathbf{C}(\theta)x(kT) + v(kT)

The additional terms :math:`w` and :math:`v` represent the process and
measurement noise vectors, respectively, which are assumed to be sequences of
white Gaussian noise with zero mean and some covariance. By making use of the
Kalman filter this formulation can be transformed such that the optimal
estimate of the states with respect to the process and measurement noise
covariance :math:`\hat{x}` are utilized, see [Ljung1999]_.

.. math::
   :label: eqInnovations

   \hat{x}(kT + T, \theta) & = \mathbf{A}(\theta)\hat{x}(kT) +
   \mathbf{B}(\theta)u(kT) + \mathbf{K}(\theta)e(kT)\\

   y(kT) & = \mathbf{C}(\theta)\hat{x}(kT) + e(kT)

where :math:`\mathbf{K}` is the Kalman gain matrix. :math:`\mathbf{K}` is a
function of :math:`\mathbf{A}(\theta)`, :math:`\mathbf{C}(\theta)` and the
covariance and cross covaraince of the process and measurment noise, but it can
also be directly parameterized by :math:`\theta`. With that, this equation is
called the directly parameterized innovations form and the entries of the four
matrices in equation :eq:`eqInnovations` can be estimated directly.

The :math:`\mathbf{A}` and :math:`\mathbf{B}` matrices are related to
:math:`\mathbf{F}` and :math:`\mathbf{G}` by

.. math::

   \mathbf{A}(\theta) = e^{\mathbf{F}(\theta)T}

   \mathbf{B}(\theta) = \int_{\tau=0}^T e^{\mathbf{F}(\theta)\tau} \mathbf{G}(\theta) d\tau

and with a linear assumption can even be directly estimated in discrete form by

.. math::

   \mathbf{A}(\theta) = \mathbf{I} +  \mathbf{F}(\theta)T

   \mathbf{B}(\theta) = \int_{\tau=0}^T e^{\mathbf{F}(\theta)\tau} \mathbf{G}(\theta) d\tau

.. todo:: what is the form of B when assuming e^{AT} = I + AT

The one step ahead predictor for the innovations form is

.. math::
   :label: eqOneStepInnovations

   \hat{y}(t|\theta) = \mathbf{C}(\theta) \left[qI - \mathbf{A}(\theta) +
   \mathbf{K}(\theta) \right]^{-1} \left[\mathbf{B}(\theta) u(t) +
   \mathbf{K}(\theta)y(t) \right]

where :math:`q` is the forward shift operator (:math:`q u(t) = u(t+1)`)
[Ljung1999]_. The predictor is a vector of length :math:`p` where each entry is
a ratio of polynomials in :math:`q`. These are transfer functions in :math:`q`
from the previous inputs and outputs to the current output. In general, the
coefficients of :math:`q` are non-linear functions of the parameters
:math:`\theta`.

.. todo:: the following doesn't make sense, fix it up

We can now construct the cost function, which will enable the computation of
the parameters which give the best fit using optimization methods. We'd like to
minimize the error in the predicted output with respect to the measured output
at each time step. First form :math:`Y_N` which is a :math:`pN x 1` vector
containing all of the current outputs at time :math:`kT`.

.. math::

   Y_N = \left[y_1(1) \ldots y_p(1) \ldots y_1(N) \ldots y_p(N) \right]^T

where :math:`p` are the number of outputs and :math:`N` is the number of samples.
Then compute the predictor vector, :math:`\hat{Y}_N(\theta)`, the one step ahead
prediction of :math:`Y_N` given :math:`y(s)` and :math:`u(s)` where :math:`s
\leq t - 1`

.. math::

   \hat{Y}_N = \left[\hat{y}_1(1) \ldots \hat{y}_1(1) \ldots \hat{y}_p(N) \ldots \hat{y}_p(N) \right]^T

The cost function is then the norm of the difference of :math:`Y_N` and
:math:`\hat{Y}_N(\theta)` for all :math:`k`.

.. math::

   V_N(\theta) = \frac{1}{pN}||Y_N - \hat{Y}_N(\theta)||

.. todo:: do I need the 1/pN? I'm just copying that from the book somewhere.

The value of :math:`\theta` which minimizes cost function is the best
prediction

.. math::

   \hat{\theta}_N = \underset{x}{\operatorname{argmax}} V_N(\theta, Z^N)

where :math:`Z^N` are all the measured inputs and outputs.

In general, the minimization problem is not trivial and may be susceptible to
many of the issues association with optimization including only being able to
find a local minima. The number unknown parameters in the :math:`\mathbf{K}`
matrix are function of the number of states and the number of outputs, in our
case in :math:`\mathbb{R}^{4\times4}` which more than doubles the number of
unknowns present in the :math:`\mathbf{A}` and :math:`\math{B}` matrices. It is
thus critical to reduce the number of unknown parameters to have a more likely
chance at finding the global minima of the cost function. The accuracy of the
system parameters depend on the ability to estimate the :math:`\mathbf{K}`
matrix along with the other parameters.

.. todo:: Compare the fit from a k=0 fit and one without, note how we aren't
   getting to the global minima---> this isn't really working out, can't really
   find a good model when searching for the noise

Before identification I further processed all of the signals that were
generally symmetric about zero by subtracting the means over time. For some of
the pavilion runs, this may have actually introduced a small bias, as the short
duration runs with unbalanced pertubations may not have a mean at true zero.

I made use of the Matlab System Identification Toolbox for the identification
of the parameters :math:`\theta` in each run of this model structure. In
particular a structured `idss` object was built for with the initial guesses of
the unknown parameters based on the Whipple model and the initial guesses for
the initial conditions and the Kalman gain matrix being equal to zero.

.. todo:: more about the software?

Results
~~~~~~~

It turns out that finding a model than which meets the criterion is not too
difficult when the output error form is considered (:math:`\mathbf{K}=0`). This
model may be able to explain the data well, but the parameter estimation could
is potentially be poor because the parameters in the state and input matrices
were adjusted such that the results fit both the true trajectories and the
noise. Global minima in the search routine are quickly found when the number of
parameters are 10-14. When the :math:`\mathbf{K}` matrix is added the number of
unknown parameters increases by 16 and the global minima becomes more difficult
to find and I was rarely able if at all to find the global minima for the
general problem, even when reducing the number of outputs to one. This was
confirmed

Figure :ref:`figExampleFit` shows a typical example input and output data for a
single run (#596) with both steer torque and lateral force as inputs. The plot
compares the simulation response to the input to the measured response. Notice
that the identified model predicts the trajectory extremely well and similar
results are found for the majority of the runs. The Whipple model predicts the
trajectory directions but the magnitudes are large, meaning that for a given
trajectory, the Whipple model requires less torque than what was measured. The
Whipple model with the arm inertial effects does a better job than the Whipple
model, but still has some magnitude differences and in particular has a harder
time predicting the roll angle than the other two models.

The identified models are almost always unstable and the even though the
measured inputs stabilize the true system, they will not necessarily stabilize
the models. This poses an issue when gaging the model quality by it's
percentage variance. A model that blows up during the simulation may not
necessarily be a bad model, but will return a very small percent variance and
loose its ability to be compared by that criteria. [Biral2003]_ and
[Teerhuis2010]_ both are able to feed forward simulations of their models with
the measured steering torque.  They both are dealing with high speed
motorcycles which typically only have a slightly unstable capsize mode.
[Teerhuis]_ uses a controller to compensate the torque for unbounded errors so
that the simluation doesn't blow up. The method I use here is to chose short
duration portions of the runs for simulation and search for the best set of
initial conditions to keep the model stable during the duration. This generally
works but there is ultimately some uncomparable runs due to this issue.

.. figure:: figures/systemidentification/example-fit.*

   The example results for the identification of a single run (#596). The
   experimentally measured steer torque and lateral force are shown in the top
   two graphs. All of the signals were filtered with a 2nd order 15 hertz low
   pass Butterworth filter. The remaining four graphs show the simulation
   results for the Whipple model (W), Whipple model with the arm inertia (A),
   and the identified model for that run (I) plotted with the measured data
   (M). The percentages give the percent of variance explained by the model.}

I use this structured state space output error identification procedure for a
collection of experiments (:math:`n=368`) over a range of speeds between about
1 and 9 m/s. Figure :ref:`figCoefficients` plots identified coefficients of the
dynamical equations of motion (i.e. the bottom two rows of the
:math:`\mathbf{F}` and :math:`\mathbf{G}` matrices) as a function of speed for
each experiment compared to both the Whipple and arm model predictions. From
visual inspection the :math:`\ddot{\phi}` equation seems to be better predicted
by the two models. The roll equation also seems to have less spread in the
experimental data. For example, the :math:`a_{\ddot{\phi}\delta}` coefficient
appears to be very tight and the first principles models predict it very well.
The constant, linear and quadratic trends in the coefficients are not easily
seen for most coefficients. This is due to the high variability in the results
of a large number of repeated experiments at some speeds, more detailed
regression models may be able to reveal the true trends [1]_.

Figure :ref:`figBode` gives another view of the resulting data. It is a frequency
response plot at the mean speed for a set of runs. The blue lines give the mean
and standard deviation of the magnitude and phase of the system transfer
function :math:`\frac{\phi}{T_\delta}(s)`. Even though the spread in the
identified parameters seems high in Figure [fig:coefficients], the Bode plot
shows that the identified system response is not as variable, especially in
magnitude. It is also apparent that the experimental magnitude has a -5 to -10
dB offset across the frequency range shown with respect to the Whipple model.
This correlates with the amplitude differences in the trajectories shown in
Figure :ref:`figExampleFit`. Notice that the arm model has little to no offset
between 2 and 10 rad/s, thus the better amplitude matching.

.. _figCoefficients:

.. figure:: figures/systemidentification/coefficients.*

   Coefficients of the linear dynamical equations of motion plotted as a
   function of speed. Each blue dot is a single experiment. The green line is
   the Whipple model and the red line is the arm model. Only experiments with
   a mean fit percentage greater than zero are shown. The orange line is the
   model identified with the canonical method using runs done be Luke in the
   pavilion which is presented and discussed in the next section.

.. todo:: one way to evaluate the quality of the holistic models may would be to
   calculate the total error in the coefficient curves

.. _figStateSpaceBode:

.. figure:: figures/systemidentification/state-space-bode.*

    Frequency response of steer torque to roll angle for a set of runs at
    :math:`4.0 \pm 0.3` m/s. The solid blue line is the mean from the
    identified runs and is bounded by the standard deviation, the dotted blue
    line. The green line is the Whipple model and the red line is for the model
    which accounted for the arm inertial effects.

Conclusion
~~~~~~~~~~

I have shown that a fourth order structured state space model is both adequate
and good for describing the motion of the bicycle under manual control in a
speed range from approximately 1.5 m/s to 9 m/s. The fact that higher order
models may not be necessary for bicycle dynamic description is an important
finding. More robust models of single track vehicles are typically higher than
4th order, with degrees of freedom associate with tire dynamics, frame
flexibilities and rider biomechanics. These finding suggest that the more
complex models may be overkill for many modeling purposes. The data
subsequently also reveals that fourth order archetypal first principles models
are not robust enough to fully describe the dynamics. The deficiencies are most
likely due to un-modeled effects with the knife edge, no side slip wheel contact
assumptions being the most probable candidate. Dissipative forces in the of any
sort are potential answers. Un-modeled rider biomechanics such as passive arm
stiffness and damping and head motion may play a role too. The uncertainty in
the estimates of the physical parameters, Chapter :ref:`physicalparameters` is
not large enough to explain the difference between the coefficient
identification and their predictions from first principles. It is likely that
tire scrub torques of some sort are needed to improve the fidelity.

Canonical Identification
------------------------

One issue I faced with the state space realization was dealing with mutliple
experiments. Ideally I had hoped to identify a linear model that was a function
of speed with respect to all or subsets of the experiments. It is possible to
concatenate runs, but discontinutities in the data arise potentially throwing
off the identification. You could also imagine setting up a cost function that
gave the lowest error in all the outputs across all of the runs. Both my recently
obtained knowledge in system identification and being constrained by the
methods available in the Matlab System Identification toolbox were limiting
factors in these two approaches. Karl Astrom suggested doing the system
identification with respect to the two second order form of the equations of
motion. This would allow you to use both simple least squares for the solution
and the ability to compute models from large sets of runs. This section deals
with this approach.

Model structure
~~~~~~~~~~~~~~~

The identification of the linear dynamics of the bicycle can be formulated with
respect to the benchmark canonical form realized in [Meijaard2007]_. If the
time varying quantities in the equations are all known at each time step, the
coefficients of the linear equations can be estimated given enough time steps.

.. math::

   M \ddot{q} + v C_1 \dot{q} + [g K_0 + v^2 K_2] q = T

where the time varying states roll and steer are collected in the vector
:math:`q = [\phi \quad \delta]^T` and the time varying inputs roll torque and
steer torque are collected in the vector :math:`T = [T_\phi \quad T_\delta]^T`.
This equation form assumes that the velocity is constant with respect to time
as the model was linearized about a constant velocity equilibriumm, but the
velocity can be treated as a time varying parameter if the acceleration is
relatively small. I extend the equations to properly account for the lateral
perturbation force, :math:`F`, which was the actual input we delivered during
the experiments. It contributes to both the roll torque and steer torque
equations.

.. math::

   M \ddot{q} + v C_1 \dot{q} + [g K_0 + v^2 K_2] q = T + H F

where :math:`H = [H_{\phi F} \quad H_{\delta F}]^T` is a vector describing the
linear contribution of the lateral force to the roll and steer torque
equations. :math:`H_{\phi F}` is approximately the distance from the ground to
the force application point. :math:`H_{\delta F}` is a distance that is a
function of the bicycle geometry (trail, wheelbase) and the longitudinal
location of the force application point. For our normal geometry bicycles,
including the one used in the experiments, :math:`H_{\delta F} << H_{\phi F}`.
I compute :math:`H` for each rider/bicycle from the state space form of the
linear equations of motion calculated in Chapter :ref:`extensions`.

.. todo:: Calculate what H_{\delta F\) actually is by hand.

.. math::

   \dot{x} = A x + B u

where :math:`x = [\phi \quad \delta \quad \dot{\phi} \quad \dot{\delta}]^T` and
:math:`u = [F \quad T_\phi \quad T_\delta]^T`. The state and input matrices can
be sectioned.

.. math::

   A =
   \begin{bmatrix}
     0 & I \\
     A_l & A_r
   \end{bmatrix}

.. math::

   B =
   \begin{bmatrix}
     0 & 0\\
     B_F &  B_T
   \end{bmatrix}

where :math:`A_l` and :math:`A_r` are the 2 x 2 submatrices corresponding to the states
and their derivatives, respectively. :math:`B_F` and :math:`B_T` are the 2 x 1 and 2 x
2 submatrices corresponding to the lateral force and the torques, respectively.
The benchmark canonical form can now be written as

.. math::

   B_T^{-1} [ \ddot{q} - A_r \dot{q} - A_l q] = T + B_T^{-1} B_F F

where

.. math::

   M = B_T^{-1}

.. math::

   vC_1 = -B_T^{-1} A_r

.. math::

   [gK_0 + v^2K_2] = -B_T^{-1} A_l

.. math::

   H = B_T^{-1} B_F

.. list-table::

   * - Rider
     - :math:`H`
   * - Charlie
     - :math:`[0.9017 \quad 0.01121716]^T` m
   * - Jason
     - :math:`[0.942975 \quad 0.01062231]^T` m
   * - Luke
     - :math:`[0.9017 \quad 0.01121716]^T` m

The location of the lateral force application point is the same for Charlie an
Luke because they used the same seat height. The force was applied just below
the seat, which was adjustable in height for different riders.

Data processing
~~~~~~~~~~~~~~~

Chapter :ref:`davisbicycle` details how each of the signals were measured and
processed to obtain

For the following analysis, all of the signals were filtered with a second
order low pass Butterworth filter at 15 Hz. The roll and steer accelerations
were computed by numerically differentiating the roll and steer rate signals
with a central differencing except for the end points being handled by forward
and backward differencing. The mean was subtracted from all the signals except
the lateral force.

Identification
~~~~~~~~~~~~~~

A simple analytic identification problem can be formulated from the canonical
form. If we have good measurements of :math:`q`, their first and second
derivatives, forward speed :math:`v`, and the inputs :math:`T_\delta` and
:math:`F`, the entries in the :math:`M`, :math:`C1`, :math:`K0`, :math:`K2` and
:math:`H` matrices can be identified by forming two simple regressions, one for
each equation in the canonical form. I use the instantaneous speed at each time
step rather than the mean over a run to improve accuracy with respect to the
speed parameter as it has some variablity.

.. todo:: calculate the variablity in the forward speed measurement for each
   run

The roll and steer equation each can be put into a simple linear form

.. math::

   \Gamma \Theta = Y

where :math:`\Theta` are the unknown coefficients and :math:`\Gamma` and
:math:`\Theta` are made up of the inputs and outputs measured during a run.
:math:`\Theta` can be all or a subset of the entries in the canonical matrices.
If there are :math:`N` samples in a run and we desire to find :math:`M` entries
in the equation, then :math:`\Gamma` is an :math:`N \times M` matrix and
:math:`Y` is an :math:`N \times 1` vector. The Moore-Penrose puesdo inverse can
be employed to solve for :math:`\Theta` analytically. The estimate of the
unknown parameters is then

.. math::

   \hat{\Theta} = [\Gamma^T\Gamma]^{-1}\Gamma^T Y

For example if we fix the mass terms in the steer torque equation and let the
rest be free the linear equation is

.. math::

   \begin{bmatrix}
      v(1) \dot{\phi}(1) & v(1) \dot{\delta}(1) & g \phi(1) & g \delta(1) &
      v(1)^2 \phi(1) & v(1)^2 \delta(1) & - F(1)\\
      \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots\\
      v(N) \dot{\phi}(N) & v(N) \dot{\delta}(N) & g \phi(N) & g \delta(N) &
      v(N)^2 \phi(N) & v(N)^2 \delta(N) & - F(N)\\
   \end{bmatrix}
   \begin{bmatrix}
     C_{1\delta\phi}\\
     C_{1\delta\delta}\\
     K_{0\delta\phi}\\
     K_{0\delta\delta}\\
     K_{2\delta\phi}\\
     K_{2\delta\delta}\\
     H_{\delta F}
   \end{bmatrix}
   =
   \begin{bmatrix}
     T_\delta(1) - M_{\delta\phi} \ddot{\phi}(1) -
     M_{\delta\delta} \ddot{\delta}(1)\\
     \vdots\\
     T_\delta(N) - M_{\delta\phi} \ddot{\phi}(N) -
     M_{\delta\delta} \ddot{\delta}(N)
   \end{bmatrix}

The error in the fit is

.. math::

   \epsilon = \hat{Y} - Y = \Gamma \hat{\Theta} - Y

.. todo:: discuss how this solves for noise

This equation can be solved for each run individually, a portion of a run or if
there are :math:`P` runs then they can be all collected in :math:`\Gamma` for
best fit over multiple runs. If all the runs have the same number of time
steps, :math:`\Gamma` then becomes an :math:`NP \times M` matrix and :math:`Y`
an :math:`NP\times 1` vector if each run is the same length.

The covarance of the parameter estimatations can be computed with respect to
the error.

.. math::

   \sigma^2 = \frac{\epsilon^T\epsilon}{N - d}

.. math::

   U = \sigma^2 (\Gamma^T \Gamma)^{-1}

Secondly, all of the parameters in the canonical matrices need not be
estimated. The analytical benchmark bicycle model [Meijaard2007]_ gives a good
idea of which entries in the matrices we may be more certain about from our
physical parameters measurements in Chapter :ref:`physicalparameters`. I went
through the benchmark formulation and fixed the parameters based on these
rules:

- If the parameter is greatly affected by trail, leave it free.
- If the parameter is greatly affected by the front assembly moments and
  products of inertia, leave it free.
- If the parameter is equal or near to zero, fix it.

For the roll equation this leaves :math:`M_{\phi\delta}`,
:math:`C_{1\phi\delta}`, and :math:`K_{0\phi\delta}` as free parameters. And
for the steer equation this leaves :math:`M_{\delta\phi}`,
:math:`M_{\delta\delta}`, :math:`C_{1\delta\phi}`, :math:`C_{1\delta\delta}`,
:math:`K_{0\delta\phi}`, :math:`K_{0\delta\delta}`, :math:`K_{2\delta\delta}`,
and :math:`H_{\delta F}` as free. The choice of fixing the majority of the roll
equation is also justified by the smaller variance seen in the state space
estimation of the roll acceleration equation.

I start by identifying the three coefficeints of the roll equation for the
given time steps due to having much more certainty in the roll equation
estimates from first principles.

.. math::

   \begin{bmatrix}
      \ddot{\delta}(1) &
      v(1) \dot{\delta}(1) &
      g \delta(1) \\
      \vdots & \vdots & \vdots\\
      \ddot{\delta}(N) &
      v(N) \dot{\delta}(N) &
      g \delta(N) \\
   \end{bmatrix}
   \begin{bmatrix}
     M_{\phi\delta} \\
     C_{1\phi\delta} \\
     K_{0\phi\delta}
   \end{bmatrix}
   =
   \begin{bmatrix}
     H_{\phi F} F(1)
     - M_{\phi\phi} \ddot{\phi}(1)
     - C_{1\phi\phi} v(1) \dot{\phi}(1)
     - K_{0\phi\phi} g \phi(1)
     - K_{2\phi\phi} v(1)^2 \phi(1)
     - K_{2\phi\delta} v(1)^2 \delta(1) \\
   \vdots\\
     H_{\phi F} F(N)
     - M_{\phi\phi} \ddot{\phi}(N)
     - C_{N\phi\phi} v(N) \dot{\phi}(N)
     - K_{0\phi\phi} g \phi(N)
     - K_{2\phi\phi} v(N)^2 \phi(N)
     - K_{2\phi\delta} v(N)^2 \delta(N) \\
   \end{bmatrix}

I then I enforce the assumptions that :math:`M_{\phi\delta} = M_{\delta\phi}`
and :math:`K_{0\phi\delta} = K_{0\delta\phi}` to fix these values in the steer
equation to the ones identified in the roll equation, leaving less free
parameters in the steer equation. This matrix symmetry is likely enforced in
reality due to the simple coupling of the front and rear frames by a revolute
joint. It is also possible to solve the roll and steer equations simultaneously
and enforce the symmetry but this was the easier solution. Finally, I identify
the remaining steer equation coefficients.

.. math::

   \begin{bmatrix}
     \ddot{\delta}(1) &
     v(1) \dot{\phi}(1) &
     v(1) \dot{\delta}(1) &
     g \phi(1) &
     v(1)^2 \delta(1) &
     - F(1)\\
     \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
     \ddot{\delta}(N) &
     v(N) \dot{\phi}(N) &
     v(N) \dot{\delta}(N) &
     g \phi(N) &
     v(N)^2 \delta(N) &
     - F(N)\\
   \end{bmatrix}
   \begin{bmatrix}
     M_{\delta\delta} \\
     C_{1\delta\phi} \\
     C_{1\delta\delta} \\
     K_{0\delta\phi} \\
     K_{2\delta\delta} \\
     H_{\delta F}
   \end{bmatrix}
   =
   \begin{bmatrix}
     T_\delta(1)
     - \hat{M}_{\delta\phi} \ddot{\phi}(1)
     - K_{0\delta\delta} g \delta(1)
     - \hat{K}_{2\delta\phi} v(1)^2 \phi(1) \\
     \vdots\\
     T_\delta(N)
     - \hat{M}_{\delta\phi} \ddot{\phi}(N)
     - K_{0\delta\delta} g \delta(N)
     - \hat{K}_{2\delta\phi} v(N)^2 \phi(N) \\
   \end{bmatrix}

Results
~~~~~~~

I selected data for three riders on the same bicycle, performing two maneuvers,
on two different environments. I have little reason to believe the dynamics of
the passive system should vary much with respect to different maneuvers, but
there is potentially a small variation across riders primarily due to their
inertial properties and there may be variation across environments because of
the differences in the wheel to floor interaction. I opted to compute the best
fit model across series of runs to benefit from the large dataset. This leaves
these four scenarios:

- All riders in both environments (n=1)
- All riders in each environment (n=2)
- Each rider in both environments (n=3)
- Each rider in each environment (n=6)

.. list-table::

   * - Rider
     - Environment
     - Runs
     - N
   * - C
     - H
     - 24
     - 267773
   * - C
     - P
     - 87
     - 118700
   * - C
     - A
     - 111
     - 386473
   * - J
     - H
     - 57
     - 804995
   * - J
     - P
     - 93
     - 112582
   * - J
     - A
     - 150
     - 917577
   * - L
     - H
     - 25
     - 272719
   * - L
     - P
     - 88
     - 125878
   * - L
     - A
     - 113
     - 398597
   * - A
     - H
     - 106
     - 1345487
   * - A
     - P
     - 268
     - 357160
   * - A
     - A
     - 374
     - 1702647

A total of 12 different models can be derived from this perspective.

All riders in both environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here I'll make the assumption that the best fit model doesn't vary much across
riders or environments. The assumption that the passive model of the bicycle
and rider are similar with respect to rider can be justified by recognizing
that the Whipple model predicts little difference in the dynamics with respect
to the three bicycle/rider combinations. On the other hand, I have little
reason to believe the enviromenters are the same except that both floors are
made of a rubber like material. I calculated the best fit over 374 runs giving
about 142 minutes of data sampled at 200 Hz, :math:`N=1720000`.

.. figure:: figures/systemidentification/A-A-rlocus.*

   The root locus of the identified model (circle), the Whipple model
   (diamond), and the arm model (triangle) with respect to speed.

The eigenvalues as a function of speed of the identified model can be compared
to those of the Whipple and arm models. Figure :ref:`figAARloc` shows the root
locus of the three models. We see clearly that the weave mode exists in all
three models, with it being always stable in the arm model and with it being
unstable at lower speeds in the other two models. The identified model is
unstable over most of the shown speed range. Above 3 m/s or so, the Whipple
model's weave mode diverges from the identified model to different asymptotes.
The arm model weave mode diverges somewhere in between. Note that the arm model
has an unstable real mode for all speeds. Figure :ref:`figAAEig` gives a
different view of the root locus allowing one to more easily compare the real
eigenvalues. The imaginary parts of the weave mode have similar curavture with
respect to speed for all the models, with the identified model having about 1
rad/s larger frequency of osciallation for all speeds. The identified model
does have a stable speed range with the Whipple model underpredicting the weave
critical speed by almost 2 m/s. The identifed caster mode is much faster than
the one predicted by the Whipple model.

.. figure:: figures/systemidentification/A-A-eig.*

   Real and imaginary parts of the eigenvalues as a function of speed for model
   identified from all runs, the Whipple model and the arm model.

The identification process is structured around identifiying the input/output
relationship among measured varibles. The frequency response provides a view
into these relationships. Figures :ref:`fig` to :ref:`fig` give a picture of
how the first principles models compare to the identified model with respect to
frequency response. The frequency band from 1 rad/s to 12 rad/s is of most
concern as it is the range the human operates in.

The roll torque to roll angle shows that at 2 m/s the response if predicted
well at high frequencies by all the models and that the Whipple model predicts
the response well across all frequencies. At 4 m/s the two models only predict
the high frequency behavior (>4 rad/s) with the arm model being slightly better

.. figure:: figures/systemidentification/A-A-Tphi-Phi.*

   Frequency response of the three models at four speeds. The color indicates
   the model and the line type indicates the speed.

.. figure:: figures/systemidentification/A-A-Tphi-Del.*

   Frequency response of the three models at four speeds. The color indicates
   the model and the line type indicates the speed.

The steer torque to roll angle transfer function may be the most important to
model accurately as it is the primary method of controlling the bicycle's
direction. At 2 m/s the Whipple model magnitude matches at lower frequencies
better and the arm model better at higher frequencies. At all higher speeds the
Whipple and arm models don't match well at low frequencies.

.. figure:: figures/systemidentification/A-A-Tdel-Phi.*

   Frequency response of the three models at four speeds. The color indicates
   the model and the line type indicates the speed.

The steer torque to steer angle shows that speeds above 2 m/s the first
principle models do not predict the response well at low frequencies.

.. figure:: figures/systemidentification/A-A-Tdel-Del.*

   Frequency response of the three models at four speeds. The color indicates
   the model and the line type indicates the speed.

The response changes more drastically with respect to speed for the first
principles models than the identified model.

.. include:: tables/systemidentification/canonical-id-table-one.rst

.. include:: tables/systemidentification/canonical-id-table-two.rst

.. todo:: add this caption to the tables

Table Caption: Identified coefficients of the benchmark bicycle model for
various sets of data. The first column indicates which rider's runs were used:
(C)harlie, (J)ason, (L)uke or (A)ll. The second column indicates which
environment's runs were used: (P)avilion Floor, (H)orse Treadmill, or (A)ll.
The remaining columns give the resulting numerical value of the identified
parameter, its standard deviation with respect to the model fit, and the
percent difference with respect to the value predicted by the Whipple model.

Each rider in both environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: Show the differences in the three rider models and point out that
   Charlie seems more different.

Comparison of identified models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The identified models in Tables X and X have differences in their dynamics. The
measurement errors, model structure and order dictate how well the models can
predict the input-output behavior of each run or even each perturbation. I
would ultimately like to select one or a small set of models that generally do
a good job at predicting the measured behavior for each run. I have shown that
the Whipple and arm models may not give good enough predictions.

Figures X through X plot the steer torque to roll angle frequency response for
three speeds: 2 m/s, 5.5 m/s and 9.0 m/s for each of the models in Tables X and
X. At the lowest speed, all of the models have a similar frequency response,
especially in the frequency band between about 1 an 20 rad/s. At 5.5 m/s the
models are similar at a higher bandwith, 4 to 30 rad/s. At 9.0 m/s even higher,
10 to 50 rad/s. For all speeds the variation among the response is most likely
   well within the uncertainty of the models as group. The model derived from
   all of the data (all rider and all runs), gives somewhat of a mean model and
   if this model is significantly better at predicting the measured behavior of
   the Whipple and arm models, it may be a good general candidate model for
   this bicycle.

.. todo:: Make a plot showing how all of the identified models frequency
   responses compared at a single speed (could do multiple graphs. This would
   hopefully support choosing the one identified model for all runs.

.. figure:: figures/systemidentification/compare-id-bode-2.0.*

   Steer torque to roll angle frequency responses at 2.0 m/s for all the
   identified models in Tables X and X.

.. figure:: figures/systemidentification/compare-id-bode-5.5.*

   Steer torque to roll angle frequency responses at 5.5 m/s for all the
   identified models in Tables X and X.

.. figure:: figures/systemidentification/compare-id-bode-9.0.*

   Steer torque to roll angle frequency responses at 9.0 m/s for all the
   identified models in Tables X and X.

Notice that the frequency band where the models are most similar shifts to
higher frequencies at higher speeds.

The predictive capability of a given model can be quantified by mutliple
methods. I've made use of two criterion to judge the quality of a model with
respect to given data. The first is to simulate the system given the measured
inputs.  This method works well when the open loop system is stable, but if it
is unstable as so in the case of the bicycle, it may be difficult to simulate.
Searching for initial conditions that give rise to a stable model for the
duration of the run or simulating by weighting the future error less may
relieve the instability issues. Another option is to see how well the inputs
are predicted given the measured outputs. The canonical form of the equations
lend themselves to this check and only two inputs per run need be checked.

We designated the predicted torques on the system to be

.. math::

   y_p = M \ddot{q} + C \dot{q} + K q

and the measured torques to be

.. math::

   y_m = T + H F

:math:`y_p` and :math:`y_m` can be computed for each run along with the percent
variance explained by the model for both the total roll torque and the steer
torque

.. math::

   var = 1 - \frac{||y_p - y_m||}{||y_m - \bar{y}_m||}

This percentage can be used as criterion of which to judge the ability of model
versus another to predict the measurement.

I compute the percent variance for each of the 374 runs used in the canonical
identification outlined earlier using each of the 12 identified models and both
the Whipple and Arm models. This percentage can be used ascriterion of which to
judge the ability of model versus another to predict the measurement.  I then
take the median of the percent variances over 12 sets of runs corresponding,
each set corresponding to the set of runs used in computing the various
identified models. The results give an idea of how well the various models are
able to predict the data for all of the runs in a given set.

.. include:: tables/systemidentification/median-roll.rst

.. include:: tables/systemidentification/median-steer.rst

Tables X and X give the median percent fit for each set of runs in each column
for each model in given in the row for roll and steer respectively. The maximum
fit percentage in the column gives a measure of the best model for predicting
each indiviudal run in that set of runs. Intuitively I would expect that the
diagonal of the upper 12 rows would be the maximum in each column, but that is
not the case. I believe that this can be explained by the fact that there are
more outlier runs in some sets. These outliers have enough effect in the
resulting regressions, that the models generated from sets of runs with less
outliers are able to predict the data better.

The models are able to predict the steer torque much better than the roll
torque. The roll torque should be zero in all of the runs without disturbances.
We fixed six of the nine parameters in the roll equation to those of the
Whipple model and fixed three of the nine parameters in the steer equation.
This can partially explain why the steer predictions are better than the roll
predictions. The model for the roll torque is more suspectible to the noise in
the rate and angle measurements and has cosquenses of +/- X Nm variation in the
predicted roll torques. These are comparable to the measured roll torques. But
Table X can still be used to gage which models are better with reference to
each other. The values in Table X are only generated from the runs with
disturbances as a relative measure of quality to zero is hard to make.

.. todo:: Maybe this is where the complimentary filter should come in to play.
   Ultimately you'd like to measure the angle, angular rate and angular
   acceleration directly and with little noise so that they are all related to
   each other by the derivative. The second option is to measure some of the
   signals and then combine them in a way that the derivitive is enforced.

.. todo:: If the roll torque is supposed to be zero in the runs without
   disturbances, how do I measured the percent variance explained by the model?

Tables X and X reveal:

- The arm model is poor at predicting the steer torque.
- The models derived from Charlie's runs are poorer at predicting the inputs.
- The Whipple model is not really bad at predicting steer torque, but on median
  10% worse than the best models.
- The models identified from the pavilion runs are generally the best (with
  exception of Charlies). The ones generated from Luke and Jason's runs are
  typically the best at predicting both steer torque and roll torque, with
  Luke's giving better roll torque predictions.

It may seem odd that the model identified from the subset of runs one rider's
in one environments set of runs is the best at predicting the runs on a
individual basis, but the uncertaintiy and error in both the data and the model
structures don't dictate that this can't be. Keep in mind that all of the
frequency response of all 12 models shown in Figures X, X, and X are probably
bounded in the uncertainty of the prediced responses and each is can be
considered a "good" model and even including the Whipple model.

.. todo:: I probably should have checked the fits with respect to the manuevers
   too to make sure the models were very different...

The second method of evaluating the quality of the identified models is to
simulate the model with the measured inputs and compare the predicted outputs
with the measured outputs. I simulated all 14 models with the inputs from the
374 runs and computed the percent variance explained by the model for each
output. Since the models are typically unstable at all of the speeds we tested
at I search for the set of initial conditions which minimizes the percent
variance for all outputs. For the majority of runs and models, this is
sufficient to to have a stable simulation for the the duration of the run.
However, this is not always the case. For long duration runs I select a random
20 second section of the data to simulate, reducing the likelihood that the
simulation blows up.  Finally, I ignore any outputs varainces that are less
than -100 percent as they are most likely due to unstable simulations. Table X
presents the median percent variance across all runs for each model and each
output. The best model seems to be the one generated from the data with Luke on
the Pavilion Floor, once again but these results differ from the previous
otherwise.

- For all outputs other than roll angle, the arm model is better than the
  Whipple model.
- The models from Charlie's data fair much better than the input comparisons
  and are better than some of Jason's.
- The model identified from the data with Jason on the Pavilion floor is very
  poor in roll angle predicition as opposed to it being a good choice from the
  input comparison results.
- All of the identified models are better predictors than the first principles
  models.

.. todo:: the AIC could be checked for all these models to compare their
   quality

.. include:: tables/systemidentification/output-median.rst

The mean percent variance across the outputs can be computed and the models
ranked by the mean. The best model seems to be LP and the AA is also a pretty
good predictor. Notice that the Whipple model is poorer than the arm model.

+----------+-----------+
| Model    | Mean      |
+==========+===========+
| LP       | 57.572049 |
+----------+-----------+
| AP       | 53.089569 |
+----------+-----------+
| LA       | 52.484939 |
+----------+-----------+
| AA       | 51.848794 |
+----------+-----------+
| JA       | 51.062998 |
+----------+-----------+
| LH       | 48.452488 |
+----------+-----------+
| CH       | 47.660752 |
+----------+-----------+
| AH       | 47.187107 |
+----------+-----------+
| JH       | 45.310893 |
+----------+-----------+
| CA       | 45.241640 |
+----------+-----------+
| CP       | 38.507042 |
+----------+-----------+
| JP       | 31.948126 |
+----------+-----------+
| Arm      | 12.328113 |
+----------+-----------+
| Whipple  |  1.827987 |
+----------+-----------+

.. todo:: show output comparison plot for one run with the top two and bottom
   two models.

The orange line in Figure :ref:`figCoefficients` is that of the L-P model and
allows us to compare the results of the canonical identification process with
those of the state space models. The L-P model seems to obviously be better at
fitting the data, especially in the steer equation. This lends more confidence
that this is a better model choice than the Whipple and arm model.

Discussion
~~~~~~~~~~

Canonical formulation
   The canonical realization seems to be a good method for identifiying a model
   for data from mutliple runs. It relies on quality measurements of the
   coordinates, their rates and accelerations. I use numerical differentiation
   of the rates to get the accelerations instead of direct measurements and the
   angles are not perfectly related to the rates through differentiation
   because they were measured from different sensors. The noise in the
   measurements and whether the measurements are accurately the derivatives of
   one another have bearing on the results. It is possible to identify all of
   the entries in the canonical matrices, but it is likely some of those are
   easily predicted from first princples and I fix them if that is the case.
   This leaves the roll equation mostly fixed and the steer equation mostly
   free and the results reflect better fits with respect to steer than roll as
   a result. This formulation does not explicitly account for process noise, so
   it may be be suspectible to similar accuracy errors as the state space
   formulation does.

   It is suprising that a model from a small subset of the data is better at
   predicting all of the runs on an individual basis.
Input comparison
   The input prediction comparisons do not predict the roll torque well at all.
   It seems that the roll equation magnifies the noise in the coordinate, rate
   and acceleration measurments such that the resutling noise in the roll
   torque is equivalent in magnitude to the roll perturbations. But the roll
   pertubations do seem to clearly be present in the predictions. This results
   in difficultly comparing the quality of the resulting models with respect to
   the roll equation.
Output comparison
   The output comparison (simulations) give more reasonable results because all
   four outputs generally fit well across runs given the measured inputs.  It
   is suprising that the ranking of model predition ability is different for
   the input comparisons than the output comparisons, but the fact that the
   model identified from Luke's pavilion runs is the best from both
   comparisons, at least gives credencen to it further adoption. The first
   principles models are dead last in the ranking and the model identified from
   Jason's pavilion runs is suprisingly poor due to poor roll angle prediction.
Whipple model
   The input comparisons show that the Whipple model is relatively reasonable
   at predicting the data but the output comparisons make it out to be much
   poorer. The Whipple model is clearly the worst at explaining the variance in
   the steer angle, roll rate and steer rate outputs and is second to worst in
   roll angle.

   Also contrary to the Whipple model predictions, the weave mode of all
   identified models are unstable until at least 8-9 m/s or so. The caster mode
   is also typically much faster in the identified models. This implies that
   the real system does not benefit from open loop stability at all during most
   normal speed bicycling and that the rider is always responsible for
   stabilizing the vehicle. This may explain why none of the riders ever felt
   comfortable enough to try hands-free riding while strapped into the harness.
Arm model
   I had hypothesized that the arm model would better predict the measured
   motion because it more accurately modeled the fact that we allowed the rider
   full use of his arms to control the steering. This was validated with
   respect to the output simulation comparsons. They predict that the arm model
   is much better than the Whipple model for most of the output variables. But
   this is in constract to the input comparison predictions which were
   opposite, with the Whipple being much better than the arm model. More work
   is needed to verify which model is better, but I'm leaning with the output
   comparison results myself.
Rider biomechanics may mot be modeled
   The models identified from Charlie's runs are different than those of Jason
   and Luke. The models from Charlie's runs do not predict the runs very well,
   even including the subset of Charlie's. I'm not sure if the rider's arm
   stiffness can affect these results. Or how much the different riders can
   effect this if we are only searching for the passive bicycle-rider model.
   The other potenital explanation is that I have too many outliers in
   Charlie's runs. This could have something to do with all of the runs that
   had sycronization issues.
Predicting derivatives
   The roll angle is more poorly predicted than the other variables. The steer
   angle and steer rate are better predicted than the roll angle and roll rate.
   In the output comparisons we enforce that the roll rate is the derivative of
   the roll and the same for the steer varibles. The poorer predictions of roll
   angle is probably due to noise and error in the indepedent measurements of
   these variables. I toyed with complementary filters to try an combine the
   angle and rate measurements in a way that filtered and enforced the
   derivative relationship between the measured varialbes, but did not have
   much luck improving the results. It may be better to focus on one each of
   the roll and steer variables for minimization purposes. It is well known
   that fitting models with much fewere inputs to outputs is difficult and the
   fewer ouputs reduces the number of noise terms to estimate.

Conclusion
~~~~~~~~~~

The best candidate model for the measured system is the model identified from
the data subset with rider Luke and the pavilion floor. I find no reason to use
different models for each rider, environment as this model does a better job at
predicting than the other models derived from matching subsets. I will use the
model identified from the set of runs with Luke on the pavilion floor as the
base bicycle model for identifying the controller for all the runs in the
following section of this Chapter. I could use the individual bicycle
identifications for each run, but using a model derived from a set of runs has
the advantage that it will be less affected by the lack of identifying the
process noise explicitly.

Suggestions for improving the results.

- Fit to MISO, fix the :math:`a_{\phi\delta}` coefficient and make the noise
  with respect to the kinematical equations equal to zero giving 11-13 total
  parameters to fit
- Using model reduction techniques to combine many MISO and SISO models for a
  given run.
- Use better initial guess techniques and try global optimizers to get to the
  best solution

Rider Controller Identification
===============================

Do I really have to figure this out?? Yes.

Now that I have a reasonable estimate of the plant, the rider control system
can be identified. There are many control structures that can and may work to
explain the data. If the feedback and input variables are the same for a set of
cotnrol strucutres they can be mapped to each other and are equivalent. Much of
the difference in control structures such as PID, sequential loop closure, LQR
are the physcial interpretations of the gains, delays, and such. Here I limit
our control structure the one developed in [Hess2012]_ and Chapter
:ref:`control`. With this stucture, I will have the ability to compare the
results with the theorectical hypothesis we developed.

Grey Box Models
---------------

The block diagram control structure in Chapter :ref:`control` can be written in
state space form, which will be used in the identificatin procedure defined in
the previous section. I'll develop forms for pure heading tracking and lateral
deviation tracking.

.. todo:: maybe add the block diagram again here

The bicycle block for lateral deviation tracking has states :math:`x_b = \left[
\phi \quad \delta \quad \dot{\phi} \quad \dot{\delta} \quad \psi \quad y_p
\right]^T`, inputs :math:`u_b = \left[ T_\delta \quad F \right]^T`, and outputs
:math:`y_b = \left[ \delta \quad \phi \quad \dot{\phi} \quad \psi \quad y_q
\right]^T`. The state, input and output matrices are follows

.. math::
   :label: eqBicycleStateSpace

   \mathbf{A}_b
   =
   \begin{bmatrix}
     0 & 0 & 1 & 0 & 0 & 0 \\
     0 & 0 & 0 & 1 & 0 & 0 \\
     a_{b\ddot{phi}\phi} & a_{b\ddot{phi}\delta} &
     a_{b\ddot{\phi}\dot{\phi}} & a_{b\ddot{\phi}\dot{\delta}} &
     0 & 0 \\
     a_{b\ddot{\delta}\phi} & a_{b\ddot{\delta}\delta} &
     a_{b\ddot{\delta}\dot{\phi}} & a_{b\ddot{\delta}\dot{delta}} & 0 & 0 \\
     0 & a_{b\dot{\psi}\delta} & 0 & a_{b\dot{\psi}\dot{\delta}} & 0 & 0\\
     0 & 0 & 0 & 0 & a_{b\dot{y}_p\psi} & 0
   \end{bmatrix}

   \mathbf{B}_b
   =
   \begin{bmatrix}
     0 & 0 \\
     0 & 0 \\
     b_{b\ddot{\phi}T_\delta} & b_{b\ddot{\phi}F} \\
     b_{b\ddot{\delta}T_\delta} & b_{b\ddot{\delta}F} \\
     0 & 0 \\
     0 & 0
   \end{bmatrix}

   \mathbf{C}_b
   =
   \begin{bmatrix}
     0 & 1 & 0 & 0 & 0 & 0 \\
     1 & 0 & 0 & 0 & 0 & 0 \\
     0 & 0 & 1 & 0 & 0 & 0 \\
     0 & 0 & 0 & 0 & 1 & 0 \\
     0 & 1 & 0 & 0 & c_{by_q\psi} & c_{by_qy_p} \\
   \end{bmatrix}

The neuromuscular block is described by the transfer function

.. math::
   :label: eqNeuromuscular

   G_{nm}(s) = \frac{\omega_{nm}^2}{s^2 + 2 \zeta_{nm} \omega_{nm}s + \omega_{nm}}

and can be written in state space form with the states :math:`x_{nm} = \left[
T_\delta \quad \dot{T}_\delta \right]^T`, input :math:`u_{nm} = U_{nm}` and
output :math:`y_{nm} = T_\delta`.

.. math::
   :label: eqNeuroStateSpace

   \mathbf{A}_{nm}
   =
   \begin{bmatrix}
     0 & 1 \\
     -\omega^2 & - 2 \zeta \omega
   \end{bmatrix}

   \mathbf{B}_{nm}
   =
   \begin{bmatrix}
     0 \\
     \omega^2
   \end{bmatrix}

   \mathbf{C}_{nm}
   =
   \begin{bmatrix}
     1 & 0
   \end{bmatrix}

The combined plant (rider nueromuscular model and bicycle) has states
:math:`x_p = \left[ \phi \quad \delta \quad \dot{\phi} \quad \dot{\delta} \quad
\psi \quad y_p \quad T_\delta \quad \dot{T}_\delta \right]^T`, inputs
:math:`u_p = \left[ F \quad U_{nm} \right]^T`, and outputs :math:`y_p = \left[
\delta \quad \phi \quad \dot{\phi} \quad \psi \quad y_q \right]^T`. The state,
input and output matrices are follows

.. math::
   :label: eqPlantStateSpace

   \mathbf{A}_p
   =
   \begin{bmatrix}
     \mathbf{A}_b & \mathbf{B}_{bT_\delta} & 0_{6 \times 1} \\
     0_{2 \times 6} & \mathbf{A}_{nm}
   \end{bmatrix}

   \mathbf{B}_p
   =
   \begin{bmatrix}
     \mathbf{B}_{bF} & 0_{6 \times 2} \\
     0_{2 \times 1} & \mathbf{B}_{nm}
   \end{bmatrix}

   \mathbf{C}_p
   =
   \begin{bmatrix}
     \mathbf{C}_b & 0
   \end{bmatrix}

The sequential loop closure dictates that the commanded output variables are

.. math::

   \psi_c = k_{y_q} ({y_q}_c - y_q)

   \phi_c = k_\psi (\psi_c - \psi)

   \dot{\phi}_c = k_\phi (\phi_c - \phi)

   \delta_c = k_\dot{\phi} (\dot{\phi}_c - \dot{\phi})

and the input to the neuromuscular block as a function of the desired path
is

.. math::

   U_{nm} = k_\delta * (\delta_c - \delta)

The input to the neuromuscular block can be written in linear form as

.. math::

   U_{nm}
   =
   \begin{bmatrix}
     -k_\delta k_\phi k_\dot{\phi} k_\psi \\
     -k_\delta k_\phi k_\dot{\phi} \\
     -k_\delta \\
     -k_\delta k_\dot{\phi} \\
     -k_\delta k_\phi k_\dot{\phi} k_\psi k_{y_q} \\
     k_\delta k_\phi k_\dot{\phi} k_\psi k_{y_q}
   \end{bmatrix}^T
   \begin{bmatrix}
      \psi \\
      \phi \\
      \delta \\
      \dot{\phi} \\
      y_q \\
      y_c \\
   \end{bmatrix}

The closed loop state space for lateral deviation tracking can be form by
inserting the controller output :math:`U_{nm}` into the plant dynamics
:math:`(\mathbf{A}_p,\mathbf{B}p)` to rearrange the plant state space to be a
function of the desired path and the lateral force, :math:`u_l = \left[ F \quad
y_{qc} \right]^T`. The closed loop system :math:`(\mathbf{A}_p,\mathbf{B}p)`
takes the same form as the plant system with excepetion to the steer torque
acceleration equation, which is now a function of the controller gains, the
neuromuscular parameters and the desired path of the front wheel contact point.
The new entries to the state matrix are

.. math::
   :label: eqLateralStateSpace

   x_l = \left[ \phi \quad \delta \quad \dot{\phi} \quad \dot{\delta} \quad
   \psi \quad y_p \quad T_\delta \quad \dot{T}_\delta \right]^T

   u_l = \left[ F \quad y_{qc} \right]^T

   \mathbf{A}_l
   =
   \begin{bmatrix}
     0 & 0 & 1 & 0 & 0 & 0 & 0 & 0\\
     0 & 0 & 0 & 1 & 0 & 0 & 0 & 0\\
     a_{b\ddot{\phi}\phi} &
     a_{b\ddot{\phi}\delta} &
     a_{b\ddot{\phi}\dot{\phi}} &
     a_{b\ddot{\phi}\dot{\delta}} &
     0 & 0 & 0 & 0\\
     a_{b\ddot{\delta}\phi} &
     a_{b\ddot{\delta}\delta} &
     a_{b\ddot{\delta}\dot{\phi}} &
     a_{b\ddot{\delta}\dot{\delta}} &
     0 & 0 & 0 & 0\\
     0 & a_{b\dot{\psi}\delta} & 0 & a_{b\dot{\psi}\dot{\delta}} & 0 & 0 & 0 & 0\\
     0 & 0 & 0 & 0 & a_{b\dot{y}_p\psi} & 0 & 0 & 0 \\
     0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
     -\omega^2 k_\delta k_\dot{\phi} k_\phi &
     -\omega^2 k_\delta (1 + c_{b y_q \delta} k_\dot{\phi} k_\phi k_\psi k_{y_q}) &
     -\omega^2 k_\delta k_\dot{\phi} &
     0 &
     -\omega^2 k_\delta k_\dot{\phi} k_\phi k_\psi (1 + c_{b y_q \psi} k_{y_q}) &
     -\omega^2 k_\delta k_\dot{\phi} k_\phi k_\psi k_{y_q} &
     -\omega^2 &
     -2 \omega \zeta
   \end{bmatrix}

   \mathbf{B}_l
   =
   \begin{bmatrix}
     0 & 0 \\
     0 & 0 \\
     b_{b\ddot{\phi}F} & 0 \\
     b_{b\ddot{\delta}F} & 0 \\
     0 & 0 \\
     0 & 0 \\
     0 & \omega^2 k_\delta k_\dot{\phi} k_\phi k_\psi k_{y_q}
   \end{bmatrix}

The output matrix can be constructed to provide any desired outputs, which I
choose a subset of the outputs we measured during the experiments such as steer
angle, roll rate, steer torque, etc.

Given that the bicycle model is known this analytical state space
representation is parameterized by seven parameters: the five controller gains
and the two neuromuscular parameters. The seven parameters are uniquely
idenfitiable. The model is eighth order with two inputs.

.. todo:: i think they are uniquely identifiable but I'm not real sure how to
   check this throughly. it is function of what inputs and outputs that are
   measured

.. todo:: This next paragraph may be wrong. A state feedback would be something
   like (A-BK)x where x is 6 x 1, B is 6 x 1 and K is 1 x 6 to get a gain
   matrix single steer torque which is effectively the same as what is here,
   except that our gains have a different interpretation. How does this relate
   (A-BK)x? or the basic full state feedback. Interesting to note that the gain
   structure is all multiplied by the neuro frequency. It is akin to only
   having gains in the bottom row of the full state feedback K matrix, this
   would only add gains to the bottomr row of A-BK.

Notice that the controller is unlike an state or output feeback model in the
sense that the gains only have the ability to affect a single row in the A and
B matrices. This reflects the some of the inherent limitations in the human has
for sensory and acutuation in this system. Output feeback systems often have an
observer so that full estimated state feedback can be used. This model assumes
that the rider does not have that abitily and is able to sense noisy outputs
and adjust his torque compesation within the limits of his neuromuscular system
based on five simple gains.

I also make use of a second closed loop model which is essentially the same,
but the outer lateral deviation tracking loop is removed and tracking a
commanded heading is left. This model is seventh order with two inputs.

.. math::
   :label: eqHeadingStateSpace

   x_h = \left[ \phi \quad \delta \quad \dot{\phi} \quad \dot{\delta} \quad
   \psi \quad T_\delta \quad \dot{T}_\delta \right]^T

   u_h = \left[ F \quad \psi_c \right]^T

   \mathbf{A}_h
   =
   \begin{bmatrix}
     0 & 0 & 1 & 0 & 0 & 0 & 0 \\
     0 & 0 & 0 & 1 & 0 & 0 & 0 \\
     a_{b\ddot{\phi}\phi} & a_{b\ddot{\phi}\delta} &
     a_{b\ddot{\phi}\dot{\phi}} & a_{b\ddot{\phi}\dot{\delta}} &
     0 & 0 & 0 \\
     a_{b\ddot{\delta}\phi} & a_{b\ddot{\delta}\delta} &
     a_{b\ddot{\delta}\dot{\phi}} & a_{b\ddot{\delta}\dot{\delta}} & 0 & 0 & 0 \\
     0 & a_{b\dot{\psi}\delta} & 0 & a_{b\dot{\psi}\dot{\delta}} & 0 & 0 & 0 \\
     0 & 0 & 0 & 0 & 0 & 0 & 1 \\
     -\omega^2 k_\delta k_\dot{\phi} k_\phi &
     -\omega^2 k_\delta &
     -\omega^2 k_\delta k_\dot{\phi} &
     0 &
     -\omega^2  k_\delta k_\phi k_\dot{\phi} k_{\psi} &
     -\omega^2 &
     -2 \omega \zeta
   \end{bmatrix}

   \mathbf{B}_h
   =
   \begin{bmatrix}
     0 & 0 \\
     0 & 0 \\
     b_{b\ddot{\phi}F} & 0 \\
     b_{b\ddot{\delta}F} & 0 \\
     0 & 0 \\
     0 & 0 \\
     0 & \omega^2 k_\delta k_\phi k_\dot{\phi} k_\psi
   \end{bmatrix}

The numerical values from the model derived from Luke's runs in the pavilion
were used to populate the bicycle state space entries, except for the entries
in the heading and lateral deviation acceleration equations which were
calculated with the Whipple model. This has the consequence that those entries
are developed with potentially erronous geometric values such as trail.

In the following analysyses the Kalman gain matrix is assumed to be equal to
zero and the model takes on an output error form. This was required to bring
the number of parameters to a reasonable size and provide a chance at finding
the optimal solution.

Data
----

Only the runs with lateral disturbances are suitable for identifying the rider
controller. I used the subset of 262 valid disturbance runs for the following
analysis. This subset included runs from all three riders, both environments
and both the lateral deviation and heading tracking maneuvers. All signals had
their means subtracted except for the lateral force.

Identification
--------------

Through trial and error with many different approaches [#]_ to identification,
I found that the optimal solution was not a trivial problem. The SIMO problem
with noise full noise estimation has a minimum of 15 parameters. This problem
is fraught with local minima. Even with the assumption of an output error
structure and the reduced parameter space to seven, doesn't escape the
difficulty of finding the true minima. To have a decent chance at finding a
good solution, I opted to identify only the SISO system with the lateral force
as the input and the steering angle as the output. The choice of steer angle as
the sole output is much the same reason as [Lange2011]_. The steer angle is a
very good quality measurement and along with steer torque reflects the rider's
contribution to the system dynamics as a reaction to the lateral force.

I used the prediction error method [Ljung1999]_ to find the optimal parameters
for each run.  A good solution required good initial parameter guesses of which
I used a combination of stable starting guesses from the loop closure technique
described in Chapter :ref:`control` and using random guesses from previous good
and bad solutions as starting points.

The criteria for a good model was based on the percentage of variance in the
measurement output explained by the model. The mean percent variance for all
the identified runs is :math:`62 \pm 12 %`, and considering the large relative
human remnant, fits above 30% are still relatively good. I ensured stability on
in the identified models and no issues associated with unstable simulations
corrupting the model quality criteria were present.

It turned out that the identified parameters for the SISO model not only
predicted the steer angle, but when extra outputs are added it predicts them
well too.

1. Process, filter and detrend the data.
2. Construct the SISO (I: :math:`F_B`, O: :math:`\delta`) grey box state space model.
3. Identify the five gains and the neuromuscular frequency for the lateral
   force and steer angle data using a variety of initial parameter guesses.
4. Construct the SIMO grey box state space model.
5. Identify the six parameters as before using the result of the SISO
   identification as the initial parameter guess.

.. figure:: figures/systemidentification/rider-id-treadmill-run.*
   :width: 4in

   Simulation of an identified model derived from the inputs and outputs (SIMO)
   of one of Charlie's treadmill runs #288 (4.23 m/s) validated against the
   data from run #289 (4.22 m/s). The black line is the processed and filtered
   (low pass 15 hz) measured data, the blue line is the simulation from the
   identified SIMO model and the green line is the identified SISO model.

.. figure:: figures/systemidentification/rider-id-pavilion-run.*
   :width: 4in

   Simulation of an identified model derived from the inputs and outputs (SIMO)
   of one of Luke's pavilion runs #657 (3.99 m/s) validated against the data
   from run #658 (3.74 m/s). The black line is the processed and filtered (low
   pass 15 hz) measured data, the blue line is the simulation from the
   identified SIMO model, and the green line is the identified SISO model.

The results in Figures X and X give average examples of the model's ability to
predict the measured data in two different runs. Notice that the human's
remnant is relatively large especially in the treadmill run. The model
generally predicts the human's initial control response to the external input.
This response is very repeatable across riders and runs with the level of
remnant minimized in the second after the perturbation. The model considers the
remnant as output error during the non perturbed portions of the run. Notice
that the steer torque is well predicted around the perturbation. Previous
identifications with the Whipple model predicted much lower torque magnitudes
and much different parameters. Including the identified bicycle model proved to
give better control predictions.

Results
-------

I computed the optimal five gains and neuromuscular frequency for all 262 runs
and recorded the percent variance of the steer angle output explained by the
model for each run along with the identified parameters.

The first set of quantities of interest are the identified parameters
themselves. As I've already mentioned in the previous section, identifying the
parameters accurately is a function of the number of free parameters, which
parameters are free and the quality of the noise model. In my case, our noise
model is an output error structure and may contribute to much more spread in
the identified parameters. Figure X gives an idea of how the six identified
speeds vary with speed. As shown in Chapter :ref:`control` the theory predicts
that the gains are linear above about 2 m/s and that the neuromuscular
frequency is a constant parameter with respect to the human operator.

- The gains increase with speed with :math:`k_\phi` and :math:`k_{y_q}` having
  small slopes.
- The low speed runs have much more spread. This is probably due to the fact
  that the human remnant is relatively large at these speeds and the model
  attempts to fit the noise rather than casting it as output error.
- The ~9 m/s have poorer data quality than other runs due to the treadmill
  interference in the measurement electronics, thus the spread is large.
- The neuromuscular frequency stays relatively constant just below 30 rad/s
  barring the higher variability in the low speed runs.

.. figure:: figures/systemidentification/par-vs-speed-box-all.*

   Each of the five idenitifed parameters as a function of speed. The parameter
   values are grouped into 0.5 m/s speed bins and boxplots showing their
   distrubutions are given for each speed bin. The red line gives the median of
   the speed bin, box bounds the quartiles and the whisker the 1.5 times the
   inner quarile range. The width of the boxes are proportional to the square
   of the number of runs in the bin. The green line gives the linear fit to the
   median values which are weighted with respect to the standard deviation of
   each speed bin. The neuromuscular frequency is the best constant that fits
   the data.

Loop Shaping
~~~~~~~~~~~~

The values of the parameters are difficult to directly compare with the ones
found by the loop shaping technique described in Chapter :ref:`control` due to
some of the educated guesses about the rider's internal control choices. But it
is possible to evaluate the same loops' frequency responses in an effort to
understand how the rider chooses the gains.

Figure X shows the frequency response of the closed the inner most loop a
single speed bin. The theory presented in [Hess2012]_ and Chapter
:ref:`control` postulates that the rider chooses a gain such that the damping
ratio of the high frequency neuromuscular around 10 rad/s and about gives about
a 10 db peak (:math:`\zeta=0.15`). Figure X shows that there may be a more
heavily damped neuromuscular peak, but the large variability in the lower
frequencies indicates that this may not always be the rider's choice. This may
be explained by the fact that it is most critical to for the roll rate loop to
exhibit the neuromuscular peaking and that there are not unique gains in the
first too loops to achieve this.

.. figure:: figures/systemidentification/all-delta_deltac-4.*

   Frequency responses of the closed steer angle loop. The grey lines plot the
   response of each individula run in the speed bin while the solid black line
   give the mean gain and phase bounded by the dotted black lines which
   indication the one sigma standard deviation.
   .. todo:: I'm not sure what the positive and negative phase shifts mean with
      regards to a closed loop Bode plot.

Figure X shows the frequency response of the closed roll rate loop
:math:`\frac{\dot{\phi}}{\dot{\phi}_c}(s)`. As was just pointed out, the theory
is that this loop which completes the inner control loop, must exhibit this
typical neuromuscular peaking seen in human-machine control tasks. The mean
magnitude plots indicates that this is the case and that the riders do choose
their steer and roll rate gains such that the inner loops exhibit the typical
response.

.. figure:: figures/systemidentification/all-phiDot_phiDotc-4.*

   Frequency responses of the closed roll rate loop. The grey lines plot the
   response of each individula run in the speed bin while the solid black line
   give the mean gain and phase bounded by the dotted black lines which
   indication the one sigma standard deviation.

Our theory for the selection of the remaining three gains suggests that the
loops follow the dictates of the crossover model (i.e. 20 db slope around
crossover) and that the crossover frequencies start at 2 and each successive
loop is closed at half the previous crossover frequency such that the roll
angle, heading and lateral deviation loops are closed in that order. Figures X
through X show the empirically derived frequency responses for the remaining
loops.

.. figure:: figures/systemidentification/all-phi_ePhi-4.*

   Frequency responses of the open roll angle loop. The grey lines plot the
   response of each individual run in the speed bin while the solid black line
   give the mean gain and phase bounded by the dotted black lines which
   indication the one sigma standard deviation.

.. figure:: figures/systemidentification/all-psi_ePsi-4.*

   Frequency responses of the open heading loop. The grey lines plot the
   response of each individual run in the speed bin while the solid black line
   give the mean gain and phase bounded by the dotted black lines which
   indication the one sigma standard deviation.

.. figure:: figures/systemidentification/all-yQ_eyQ-4.*

   Frequency responses of the open lateral deviation loop. The grey lines plot the
   response of each individual run in the speed bin while the solid black line
   give the mean gain and phase bounded by the dotted black lines which
   indication the one sigma standard deviation.

The median crossover frequencies for this bin are :math:`w_{\phi c}=3.66`,
:math:`w_{\psi c}= 0.98`, and :math:`w_{y_q c}=1.06`. This indicates that the
rider is more aggressive than our theory with the higher roll crossover
frequency in the roll angle loop. Also, the riders do not crossover at half the
previous frequency, with the two outer loops crossing over at about the same
frequency indicating that the lateral deviation tracking is more pertinent to
the rider than the theory suggests. This may be partially due to the narrowness
of the treadmill which constitutes 80% of the data.

Our hypothesis is that the crossover frequencies are constant with respect to
speed, so the distribution of the crossover frequencies for all runs should
have a tight distribution regardless of speed. Secondly, we postulated that the
rider crosses the roll angle loop around 2 rad/s. Figure X shows the
distribution of the crossover frequencies for each loop where the median
values of the crossover frequencies are :math:`w_{\phi c}=3.31`,
:math:`w_{\psi c}= 1.20`, and :math:`w_{y_q c}=0.98`, all with relatively large
standard deviations.

.. figure:: figures/systemidentification/crossover-all.*

Full System Response
~~~~~~~~~~~~~~~~~~~~

Once the loops are all closed the system output response to the two inputs
:math:`F_B` and :math:`y_{qc}` can be examined. Given a commanded input
:math:`y_{qc}`, the tracking performance can be gauged by the closed loop Bode
plot :math:`\frac{y_q}{y_{qc}}(s)` given in Figure X. Notice that in general,
the response is well behaved with a 0 dB magnitude out to about 10 rad/s, all
poles are stable and the phase lag increases gradually with frequency.

.. figure:: figures/systemidentification/all-yQ_yQc-4.*

   Frequency responses of the closed system lateral devaition tracking
   response. The grey lines plot the response of each individual run in the
   speed bin while the solid black line give the mean gain and phase bounded by
   the dotted black lines which indication the one sigma standard deviation.

Similarly, the system's response to the lateral disturbance force is favorable
for all the identified models. Figure X shows a similar stable response.

.. figure:: figures/systemidentification/all-yQ_fB-4.*

   Frequency responses of the closed system disturbance recovery response. The
   grey lines plot the response of each individual run in the speed bin while
   the solid black line give the mean gain and phase bounded by the dotted
   black lines which indication the one sigma standard deviation.

.. figure:: figures/systemidentification/all-tDelta_fB-4.*

   Frequency responses of the closed system disturbance recovery response for
   steer torque. The grey lines plot the response of each individual run in the
   speed bin while the solid black line give the mean gain and phase bounded by
   the dotted black lines which indication the one sigma standard deviation.

Conclusion
----------

I have shown that the rider controller can be identified from the collected
data. The basic conclusions are:

- The fundamental, remnant-free, control response of the rider under lateral
  perturbations can be described reasonably well by the simple five gain
  sequential loop closure and an eighth order closed loop system.
- The identified gains seem to exhibit linear trends with respect to speed as
  predicted by theory and the identified neuromuscular frequency seems to be
  constant with a median around the theoretical prediction of 30 rad/s.
- The identified parameters show resemblance to the patterns in the theoretical
  loop closure techniques. Especially that the rider selects their gains such
  that the closed roll rate loop exhibits a 10 db peak around 10-11 rad/s and
  that the riders cross over the outer three loops in the predicted order.
- The parameters do not seem to be unique if the neuromuscular damping ratio is
  included.

All of these conclusions are based on a weak and preliminary statistical view
of the data. I believe the spread in the results can be tightened up
significantly with further data processing and the use of simple statistical
methods.

Improving the bicycle model.
   To have any hope of identifying a realistic and accurate controller, the
   plant must have a very good representative model. The bicycle is an
   excellent platform for testing the human's control system due to it's low
   speed instability and the fact that non-trivial control is needed to stabilize
   and direct the non-minimum phase system, but the first principles models for
   bicycle/rider biomechanics are not yet adequate enough to describe the
   plant. This is mostly due to poor understanding of the tire to ground
   interaction and the rider's complicated coupling to the bicycle frames in
   which the rider is free to use a multitude of actuations for control.
   But, as has been shown here, system identification can be used to develop a
   realistic plant model for specific bicycles and even small variation in
   riders. A data driven model is currently the best choice until the first
   principles models catch up.
Estimating the process noise matrix.
   The better one can estimate the process noise in the system, the more
   accurate the parameter predictions will get. In all of my attempts I had
   little success in every estimating the optimal model when some or all of the
   process noise parameters were free. For the controller portion, the process
   noise is not awfully different than the rider's control actions to the
   disturbance and it is very apparent in the low speed runs. This type of
   noise is much more difficult to properly account for. The parameter
   estimates from the output error structures used in this study are
   susceptible to the model fitting the noise and the control actions as
   opposed to just the control actions. The identifications fortunately were
   able to fit the control actions and not the noise and this is much more
   apparent and true in the treadmill runs. It may be possible to developed
   estimates to the process and measurement noise covariance matrices from the
   undisturbed runs where the human's remnant is the dominant source of
   variability in the outputs.
Fixing the neuromuscular model.
   The results give some indication that the neuromuscular model is an
   appropriate choice. The gain identification could possibly be improved by
   fixing both the neuromuscular frequency and damping ratio, and only
   estimating the gains. In general, the more parameters you can be confident
   about via first principles, the easier the model may fit the data.
Removing outliers.
   A more systematic approach to the removal of outlier data using criteria
   from the resulting fit variance, parameters, and, frequency responses would
   help tighten up the data. The outliers are quite apparent in the data I've
   shown and a detailed look at why they are outliers may allow many of them to
   be removed.
Mixed effects modeling.
   To take into account all the factors and repeated experiments there are
   statistical methods available that can account for these. One such is mixed
   effects or multilevel modeling. I explored the use of these in a preliminary
   fashion but need more time to understand the methods so that I apply them
   correctly.

If I had unlimited time, I would work on these ideas more thoroughly. The data
is available if others would like to try out different methods, plant models,
bicycle models, etc.

.. rubric:: Footnotes

.. [#] I spent some time trying to regress models to each of the speed dependent
   coefficients in the state space model by assuming either a constant, linear
   or quadratic line. I tried simple regression techniques and also some mixed
   effects techniques to obviate the fact that some of the speed bins had many
   more runs than others. This method may be able to find a better model, but
   needs more work.

.. [#] I tried many ways of identifiyig: explain a little

.. [#] The nueromuscaulr damping ratio was fixed to 0.707 as per [XXXX]_. The
   uniqueness of the identifiablity of the parameters is question if this is not
   fized, as wildly different solutions for the neuromuscular frequency were often
   found if the damping ratio was left free.
   .. todo:: Get citation from Ron on this number

