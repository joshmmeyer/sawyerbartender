import rospy
import intera_interface
import numpy as np
import argparse
import cv2

rospy.init_node('Hello_Sawyer')
limb = intera_interface.Limb('right')
gripper = intera_interface.Gripper('right_gripper')

home = {'right_j6': 0.067853515625, 'right_j5': -1.5171982421875, 'right_j4': 0.8077958984375, 'right_j3': 1.82715625, 'right_j2': -1.2073818359375, 'right_j1': 0.865412109375, 'right_j0': 0.384044921875}


pre_grip_all = {'right_j0': 0.373650390625, 'right_j1': 0.863353515625, 'right_j2': -1.209701171875, 'right_j3': 1.769767578125, 'right_j4': 0.857619140625, 'right_j5': -0.137341796875, 'right_j6': 0.0682666015625}


pre_grip_1_wp1 = {'right_j0': -0.1739697265625, 'right_j1': 0.9375439453125, 'right_j2': -1.2099892578125, 'right_j3': 1.7511064453125, 'right_j4': 0.932451171875, 'right_j5': -0.3888984375, 'right_j6': 0.0682666015625}
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


pre_pour_1 = {'right_j0': 0.311140625,'right_j1': 0.3977373046875,'right_j2': -1.4644501953125,'right_j3': 1.940607421875, 'right_j4': 0.382341796875, 'right_j5': -1.5726767578125,'right_j6': 0.120556640625}
pre_pour_2 = {'right_j0': 0.2438056640625, 'right_j1': 0.7280224609375, 'right_j2': -1.8675263671875, 'right_j3': 1.69154296875, 'right_j4': 0.6896865234375, 'right_j5': -1.554111328125, 'right_j6': 0.46082421875}
pour = {'right_j0': 0.43605859375, 'right_j1': 0.607818359375, 'right_j2': -1.7963046875, 'right_j3': 1.652931640625, 'right_j4': 0.598212890625, 'right_j5': -1.46297265625, 'right_j6': -2.46848828125}


order = None
image = None

#install cvBridge
    
def colorDetect(image):

	num_bottles = 4
	#use cvBridge to convert from ros image to cv image
	image = cv2.imread(image)

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

#Making Nodes
#make a publisher that publishes on topic order 
	#make a topic called drink order of type: string
  
#make a subscriber that subscribes to "order"

#make a subscriber that is subscribed to camera
def camera_callback(msg):
  if global image is None:
    image = msg.data
    
def order_callback(msg):
  global order = msg.data

def init_sawyer():
  limb.move_to_joint_positions(home)
  color_pos = colorDetect("bottlecolors.jpg")
     
def recipe_1():
		print "Recipe 1:"
    print
    for i in range(4):
        if node[i]=="green":
            bottle1=i
        elif node[i]=="red":
            bottle2=i
            
            
    get_replace_bottle(i, )
    print "Move arm to pregrip position for node",bottle1
    print "Grip bottle",bottle1
    print "Move arm to safe position",bottle1
    print "Move arm above glass"
    print "Pour"
    print "Move arm to safe position",bottle1
    print "Place bottle back at node",bottle1
    print "Move arm to pregrip position for node",bottle1

    print "Move arm to pregrip position for node",bottle2
    print "Grip bottle",bottle2
    print "Move arm to safe position",bottle2
    print "Move arm above glass"
    print "Pour"
    print "Move arm to safe position",bottle2
    print "Place bottle back at node",bottle2
    print "Move arm to pregrip position for node",bottle2

    print "Move arm back to starting position"

def recipe_2():
    print "Recipe 2:"
    print
    for i in range(4):
        if node[i]=="yellow":
            bottle1=i
        elif node[i]=="blue":
            bottle2=i
    print "Move arm to pregrip position for node",bottle1
    print "Grip bottle",bottle1
    print "Move arm to safe position",bottle1
    print "Move arm above glass"
    print "Pour"
    print "Move arm to safe position",bottle1
    print "Place bottle back at node",bottle1
    print "Move arm to pregrip position for node",bottle1

    print "Move arm to pregrip position for node",bottle2
    print "Grip bottle",bottle2
    print "Move arm to safe position",bottle2
    print "Move arm above glass"
    print "Pour"
    print "Move arm to safe position",bottle2
    print "Place bottle back at node",bottle2
    print "Move arm to pregrip position for node",bottle2

    print "Move arm back to starting position"
    

 

def get_replace_bottle(i, is_get):
  if i == 0:
    limb.move_to_joint_positions(home)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(pre_grip_1_wp1)
    limb.move_to_joint_positions(pre_grip_1_wp2)
    limb.move_to_joint_positions(grip_1)
    if is_get:
      gripper.set_position(0)
    else:
      gripper.set_position(100)
    limb.move_to_joint_positions(pre_grip_1_wp2)
    limb.move_to_joint_positions(pre_grip_1_wp1)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(home)
    
  elif i == 1:
    limb.move_to_joint_positions(home)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(pre_grip_2_wp1)
    limb.move_to_joint_positions(pre_grip_2_wp2)
    limb.move_to_joint_positions(grip_2)
    if is_get:
      gripper.set_position(0)
    else:
      gripper.set_position(100)
    limb.move_to_joint_positions(pre_grip_2_wp2)
    limb.move_to_joint_positions(pre_grip_2_wp1)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(home)
    
  elif i == 2:
    limb.move_to_joint_positions(home)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(pre_grip_3_wp1)
    limb.move_to_joint_positions(pre_grip_3_wp2)
    limb.move_to_joint_positions(grip_3)
    if is_get:
      gripper.set_position(0)
    else:
      gripper.set_position(100)
    limb.move_to_joint_positions(pre_grip_3_wp2)
    limb.move_to_joint_positions(pre_grip_3_wp1)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(home)
    
  else:
    limb.move_to_joint_positions(home)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(pre_grip_4_wp1)
    limb.move_to_joint_positions(pre_grip_4_wp2)
    limb.move_to_joint_positions(grip_4)
    if is_get:
      gripper.set_position(0)
    else:
      gripper.set_position(100)
    limb.move_to_joint_positions(pre_grip_4_wp2)
    limb.move_to_joint_positions(pre_grip_4_wp1)
    limb.move_to_joint_positions(pre_grip_all)
    limb.move_to_joint_positions(home)
    

def pour_bottle():
  limb.move_to_joint_positions(home)
  limb.move_to_joint_positions(pre_pour_1)
  limb.move_to_joint_positions(pre_pour_2)
  limb.move_to_joint_positions(pour)
  limb.move_to_joint_positions(pre_pour_2)
  limb.move_to_joint_positions(pre_pour_1)
  limb.move_to_joint_positions(home)
  
  
  
  
  
def main():
	init_sawyer()
  rospy.subscriber("camera topic", image, camera_callback)
  rospy.subscriber("order topic", int, order_callback)
  order = -1
  shutdown = -1
	while not rospy.is_shutdown():
		if order is None: continue
    if order==0:
      recipe_1()
    elif order==1:
      recipe_2()
    else:
      rospy.shutdown()
      
    order = None


if __name__ == "__main__":
	main()