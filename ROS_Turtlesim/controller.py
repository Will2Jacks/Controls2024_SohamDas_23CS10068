#!/usr/bin/env python

import rospy # type: ignore
from turtlesim.msg import Pose # type: ignore
from geometry_msgs.msg import Twist # type: ignore
from math import atan2, sqrt, pi

class PIDController:
    def __init__(self, desired_position, desired_orientation):
        # Initialize PID parameters for linear and angular control
        self.Kp_linear_x= 10
        self.Ki_linear_x = 0
        self.Kd_linear_x= 0
        self.Kp_linear_y= 10
        self.Ki_linear_y = 0
        self.Kd_linear_y= 0
        self.Kp_angular = 10
        self.Ki_angular = 0
        self.Kd_angular = 0

        # Initialize variables for storing previous errors and integrals
        self.prev_error_linear_x = 0
        self.integral_linear_x = 0
        self.prev_error_linear_y = 0
        self.integral_linear_y = 0
        self.prev_error_angular = 0
        self.integral_angular = 0

        # Set desired position and orientation
        self.desired_position = desired_position
        self.desired_orientation = desired_orientation

        # Subscribe to current pose topic
        rospy.Subscriber("/turtle1/pose", Pose, self.pose_callback)

        # Publisher for control commands
        self.cmd_vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    def pose_callback(self, data):
        # Get current pose
        current_position = (data.x, data.y)
        current_orientation = data.theta

        # Calculate errors for linear and angular control
        # error_linear = sqrt((self.desired_position[0] - current_position[0])**2 + (self.desired_position[1] - current_position[1])**2)

        error_linear_x=self.desired_position[0]-current_position[0]

        error_linear_y=self.desired_position[1]-current_position[1]
        
        if(self.desired_position[1] - current_position[1]!=0 or self.desired_position[0] - current_position[0]!=0):
            error_orientation = atan2(self.desired_position[1] - current_position[1], self.desired_position[0] -    current_position[0]) - current_orientation
        else:
            error_orientation=self.desired_orientation-current_orientation

        if error_orientation > pi:
            error_orientation -= 2 * pi
        elif error_orientation < -pi:
            error_orientation += 2 * pi

        # Update integrals for linear and angular control
        self.integral_linear_x += error_linear_x
        self.integral_linear_y += error_linear_y
        self.integral_angular += error_orientation

        # Calculate linear control command using PID algorithm
        control_command_linear_x = self.Kp_linear_x * error_linear_x + self.Ki_linear_x * self.integral_linear_x + self.Kd_linear_x * (error_linear_x - self.prev_error_linear_x)

        control_command_linear_y = self.Kp_linear_y * error_linear_y + self.Ki_linear_y * self.integral_linear_y + self.Kd_linear_y * (error_linear_y - self.prev_error_linear_y)

        # Calculate angular control command using PID algorithm
        control_command_angular = self.Kp_angular * error_orientation + self.Ki_angular * self.integral_angular + self.Kd_angular * (error_orientation - self.prev_error_angular)

        

        # Publish control command
        self.publish_control_command(control_command_linear_x,control_command_linear_y, control_command_angular)

        # Update previous errors
        self.prev_error_linear_x = error_linear_x
        self.prev_error_linear_y = error_linear_y
        self.prev_error_angular = error_orientation

    def publish_control_command(self, control_command_linear_x,control_command_linear_y, control_command_angular):
        # Publish control command as Twist message
        twist_msg = Twist()
        twist_msg.linear.x = control_command_linear_x
        twist_msg.linear.y = control_command_linear_y
        twist_msg.angular.z = control_command_angular
        self.cmd_vel_pub.publish(twist_msg)

if __name__ == "__main__":
    rospy.init_node("pid_controller")

    # Get desired position and orientation from the user
    desired_x = float(input("Enter desired x position: "))
    desired_y = float(input("Enter desired y position: "))
    desired_orientation = float(input("Enter desired orientation (in radians): "))

    pid_controller = PIDController((desired_x, desired_y), desired_orientation)
    rospy.spin()
