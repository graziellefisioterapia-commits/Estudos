import pyautogui
import time
import os


os.system("start chrome")

time.sleep(3)

pyautogui.typewrite("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal", interval= 0.1)
pyautogui.press("enter")