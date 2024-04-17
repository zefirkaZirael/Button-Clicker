import pyautogui as pa
import time
import keyboard
import cv2
import numpy as np

import multiprocessing


HOTKEY = "F2"

def activation():
    button_img = cv2.imread('button_image.png', cv2.IMREAD_COLOR)

    button_location = None
    while button_location is None and _activated.is_set():
        # screenshot of the screen
        screenshot = pa.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)

        # download buttion image

        # compare images
        result = cv2.matchTemplate(screenshot, button_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > 0.8:
            button_location = np.where(result >= max_val)
            button_center = (int(button_location[1] + button_img.shape[1]/2), int(button_location[0] + button_img.shape[0]/2))
            x, y = button_center
            print('Button found')
            pa.click(x, y)
            _button_was_pressed
            switch_active_state()
        else:
            print('No Button')
            end = time.time() + 1
            while time.time() < end:
                if keyboard.is_pressed(HOTKEY):
                    switch_active_state()
                    break
                time.sleep(0.1)

def switch_active_state():
    if _activated.is_set():
        # DEACTIVATE
        _activated.clear()

        print("AUTO-ACCEPT DEACTIVATED")
    else:
        # ACTIVATE
        _activated.set()

        print("AUTO-ACCEPT ACTIVATED")
#        play_random_sound("activate")


if __name__ == "__main__":

    # play_random_sound("startup")
    _activated = multiprocessing.Event()
    _button_was_pressed = multiprocessing.Event()


    while True:
        print(f"Waitig for hotkey {HOTKEY}...")

        keyboard.wait(HOTKEY)

        switch_active_state()
        activation()
