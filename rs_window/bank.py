import pyautogui as pag
import cv2 as cv 
import numpy as np
from rs_window import Client_Window, Rectangle
from bag import Bag
import time

class Bank():
    path = './rs_window/photos/'
    def __init__(self):
        self.client = Client_Window()
        self.bag = Bag()
        self.topleft_window = (17, 41)
        self.bottomright_window = (508, 350)
        self.rectangle = Rectangle((self.topleft_window, self.bottomright_window), 'w')
        self.bank_rect_screen_list = self.rectangle.screen_rect

    def check_bank_open(self, confidence=0.8):
        """check if the bank window is open"""
        result = pag.locateOnScreen(self.path+'bankicons.png', region=self.bank_rect_screen_list, confidence=confidence)
        if result:
            return True 
        elif result == None:
            return False 

    def deposit_all(self, confidence=0.8):
        """deposit all items in the bank"""
        bank_open = self.check_bank_open()
        if bank_open:
            loc = pag.locateCenterOnScreen(self.path+'deposit_all_icon.png', region=self.bank_rect_screen_list, confidence=confidence)
            pag.moveTo(loc)
            pag.click(clicks=2, interval=0.2)
            return True
        else:
            return False

    def deposit_item(self, image, **kwargs):
        """deposit an item on bank. if keyword how == all, deposit all items"""
        x = kwargs.get('how', 0)
        if x == 0:
            self.bag.click_item_on_bag(image)
            return True 
        elif x == 'all':
            self.bag.click_item_on_bag(image, button='right')
            time.sleep(0.1)
            self.bag.click_item_on_bag('all_icon')
            return True

    def close_bank(self):
        path = self.path + 'close_bank_icon.png'
        loc = pag.locateCenterOnScreen(path, region=self.client.window.box, confidence=0.8)
        if loc:
            pag.moveTo(loc)
            pag.click()
            return True 
        else:
            return False




if __name__ == '__main__':
    bank = Bank()
    bank.close_bank()
    bank.rectangle.show_rectangle()


"""     bank.client.activate()
    path = bank.path
    result = pag.locateOnScreen(path+'bankicons.png', region = bank.bank_rect_screen_list)
    print(result)
    print(bank.check_bank_open())
    print(bank.deposit_item('money', how='all')) """