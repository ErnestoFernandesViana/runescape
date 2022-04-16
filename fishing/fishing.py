import cv2 as cv
import numpy as np
import pyautogui as pag
import sys 

sys.path.insert(0, '../RUNESCAPE/rs_window')

from rs_window import Client_Window




class Fishing():
    path = 'C:/Users/Ernesto Fernandes/Desktop/projects/runescape/fishing/photos/'
    def __init__(self):
        self.client = Client_Window()


    def show_fish_on_screen(self, fish):
        self.client.activate()
        fish_path =  self.path + fish + str('.png')
        result = pag.locateAllOnScreen(fish_path, confidence=0.6, region=self.client.client_region())
        self.client.show_rectangles(result)



if __name__ == '__main__':
    fish = Fishing()
    fish.show_fish_on_screen('raw_lobster')