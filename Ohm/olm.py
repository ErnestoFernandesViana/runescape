import pyautogui as pag
import cv2 as cv 
import numpy as np
import time 
import keyboard
from timeit import default_timer as timer 
import sys 

sys.path.insert(0,'combat')
sys.path.insert(0,'rs_window')
from combat import Combat
from rs_window import Skilling_StartUp

class Olm(Skilling_StartUp):
    head_center_paths = [f'Ohm\photos\olm_head\head_center{x}.png' for x in range(1, 8)]
    head_right_paths = [f'Ohm\photos\olm_head\head_right{x}.png' for x in range(1, 8)]
    def __init__(self):
        Skilling_StartUp.__init__(self)
        self.head_status = None
        self.phase = None
        self.right_hand = None 
        self.left_hand = None 
        self.general_status = None

    def check_olm_head(self, confidence=0.9):
        for path in self.head_center_paths:
            result = pag.locateCenterOnScreen(path, confidence=confidence, region=self.action_screen_rect)
            if result:
                if self.head_status == 'center':
                    break
                elif self.head_status != 'center':
                    self.head_status = 'center'
                    print('MF looking to center')
                    break
        for path in self.head_right_paths:
            result = pag.locateCenterOnScreen(path, confidence=confidence, region=self.action_screen_rect)
            if result:
                if self.head_status == 'right':
                    break
                elif self.head_status != 'right':
                    self.head_status = 'right'
                    print('MF looking right')
                    break
        

        


class Olm_fighter(Combat):
    pass

    def find_right_hand(self):
        pass

    def find_left_hand(self):
        pass

    def find_head(self):
        pass 


if __name__ == '__main__':
    olm = Olm()
    while True:
        olm.check_olm_head()
