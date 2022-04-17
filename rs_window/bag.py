import pyautogui as pag
import cv2 as cv 
import numpy as np
from rs_window import Client_Window, Rectangle
import json 
import os 

with open("./rs_window/bag_slots_cords.json", 'r') as file:
    window_slots = json.load(file)

class Bag():
    path = "./rs_window/photos/"
    def __init__(self):
        self.client = Client_Window()
        self.bag_window_cords = {int(key[-2:]) : value for key, value in window_slots.items()}
        self.bag_screen_cords = {key: self.client.convert_window_to_screen_cord(value)
                                for key, value in self.bag_window_cords.items()}
        self.topleft_window = (551, 234)
        self.bottomright_window = (739, 490)
        self.bag_rectangle = Rectangle((self.topleft_window, self.bottomright_window), 'w')
        self.bag_list_cords = self.bag_rectangle.screen_list

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
        img_name = self.path + image + '.png'
        item_loc = pag.locateCenterOnScreen(img_name, confidence=confidence,
                                             region=self.bag_list_cords)
        if item_loc:
            pag.moveTo(*item_loc, 0.1) 
            pag.click()
        




if __name__ == '__main__':
    bag = Bag()
    """ print(bag.bag_rectangle.window_tuple)
    print(bag.bag_rectangle.screen_tuple)
    bag.client.show_rectangles(bag.bag_rectangle.window_tuple) """



    bag.move(10)
    bag.click_on_item('money')





    """ print(bag.client.client_region())
    print(bag.bag_rectangle.window_dict)
    print(bag.bag_rectangle.screen_dict)
    print(bag.bag_rectangle.window_list)
print(bag.bag_rectangle.screen_list) """