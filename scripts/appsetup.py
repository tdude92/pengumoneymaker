import pyautogui
import time

print("Please move your mouse to the icon of an open browser running club penguin on the task bar.")
print("Capturing in...")
for i in range(10, 0, -1):
    print("", i, "  ", end = "\r")
    time.sleep(1)

mouse_pos = pyautogui.position()
print("Position successfully captured.")

with open("browser_pos.txt", "w") as write_file:
    write_file.write(str(mouse_pos.x) + " " + str(mouse_pos.y))
