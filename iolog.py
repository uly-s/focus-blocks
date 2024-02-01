import logging
import time
from pynput import mouse, keyboard

# Cooldown time in seconds
COOLDOWN = 0.1  # Adjust this to control frequency of log entries

last_time_logged = 0

# Setting up logging
logging.basicConfig(filename='io_log.txt', level=logging.INFO, 
                    format='%(asctime)s: %(message)s')

# mouse
def on_move(x, y):
    global last_time_logged
    current_time = time.time()
    if current_time - last_time_logged > COOLDOWN:
        logging.info(f"Mouse moved to ({x}, {y})")
        last_time_logged = current_time


def on_click(x, y, button, pressed):
    logging.info(f"Mouse {'Pressed' if pressed else 'Released'} at ({x}, {y}) with {button}")

def on_scroll(x, y, dx, dy):
    logging.info('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    
# # Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()

# # ...or, in a non-blocking fashion:
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()
    
# keyboard
def on_press(key):
    try:
        logging.info('key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    logging.info('key {0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as keyboard_listener, \
    mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as mouse_listener:
    keyboard_listener.join()
    mouse_listener.join()
    
