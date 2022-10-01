#Importing only neccesary things to save processing time
from pyautogui import moveTo, FAILSAFE, click, scroll, hotkey, press, pixelMatchesColor
from pynput.mouse import Events as event
from pynput.mouse import Controller as Mcontroller

mouse = Mcontroller() #Assigning Controllers to a var for easiar use.
current_cycle = 0 #the cycle its currently on.
delay = event() #to add a delay in-between cetain actions.
delay.get(3)
FAILSAFE = True

while current_cycle != 1: #Start of the loop change the num after "!=" to the amount of applications you need to fill.
    at_right_place = 0
    moveTo(1025, 372, .2)
    click()
    delay.get(.9)
    mouse.scroll(0,-20)

    while at_right_place != 1:#confirming if the script has scrolled to the bottom, by checking if the color of a pixiel in bottom left, if its grey
        if pixelMatchesColor(1365, 763,(135, 135, 135)) == True :
            delay.get(0.3)
            moveTo(688, 650,)
            click(clicks=2)
            at_right_place += 1
        else:
            mouse.scroll(0,-20)

    hotkey('ctrl', 'c')
    delay.get(.3)
    press('esc')

    delay.get(.5)
    moveTo(1128, 372)
    click()

    delay.get(.7)
    moveTo(688, 236)
    click()

    hotkey('ctrl', 'v')
    moveTo(883, 465)
    click()

    delay.get(3.5)
    current_cycle += 1
    print(current_cycle)