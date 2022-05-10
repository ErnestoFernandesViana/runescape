from jinja2 import pass_context
import pyautogui as pag
import sys 
import keyboard 
import time 
import cv2
import tensorflow as tf

sys.path.insert(0, 'rs_window')

from rs_window import Skilling_StartUp
sk = Skilling_StartUp()

categories = ['left','forward','right']

model = tf.keras.models.load_model('Ohm\olms.model33.hdf5')

def prepare(filepath):
    img_size = 200
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size, img_size))
    return new_array.reshape(-1, img_size, img_size, 1)

while True:
    if keyboard.is_pressed('b'):
        while True:
            im = pag.screenshot(region = sk.action_screen_rect)
            im.save(f'olm_state.png')
            prediction = model.predict([prepare('olm_state.png')])
            print(prediction)
            time.sleep(0.5)
            if keyboard.is_pressed('b'):
                time.sleep(2)
                break 
    if keyboard.is_pressed('q'):
        break 


