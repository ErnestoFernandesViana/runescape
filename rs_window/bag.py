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

    def check_last_space_empty(self):
        image = bag.path + 'empty' + '.png'
        result = pag.locateAllOnScreen(image, confidence=0.8, region=bag.bag_list_cords)
        result_list = list(result)
        if len(result_list) == 0:
            return False 
        else:
            return True 

    def show_items_in_bag(self, figure, confidence=0.8):
        image = self.path + figure + '.png'
        result = pag.locateAllOnScreen(image, confidence=confidence, region=bag.bag_list_cords)
        self.client.show_rectangles(result)
        return None


    def many_items_in_bag(self, figure, confidence=0.8):
        image = bag.path + figure + '.png'
        result = pag.locateAllOnScreen(image, confidence=confidence, region=bag.bag_list_cords)
        result_list = list(result)
        print(result_list)
        return len(result_list)



if __name__ == '__main__':
    bag = Bag()
    image = bag.path + 'empty' + '.png'

    print(bag.many_items_in_bag('money', 0.9))
    bag.show_items_in_bag('money', 0.9)
"""     result = pag.locateAllOnScreen(image, confidence=0.8, region=bag.bag_list_cords)
    bag.client.show_rectangles(result)
    print(bag.check_last_space_empty()) """
    