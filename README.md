This is a project for controlling the mouse using hand gestures on the camera.
The code will create a frame where the camera will be visible and it will take coordinates of the hand. 
On the camera it will check the distance between the thumb and the index finger.
If the distance matches the criteria then it will be considered as left click.
It will only be able to calculate this distance if all the fingers are shut and only the thumb and the index finger is open.
For right click it will be the thumb and the middle finger.
Same process of detecting the distance.
Once it knows which click it is, a label is shown on top of the frame.
It will either say "left click" or "right click".
The user needs to keep their hand infront of the camera and then move their hand towards the folder.
Once near the folder,only keep those two fingers open.
For left click on a folder/app/file etc,double click.
So open close those two fingers quickly twice infront of the camera.
To close the camera frame,press the esc key.
If the camera shutter is off or no camera on the device then a error message will be shown.
Four librarys are used:cv2(opencv-python),mediapipe,pyautogui and numpy.
The cv2 is used for hand gesture recognitionsseen on the camera.
The mediapipe is for opening the camera, handling the frame and the image.
Numpy is for all the calculations.
