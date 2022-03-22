#!/bin/python3 
from simple_goal import movebase_client
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
    
    rospy.loginfo("next!")
    main()
    rospy.sleep(3) # Sleeps for 3 sec
    
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client(.1, 2.3, .5)
        if result:
            rospy.loginfo("Goal execution done!")
            rospy.sleep(3) # Sleeps for 3 sec
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")