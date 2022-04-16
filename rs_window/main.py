import pyautogui as pag
import cv2 as cv 
import numpy as np
from rs_window import Client_Window, Rectangle
import json
import time 

dictionary = {}
position = 1
client = Client_Window()
while position < 29:
    dictionary['bag_slot: ' + str(position)] = client.get_location_on_window()
    position += 1
    time.sleep(0.2)
with open("bag_slots_cords.json", "w") as outfile:
    json.dump(dictionary, outfile)
