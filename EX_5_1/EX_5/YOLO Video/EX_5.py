"""
EX 5
YOLO-ga tuvastus video või live kaamera pealt

"""
from sympy.physics.vector import CoordinateSym
from ultralytics import YOLO
import cv2 as cv

# Laeme mudeli
model = YOLO('yolo11n.pt')

# laeme video- cv.VideoCapture(0)
#capture = cv.VideoCapture(0)
#capture = cv.VideoCapture("")
capture = cv.VideoCapture("VIDEO_1.mp4")


if not capture.isOpened():
    print("something exploded")
    exit()

while(True):

    ret, image = capture.read()

    if not ret:
       print("frame return error")
       break

    results = model(image)
    results = results[0]


    for box in results.boxes:
        coordinates = box.xyxy[0].tolist()
        confidence = round(box.conf[0].item(), 2)
        class_id = results.names[int(box.cls)]

        cv.rectangle(image, (int(coordinates[0]), int(coordinates[1])), (int(coordinates[2]), int(coordinates[3])),
                     (255, 0, 0), 2)
        cv.putText(image, class_id, (int(coordinates[0]), int(coordinates[1])), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0),
                   2)
        cv.putText(image, str(confidence), (int(coordinates[2]), int(coordinates[3])), cv.FONT_HERSHEY_SIMPLEX, 1,
                   (255, 0, 0), 2)

    cv.imshow('window', image)

    # Ootame nupu vajutust, et lõpetada tsükkel
    key = cv.waitKey(10) & 0xFF
    if key == ord("q"):
        break


cv.destroyAllWindows()