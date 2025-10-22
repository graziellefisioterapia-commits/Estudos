import pyautogui
import time

pyautogui.PAUSE= 2

pyautogui.dragRel(-200, 0, duration=2)
pyautogui.dragRel(0, 200, duration=2)
pyautogui.dragRel(200, 0, duration=2)
pyautogui.dragRel(0, -200, duration=2)