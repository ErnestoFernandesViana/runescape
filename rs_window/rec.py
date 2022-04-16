import pyautogui as pag
import sys 
import cv2 as cv
import numpy as np
from rs_window import Client_Window
from screen_input import de_rectangle

attrs = lambda x : [y for y in dir(x) if not y.startswith('_')]

client = Client_Window()
client.activate()
client_region = client.client_region()
print(client_region)
print(client.topleft_cord, client.bottomright_cord)
s_path = 'C:/Users\Ernesto Fernandes/Desktop/projects/runescape/fishing/photos/shrimp.png'
result = pag.locateAllOnScreen(s_path, confidence=0.7, region=client.client_region())
boxes = list(result)
print(boxes)
print(attrs(boxes[0]))
print(boxes[0])
color = (255, 0, 0)
im = pag.screenshot(region= client.client_region())
open_cv_image = np.array(im.convert('RGB'))
open_cv_image = open_cv_image[:, :, ::-1].copy() 
if boxes:
    for box in boxes:
        #cordenates = box.left, box.top, box.width, box.height
        print(box)
        cordenates = de_rectangle(box.left, box.top, box.width, box.height)
        print(cordenates)
        cordenates[0] -= client.topleft_cord[0]
        cordenates[2] -= client.topleft_cord[0]
        cordenates[1] -= client.topleft_cord[1]
        cordenates[3] -= client.topleft_cord[1]
        print(cordenates)
