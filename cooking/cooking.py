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
    def __init__(self):
        super().__init__()
        self.bank = Bank()
        self.bag = Bag()
        self.cooking = None 
        self.banking = None 
        self.fish = None 

    def cook_item(self):
        pass 

    def go_bank(self):
        pass 

    def work_modifoca(self):
        pass






if __name__ == '__main__':
    cook = Cooking()
    print(cook.action_topleft_window)
