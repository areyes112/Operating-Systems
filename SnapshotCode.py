import cv2 as cv

# Initialize webcam
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Default mode (regular / no filter)
mode = 'regular'
print("Press 'r' for regular, 'g' for grayscale, 'b' for Gaussian blur, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting ...")
        break

    # Apply filter based on current mode
    if mode == 'regular':
        processed = frame  # No filter applied
    elif mode == 'grayscale':
        processed = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    elif mode == 'gaussian':
        processed = cv.GaussianBlur(frame, (15, 15), 0)

    # Display result
    cv.imshow('Webcam Filters', processed)

    # Check for key presses
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Exiting...")
        break
    elif key == ord('r'):
        mode = 'regular'
        print("Switched to Regular (no filter) mode")
    elif key == ord('g'):
        mode = 'grayscale'
        print("Switched to Grayscale mode")
    elif key == ord('b'):
        mode = 'gaussian'
        print("Switched to Gaussian Blur mode")

# Release resources
cap.release()
cv.destroyAllWindows()
