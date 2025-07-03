import pyautogui
import keyboard
import time

# Function to simulate desktop change
def change_desktop(direction):
    if direction == "left":
        keyboard.press_and_release("ctrl+win+left")
    elif direction == "right":
        keyboard.press_and_release("ctrl+win+right")
    
    # time.sleep(0.5)  # Delay to prevent rapid switching

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Set a small buffer for edge detection
edge_buffer = 10

while True:
    # Get current mouse position
    x, y = pyautogui.position()

    # Check if the mouse pointer is at the left or right edge
    if x <= edge_buffer and y >= screen_height*0.2 and y <= screen_height*0.8:
        change_desktop("left")
        time.sleep(1.5)  # Prevent rapid switching
    elif x >= screen_width - edge_buffer and y >= screen_height*0.2 and y <= screen_height*0.8:
        change_desktop("right")
        time.sleep(1.5)  # Prevent rapid switching

    time.sleep(0.1)  # Polling interval
