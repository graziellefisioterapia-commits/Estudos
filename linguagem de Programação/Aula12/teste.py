import pyautogui
import time

time.sleep(5)
im1= pyautogui.screenshot(region=(45,29,329,532))
im1.save("imagem2.png")







im2= pyautogui.screenshot ("imagem.png")