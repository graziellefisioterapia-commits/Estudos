import pyautogui
import time

pyautogui.PAUSE= 0.6


pyautogui.press("win")
pyautogui.write("bloco de notas")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("Automatizando com PyAutoGUI e divertido!",interval=0.2)


