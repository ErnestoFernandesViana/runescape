from jinja2 import pass_context
import pyautogui as pag
import sys 
import keyboard 
from timeit import default_timer as time 

sys.path.insert(0, 'rs_window')

from rs_window import Skilling_StartUp
sk = Skilling_StartUp()
while True:
    if keyboard.is_pressed('5'):
        t = time()
        im = pag.screenshot(region = sk.action_screen_rect)
        try:
            im.save(f'Ohm\photos\olm_head\olm_photo_{int(t)}.png')
            continue
        except:
            print('couldn save the photo')
            continue
    elif keyboard.is_pressed('q'):
        break

