import pyautogui as pag
import cv2 as cv 
import numpy as np
from rs_window import Client_Window, Rectangle
from bag import Bag

class Bank():
    path = './rs_window/photos/'
    def __init__(self):
        self.client = Client_Window()
        self.bag = Bag()
        self.topleft_window = (25, 47)
        self.bottomright_window = (458, 325)
        self.rectangle = Rectangle((self.topleft_window, self.bottomright_window), 'w')
        self.bank_rect_screen_list = self.rectangle.screen_tuple

    def check_bank_open(self, confidence=0.8):
        result = pag.locateOnScreen(self.path+'bankicons.png', region=self.bank_rect_screen_list, confidence=confidence)
        if result:
            return True 
        elif result == None:
            return False 

    def deposit_all(self, confidence=0.8):
        bank_open = self.check_bank_open()
        if bank_open:
            loc = pag.locateOnScreen(self.path+'deposit_all_icon.png', region=self.bank_rect_screen_list, confidence=confidence)
            pag.moveTo(loc)
            pag.click(clicks=2, interval=0.2)
        else:
            return False

    def deposit_item(self, image, **kwargs):
        pass




if __name__ == '__main__':
    bank = Bank()
    bank.client.activate()
    path = bank.path
    result = pag.locateOnScreen(path+'bankicons.png', region = bank.bank_rect_screen_list)
    print(result)
    print(bank.check_bank_open())
    bank.deposit_all()