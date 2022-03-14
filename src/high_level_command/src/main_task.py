#!/bin/python3 
from move_command import move_to_goal
import rospy

if __name__ == '__main__':
   rospy.init_node('map_navigation', anonymous=False)
   x_goal = 0.3
   y_goal = 1.5
   z_goal = 0
   w_goal = 1
   x1 = 1
   y1 = 1
   z1 = -.7
   w1 = .7
   x2 = 1
   y2 = 0
   z2 = 1
   w2 = 0
   x3 = 0
   y3 = 0
   z3 = .7
   w3 = .7
   x4 = 0
   y4 = 1
   z4 = 0
   w4 = 1
   print("start go to goal")
   move_to_goal(x_goal,y_goal,z_goal,w_goal)
   rospy.sleep(3) # Sleeps for 3 sec

   move_to_goal(x1,y1,z1,w1)
   rospy.sleep(3) # Sleeps for 3 sec
   move_to_goal(x2,y2,z2,w2)
   rospy.sleep(3) # Sleeps for 3 sec
   move_to_goal(x3,y3,z3,w3)
   rospy.sleep(3) # Sleeps for 3 sec
   move_to_goal(x4,y4,z4,w4)
   rospy.sleep(3) # Sleeps for 3 sec
   
   rospy.spin()