#! /usr/bin/python
# Copyright (c) 2015, Rethink Robotics, Inc.

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

import numpy as np
import argparse

# Instantiate CvBridge
bridge = CvBridge()

def image_callback(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        cv2.imwrite('camera_image.jpeg', cv2_img)


def colorDetect(image):

    num_bottles = 4
    #use cvBridge to convert from ros image to cv image
    img = cv2.imread(image)
    image=img[415:570, 575:875]
    cv2.imshow("cropped",image)
    cv2.waitKey(0)

    height, width = image.shape[:2]

    Pos1 = image[0:int(height) , 0:int(width*.25)]

    Pos2 = image[0:int(height) , int(width*.25):int(width*.5)]

    Pos3 = image[0:int(height) , int(width*.5):int(width*.75)]

    Pos4 = image[0:int(height), int(width*.75):int(width)]

    # sub_image = full_image[y_start: y_end, x_start:x_end]

    boundaries = [
        ([31, 41, 130], [67, 68, 160]), #red
        ([70, 55, 45], [115, 80, 70]), #blue
        ([74, 128, 105], [100, 150, 133]), #green
        ([40, 156, 170], [60, 177, 190]) #yellow
    ]

    images = [Pos1, Pos2, Pos3, Pos4]
    color_pos = []

    #for "color", red = 1, blue = 2, green = 3, yellow = 4

    for i in range(0, num_bottles):

        color = 1
        for (lower, upper) in boundaries:
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")

            mask = cv2.inRange(images[i], lower, upper)
            output = cv2.bitwise_and(images[i], images[i], mask = mask)

            if cv2.countNonZero(mask) > 100000:
                color_pos.append(color) 


            color = color + 1

    for i in range(0, len(color_pos)):
        if (color_pos[i]) == 1:
            color_pos[i] = "red"
        elif (color_pos[i]) == 2:
            color_pos[i] = "blue"
        elif (color_pos[i]) == 3:
            color_pos[i] = "green"
        else:
            color_pos[i] = "yellow"

    return color_pos

def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/io/internal_camera/head_camera/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.sleep(1)
    color_pos=colorDetect('camera_image.jpeg')
    #print(color_pos[1])

if __name__ == '__main__':
    main()