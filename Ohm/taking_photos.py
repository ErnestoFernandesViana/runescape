from jinja2 import pass_context
import pyautogui as pag
import sys 
import keyboard 
import time 

sys.path.insert(0, 'rs_window')

from rs_window import Skilling_StartUp
sk = Skilling_StartUp()
left_c = 0
middle_c = 0
right_c = 0

while True:
    if keyboard.is_pressed('b'):
        while True:
            if keyboard.is_pressed('3'):
                while True:
                    im = pag.screenshot(region = sk.action_screen_rect)
                    im.save(f'Ohm\Olm\olm_head\olm_right\{right_c}.png')
                    print('Olm looking right saved.')
                    right_c += 1 
                    time.sleep(0.1)
                    if keyboard.is_pressed('b') or keyboard.is_pressed('1') or keyboard.is_pressed('2'):
                        break 
            if keyboard.is_pressed('2'):
                while True:
                    im = pag.screenshot(region = sk.action_screen_rect)
                    im.save(f'Ohm\Olm\olm_head\olm_middle\{middle_c}.png')
                    print('Olm looking forward saved.')
                    middle_c += 1 
                    time.sleep(0.1)
                    if keyboard.is_pressed('b') or keyboard.is_pressed('1') or keyboard.is_pressed('3'):
                        break 
            if keyboard.is_pressed('1'):
                while True:
                    im = pag.screenshot(region = sk.action_screen_rect)
                    im.save(f'Ohm\Olm\olm_head\olm_left\{left_c}.png')
                    print('Olm looking right saved.')
                    left_c += 1 
                    time.sleep(0.1)
                    if keyboard.is_pressed('b') or keyboard.is_pressed('3') or keyboard.is_pressed('2'):
                        break 
            if keyboard.is_pressed('q'):
                break 
    if keyboard.is_pressed('q'):
        break 
