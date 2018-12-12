import rospy
import intera_interface
import numpy as np
import argparse
import cv2
rospy.init_node('Hello_Sawyer')
limb = intera_interface.Limb('right')
gripper = intera_interface.Gripper('right_gripper')

gripper.set_position(100)