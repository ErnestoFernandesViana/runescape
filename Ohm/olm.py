import pyautogui as pag
import cv2 as cv 
import numpy as np
import time 
import keyboard
from timeit import default_timer as timer 
import sys 

sys.path.insert(0,'combat')
from combat import Combat



class Olm(Combat):
    pass


olm = Olm()
olm.health_status()