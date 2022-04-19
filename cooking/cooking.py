import pyautogui as pag
import sys 
import cv2 as cv
import numpy as np
import time 
import os 

sys.path.insert(0, './rs_window')
from rs_window import Skilling_StartUp
from bag import Bag 
from bank import Bank 

class Cooking(Skilling_StartUp):
    cooking_photo_path = './cooking/photos/'
    def __init__(self):
        super().__init__()
        self.bank = Bank()
        self.bag = Bag()
        self.cooking = None 
        self.banking = None 
        self.fish = None 

    def cook_item(self):
        self.bag.click_item_on_bag(self.fish)
        furnance = pag.locateCenterOnScreen(self.cooking_photo_path + 'forno.png',
                         region = self.action_screen_rect, confidence=0.5)
        if furnance:
            print('Furnance found')
            pag.moveTo(*furnance, 0.1)
            pag.click()
            time.sleep(2)
            pag.press('1')
            print(f'Cooking {self.fish}')
            return True
        else:
            print('Furnance could not be found')
            return False 

        
    def check_if_cooking(self):
        pass 


    def check_if_done_cooking(self, confidence= 0.4):
        path = './rs_window/photos/'
        last_space_region = self.bag.bag_rectangle_slots_dict[28].screen_rect
        fish_on_last_square = pag.locateCenterOnScreen(path + self.fish + '.png', 
                        confidence = confidence, region = last_space_region)
        if fish_on_last_square:
            print('Continues cooking')
            return True 
        else:
            print('Done cooking!')
            return False 

    def go_bank(self):
        result = pag.locateCenterOnScreen(self.cooking_photo_path + 'bank.png',
         confidence=0.6, region = self.action_screen_rect)
        if result:
            print('Found bank')
            pag.moveTo(*result, 0.1)
            pag.click()
            time.sleep(3)
            if self.bank.deposit_all():
                print('All fish deposited.')
                if self.bank.draw_item(self.fish, hm='all', confidence=0.5):
                    print('Loaded the bag')
                    time.sleep(0.1)
                    self.bank.close_bank()
                    return True 
            else:
                print('Could not deposit the fish.')
                return False 
        else:
            print('Could not find bank')
            return False


    def work_modifoca(self):
        pass


if __name__ == '__main__':
    cook = Cooking()
    cook.fish = 'raw_lobster'
    cook.check_if_done_cooking()
    #cook.bank.show_items_rectangles('lupa')
