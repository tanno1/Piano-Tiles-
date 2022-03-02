import pyautogui
import time
import keyboard
import random

#Tile 1 position: x=1196 y=650
#Tile 2 position: x=1301 y=650
#Tile 3 position: x=1386 y=650
#Tile 4 position: x=1507 y=650

# while True:
#     print(pyautogui.position())
#     time.sleep(1)

def click(x,y):
    pyautogui.position(x,y)
    pyautogui.click()
    time.sleep(.01)

while keyboard.is_pressed("q") == False:

    while True:
        pyautogui.moveTo(1196,650)
        if pyautogui.pixel(1196,650)[0] == 43:
            click(1196,650)
        elif pyautogui.moveTo(1301,650):
            if pyautogui.pixel(1301, 650)[0] == 43:
                click(1301, 650)
        elif pyautogui.moveTo(1386,650):
            if pyautogui.pixel(1386, 650)[0] == 43:
                    click(1386, 650)
        elif pyautogui.moveTo(1507,650):
            if pyautogui.pixel(1507, 650)[0] == 43:
                    click(1507, 650)