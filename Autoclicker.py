from asyncio import _enter_task
from turtle import left, right
import pyautogui
import time
import keyboard
import appJar

q = ("How many clicks do you want")
app = appJar.gui("auto clicker")
app.setSize("300x200")
app.setSticky("new")
app.addLabel(q)
pyautogui.PAUSE = 0

number_of_clicks = int (input ("Enter a Number: "))
time.sleep(5)
for i in range(number_of_clicks):
    pyautogui.leftClick()

keyboard.wait(pyautogui.rightClick)
