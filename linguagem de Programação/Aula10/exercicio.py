import pyautogui
import time

pyautogui.Pause = 0.7

pyautogui.press("win")#pausa de um segundo entre cada ação
pyautogui.write("bloco de notas")#escreve no teclado
pyautogui.press("enter")# aperte enter 
pyautogui.sleep(2)
pyautogui.press("enter")
pyautogui.write("Edna Assis")
pyautogui.sleep(1)
pyautogui.hotkey("ctrl","w")
pyautogui.press("right")
pyautogui.press("enter")

