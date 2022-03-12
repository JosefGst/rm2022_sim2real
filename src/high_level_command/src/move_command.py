#!/bin/python3 
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point




#this method will make the robot move to the goal location
def move_to_goal(xGoal,yGoal,z_orient,w_orient):

   #define a client for to send goal requests to the move_base server through a SimpleActionClient
   ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

   #wait for the action server to come up
   while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
           rospy.loginfo("Waiting for the move_base action server to come up")

   goal = MoveBaseGoal()
   
   
   #set up the frame parameters
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()

   # moving towards the goal*/

   goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
   goal.target_pose.pose.orientation.x = 0.0
   goal.target_pose.pose.orientation.y = 0.0
   goal.target_pose.pose.orientation.z = z_orient
   goal.target_pose.pose.orientation.w = w_orient

   rospy.loginfo("Sending goal location ...")
   ac.send_goal(goal)

   ac.wait_for_result(rospy.Duration(90))

   if(ac.get_state() ==  GoalStatus.SUCCEEDED):
           rospy.loginfo("You have reached the destination")
           return True

   else:
           rospy.loginfo("The robot failed to reach the destination")
           return False

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