from pynput import mouse, keyboard
from pynput.mouse import Button
import time
import threading
import ctypes, os
from modules.readjson import read_json as rjv


### PLEASE NOTE,  NO MATTER WHAT PRESET YOU USE, THE TOGGLE KEY AND RESET BUTTON WRITTEN IN configuration/config.json WILL ALWAYS BE USED ###






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
    elif key == keyboard.KeyCode.from_char("h"):
        return init()


def init():
    os.system("cls")
    print("-- r6 recoil compensator --")
    print("--- Presets ---\nCustom\nG36C\nMP7")
    a = input("\n\n\n\n> ")
    if a.lower() == "g36c":
        os.system("cls")
        print("-- g36c preset loading --")
        time.sleep(2)
        run_all("g36c")
    elif a.lower() == "mp7":
        os.system("cls")
        print("-- mp7 preset loading --")
        time.sleep(2)
        run_all("mp7")
    elif a.lower() == "custom":
        os.system("cls")
        print("-- your custom preset is loading --")
        time.sleep(2)
        run_all("custom")

def run_all(pre):
    global x_val, y_val, speed, toggle_key, reset_button
    if pre == "g36c":
        
        x_val = 0.999
        y_val = 6.9
        speed = 0.025
        toggle_key = rjv("configuration/config.json", "toggle_key")
        reset_button = rjv("configuration/config.json", "reset_button")
    elif pre == "mp7":
        x_val = 0.05
        y_val = 7.4
        speed = 0.02
        toggle_key = rjv("configuration/config.json", "toggle_key")
        reset_button = rjv("configuration/config.json", "reset_button")
    elif pre == "custom":
        x_val = rjv("configuration/config.json", "x_val")
        y_val = rjv("configuration/config.json", "y_val")
        speed = rjv("configuration/config.json", "speed")
        toggle_key = rjv("configuration/config.json", "toggle_key")
        reset_button = rjv("configuration/config.json", "reset_button")
    
    os.system("cls")
    print("Loaded.")
    threading.Thread(target=recoil_code, daemon=True).start()

    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_press)
    mouse_listener.start()
    keyboard_listener.start()
    mouse_listener.join()
    keyboard_listener.join()







init()

















































#all settings just use compensators


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


###ASH SETTINGS G36C###
#same sens as always
#x_val = 0.999
#y_val = 6.9
#speed = 0.025
############################

## self code ##
