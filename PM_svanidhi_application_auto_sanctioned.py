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

while fail_safe != 3:
    use_mouse.position = (1243, 344)
    use_mouse.click(Button.left, 1)
    use_mouse.position = (839, 243)
    use_mouse.click(Button.left, 1)
    delay.get(3.5)
    fail_safe += 1
    print(fail_safe)

"""# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
"""

