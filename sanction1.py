from pynput.mouse import Button
from pynput.mouse import Events as events
from pynput.mouse import Controller as Mcontroller
from pynput.keyboard import Controller as Kcontroller
from pynput.keyboard import Key

delay =  events()
fill = 1
use_mouse = Mcontroller()
keyboard = Kcontroller()
delay.get(3)

while fill != 100:
    delay.get(0.1)
    use_mouse.position = (688, 212)
    use_mouse.click(Button.left, 1
    delay.get(0.1)
    use_mouse.position = (883, 446)
    use_mouse.click(Button.left, 1)
    delay.get(3.5)
    fill += 1
    print(fill)
print("done")
