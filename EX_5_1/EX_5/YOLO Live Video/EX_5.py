"""
EX 5
YOLO-ga tuvastus video või live kaamera pealt

"""
from sympy.physics.vector import CoordinateSym
from ultralytics import YOLO
import cv2 as cv
import time
import requests
import numpy as np

# Laeme mudeli
model = YOLO('yolo11n.pt')


while (True):

    ts = time.time()
    ts = round(ts)

    url = "https://www.ristmikud.tallinn.ee/last/cam069.jpg?=q"+str(ts)

    #küsime raami request-iga
    image_response = requests.get(url)
    image_array = np.array(bytearray(image_response.content), dtype=np.uint8)
    image = cv.imdecode(image_array, cv.IMREAD_COLOR)


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
