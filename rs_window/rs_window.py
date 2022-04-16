import pyautogui as pag
import sys 
import cv2 as cv
import numpy as np
from copy import deepcopy

path = 'C:/Users/Ernesto Fernandes/Desktop/projects/runescape/rs_screen_input'
sys.path.insert(0, path)
from screen_input import rectangle, de_rectangle

attrs = lambda x : [y for y in dir(x) if not y.startswith('_')]

class Client_Window():
    def __init__(self,client_name = 'Simplicity+'):
        self.client_name = client_name
        self.window = pag.getWindowsWithTitle(self.client_name)[0]
        self.topleft_cord = tuple(x for x in self.window.topleft)
        self.bottomright_cord = tuple(x for x in self.window.bottomright)
        self.window.activate()

    def top_left_cord(self):
        return self.topleft_cord
    
    def activate(self):
        self.window.activate()

    def client_region(self):
        rec = rectangle(self.topleft_cord, self.window.bottomright)
        return (rec['left'], rec['top'], rec['width'], rec['height'])

    def show_rectangles(self, rect:list):
        self.activate()
        thickness = 2
        color = (255, 0, 0)
        im = pag.screenshot(region= self.client_region())
        open_cv_image = np.array(im.convert('RGB'))
        open_cv_image = open_cv_image[:, :, ::-1].copy() 
        boxes = list(rect)
        if boxes:
            for box in boxes:
                #cordenates = box.left, box.top, box.width, box.height
                print(box)
                cordenates = de_rectangle(box.left, box.top, box.width, box.height)
                print(cordenates)
                cordenates[0] -= self.topleft_cord[0]
                cordenates[2] -= self.topleft_cord[0]
                cordenates[1] -= self.topleft_cord[1]
                cordenates[3] -= self.topleft_cord[1]
                top_left = (cordenates[0], cordenates[1])
                bottom_right = (cordenates[2], cordenates[3])
                print(cordenates)
                cv.rectangle(open_cv_image, top_left, bottom_right, color, thickness)
        cv.imshow('rectangle',open_cv_image)
        cv.waitKey()
        cv.destroyAllWindows()

    def boxes_cord_on_client(self, lista):
        boxes = list(lista)
        cords = []
        if boxes:
            for box in boxes:
                #cordenates = box.left, box.top, box.width, box.height
                print(box)
                cordenates = de_rectangle(box.left, box.top, box.width, box.height)
                print(cordenates)
                cordenates[0] -= self.topleft_cord[0]
                cordenates[2] -= self.topleft_cord[0]
                cordenates[1] -= self.topleft_cord[1]
                cordenates[3] -= self.topleft_cord[1]
                cords.append(cordenates)
        return cords

    
class Rectangle():
    """defines a rectangle and it's cordenates.
        inputs: 
            args -> Can be a dictionary containing the box attributes
                    Cab be a tuple of tuples with top-left, bottom-right cordenates
            mode -> s stands for full screen cordenates
                    w stands for window cordenates of the client"""
    client =  Client_Window()
    def __init__(self, args, mode='s'):
        self.args = args
        self.mode = mode
        self.screen_dict = self._return_screen_dict()
        self.window_dict = self._return_window_dict()
        self.screen_tuple = de_rectangle(**self.screen_dict)
        self.window_tuple = de_rectangle(**self.window_dict)

    def _return_screen_dict(self):
        arg = deepcopy(self.args)
        if self.mode == 's':
            if isinstance(arg, dict):
                return self.args
            elif isinstance(arg, tuple):
                return rectangle(*arg)
        elif self.mode == 'w':
            if isinstance(arg, dict):
                top_left = self.client.topleft_cord
                arg['top'] += top_left[1]
                arg['left'] += top_left[0]
                return arg
            elif isinstance(arg, tuple):
                arg = rectangle(*arg)
                top_left = self.client.topleft_cord
                arg['top'] += top_left[1]
                arg['left'] += top_left[0]
                return arg

    def _return_window_dict(self):
        arg = deepcopy(self.args)
        if self.mode == 's':
            if isinstance(arg, dict):
                top_left = self.client.topleft_cord
                arg['top'] -= top_left[1]
                arg['left'] -= top_left[0]
                return arg
            elif isinstance(arg, tuple):
                arg = rectangle(*arg)
                top_left = self.client.topleft_cord
                arg['top'] -= top_left[1]
                arg['left'] -= top_left[0]
                return arg                
        elif self.mode == 'w':
            if isinstance(arg, dict):
                return self.args
            elif isinstance(arg, tuple):
                return rectangle(*arg)

    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, value):
        if value not in ('s','w'):
            raise Exception('Mode must be s or w') 
        else:
            if value == 's':
                self._mode = 's'
            elif value == 'w':
                self._mode = 'w'

    def __repr__(self):
        return str(f'Rectangle {self.args}, mode:{self.mode}')



if __name__ == '__main__':
    client = Client_Window()
    client.activate()
    print(client.topleft_cord)
    rec1 = {'left': 100, 'top':100, 'width':100, 'height':100}
    rec2 = (100,100), (200,200)
    r1 = Rectangle(rec2, 's')
    print(r1.screen_dict)
    print(r1.window_dict)
    print(r1.screen_tuple)
    print(r1.window_tuple)
    

    

""" s_path = 'C:/Users\Ernesto Fernandes/Desktop/projects/runescape/fishing/photos/raw_lobster.png'
    
    print(client.client_region())
    client.activate()
    result = pag.locateAllOnScreen(s_path, confidence=0.6, region=client.client_region())
    print(result)
    boxes = list(result)
    print(boxes)
    client.show_rectangles(boxes)
    print(client.boxes_cord_on_client(boxes)) """


