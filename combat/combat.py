from abc import abstractmethod
import pyautogui as pag
import sys 
import cv2 as cv
import numpy as np
import time 
import os 

sys.path.insert(0, './rs_window')
from rs_window import Client_Window, Rectangle
from bag import Bag
from bank import Bank

class Combat():
    def __init__(self):
        self.client = Client_Window()
        self.client.activate()
        self.action_topleft_window = (9, 29)
        self.action_bottomright_window = (520, 363)
        self.action_screen = Rectangle((self.action_topleft_window, self.action_bottomright_window), 'w')
        self.action_screen_rect = self.action_screen.screen_rect
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