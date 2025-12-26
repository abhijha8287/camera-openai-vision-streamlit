import cv2
from ultralytics import YOLO
import time

# Load YOLOv8 model (nano = fastest for CPU)
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# FPS calculation
prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO tracking
    results = model.track(frame, persist=True, classes=[0], conf=0.4)

    # Draw results
    annotated_frame = results[0].plot()

    # FPS calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    cv2.putText(annotated_frame, f"FPS: {int(fps)}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("YOLOv8 Person Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
