#!/bin/python3 
from simple_goal import movebase_client
from grasp_cube import *
from detect_cube import *

import rospy

if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client(.15, 1.6, 1)
        if result:
            rospy.loginfo("Goal execution done!")
            rospy.sleep(3) # Sleeps for 3 sec
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
    

    # rospy.loginfo("next!")
    # ap = arucoPose()
    # rospy.init_node('aruco_pose_node', anonymous=True)
    # try:
    #     rospy.spin()
    # except KeyboardInterrupt:
    #     print("Shutting down")
    # rospy.sleep(3) # Sleeps for 3 sec
    
    
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client(.05, 2.8, -.1)
        if result:
            rospy.loginfo("Goal execution done!")
            rospy.sleep(3) # Sleeps for 3 sec
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")

    
    #grasp
    rospy.init_node('grasp_aruco_node', anonymous=True)
    ap = graspAruco()
    print("=====init=====")
    ap.reset_arm()
    rospy.sleep(2)
    print("=====reset arm at beginning=====")
    ap.open_gripper()
    rospy.sleep(2)
    print("=====open gripper at beginning=====")
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
        ap.forward_zero()
        # ap.reset_arm()