import pyautogui
import time
import os

os.system("start chrome https://www.youtube.com/")

time.sleep(5)

pyautogui.click(x=342, y=216)

pyautogui.typewrite("Musica relaxante", interval=0.1)
pyautogui.press("enter")