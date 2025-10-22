import pyautogui
import time
#print (pyautogui.position())

#Rodar infinitamente
#while(True):
#print(pyautogui.position())#rodar infinitamente
pyautogui.PAUSE = 0.3
# mover o mouse para diferentes direcoes.



time.sleep(1)
pyautogui.moveTo(822,149,duration=2)
time.sleep(1)
pyautogui.click(x=822, y=149)


time.sleep(2)
pyautogui.click(x=611,y=246)

time.sleep(1)
pyautogui.click(x=535,y=291)
pyautogui.write("Maluise3012#")
pyautogui.click(x=874,y=430)

