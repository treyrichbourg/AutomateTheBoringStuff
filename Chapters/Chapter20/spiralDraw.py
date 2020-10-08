import time
import pyautogui as pyag

time.sleep(5)
pyag.click()
distance = 300
change = 20
while distance > 0:
    pyag.drag(distance, 0, duration=0.2)  # Move Right
    distance = distance - change
    pyag.drag(0, distance, duration=0.2)  # Move Down
    pyag.drag(-distance, 0, duration=0.2)  # Move Left
    distance = distance - change
    pyag.drag(0, -distance, duration=0.2)  # Move Up
