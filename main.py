import time
import pyautogui
from random import randint

EVENTS = ['ctrl+tab', 'alt+tab']

FUNCTIONS = ["mousemove()", "key_up()", "key_down()", "key_right()", "key_left()"]

def mousemove():
    x = randint(100, 999)
    y = randint(100, 999)
    pyautogui.moveTo(x, y)

def key_up():
    pyautogui.press('up')

def key_down():
    pyautogui.press('down')

def key_right():
    pyautogui.press('right')

def key_left():
    pyautogui.press('left')

while True:
    print("Started")
    pyautogui.hotkey(*EVENTS[randint(0, len(EVENTS)-1)].split('+'))

    for i in range(0, randint(20, 25)):
        exec(FUNCTIONS[randint(0, len(FUNCTIONS)-1)])
        time.sleep(randint(1, 2))
