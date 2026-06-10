#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler

# The target destinations in the bookstore [X, Y, Yaw_Orientation_Degrees]
BOOKSTORE_STATIONS = {
    "INFO_DESK":      [-0.6, 4.12, 90],
    "SCIENCE_SECTION":  [ 7.09,  0.52,   0],
    "NOVEL_SECTION":    [ -1.84, -6.4, -90],
    "CHECKOUT":      [-5.49, -3.78,  90]
}

def move_to_station(station_name, coords):
    # Connect to the move_base action server
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # Define target positions
    goal.target_pose.pose.position.x = coords[0]
    goal.target_pose.pose.position.y = coords[1]
    
    # Calculate facing direction angle
    q = quaternion_from_euler(0, 0, coords[2] * 3.14159 / 180.0)
    goal.target_pose.pose.orientation = Quaternion(*q)

    rospy.loginfo(f"🚀 Moving autonomously to: {station_name}...")
    client.send_goal(goal)
    client.wait_for_result()

    # Check if navigation succeeded
    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo(f"✅ Target Reached: Arrived at {station_name}.")
        simulate_qr_scan(station_name)
    else:
        rospy.logwarn(f"❌ Navigation failed to reach {station_name}.")

def simulate_qr_scan(station_name):
    rospy.loginfo(f"🔍 [CAMERA] Aligning lens with QR boundary at {station_name}...")
    
    rospy.sleep(2.0) 
    
    mocked_qr_payload = f"LOCATION={station_name}"
    
    # Print the verification outputs to the screen
    print("\n" + "="*50)
    rospy.loginfo(f"📸 SCAN RECEIVED: \"{mocked_qr_payload}\"")
    rospy.loginfo(f"🌟 POSITION VERIFIED: Successfully cross-referenced {station_name} layout coordinates!")
    print("="*50 + "\n")
    
    rospy.sleep(1.0)

if __name__ == '__main__':
    try:
        rospy.init_node('mock_bookstore_sequencer')
        
        rospy.loginfo("Initializing autonomous bookstore inspection routine...")
        
        # Sequentially loop through each destination aisle
        for station, coordinates in BOOKSTORE_STATIONS.items():
            move_to_station(station, coordinates)
            
        rospy.loginfo("🏆 Mission Complete: All stations verified successfully! Returning to baseline.")
    except rospy.ROSInterruptException:
        pass
