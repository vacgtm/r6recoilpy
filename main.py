from pynput import mouse, keyboard
from pynput.mouse import Button
import time
import threading
import ctypes, os
from modules.readjson import read_json as rjv


mouse_controller = mouse.Controller()
is_pressed = False
is_left_pressed = False
is_right_pressed = False

x_val = 0
y_val = 0
speed = 0
toggle_key = "p"
reset_button = "h"

toggled = False
running = True


def move_mouse(dx, dy):
    ctypes.windll.user32.mouse_event(0x0001, int(dx), int(dy), 0, 0)


def recoil_code():
    global is_pressed, toggled, running
    while running:
        if is_pressed and toggled:
            move_mouse(x_val, y_val)
            time.sleep(speed)
        else:
            time.sleep(0.01)


def on_click(x, y, button, pressed):
    global is_left_pressed, is_right_pressed, is_pressed

    if button == Button.left:
        is_left_pressed = pressed
    elif button == Button.right:
        is_right_pressed = pressed

    is_pressed = is_left_pressed and is_right_pressed


def on_press(key):
    global toggled
    try:
        if key == keyboard.KeyCode.from_char(toggle_key):
            toggled = not toggled
            print("toggled" if toggled else "untoggled")
        elif key == keyboard.KeyCode.from_char(reset_button):
            return init()
    except AttributeError:
        pass


def init():
    global toggle_key, reset_button
    os.system("cls")
    print("-- r6 recoil compensator --")
    print("--- Presets ---\nCustom\nG36C\nMP7\nSMG12\nMP5\nAK12\nF2")

    toggle_key = rjv("configuration/config.json", "toggle_key")
    reset_button = rjv("configuration/config.json", "reset_button")

    a = input("\n\n\n\n> ")
    run_all(a.lower())


def run_all(pre):
    global x_val, y_val, speed, toggled
    toggled = False

    if pre.lower() == "g36c":
        x_val = 0.999
        y_val = 6.9
        speed = 0.025
    elif pre.lower() == "mp7":
        x_val = 0.05
        y_val = 7.4
        speed = 0.02
    elif pre.lower() == "smg12":
        x_val = 3.5
        y_val = 23
        speed = 0.047
    elif pre.lower() == "mp5":
        x_val = 0.05
        y_val = 11
        speed = 0.05
    elif pre.lower() == "ak12":
        x_val = 0.0001
        y_val = 5
        speed = 0.02
    elif pre.lower() == "f2":
        x_val = -1.75
        y_val = 21.3
        speed = 0.048
    elif pre.lower() == "custom":
        x_val = rjv("configuration/config.json", "x_val")
        y_val = rjv("configuration/config.json", "y_val")
        speed = rjv("configuration/config.json", "speed")

    os.system("cls")
    print(f"Loaded {pre} preset.")


threading.Thread(target=recoil_code, daemon=True).start()

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener.start()
keyboard_listener.start()

init()

mouse_listener.join()
keyboard_listener.join()
