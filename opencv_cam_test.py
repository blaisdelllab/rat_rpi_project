import cv2

# Open a connection to the USB camera (usually index 0 for the first USB camera)
camera = cv2.VideoCapture(0)

# Check if the camera is opened correctly
if not camera.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Continuously capture frames
while True:
    ret, frame = camera.read()  # Read a frame from the camera
    
    if not ret:
        print("Failed to capture frame")
        break
    
    # Display the frame
    cv2.imshow('USB Camera Feed', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
camera.release()
cv2.destroyAllWindows()
