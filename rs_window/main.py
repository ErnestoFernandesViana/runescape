import pyautogui as pag
import cv2 as cv 
import numpy as np
from rs_window import Client_Window, Rectangle, Skilling_StartUp
import time 
import keyboard
from timeit import default_timer as timer 

client = Client_Window()
ss = Skilling_StartUp()
color_90 = (134, 39, 18)
center_window = (268, 208)
center_screen = client.convert_window_to_screen_cord(center_window)
movement  = lambda location: (location[0]-20, location[1])
pag.moveTo(movement(center_screen))
""" pag.click(button='right')
time.sleep(0.05)
location = pag.locateCenterOnScreen('combat\photos\walk.png', region=ss.action_screen_rect)
pag.moveTo(location)
pag.click() """