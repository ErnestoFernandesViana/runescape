import pyautogui as pag
import cv2 as cv 
import numpy as np
from rs_window import Client_Window, Rectangle
import json 
import os 

with open("./rs_window/bag_slots_cords.json", 'r') as file:
    window_slots = json.load(file)

class Bag():
    def __init__(self):
        self.client = Client_Window()
        self.bag_window_cords = {int(key[-2:]) : value for key, value in window_slots.items()}
        self.bag_screen_cords = {key: self.client.convert_window_to_screen_cord(value)
                                for key, value in self.bag_window_cords.items()}


bag = Bag()
print(bag.bag_window_cords)
print(bag.bag_screen_cords)