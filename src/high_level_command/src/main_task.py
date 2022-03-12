#!/bin/python3 
from move_command import move_to_goal
import rospy

if __name__ == '__main__':
   rospy.init_node('map_navigation', anonymous=False)
   x_check_stat = 0.3
   y_checl_stat = 1.5
   x1 = .4
   y1 = 2.8

   print("start go to check status")
   move_to_goal(x_check_stat,y_checl_stat)
   rospy.sleep(3) # Sleeps for 1 sec

   print("start go to 1")
   move_to_goal(x1,y1)
   rospy.spin()