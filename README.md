# Aerial Robotics Kharagpur 
## Controls Team Tasks

### Cartpole Control

This task consisted of 5 files. They were as follows:

#### system_param.m
All the parameters the system requires are mentioned here, the value of the acceleration due to gravity, the mass of the cart, the mass of the pendulum and the length of the pendulum.

#### physics.m
This file contains the non-linearised State Space Model of the Cartpole System.It utilises the parameters of the system, the current state of the system and the control function to generate the equations of motion of the cart. It then generates the state space of the system.

#### runsim.m
This file runs the simulation of the inverted pendulum. It uses the initial position of the cart and the final position of the cart to generate the simulation for a given time span at fixed time intervals. It utilises the ode45 which is a highly accurate iterative method that is used to solve the differential equations.

#### display_function.m
This function takes the solution for every time-stamp and prints them individually in order(frame-by-frame) to create the simulation. It also somewhat helps us in evaluating the pid controller for the force function of the cart and gives us an idea about how well our controller has been tuned to stabilise the inverted pendulum in the vertically upright position. Since the position of the cart has not been controlled using pid control, the best that it displays is 'Pole is balanced.Target not reached.', along with the error in the angle of the inverted pendulum
