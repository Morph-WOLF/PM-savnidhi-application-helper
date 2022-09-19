from pyautogui import moveTo, FAILSAFE, click, scroll, hotkey, press, pixelMatchesColor
from pynput.mouse import Events as event
from pynput.mouse import Controller as Mcontroller
mouse = Mcontroller()
current_cycle = 0
delay = event()
delay.get(3)
FAILSAFE = True
while current_cycle != 100:
    at_right_place = 0
    moveTo(1010, 344, .2)
    click()
    delay.get(.9)
    mouse.scroll(0,-20)

    while at_right_place != 1:
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
    moveTo(1128, 333)
    click()

    delay.get(.7)
    moveTo(688, 212)
    click()
    hotkey('ctrl', 'v')
    moveTo(883, 446)
    click()

    delay.get(3.5)
    current_cycle += 1
    print(current_cycle)