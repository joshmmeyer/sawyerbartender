import rospy
import intera_interface
import numpy as np
import argparse
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import tkinter




rospy.init_node('Hello_Sawyer')
limb = intera_interface.Limb('right')
gripper = intera_interface.Gripper('right_gripper')

home = {'right_j6': 0.067853515625, 'right_j5': -1.5171982421875, 'right_j4': 0.8077958984375, 'right_j3': 1.82715625, 'right_j2': -1.2073818359375, 'right_j1': 0.865412109375, 'right_j0': 0.384044921875, 'head_pan': -1.0854375}

pre_grip_all = {'right_j0': 0.373650390625, 'right_j1': 0.863353515625, 'right_j2': -1.209701171875, 'right_j3': 1.769767578125, 'right_j4': 0.857619140625, 'right_j5': -0.137341796875, 'right_j6': 0.0682666015625}

pre_grip_1_wp1 = {'right_j0': -0.1739697265625, 'right_j1': 0.9375439453125, 'right_j2': -1.2099892578125, 'right_j3': 1.7511064453125, 'right_j4': 0.932451171875, 'right_j5': -0.3888984375, 'right_j6': 0.0682666015625 }
pre_grip_1_wp2 = {'right_j0': -0.6456640625, 'right_j1': 1.0157353515625, 'right_j2': -1.4324443359375, 'right_j3': 1.6012373046875, 'right_j4': 0.957046875, 'right_j5': -0.8271220703125, 'right_j6': 0.1224150390625}
grip_1 = {'right_j0': -0.8483037109375, 'right_j1': 1.030052734375,'right_j2': -1.593611328125, 'right_j3': 1.476822265625, 'right_j4': 1.02020703125, 'right_j5': -0.843931640625, 'right_j6': 0.1224150390625}

pre_grip_2_wp1 = {'right_j0': -0.167177734375,'right_j1':  1.2165615234375, 'right_j2': -1.5647998046875, 'right_j3': 1.6583818359375, 'right_j4': 0.9209609375, 'right_j5':  -0.360791015625, 'right_j6':  0.4550400390625}
pre_grip_2_wp2 = {'right_j0': -0.524431640625,'right_j1':  1.1500380859375, 'right_j2': -1.6661591796875, 'right_j3': 1.5544052734375, 'right_j4': 1.0692041015625, 'right_j5':  -0.6759345703125, 'right_j6':  0.1934638671875}
grip_2 = {'right_j0': -0.72278125,'right_j1':  1.1339775390625, 'right_j2': -1.833796875, 'right_j3': 1.455833984375,'right_j4':  1.0888798828125, 'right_j5':  -0.7047392578125, 'right_j6':  0.1936708984375}

pre_grip_3_wp1 = {'right_j0': 0.0271123046875,'right_j1':  1.1039091796875, 'right_j2': -1.5546572265625, 'right_j3': 1.5986474609375, 'right_j4': 0.7286396484375, 'right_j5':  -0.3638896484375, 'right_j6':  0.5534599609375}
pre_grip_3_wp2 = {'right_j0': -0.3498857421875,'right_j1':  1.2111015625,'right_j2': -1.9300498046875,'right_j3':  1.5295546875, 'right_j4': 0.9349169921875,'right_j5':  -0.44347265625,'right_j6':  0.4721728515625}
grip_3 = {'right_j0': -0.537802734375,'right_j1':  1.174240234375, 'right_j2': -2.026275390625,'right_j3':  1.444193359375,'right_j4':  1.0218466796875,'right_j5':  -0.5479228515625,'right_j6':  0.354115234375}

pre_grip_4_wp1 = {'right_j0': 0.2512216796875, 'right_j1': 1.078265625,'right_j2':  -1.6374833984375,'right_j3':  1.5519599609375,'right_j4':  0.7011650390625,'right_j5':  -0.236716796875,'right_j6':  0.494857421875}
pre_grip_4_wp2 = {'right_j0': -0.0898935546875,'right_j1':  1.0576640625, 'right_j2': -1.7534609375,'right_j3':  1.4214814453125,'right_j4':  0.992732421875,'right_j5':  -0.44884375,'right_j6':  0.1913984375}
grip_4 = {'right_j0': -0.2847705078125, 'right_j1': 1.0234599609375, 'right_j2': -1.8557958984375,'right_j3':  1.2920498046875,'right_j4':  1.054640625,'right_j5':  -0.5713173828125,'right_j6':  0.0856318359375}

pre_pour_2 = {'right_j0':0.1582568359375, 'right_j1': 0.862119140625, 'right_j2': -1.3791513671875, 'right_j3': 1.66685546875, 'right_j4': 0.7924189453125, 'right_j5': -1.556615234375, 'right_j6': -0.0296875}
pour = {'right_j0': 0.279431640625, 'right_j1':  0.725552734375, 'right_j2': -1.4572041015625, 'right_j3':1.81466796875, 'right_j4':0.544865234375, 'right_j5': -1.3916787109375, 'right_j6': -1.5480908203125}

#order = None
#image = None

bridge = CvBridge()
root = tkinter.Tk()
recipe=0

#install cvBridge
def image_callback(msg):
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        cv2.imwrite('camera_image.jpeg', cv2_img)


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def colorDetect(image):
	num_bottles = 4

	# ap = argparse.ArgumentParser()
	# ap.add_argument("-i", "--image")
	# args = vars(ap.parse_args())

	img = cv2.imread(image)

	image=img[415:570, 575:875]
	#image=increase_brightness(image,value=2000)

	# cv2.imshow("cropped", image)
	# cv2.waitKey(0)

	# cv2.imwrite('cropped_image.jpg', image)

	height, width = image.shape[:2]

	# Let's get the starting pixel coordiantes (top left of cropped top)
	# start_row, start_col = int(0), int(0)
	# # Let's get the ending pixel coordinates (bottom right of cropped top)
	# end_row, end_col = int(height), int(width * .25)

	Pos1 = image[0:int(height) , 0:int(width*.25)]


	#cv2.imshow("Far Left", Pos1) 
	#cv2.waitKey(0) 
	#cv2.destroyAllWindows()

	# Let's get the starting pixel coordiantes (top left of cropped bottom)
	# start_row, start_col = int(0), int(width * .25)
	# # Let's get the ending pixel coordinates (bottom right of cropped bottom)
	# end_row, end_col = int(height), int(width*.5)
	Pos2 = image[0:int(height) , int(width*.25):int(width*.5)]

	# print start_row, end_row 
	# print start_col, end_col

	#cv2.imshow("Middle Left", Pos2) 
	#cv2.waitKey(0) 
	#cv2.destroyAllWindows()

	# Let's get the starting pixel coordiantes (top left of cropped bottom)
	# start_row, start_col = int(0), int(width * .5)
	# # Let's get the ending pixel coordinates (bottom right of cropped bottom)
	# end_row, end_col = int(height), int(width*.75)
	Pos3 = image[0:int(height) , int(width*.5):int(width*.75)]

	#cv2.imshow("Middle Right", Pos3) 
	#cv2.waitKey(0) 
	#cv2.destroyAllWindows()

	# Let's get the starting pixel coordiantes (top left of cropped bottom)
	# start_row, start_col = int(0), int(width * .75)
	# # Let's get the ending pixel coordinates (bottom right of cropped bottom)
	# end_row, end_col = int(height), int(width)
	Pos4 = image[0:int(height), int(width*.75):int(width)]

	#cv2.imshow("Far Right", Pos4) 
	#cv2.waitKey(0) 
	#cv2.destroyAllWindows()

	# Finally, we can use image.size to give use the number of pixels in each part.

	# cropped_top.size
	# cropped_bot.size

	

	# sub_image = full_image[y_start: y_end, x_start:x_end]


	boundaries = [
		([33, 35, 85], [56, 55, 127]), #red
		([39, 24, 19], [50, 31, 28]), #blue
		([48, 65, 54], [68, 86, 68]), #green
		([65, 110, 120], [88, 145, 154]) #yellow
	]

	images = [Pos1, Pos2, Pos3, Pos4]
	color_pos = []

	#for "color", red = 1, blue = 2, green = 3, yellow = 4

	for i in range(0, num_bottles):

		color = 1
		temp = 0
		bestcolor=-1
		for (lower, upper) in boundaries:
			lower = np.array(lower, dtype = "uint8")
			upper = np.array(upper, dtype = "uint8")

			mask = cv2.inRange(images[i], lower, upper)
			output = cv2.bitwise_and(images[i], images[i], mask = mask)
			# cv2.imshow("images", np.hstack([image, output]))
			# cv2.waitKey(0)
			# print(cv2.countNonZero(mask))
			if cv2.countNonZero(mask) > temp:
				temp=cv2.countNonZero(mask)
				bestcolor=color

			color = color + 1

		color_pos.append(bestcolor) 

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


def recipe_1(node):
    for i in range(4):
        if node[i]=="green":
          get_replace_bottle(i,True)
          pour_bottle(3)
          get_replace_bottle(i,False)
        elif node[i]=="red":
          get_replace_bottle(i,True)
          pour_bottle(8)
          get_replace_bottle(i,False)
            

def recipe_2(node):
    for i in range(4):
        if node[i]=="yellow":
          get_replace_bottle(i,True)
          pour_bottle(8)
          get_replace_bottle(i,False)
        elif node[i]=="blue":
          get_replace_bottle(i,True)
          pour_bottle(3)
          get_replace_bottle(i,False)


 
def get_replace_bottle(i, is_get):
  if i == 3:
    limb.move_to_joint_positions(home)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(pre_grip_1_wp1)
    limb.move_to_joint_positions(pre_grip_1_wp2)
    limb.set_joint_position_speed(0.1)
    limb.move_to_joint_positions(grip_1)
    rospy.sleep(.5)
    if is_get:
      gripper.set_position(0)
    else:
      gripper.set_position(100)
    rospy.sleep(.5)
    limb.move_to_joint_positions(pre_grip_1_wp2)
    limb.set_joint_position_speed(0.3)
    limb.move_to_joint_positions(pre_grip_1_wp1)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(home)
    
  if i == 2:
    limb.move_to_joint_positions(home)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(pre_grip_2_wp1)
    limb.move_to_joint_positions(pre_grip_2_wp2)
    limb.set_joint_position_speed(0.1)
    limb.move_to_joint_positions(grip_2)
    rospy.sleep(.5)
    if is_get:
      gripper.set_position(0)
    else:
      gripper.set_position(100)
    rospy.sleep(.5)
    limb.move_to_joint_positions(pre_grip_2_wp2)
    limb.set_joint_position_speed(0.3)
    limb.move_to_joint_positions(pre_grip_2_wp1)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(home)
    
  if i == 1:
    limb.move_to_joint_positions(home)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(pre_grip_3_wp1)
    limb.move_to_joint_positions(pre_grip_3_wp2)
    limb.set_joint_position_speed(0.1)
    limb.move_to_joint_positions(grip_3)
    rospy.sleep(.5)
    if is_get:
      gripper.set_position(0)
    else:
      gripper.set_position(100)
    rospy.sleep(.5)
    limb.move_to_joint_positions(pre_grip_3_wp2)
    limb.set_joint_position_speed(0.3)
    limb.move_to_joint_positions(pre_grip_3_wp1)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(home)
    
  if i == 0:
    limb.move_to_joint_positions(home)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(pre_grip_4_wp1)
    limb.move_to_joint_positions(pre_grip_4_wp2)
    limb.set_joint_position_speed(0.1)
    limb.move_to_joint_positions(grip_4)
    rospy.sleep(.5)
    if is_get:
      gripper.set_position(0)
    else:
      gripper.set_position(100)
    rospy.sleep(.5)
    limb.move_to_joint_positions(pre_grip_4_wp2)
    limb.set_joint_position_speed(0.3)
    limb.move_to_joint_positions(pre_grip_4_wp1)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(home)
    

def pour_bottle(amount):
  limb.move_to_joint_positions(home)
  limb.move_to_joint_positions(pre_pour_2)
  limb.move_to_joint_positions(pour)
  rospy.sleep(amount)
  limb.move_to_joint_positions(pre_pour_2)
  limb.move_to_joint_positions(home)
  
def recipe1():
    global recipe
    recipe = 2
    root.quit()

def recipe2():
    global recipe
    recipe = 1
    root.quit()

def printVariable():
    print(variable)
  
def main():
  # Define your image topic
  image_topic = "/io/internal_camera/head_camera/image_raw"
  # Set up your subscriber and define its callback
  rospy.Subscriber(image_topic, Image, image_callback)
  # Spin until ctrl + c
  rospy.sleep(1)
  color_pos=colorDetect('camera_image.jpeg')
  print(color_pos)



  
  button1 = tkinter.Button(root, text="Screwdriver",font = ('Helvetica', '100'), command = recipe1)

  button1.pack()
  button2 = tkinter.Button(root, text="Rum and Coke", font = ('Helvetica', '100'), command = recipe2)
  button2.pack()

  button3 = tkinter.Button(root, text="Quit", font = ('Helvetica', '100'), command = root.quit)
  button3.pack()





  root.mainloop()
  print(recipe)

  if recipe == 1:
    recipe_1(color_pos)
  if recipe == 2:
    recipe_2(color_pos)


if __name__ == "__main__":
	main()

'''
  #recipe_2(color_pos)
  #get_replace_bottle(0,True)
  #pour_bottle(2)
  #get_replace_bottle(0,False)  
  root.title("Sawyer Bartender")
  chooseDrink=tkinter.Label(root, text="Choose a Drink", font=('Helvetica','15'))
  chooseDrink.place(x=187, y=130)
  screwdriverPic=tkinter.PhotoImage(file="ClassicScrewdriver.png")
  
  chooseDrink=tkinter.Label(root, text="Screwdriver", font=('Helvetica','10'))
  chooseDrink.place(x=35, y=50)
  chooseDrink1=tkinter.Label(root, text="Rum and Coke", font=('Helvetica','10'))
  chooseDrink1.place(x=400, y=50)
  chooseDrink2=tkinter.Label(root, text="Welcome to the Sawyer Bartender!", font=('Helvetica 17 underline'))
  chooseDrink2.place(x=75, y=1)
  #tkinter.button1.pack(side=LEFT)
  rumandcokePic=tkinter.PhotoImage(file="CruzanWithCola.png")
  button2 = tkinter.Button(root, image=rumandcokePic, height=142,width=140,command = recipe2)
  #text="Rum and Coke", font = ('Helvetica', '10')
  #button2.pack(side=RIGHT)

  button3 = tkinter.Button(root, text="Quit", font = ('Helvetica', '10'), command = root.quit)
  #button3.pack(side=BOTTOM)
'''

