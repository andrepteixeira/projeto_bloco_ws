#!/usr/bin/env python3 

#import library ros 
from os import truncate
import rospy 
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Point
from std_msgs.msg import Empty


turn = .5

class AutoFlight():
    # def callback(dronePose): 
    #     pose = Pose()
    #     pose.position.x = dronePose.position.x 
    #     pose.position.y = dronePose.position.y 
    #     pose.position.z = dronePose.position.y

    def __init__(self):
        self.status = ""
        self.pub_takeoff = rospy.Publisher('/drone/takeoff',Empty,queue_size = 2) #Drone Takeoff
        self.land_drone = rospy.Publisher('/drone/land',Empty,queue_size = 2) #land drone
        self.position = rospy.Subscriber('/drone/gt_pose/position',Point)
        self.orientation = rospy.Subscriber('/drone/gt_pose/orientation',Quaternion)
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
    
    def home():
        position = Point()
        position.x = 0.0
        position.y = 0.0
        position.z = 1.5
    
    # def goRed(self):
        
    #     while(self.position.x != 8.0):
    #         self.foward()
    #         rospy.sleep(10)
    #     self.stop()
    #     rospy.sleep(10)
    #     while(self.orientation.z != -0.5):
    #         self.clockwise()
    #         rospy.sleep(10)
    #     self.stop()
    #     rospy.sleep(10)
    #     while(self.position.z != -6.0):
    #         self.foward()
    #         rospy.sleep(10)
    #     self.stop()
    #     rospy.sleep(10)
    #     self.Land()
    
    #def green():
        position = Point()
        position.x = 8.0
        position.y = 8.0
        position.z = 1.5

    def goBlue(self):
        
        while(self.position != -8.0):
            self.foward()
            rospy.sleep(10)
        self.stop()
        rospy.sleep(10)
        while(self.orientation != 0.0):
            self.clockwise()
            rospy.sleep(10)
        self.stop()
        #rospy.sleep(10)
        # while(self.position.z != -6.0):
        #     self.foward()
        #     rospy.sleep(10)
        # self.stop()
        rospy.sleep(10)
        self.Land()


if __name__== "__main__":

    rospy.init_node('pb_drone_node',anonymous=True) #Node Initiaton
    drone = AutoFlight()
    

    try:
        drone.Take_off()
        rospy.sleep(10)

        print(drone.position)
        
        drone.goBlue()

        
    except rospy.ROSInterruptException: 
        pass