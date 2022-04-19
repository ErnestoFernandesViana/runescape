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

        

    def go_bank(self):
        pass 

    def work_modifoca(self):
        pass


if __name__ == '__main__':
    cook = Cooking()
    cook.fish = 'raw_lobster'
    cook.cook_item()
