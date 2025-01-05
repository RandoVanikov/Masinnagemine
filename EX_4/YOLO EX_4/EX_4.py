"""
EX 4

Tehke ise video asjadest, mida soovite kokku loendada.

Luua kontuuride leidmise programm, mis loetleb õige koguse objekte videos
ning kuvab selle numbri ekraanil. Lisaks, joonistab kastid ümber objektide.

"""
import cv2 as cv
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('best.pt')

# Load video (change source to 0 for webcam)
video_source = "VID_3.mp4"  # Replace with your video file path or 0 for webcam
capture = cv.VideoCapture(video_source)

if not capture.isOpened():
    print("Error: Unable to open video source.")
    exit()

# Set confidence threshold
confidence_threshold = 0.5  # Confidence threshold (0.0 to 1.0)

while True:
    ret, frame = capture.read()
    if not ret:
        print("Error: Frame capture failed or video ended.")
        break

    # Detect objects using YOLO
    results = model(frame)[0]

    object_count = 0

    for box in results.boxes:
        coordinates = box.xyxy[0].tolist()
        confidence = round(box.conf[0].item(), 2)

        if confidence >= confidence_threshold:
            object_count += 1
            class_id = results.names[int(box.cls)]

            # Draw bounding box and label
            cv.rectangle(frame, (int(coordinates[0]), int(coordinates[1])),
                         (int(coordinates[2]), int(coordinates[3])), (255, 0, 0), 2)
            cv.putText(frame, f"{class_id} {confidence:.2f}",
                       (int(coordinates[0]), int(coordinates[1]) - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display object count
    cv.putText(frame, f"Objects Detected: {object_count}", (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the video frame with detections
    cv.imshow("Object Counter", frame)

    # Exit on 'q' key
    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release resources
capture.release()
cv.destroyAllWindows()
