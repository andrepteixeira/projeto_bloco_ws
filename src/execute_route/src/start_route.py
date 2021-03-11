#!/usr/bin/env python3 

#import library ros 
import rospy 
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty


turn = .5

class AutoFlight():

    def __init__(self):
        self.status = ""
        self.pub_takeoff = rospy.Publisher('/drone/takeoff',Empty,queue_size = 2) #Drone Takeoff
        self.land_drone = rospy.Publisher('drone/land',Empty,queue_size = 2) #land drone
        self.vel = rospy.Publisher('/cmd_vel',Twist,queue_size= 2)
        self.Reset = rospy.Publisher('/drone/reset',Empty,queue_size = 2)
        self.rate=rospy.Rate(10)
        self.sleep_mode= rospy.sleep(10)
        #self.Shutdown_mode = rospy.on_shutdown(self.land_drone)



    def Take_off(self):
        self.pub_takeoff.publish(Empty())
        self.sleep_mode

    def Land (self):
        self.land_drone.publish(Empty())
        self.sleep_mode

    def Reset_drone(self):
        self.Reset.publish(Empty())
        self.sleep_mode

    def stop(self):
        vel = Twist()
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        self.vel.publish(vel)

    def foward(self):
        vel = Twist()
        vel.linear.x = 1
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        self.vel.publish(vel)

    def backward(self):
        vel = Twist()
        vel.linear.x = -1
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        self.vel.publish(vel)

    def left(self):
        vel = Twist()
        vel.linear.x = 0
        vel.linear.y = 1
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        self.vel.publish(vel)

    def right(self):
        vel = Twist()
        vel.linear.x = 0
        vel.linear.y = -1
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        self.vel.publish(vel)

    def up(self):
        vel = Twist()
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 1
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        self.vel.publish(vel)

    def down(self):
        vel = Twist()
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = -1
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        self.vel.publish(vel)

    def clockwise(self):
        vel = Twist()
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = -1*turn
        self.vel.publish(vel)

    def counterclockwise(self):
        vel = Twist()
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 1*turn
        self.vel.publish(vel)

if __name__== "__main__":

    rospy.init_node('pb_drone_node',anonymous=True) #Node Initiaton
    drone = AutoFlight()
    stop = drone.stop()
    fly_forward = drone.foward()
    fly_backward = drone.backward()
    fly_left = drone.left()
    fly_right = drone.right()
    fly_up = drone.up()
    fly_down = drone.down()
    fly_clockwise = drone.clockwise()
    fly_counterclockwise = drone.counterclockwise()

    try:
        drone.Take_off()

        for i in range(7):
            if i == 0:
                fly_forward
            
            elif i == 1: 
                fly_counterclockwise
            
            elif i == 2:
                fly_left

            elif i == 3:
                fly_right
            
            elif i == 4:
                fly_clockwise
            
            elif i == 5:
                fly_up
            
            elif i == 6:
                fly_down

            else:
                drone.Land()
        
    except rospy.ROSInterruptException: 
        pass