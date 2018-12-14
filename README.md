### Sawyer Bartender

Ryan Wood, Josh Meyer, Josiah Graham, Eli Kopp-Devol

#### How To Run
First begin by running the following command:
python cameratest.py 
This will initialize the head camera, and show you a live feed of what the head camera sees.  Without running this code first, the head camera will not function properly.
Next run:
python sawyer_bot.py
This will bring up a tkinter GUI in which you can select a drink you wish to order.  Once either Screwdriver or Rum and Coke has been selected, the sawyer arm will pick up the correct bottles and make your drink for you.  The gui and program will then exit.

#### Important Note
In order for this program to run properly, the 4 bottles must be located on the correct spaces.  It does not matter which bottle is in which space, our script will use OpenCV to detect the color of each bottle at each location, but if the bottles are misaligned, the sawyer arm will not function properly.  The glass must also be located in the correct position or else the sawyer arm will make a hug mess.

#### Other Scripts
Clearly, there are many other scripts in this git repo.  They were mainly used for testing purposes.  Noteably, app.html and app.css, were originally going to act as our gui, but due to time contraints, we ended up using tkinter instead.  ColorDetect.py houses an early version of our OpenCV code that is implemented in sawyer_bot.py.  gripTest.py was a file used when testing whether the sawyer could easily grab and maneuver the bottles.  ros_image_saver.py was our final code we used to take a picture with the head camera, subscribe to that image, save it, and then pass it to colorDetect.py.  sawyer_test.py was mainly used for testing the sawyer's movements and finding waypoints.  tkintertest.py was used to create and test the original tkinter gui.  And waypoints.txt was the document where we originally stored all of our waypoints for sawyer.
