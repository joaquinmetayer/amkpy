'''AMKpy
   Powerful auto mouse click and keyboard type in python.
   
   https://joaquinmetayer.github.io/amkpy/
   https://github.com/joaquinmetayer/amkpy'''

#imports
from time import sleep
import pyautogui
import math
import time
import random

#time to start spotligth search
time.sleep(5)

#calling google chrome
pyautogui.typewrite('chrome')
pyautogui.hotkey('return')

#waiting load
time.sleep(2)

#go fullscreen
pyautogui.click(70, 40)

#go web to draw
pyautogui.click(325, 55, duration=1)
pyautogui.typewrite('https://kleki.com/')
pyautogui.hotkey('return')
time.sleep(3)

#starting draw

#circles
R = 90
(x,y) = pyautogui.size()
(X,Y) = pyautogui.position(580,311)
pyautogui.moveTo(X+R,Y)
pyautogui.mouseDown();
for i in range(360):  
    if i%6==0:
       pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
R = 80
(x,y) = pyautogui.size()
(X,Y) = pyautogui.position(580,311)
pyautogui.moveTo(X+R,Y)
pyautogui.mouseDown();
for i in range(360):  
    if i%6==0:
       pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
R = 70
(x,y) = pyautogui.size()
(X,Y) = pyautogui.position(580,311)
pyautogui.moveTo(X+R,Y)
pyautogui.mouseDown();
for i in range(360):  
    if i%6==0:
       pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
R = 60
(x,y) = pyautogui.size()
(X,Y) = pyautogui.position(580,311)
pyautogui.moveTo(X+R,Y)
pyautogui.mouseDown();
for i in range(360):  
    if i%6==0:
       pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))

#3d tunnel
distance = 300
delta = 5
button='left'
delay=0.1
pyautogui.mouseDown();
while distance > 0:
  pyautogui.dragRel(distance, random.randint(0, 10), duration=delay, button=button)
  distance = distance - delta
  pyautogui.dragRel(random.randint(0, 10), distance, duration=delay, button=button)
  pyautogui.dragRel(-distance, random.randint(0, 10), duration=delay, button=button)
  distance = distance - delta
  pyautogui.dragRel(random.randint(0, 10), -distance, duration=delay, button=button)
