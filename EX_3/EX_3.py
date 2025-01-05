"""
kasutades opencv-d luua programm, mis:

küsib, mida teha soovid, seejärel

avab pildi

kui valitud "treshold", saab seadistada "treshold" väärtust
kui valitud "blur", saab seadistada "blur" väärtust
kui valitud "dialate", saab seadistada "dialate" väärtust
kui valitud "erode", saab seadistada "erode" väärtust
kui valitud "canny", saab seadistada "canny" väärtust

"""
import cv2 as cv
import numpy as np

def on_change(value):
    pass

# Window name
window_name = 'Image Processor'

# Create the window and set its size
cv.namedWindow(window_name, cv.WINDOW_NORMAL)
cv.resizeWindow(window_name, 800, 600)

# Load the image
image_path = '../coins.png'  # Replace with your image path
image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print("Failed to load image. Check the file path.")
    exit()

# Create trackbars for different operations
cv.createTrackbar('Threshold Value', window_name, 127, 255, on_change)
cv.createTrackbar('Blur Kernel', window_name, 1, 50, on_change)
cv.createTrackbar('Dilate Iterations', window_name, 1, 50, on_change)
cv.createTrackbar('Erode Iterations', window_name, 1, 50, on_change)
cv.createTrackbar('Canny Threshold', window_name, 50, 255, on_change)

while True:
    # Start with the original image
    result_image = image.copy()

    # Apply Threshold
    thresh_val = cv.getTrackbarPos('Threshold Value', window_name)
    _, result_image = cv.threshold(result_image, thresh_val, 255, cv.THRESH_BINARY)

    # Apply Blur
    blur_val = cv.getTrackbarPos('Blur Kernel', window_name)
    if blur_val % 2 == 0:
        blur_val += 1  # Kernel size must be odd
    if blur_val > 1:  # Skip if kernel size is too small
        result_image = cv.GaussianBlur(result_image, (blur_val, blur_val), 0)

    # Apply Dilate
    dilate_iter = cv.getTrackbarPos('Dilate Iterations', window_name)
    if dilate_iter > 0:
        kernel = np.ones((3, 3), np.uint8)
        result_image = cv.dilate(result_image, kernel, iterations=dilate_iter)

    # Apply Erode
    erode_iter = cv.getTrackbarPos('Erode Iterations', window_name)
    if erode_iter > 0:
        kernel = np.ones((3, 3), np.uint8)
        result_image = cv.erode(result_image, kernel, iterations=erode_iter)

    # Apply Canny Edge Detection
    canny_thresh = cv.getTrackbarPos('Canny Threshold', window_name)
    if canny_thresh > 0:
        result_image = cv.Canny(result_image, canny_thresh, canny_thresh * 2)

    # Resize the processed image for display
    image_height = 500  # Space reserved for image
    image_width = 800   # Same as the window width
    resized_image = cv.resize(result_image, (image_width, image_height))

    # Create a blank canvas for combining image and trackbars
    combined_height = 600  # Window height
    canvas = np.zeros((combined_height, image_width), dtype=np.uint8)

    # Place the resized image in the canvas
    canvas[:image_height, :] = resized_image

    # Display the combined canvas
    cv.imshow(window_name, canvas)

    # Break the loop if 'q' is pressed
    key = cv.waitKey(10) & 0xFF
    if key == ord('q'):
        break

cv.destroyAllWindows()
