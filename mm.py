import pyautogui
import time

# Interval for moving the mouse (in seconds)
interval = 10  # 3 minutes
intervale = 10
# Distance to move the mouse (in pixels)
distance = 200

try:
    print("Mouse mover started. Press Ctrl+C to stop.")
    while True:
        # Move the mouse to the right
        pyautogui.moveRel(distance, 0, duration=0.25)
        print("Mouse moved right.")
        time.sleep(interval)
        pyautogui.click()
        # Move the mouse to the left
        pyautogui.moveRel(-distance, 0, duration=0.25)
        print("Mouse moved left.")
        time.sleep(intervale)

except KeyboardInterrupt:
    print("Mouse mover stopped by user.")