import pyautogui as pag
import cv2 as cv 
import numpy as np
from rs_window import Client_Window, Rectangle
import json 

class Skill_tab():
    path = "./rs_window/photos/skill_tab/"
    def __init__(self):
        self.client = Client_Window()
        self.topleft_window = (550, 235)
        self.bottomright_window = (739, 487)





    def _skill_inventory(self):
        self.client.activate()
        
        pag.press('f3')
    
