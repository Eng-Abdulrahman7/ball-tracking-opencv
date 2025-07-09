# ball-tracking-opencv
This project is designed to track a moving ball in a video using CSRT Tracker in OpenCV. 

Ball Tracking with CSRT Tracker

This project is designed to track a moving ball in a video using CSRT Tracker in OpenCV. The user selects the ball manually using selectROI and the tracker follows the ball throughout the video. If tracking is lost, the program will display a “Tracking Lost!” message.

Features
	•	Manual Ball Selection: The user selects the ball in the first frame using a rectangular bounding box (selectROI).
	•	Real-Time Tracking: The ball is tracked frame-by-frame using the CSRT Tracker.
	•	Tracking Lost Detection: If the tracker loses the ball, it will display a “Tracking Lost!” message.
	•	Resizable Frame: The frame is resized to 640x480 for easier visibility and processing.

Requirements:
	•	Python 3.x
	•	OpenCV (Make sure to install it with pip install opencv-python).

⸻

How to Use:
	1.	Download the Files:
	•	Download the code file (ball_tracking.py) and the video file (play.mp4).
	2.	Place the Video and Code in the Same Folder:
	•	Place the video file play.mp4 in the same folder where the code ball_tracking.py is located.
	3.	Run the Code
 4.	Select the Ball Manually:
	•	When the script starts, it will show a window asking you to manually select the ball by drawing a bounding box around it using the mouse.
	5.	Tracking:
	•	Once the ball is selected, the script will begin tracking it. If the tracking is lost, the message “Tracking Lost!” will appear on the screen.
	6.	Exit:
	•	Press q to exit the program.

⸻

Code Explanation:
	1.	Video Capture: The code starts by opening the video using cv2.VideoCapture(). If the video cannot be opened, an error message is displayed.
	2.	ROI Selection: At the beginning of the script, cv2.selectROI() is used to manually select the bounding box around the ball.
	3.	Tracker Initialization: After selecting the bounding box, the tracker is initialized with TrackerCSRT_create() and tracker.init().
	4.	Tracking Loop: In each frame, tracker.update() is called to update the tracker. If tracking is successful, a rectangle is drawn around the ball. If tracking fails, the message “Tracking Lost!” is displayed.
	5.	Exit Mechanism: Press q to stop the program and exit.
