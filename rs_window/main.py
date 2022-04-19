import pyautogui as pag
import cv2 as cv 
import numpy as np
from rs_window import Client_Window
import json
import time 

dictionary = {}
position = 1
client = Client_Window()
while position < 29:
    x = client.get_location_on_window()
    time.sleep(0.2)
    y = client.get_location_on_window()
    time.sleep(0.2)
    dictionary['bag_rect_slot: ' + str(position)] = (x, y)
    position += 1
    time.sleep(0.2)
with open("bag_rect_slots_cords.json", "w") as outfile:
    json.dump(dictionary, outfile)
