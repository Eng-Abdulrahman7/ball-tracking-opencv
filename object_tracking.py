import cv2
import numpy as np

cap = cv2.VideoCapture("play.mp4")
ret, frame = cap.read()
if not ret:
    print("Error: Cannot read video!")
    exit()

frame = cv2.resize(frame, (640, 480), )  


bbox = cv2.selectROI("Select the Ball (Zoom Out)", frame, False)
tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 
    frame = cv2.resize(frame, (640, 480), )  # نفس نسبة التصغير
    
    success, bbox = tracker.update(frame)
    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Tracking Lost!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Tracking", frame)
    if cv2.waitKey(30) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()