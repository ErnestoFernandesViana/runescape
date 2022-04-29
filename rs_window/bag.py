from subprocess import NORMAL_PRIORITY_CLASS
import pyautogui as pag
import cv2 as cv 
import numpy as np
from rs_window import Client_Window, Rectangle
import json 
import os 
import copy
import time

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
        self.bag_list_cords = self.bag_rectangle.screen_rect

    def move(self, number):
        """move o cursor para uma posição da bag"""
        self._bag_inventory()
        if (number < 1) or (number > 28) or not(isinstance(number, int)):
            raise Exception('Number must be integer between 1 and 28')
        pag.moveTo(*self.bag_screen_cords[number], 0.1)
        return None

    def _bag_inventory(self):
        """go to bag page"""
        self.client.activate()
        pag.press('f3')

    def click(self, number, button='left'):
        """clica em uma posição da bag"""
        self._bag_inventory()
        self.move(number)
        pag.click(button = button)
        return True 

    def click_on_item(self, image, confidence=0.8, button='left'):
        """Clica em uma imagem na bag"""
        self._bag_inventory()
        img_name = self.path + image + '.png'
        item_loc = pag.locateCenterOnScreen(img_name, confidence=confidence,
                                             region=self.bag_list_cords)
        if item_loc:
            pag.moveTo(*item_loc, 0.1) 
            pag.click(button = button)
            return True 
        else:
            return False
    
    def click_item_on_bag(self, value, confidence=0.7, button = 'left'):
        """click on an image or number"""
        if isinstance(value, str):
            self.click_on_item(value, confidence, button=button)
        if isinstance(value, int):
            self.click(value, button=button)

    def check_last_space_empty(self):
        """checa se o ultimo espaço no ivnentório esta vazio"""
        self._bag_inventory()
        image = self.path + 'empty' + '.png'
        result = pag.locateOnScreen(image, confidence=0.8, region=self.bag_list_cords)
        if result == None:
            return False 
        else:
            return True 

    def show_items_in_bag(self, figure, confidence=0.8):
        """mostra em retângulos os itens na bag"""
        self._bag_inventory()
        image = self.path + figure + '.png'
        result = pag.locateAllOnScreen(image, confidence=confidence, region=bag.bag_list_cords)
        self.client.show_rectangles(result)
        return None




    def many_items_in_bag(self, figure, confidence=0.8):
        """conta quantos itens tem na bag. Intervalo de confiança é imporante"""
        self._bag_inventory()
        image = bag.path + figure + '.png'
        result = pag.locateAllOnScreen(image, confidence=confidence, region=bag.bag_list_cords)
        result_list = list(result)
        print(result_list)
        return len(result_list)

    def drop_item(self, value, confidence=0.8):
        """drop some item. It can be an integer or an image"""
        self._bag_inventory()
        if isinstance(value, str):
            img_name = self.path + value + '.png'
            item_loc = pag.locateCenterOnScreen(img_name, confidence=confidence,
                                                region=self.bag_list_cords)
            if item_loc:
                try:
                    pag.moveTo(*item_loc, 0.1)
                    with pag.hold('shift'):
                        pag.click()
                except:
                    print('Could not drop the item!')    
            else:
                return item_loc
        if isinstance(value, int):
            self.move(value)
            try:
                with pag.hold('shift'):
                    pag.click()
            except:
                print('Could not drop the item!')





if __name__ == '__main__':
    bag = Bag() 
    bag.show_items_in_bag('raw_monkfish', confidence=0.90)


    


"""     rect_tuples = {int(key[-2:]) : (tuple((value[0][0], value[0][1])), tuple((value[1][0], value[1][1]))) for key, value in window_rect_slots.items()}
    rect_tuples = {key: Rectangle(value, 'w') for key, value in rect_tuples.items()}
    print(type(rect_tuples[1])) """
    #{int(key[-2:]) : value for key, value in window_slots.items()}





"""     result = pag.locateCenterOnScreen(path+'empty.png')
    print(result)
    print(type(result))
    print(bag.check_last_space_empty()) """
    