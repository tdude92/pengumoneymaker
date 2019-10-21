import pyautogui
import keyboard
import random
import time

# Coordinates of bounding box in form [x1, y1, x2, y2].
# Point 1 is the top left, point 2 is the bottom right.
mining_area_bbox = [720, 720, 1080, 925]
mineable_colors = [(103, 80, 76), (95, 73, 70), (99, 77, 73)]

with open("browser_pos.txt", "r") as read_file:
    browser_pos = list(map(int, read_file.read().split()))

# Open Firefox window with opened Club Penguin Tab.
pyautogui.moveTo(*browser_pos)
pyautogui.click(button = "left")

# Open map.
pyautogui.click(350, 950, button = "left")
time.sleep(0.5)

# Go to mine.
pyautogui.click(1315, 565, button = "left")
time.sleep(4)

# Enter mine.
pyautogui.click(1160, 480, button = "left")
time.sleep(5)

# Go to mining area.
pyautogui.click(1600, 815, button = "left")
time.sleep(5)

# Get some $$$
while True:
    randX = random.randint(mining_area_bbox[0], mining_area_bbox[2])
    randY = random.randint(mining_area_bbox[1], mining_area_bbox[3])

    pyautogui.moveTo(randX, randY)
    if not pyautogui.pixel(randX, randY) in mineable_colors:
        continue
    pyautogui.click(button = "left")
    time.sleep(2)

    pyautogui.click(590, 990, button = "left")
    pyautogui.click(590, 640, button = "left")

    time.sleep(8.5 + (random.randint(0, 100)/100))
    