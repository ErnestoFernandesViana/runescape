import pyautogui as pag
import cv2 as cv 
import numpy as np
from rs_window import Client_Window, Rectangle
from bag import Bag
import time

class Bank():
    def __init__(self):
        self.path = './rs_window/photos/'
        self.client = Client_Window()
        self.bag = Bag()
        self.topleft_window = (17, 41)
        self.bottomright_window = (508, 350)
        self.rectangle = Rectangle((self.topleft_window, self.bottomright_window), 'w')
        self.bank_rect_screen_list = self.rectangle.screen_rect

    def check_bank_open(self, confidence=0.8):
        """check if the bank window is open"""
        result = pag.locateOnScreen(self.path+'bankicons.png', region=self.bank_rect_screen_list, confidence=confidence)
        result2 = pag.locateOnScreen(self.path+'infinity_bank.png', region=self.bank_rect_screen_list, confidence=confidence)
        if result or result2:
            return True 
        elif result == None:
            return False 

    def deposit_all(self, confidence=0.8):
        """deposit all items in the bank"""
        bank_open = self.check_bank_open()
        while bank_open:
            loc = pag.locateCenterOnScreen(self.path+'deposit_all_icon.png', region=self.bank_rect_screen_list, confidence=confidence)
            pag.moveTo(loc)
            pag.click(clicks=2, interval=0.2)
            return True
        else:
            return False

    def deposit_item(self, image, **kwargs):
        """deposit an item on bank. if keyword how == all, deposit all items"""
        x = kwargs.get('hm', 0)
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

    def draw_item(self, item, hm=1, confidence=0.6):
        self.check_bank_open()
        if self.find_item_on_bank(item, confidence=confidence):
            print(f'Found {item} on bank!')
            if isinstance(hm, int):
                pag.click(clicks=hm, interval=0.1)
                print(f'Draw {hm} {item}')
                return True 
            elif isinstance(hm, str):
                if hm == 'all':
                    pag.click(button='right')
                    time.sleep(0.1)
                    all = pag.locateCenterOnScreen(self.path + 'all_icon.png', region=self.bank_rect_screen_list, confidence=0.8)
                    if all:    
                        time.sleep(0.2)
                        pag.moveTo(*all, 0.1)
                        pag.click()
                        print('Draw till full bag')
                        return True 
                    else:
                        return False
        else:
            return False
        
        

    def find_item_on_bank(self, item, confidence=0.6):
        path  = self.path + item + '.png'
        result = pag.locateCenterOnScreen(path, region=self.bank_rect_screen_list, confidence=confidence)
        time.sleep(1)
        if result:
            pag.moveTo(*result, 0.1)
            return True 
            
        else:
            lupa = pag.locateCenterOnScreen(self.path + 'lupa.png', region=self.bank_rect_screen_list, confidence=0.8)
            pag.moveTo(*lupa, 0.1)
            pag.click(clicks=2)
            time.sleep(1)
            item_string = item.replace('_',' ')
            pag.write(item_string, interval=0.1)
            pag.press('enter')
            time.sleep(1)
            result = pag.locateCenterOnScreen(path, region=self.bank_rect_screen_list, confidence=confidence)
            if result: 
                pag.moveTo(*result, 0.1)
                return True 
            else:
                print('Couldn find item.')
                return False 


    def show_items_rectangles(self, item, confidence=0.8):
        self.client.activate()
        item_path =  self.path + item + str('.png')
        result = pag.locateAllOnScreen(item_path, confidence=confidence, region=self.bank_rect_screen_list)
        self.client.show_rectangles(result)

        
        





if __name__ == '__main__':
    bank = Bank()
    bank.rectangle.show_rectangle()


"""     bank.client.activate()
    path = bank.path
    result = pag.locateOnScreen(path+'bankicons.png', region = bank.bank_rect_screen_list)
    print(result)
    print(bank.check_bank_open())
    print(bank.deposit_item('money', how='all')) """