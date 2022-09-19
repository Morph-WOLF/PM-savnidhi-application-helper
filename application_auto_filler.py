from pynput import mouse
from pynput.mouse import Button
from pynput.mouse import Events as events
from pynput.mouse import Controller as Mcontroller
from pynput.keyboard import Controller as Kcontroller
from pynput.keyboard import Key

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        x = print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False
def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

delay =  events()
fail_safe = 00
use_mouse = Mcontroller()
keyboard = Kcontroller()
# Collect events until released
delay.get(3)

while fail_safe != 100:
    use_mouse.position = (1010, 344)
    use_mouse.click(Button.left, 1)
    delay.get(0.8)
    use_mouse.scroll(0,-15)
    delay.get(0.7)
    use_mouse.position = (688, 650)
    use_mouse.click(Button.left, 2)
    delay.get(0.6)
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('c')
        keyboard.release('c')
    delay.get(.6)
    keyboard.press(Key.esc)
    use_mouse.position = (1128, 333)
    delay.get(0.1)
    use_mouse.click(Button.left, 1)
    use_mouse.position = (688, 212)
    use_mouse.click(Button.left, 1)
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('v')
        keyboard.release('v')
    delay.get(0.1)
    use_mouse.position = (883, 446)
    use_mouse.click(Button.left, 1)
    delay.get(3.5)
    fail_safe += 1
    print(fail_safe)
