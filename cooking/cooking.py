import pyautogui as pag
import sys 
import cv2 as cv
import numpy as np
import time 
import os 

sys.path.insert(0, './rs_window')
from rs_window import Skilling_StartUp

class Cooking(Skilling_StartUp):
    def __init__(self):
        super().__init__()




if __name__ == '__main__':
    cook = Cooking()
    print(cook.action_topleft_window)
