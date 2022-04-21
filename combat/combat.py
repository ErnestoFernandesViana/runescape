from abc import abstractmethod
import pyautogui as pag
import sys 
import cv2 as cv
import numpy as np
import time 
import os 

sys.path.insert(0, './rs_window')
from rs_window import Client_Window, Rectangle, Skilling_StartUp
from bag import Bag
from bank import Bank

class Combat(Skilling_StartUp):
    combat_file_path = './combat/photos/'

    def __init__(self):
        super().__init__()
        self.bag = Bag()
        self.bank = Bank()
        self.monster = None

    def attack_the_mf(self, confidence = 0.6):
        result = pag.locateCenterOnScreen(self, confidence, region = self.action_screen_rect)
        if result:
            pag.moveTo(*result, 0.1)
            pag.click()
            return True 
        else:
            return False 

    def check_if_in_combat(self):
        pass

    @abstractmethod
    def health_status(self):
        pass 

    @abstractmethod
    def eat_food(self):
        pass 

    @abstractmethod
    def prayer(self):
        pass 

    @abstractmethod
    def loot_item(self):
        pass

    @abstractmethod
    def drink_potion(self):
        pass

    @abstractmethod
    def teleport_bank(self):
        pass

    @abstractmethod
    def switch_gear(self):
        pass

    @classmethod
    def name_to_path(cls, name, quantity):
        photo_file = cls.combat_file_path + '/'+ name + 's/'
        return [photo_file + name + str(x) + '.png' for x in range(1, quantity+1)]

    def show_rectangle_matches(self, name, quantity, confidence=0.6):
        self.client.show_rectangle_from_many_photos(self.name_to_path(name, quantity), confidence=confidence)

    



if __name__ == '__main__':

    combat = Combat()
    combat.show_rectangle_matches('frost_dragon', 10,0.7)
    #combat.client.show_rectangle_from_many_photos(combat.name_to_path('rock_crab', 5), confidence=0.6)
"""     all = pag.locateAllOnScreen(combat.combat_file_path + 'rock_crab5.png',
         region = combat.client.client_region(), confidence=0.5)
    combat.client.show_rectangles(all) """