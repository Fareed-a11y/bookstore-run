#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import String
import math

class FakeQRReader:
    def __init__(self):
        rospy.init_node('qr_reader_node')
        self.pub = rospy.Publisher('/barcode', String, queue_size=10)
        self.sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        
        # Coordinates of the stations
        self.stations = {
            "INFO_DESK": [-0.6, 4.1],
            "NOVEL_SECTION": [7.1, 0.52],
            "KIDS_CORNER": [-1.84,-6.4],
            "CHECKOUT": [-5.5, -3.8]
        }
        rospy.loginfo("QR Reader Node successfully initialized.")

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        
        # Check if robot is close to any bookstore section
        for name, coords in self.stations.items():
            distance = math.sqrt((x - coords[0])**2 + (y - coords[1])**2)
            if distance < 0.5:  # Within 0.5 meters
                payload = f"LOCATION={name}"
                self.pub.publish(payload)

if __name__ == '__main__':
    try:
        FakeQRReader()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
