#!/usr/bin/env python3 

#import library ros 
import rospy, time, sys, cv2
import numpy as np
from geometry_msgs.msg import Pose2D
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Point
from geometry_msgs.msg import Pose
from std_msgs.msg import Empty
import threading


#turn = .5
#global pos_x

class InfoGetter(object):
    def __init__(self):
        #event that will block until the info is received
        self._event = threading.Event()
        #attribute for storing the rx'd message
        self._msg = None

    def __call__(self, msg):
        #Uses __call__ so the object itself acts as the callback
        #save the data, trigger the event
        self._msg = msg
        self._event.set()

    def get_msg(self, timeout=None):
        """Blocks until the data is rx'd with optional timeout
        Returns the received message
        """
        self._event.wait(timeout)
        return self._msg


    #def listener_callback(data):
        #rospy.loginfo(data.position)
        #pos_x = rospy.Subscriber('/drone/gt_pose', Pose, listener_callback)
        #return pos_x

class AutoFlight():
    
    def __init__(self):
        self.status = ""
        self.pub_takeoff = rospy.Publisher('/drone/takeoff',Empty,queue_size = 2) #Drone Takeoff
        self.land_drone = rospy.Publisher('/drone/land',Empty,queue_size = 2) #land drone
        #self.position = rospy.Subscriber('/drone/gt_pose/position',Point)
        #self.orientation = rospy.Subscriber('/drone/gt_pose/orientation',Quaternion)
        self.vel = rospy.Publisher('/cmd_vel',Twist,queue_size= 2)
        self.Reset = rospy.Publisher('/drone/reset',Empty,queue_size = 2)
        self.rate=rospy.Rate(10)
        self.sleep_mode= rospy.sleep(10)
        #self.Shutdown_mode = rospy.on_shutdown(self.land_drone)

    def get_img(video):
        
        # Lendo a camera
        _,cv_image = video.read() 

        # Criando o conversor de imagem para ros msg	
        bridge = CvBridge()

        img_msg = bridge.cv2_to_imgmsg(cv_image, "bgr8")
        cv2.namedWindow('Webcam')
        cv2.imshow('Webcam',cv_image)
        cv2.waitKey(5)
                
        return img_msg

    #def camera_main():
        """
        This function is called from the main conde and calls 
        all work methods of fucntions into the codde.
        """

        # Global variables
        

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
    global cap
    
    # rospy.init_node('pb_drone_node',anonymous=True) 
    #rospy.init_node('infoGetter', anonymous=True)
    rospy.init_node('camera_node', anonymous=True)    # node name

    drone = AutoFlight()
    ig = InfoGetter()
    rospy.Subscriber("/drone/gt_pose", Pose, ig)

    try:       
        msg = ig.get_msg()
        print(msg)
        
        drone.Take_off()
        rospy.sleep(1)

        while(msg.position.x != -0.2000):
            print(msg)
            drone.foward()
            rospy.sleep(1)
        drone.stop()
        rospy.sleep(1)

        drone.Land()

        #print(drone.position)

        #drone.goBlue()    
    except rospy.ROSInterruptException: 
        pass