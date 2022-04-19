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
    def __init__(self):
        super().__init__()
        self.bag = Bag()
        self.bank = Bank()

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
    



if __name__ == '__main__':

    combat = Combat()
    print(combat.bag)