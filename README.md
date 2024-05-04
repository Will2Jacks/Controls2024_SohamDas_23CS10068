# Aerial Robotics Kharagpur 
## Controls Team Tasks

### Cartpole Control

This task involved writing a PID controller for the wheel of the cartpole,such that the inverted pendulum is balanced in a vertial upright position
This task consisted of 5 files. They were as follows:

#### system_param.m
All the parameters the system requires are mentioned here, the value of the acceleration due to gravity, the mass of the cart, the mass of the pendulum and the length of the pendulum.

#### physics.m
This file contains the non-linearised State Space Model of the Cartpole System.It utilises the parameters of the system, the current state of the system and the control function to generate the equations of motion of the cart. It then generates the state space of the system.

#### runsim1.m
This file runs the simulation of the inverted pendulum. It uses the initial position of the cart and the final position of the cart to generate the simulation for a given time span at fixed time intervals. It utilises the ode45 which is a highly accurate iterative method that is used to solve the differential equations.

#### display_function.m
This function takes the solution for every time-stamp and prints them individually in order(frame-by-frame) to create the simulation. It also somewhat helps us in evaluating the pid controller for the force function of the cart and gives us an idea about how well our controller has been tuned to stabilise the inverted pendulum in the vertically upright position. Since the position of the cart has not been controlled using pid control, the best that it displays is 'Pole is balanced.Target not reached.', along with the error in the angle of the inverted pendulum

#### controller1.m
The controller1 is the main function that generates the force function to be applied to the wheel of the cart in order to stabilise the pendulum in the vertically upright position. It first value of theta( that is the angle the pendulum makes with the upright vertical) and finds the error in the angle of the pendulum by calculating its difference with the desired value( that is 0, the vertically upright position). The values of Kp(the proportional constant),Kd(the derivative constant) and Ki(the integral constant) follow. The following values have been found suitable for the control function. The control function 'u' is then calculated and is returned from the given function.


### Multirotor Control
Here we had to make a PID controller for a Multirotor restricted to move in the YZ plane, that is the plane of the computer screen. The multirotor had to be tuned such that it could follow any specified trajectory.
This task consisted of a folder of trajectories(the sine, the diamond, the step and the line),a folder of utility functions, a evaluate function and 4 other matlab functions.

#### controller.m
The parameters of the system, the mass of the quadrotor, the accelaration due to gravity and its moment of inertia along with the present state of the quadrotor(which have been specified in the sys_eom.m file) have been utilised. The two functions have then been calculated using the equations of physics. The constants have been found out through repeated iterations and have been applied to the system to generate the force and tprque functions.

#### submit.m
This function uses the controller function as the control handle

#### runsim.m
This function specifies which trajectory the quadrotor is to follow out of the four possible trajectories and utilises the controller functions returned by controller.m

#### simulation_2d.m
This file runs the simulation of the quadrotor following the specified trajectory and also plots the y,z and angular position of the quadrotor.It also gives any error message(if any) and thus helps in assessing the control force and torque that is applied to the quadrotor.


