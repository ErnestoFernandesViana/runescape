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
        self.skill_rectangle = Rectangle((self.topleft_window, self.bottomright_window), 'w')
        self.skill_list_cords = self.skill_rectangle.screen_rect
        self.confidence = 0.7



    def _skill_inventory(self):
        self.client.activate()
        window_mouse_position = (271, 197)
        screen_mouse_position = self.client.convert_window_to_screen_cord(window_mouse_position)
        pag.moveTo(*screen_mouse_position, 0.2)
        pag.press('f2')

    def click_on_skill(self, photo):
        self._skill_inventory()
        path = self.path + photo + '.png'
        skill_loc = pag.locateCenterOnScreen(path, confidence=self.confidence,
                                             region=self.skill_list_cords)
        if skill_loc:
            pag.moveTo(*skill_loc, 0.1) 
            pag.click(button = 'left')
            return True 
        else:
            return False


if __name__ == '__main__':
    skill = Skill_tab()
    #skill.skill_rectangle.show_rectangle()
    skill.click_on_skill('dungeon')
    
