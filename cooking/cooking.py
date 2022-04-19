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
        self.cooking = True 
        self.banking = False
        self.fish = None 

    def _toggle(self):
        self.cooking = not(self.cooking)
        self.banking = not(self.banking)

    def cook_item(self, confidence=0.8):
        self.bag.click_item_on_bag(self.fish, confidence = confidence)
        furnance = pag.locateCenterOnScreen(self.cooking_photo_path + 'forno.png',
                         region = self.action_screen_rect, confidence=0.6)
        if furnance:
            print('Furnance found')
            pag.moveTo(*furnance, 0.2)
            pag.click()
            time.sleep(3)
            pag.press('1')
            print(f'Cooking {self.fish}')
            return True
        else:
            print('Furnance could not be found')
            return False 



    def check_if_done_cooking(self, confidence= 0.96):
        path = './rs_window/photos/'
        fish_on_last_square = pag.locateCenterOnScreen(path + self.fish + '.png', 
                        confidence = confidence, region = self.bag.bag_list_cords)
        if fish_on_last_square:
            print('Continues cooking')
            return False
        else:
            print('Done cooking!')
            return True 

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
        self.client.activate()
        self.client.adjust_window('N')
        while True:
            if self.cooking:
                if self.check_if_done_cooking():
                    self._toggle()
                    continue
                if not(self.cook_item(confidence=0.96)):
                    continue
                time.sleep(38)

            if self.banking:
                self.go_bank()
                time.sleep(1)
                self._toggle()

            
        


if __name__ == '__main__':
    cook = Cooking()
    cook.fish = 'raw_lobster'
    cook.work_modifoca()
    #cook.bank.show_items_rectangles('lupa')
