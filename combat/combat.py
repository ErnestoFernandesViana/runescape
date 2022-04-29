

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

increase_y = lambda cords, x: (cords[0], cords[1] + x*20)
movement  = lambda location,x: (location[0]+20*x, location[1])

class Combat(Skilling_StartUp):
    
    combat_file_path = 'combat/photos/'
    health_pixel_color = (134, 39, 18)
    health_window = [increase_y((541, 257), x) for x in range(0, 8)]
    char_window_position = (268, 208)
    


    def __init__(self):
        super().__init__()
        self.bag = Bag()
        self.bank = Bank()
        self.monster = None
        self.photo_number = None
        self.health_screen = self._init_health_screen()
        self.char_screen_position = self.client.convert_window_to_screen_cord(self.char_window_position)

    def _init_health_screen(cls):
        return list(map(cls.client.convert_window_to_screen_cord, cls.health_window))

    def attack_the_mf(self, confidence = 0.6):
        if self.monster:
            path_list = self.name_to_path(self.monster, self.photo_number)
            for path in path_list:
                result = pag.locateCenterOnScreen(path, confidence= confidence, region = self.action_screen_rect)
                if result:
                    pag.moveTo(*result, 0.1)
                    pag.click()
                    return True 
                else:
                    continue 
                    #'combat/photos/heath_bar.png'
    
    def farm(self, confidence = 0.6):
        while True:
            while not(self.check_if_in_combat()):
                if self.attack_the_mf(confidence=confidence): 
                    time.sleep(5)


    def check_if_in_combat(self):
        health  = pag.locateOnScreen('combat\photos\heath_bar.png', confidence=0.9, region=self.action_screen_rect)
        return True if health else False


    def health_status(self):
        for i, x in enumerate(self.health_screen):
            if pag.pixelMatchesColor(*x, self.health_pixel_color, tolerance=30):
                value = 100 - i*10
                print(f'Health currently at {value}%')
                return True 
        return False 

    def move_right(self):
        pag.moveTo(movement(self.char_screen_position,1))
        pag.click(button='right')
        time.sleep(0.1)
        location = pag.locateCenterOnScreen('combat\photos\walk.png', region=self.action_screen_rect)
        pag.moveTo(location)
        time.sleep(0.1)
        pag.click()

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
    print(combat.char_screen_position)
    combat.move_right()
    #combat.client.show_rectangle_from_many_photos(combat.name_to_path('rock_crab', 5), confidence=0.6)
"""     all = pag.locateAllOnScreen(combat.combat_file_path + 'rock_crab5.png',
         region = combat.client.client_region(), confidence=0.5)
    combat.client.show_rectangles(all) """
