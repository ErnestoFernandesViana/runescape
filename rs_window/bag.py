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


    def move(self, number):
        self._bag_inventory()
        if (number < 1) or (number > 28) or not(isinstance(number, int)):
            raise Exception('Number must be integer between 1 and 28')
        pag.moveTo(*self.bag_screen_cords[number], 0.1)

    def _bag_inventory(self):
        """go to bag page"""
        self.client.activate()
        pag.press('f3')

    def click(self, number):
        self.move(number)
        pag.click()

    def click_on_item(self, image, confidence=0.8):
        self._bag_inventory()
        img_name = "./rs_window/photos/" + image + '.png'
        item_loc = pag.locateCenterOnScreen(img_name, confidence=confidence, region=self.client.client_region())
        pag.moveTo(*item_loc, 0.1) 
        pag.click()
        

bag = Bag()
bag.move(10)
bag.click(1)
print(os.listdir())
bag.click_on_item('money')