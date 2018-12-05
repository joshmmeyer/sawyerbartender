def colorDetect(image):

	import numpy as np
	import argparse
	import cv2

	num_bottles = 4

	# ap = argparse.ArgumentParser()
	# ap.add_argument("-i", "--image")
	# args = vars(ap.parse_args())

	image = cv2.imread(image)

	height, width = image.shape[:2]

	# Let's get the starting pixel coordiantes (top left of cropped top)
	# start_row, start_col = int(0), int(0)
	# # Let's get the ending pixel coordinates (bottom right of cropped top)
	# end_row, end_col = int(height), int(width * .25)

	Pos1 = image[0:int(height) , 0:int(width*.25)]


	cv2.imshow("Far Left", Pos1) 
	cv2.waitKey(0) 
	cv2.destroyAllWindows()

	# Let's get the starting pixel coordiantes (top left of cropped bottom)
	# start_row, start_col = int(0), int(width * .25)
	# # Let's get the ending pixel coordinates (bottom right of cropped bottom)
	# end_row, end_col = int(height), int(width*.5)
	Pos2 = image[0:int(height) , int(width*.25):int(width*.5)]

	# print start_row, end_row 
	# print start_col, end_col

	cv2.imshow("Middle Left", Pos2) 
	cv2.waitKey(0) 
	cv2.destroyAllWindows()

	# Let's get the starting pixel coordiantes (top left of cropped bottom)
	# start_row, start_col = int(0), int(width * .5)
	# # Let's get the ending pixel coordinates (bottom right of cropped bottom)
	# end_row, end_col = int(height), int(width*.75)
	Pos3 = image[0:int(height) , int(width*.5):int(width*.75)]

	cv2.imshow("Middle Right", Pos3) 
	cv2.waitKey(0) 
	cv2.destroyAllWindows()

	# Let's get the starting pixel coordiantes (top left of cropped bottom)
	# start_row, start_col = int(0), int(width * .75)
	# # Let's get the ending pixel coordinates (bottom right of cropped bottom)
	# end_row, end_col = int(height), int(width)
	Pos4 = image[0:int(height), int(width*.75):int(width)]

	cv2.imshow("Far Right", Pos4) 
	cv2.waitKey(0) 
	cv2.destroyAllWindows()

	# Finally, we can use image.size to give use the number of pixels in each part.

	# cropped_top.size
	# cropped_bot.size

	

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

			# cv2.imshow("images", np.hstack([image, output]))
			# cv2.waitKey(0)
			# print(cv2.countNonZero(mask))

			if cv2.countNonZero(mask) > 100000:
				color_pos.append(color) 


			color = color + 1

	return color_pos


def main():
	color_pos = colorDetect("bottlecolors.jpg")
	print(color_pos)

main()
