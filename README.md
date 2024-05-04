# Aerial Robotics Kharagpur 
## Controls Team Tasks

### Cartpole Control

This task consisted of 5 files. They were as follows:

#### system_param.m
All the parameters the system requires are mentioned here, the value of the acceleration due to gravity, the mass of the cart, the mass of the pendulum and the length of the pendulum.

#### physics.m
This file contains the non-linearised State Space Model of the Cartpole System.It utilises the parameters of the system, the current state of the system and the control function to generate the equations of motion of the cart. It then generates the state space of the system.
