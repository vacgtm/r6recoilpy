from pynput import mouse, keyboard
from pynput.mouse import Button
import time
import threading
import json, ctypes
mouse_controller = mouse.Controller()
is_pressed = False
is_left_pressed = False
is_right_pressed = False






toggled = False
x_val = 0.05
y_val = 7.4
speed = 0.02
toggle_key = "p"

def move_mouse(dx, dy):
    ctypes.windll.user32.mouse_event(0x0001, int(dx), int(dy), 0, 0)

def recoil_code():
    global is_pressed
    global toggled
    while True:
        if is_pressed and toggled:
            
            move_mouse(x_val, y_val)
        time.sleep(speed)

def on_click(x, y, button, pressed):
    global is_left_pressed, is_right_pressed, is_pressed

    if button == Button.left:
        is_left_pressed = pressed
    elif button == Button.right:
        is_right_pressed = pressed

    if is_left_pressed and is_right_pressed:
        is_pressed = True
    else:
        is_pressed = False

def on_press(key):
    global toggled
    if key == keyboard.KeyCode.from_char("p"):
        if toggled:
            print("untoggled")
            toggled = False
        else:
            print("toggled")
            toggled = True

threading.Thread(target=recoil_code, daemon=True).start()

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener.start()
keyboard_listener.start()
mouse_listener.join()
keyboard_listener.join()




























































### Bandit Settings ###
###sens###
#800 dpi#
#29 horizontal#
#31 vertical#
###sets###
#x = 0.05
#y = 7.4
#speed = 0.02
########################






## self code ##
