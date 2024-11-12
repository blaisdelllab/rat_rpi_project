import pygame
import pygame.camera

# Initialize pygame and the camera module
pygame.init()
pygame.camera.init()

# Replace '/dev/video0' with the correct device path for your identified USB camera
camera_device = '/dev/video0'  # Use the device path you identified

# Create a Camera object with a specific resolution (adjust resolution as needed)
cam = pygame.camera.Camera(camera_device, (640, 480))

# Start the camera
cam.start()

# Create a display window
screen = pygame.display.set_mode((640, 480))

running = True
while running:
    # Capture an image from the camera
    image = cam.get_image()
    screen.blit(image, (0, 0))
    pygame.display.update()

    # Handle events to quit the display window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Stop the camera and quit
cam.stop()
pygame.quit()
