'''AMKpy
   Powerful auto mouse click and keyboard type in python.
   
   https://joaquinmetayer.github.io/amkpy/
   https://github.com/joaquinmetayer/amkpy'''

#imports
import pyautogui
import time

#open spotligth
time.sleep(5)

#calling chrome
pyautogui.typewrite('chrome')
pyautogui.hotkey('return')
time.sleep(2)
pyautogui.click(70, 40)

#reps
for i in range(2):

#code to repeat
    pyautogui.click(325, 55, duration=1)
    #paste your README.md edit link here
    pyautogui.typewrite('https://github.com/joaquinmetayer/autopusher/edit/main/README.md')
    pyautogui.hotkey('return')
    time.sleep(3)
    pyautogui.click(960, 450)
    pyautogui.hotkey('command', 'a')
    #writing the text
    pyautogui.typewrite('Hello! What do you see?? I am a script for push nothing, yes, nothing.')
    #zoom out screen
    pyautogui.hotkey('command', '-')
    pyautogui.hotkey('command', '-')
    pyautogui.hotkey('command', '-')
    pyautogui.hotkey('command', '-')
    pyautogui.hotkey('command', '-')
    #commit
    pyautogui.click(500, 720, duration=1)
    #zoom in screen
    pyautogui.hotkey('command', '+')
    pyautogui.hotkey('command', '+')
    pyautogui.hotkey('command', '+')
    pyautogui.hotkey('command', '+')
    pyautogui.hotkey('command', '+')
    time.sleep(2)
#close window
pyautogui.hotkey('command', 'q')
pyautogui.hotkey('command', 'q')
pyautogui.hotkey('command', 'q')
