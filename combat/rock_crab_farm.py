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

from combat import Combat


craber = Combat()
craber.monster = 'yak'
craber.photo_number = 13
craber.farm(0.9)
""" while True:
    if craber.attack_the_mf():
        time.sleep(10)
    else:
        continue """