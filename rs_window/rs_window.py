import pyautogui as pag
import sys 
import cv2 as cv
import numpy as np
from copy import deepcopy
import keyboard
import time 
import os 
#'C:/Users/Ernesto Fernandes/Desktop/projects/runescape
path = './rs_screen_input'
sys.path.insert(0, path)
from screen_input import rectangle, de_rectangle, mouse_position

attrs = lambda x : [y for y in dir(x) if not y.startswith('_')]

class Client_Window():
    """Class intended to control main features of client window"""
    def __init__(self,client_name = 'Simplicity+'):
        self.client_name = client_name
        self.window = pag.getWindowsWithTitle(self.client_name)[0]
        self.topleft_cord = tuple(x for x in self.window.topleft)
        self.bottomright_cord = tuple(x for x in self.window.bottomright)
        self.window.activate()

    def activate(self):
        self.window.activate()

    def client_region(self):
        rec = rectangle(self.topleft_cord, self.window.bottomright)
        return (rec['left'], rec['top'], rec['width'], rec['height'])

    def show_rectangles(self, rect:list):
        """ to_do this method would fit better in rectangle class passing in a png to see 
        where it fits on screen"""
        open_cv_image = self._create_open_cv_shoot() 
        self._draw_rectangle_on_figure(rect, open_cv_image)
        cv.imshow('rectangle',open_cv_image)
        cv.waitKey()
        cv.destroyAllWindows()

    def _create_open_cv_shoot(self):
        self.activate()
        im = pag.screenshot(region= self.client_region())
        open_cv_image = np.array(im.convert('RGB'))
        open_cv_image = deepcopy(open_cv_image[:, :, ::-1])
        return open_cv_image

    def _draw_rectangle_on_figure(self, rect, open_cv_image):
        thickness = 2
        color = (255, 0, 0)
        boxes = list(rect)
        if boxes:
            for box in boxes:
                #cordenates = box.left, box.top, box.width, box.height
                print(box)
                cordenates = de_rectangle(box.left, box.top, box.width, box.height)
                cordenates[0] -= self.topleft_cord[0]
                cordenates[2] -= self.topleft_cord[0]
                cordenates[1] -= self.topleft_cord[1]
                cordenates[3] -= self.topleft_cord[1]
                top_left = (cordenates[0], cordenates[1])
                bottom_right = (cordenates[2], cordenates[3])
                print(cordenates)
                cv.rectangle(open_cv_image, top_left, bottom_right, color, thickness)
                


    
    def show_rectangle_from_many_photos(self, photos_paths:list, confidence=0.8):
        self.activate()
        open_cv_image = self._create_open_cv_shoot()
        for path in photos_paths:
            all = pag.locateAllOnScreen(path, region=self.client_region(), confidence=confidence)
            self._draw_rectangle_on_figure(all, open_cv_image)
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

    def adjust_window(self, string):
        """this method will adjust the perspective of the client window"""
        if string not in ('N','S','E','W'):
            raise Exception('String has to be: N,S,E or W')
        self.window.activate()
        bussola_cord = (548, 52)
        screen_cords = self.convert_window_to_screen_cord(bussola_cord)
        pag.moveTo(*screen_cords, 0.1) 
        pag.click()
        pag.moveTo(*self.window.center, 0.1)
        pag.scroll(-1000)
        if string == 'S':
            pag.keyDown('left')
            pag.keyDown('up')
            time.sleep(1.8)
            pag.keyUp('left')
            time.sleep(2.5-1.8)
            pag.keyUp('up')
        elif string == 'E':
            pag.keyDown('up')
            pag.keyDown('left')
            time.sleep(0.9)
            pag.keyUp('left')
            time.sleep(2.5-0.9)  
            pag.keyUp('up')  
        elif string == 'W':
            pag.keyDown('up')
            pag.keyDown('right')
            time.sleep(0.9)
            pag.keyUp('right')
            time.sleep(2.5-0.9)
            pag.keyUp('up')
        elif string == 'N':
            pag.keyDown('up')
            time.sleep(2.5)
            pag.keyUp('up')


    def get_location_on_screen(self):
        print('Press "h" to get the mouse position on screen! Press "q" to quit!')
        while True:
            if keyboard.is_pressed('h'):
                current_mouse_position = mouse_position()
                print(f'Current screen position {current_mouse_position}')
                return current_mouse_position
            if keyboard.is_pressed('q'):
                break
            
    def get_location_on_window(self):
        print('Press "h" to get the mouse position on screen! Press "q" to quit!')
        top_left = self.topleft_cord
        while True:
            if keyboard.is_pressed('h'):
                current_mouse_position = mouse_position()
                x = current_mouse_position[0] - top_left[0]
                y = current_mouse_position[1] - top_left[1]
                print(f'Current window position {x, y}')
                client_cord = self.topleft_cord
                w = x + client_cord[0]
                z = y + client_cord[1]
                print(f'Current screen position: {current_mouse_position}')
                time.sleep(0.3)
                return x, y
            if keyboard.is_pressed('q'):
                break

    def convert_window_to_screen_cord(self, cord):
        client_cord = self.topleft_cord
        x = cord[0] + client_cord[0]
        y = cord[1] + client_cord[1]
        return x, y



    
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
        #dicionário com left, top, width, height
        self.screen_dict = self._return_screen_dict()
        self.window_dict = self._return_window_dict()
        #lista com topleft e bottomright
        self.screen_list = de_rectangle(**self.screen_dict)
        self.window_list = de_rectangle(**self.window_dict)
        #Lista com left, top, wiodth, height
        self.screen_rect = [self.screen_dict['left'], self.screen_dict['top'], self.screen_dict['width'], self.screen_dict['height']]
        self.window_rect = [self.window_dict['left'], self.window_dict['top'], self.window_dict['width'], self.window_dict['height']]
        #tuple com topleft e bottomright
        self.screen_tuple = self._list_to_tuple(self.screen_list)
        self.window_tuple = self._list_to_tuple(self.window_list)

    def _list_to_tuple(self, lista):
        t1 = lista[0], lista[1]
        t2 = lista[2], lista[3]
        return t1,t2

    def _return_screen_dict(self):
        arg = deepcopy(self._args)
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
        arg = deepcopy(self._args)
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
    def args(self):
        return self._args

    @args.setter
    def args(self, value):
        if isinstance(value, dict):
            self._args =  value
        elif isinstance(value, tuple):
            self._args =  value 
        elif isinstance(value, list):
            dictionary = {}
            dictionary['left'] = value[0] ; dictionary['top'] = value[1]
            dictionary['width'] = value[2]; dictionary['height'] = value[3]
            self._args = dictionary

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

    def show_rectangle(self):
        self.client.activate()
        thickness = 2
        color = (255, 0, 0)
        im = pag.screenshot(region= self.client.client_region())
        open_cv_image = np.array(im.convert('RGB'))
        open_cv_image = open_cv_image[:, :, ::-1].copy() 
        t1 = self.window_list[0], self.window_list[1]
        t2 = self.window_list[2], self.window_list[3]
        try:
            cv.rectangle(open_cv_image, t1,t2, color, thickness)
        except:
            print('Could not print the rectangle.')
            return False
        cv.imshow('rectangle',open_cv_image)
        cv.waitKey()
        cv.destroyAllWindows()
        
    def __repr__(self):
        return str(f'\tRectangle {self.args}, Mode: {self.mode}\n\
        Screen Dict: {self.screen_dict}\n\tWindow Dict: {self.window_dict}\n\
        Screen Rect: {self.screen_rect}\n\tWindow Rect: {self.window_rect}\n\
        Screen Tuple: {self.screen_tuple}\n\tWindow Tuple: {self.window_tuple}')


class Skilling_StartUp():
    def __init__(self):
        self.client = Client_Window()
        self.client.activate()
        self.action_topleft_window = (9, 29)
        self.action_bottomright_window = (520, 363)
        self.action_screen = Rectangle((self.action_topleft_window, self.action_bottomright_window), 'w')
        self.action_screen_rect = self.action_screen.screen_rect




if __name__ == '__main__':
    client = Client_Window()
    client.activate()
    ssp = Skilling_StartUp()
    #print(client.get_location_on_window())
    #print(attrs(client.window))
    client.get_location_on_window()




"""     rec1 = {'left': 100, 'top':100, 'width':100, 'height':100}
    r1 = Rectangle(rec1, 'w')
    r1.show_rectangle() """





"""     client.activate()
    print(client.topleft_cord)
    rec1 = {'left': 100, 'top':100, 'width':100, 'height':100}
    rec2 = (((100,100), (200,200)))
    rec3 = [100,100,100,100]
    r1 = Rectangle(rec1, 'z')
    print(r1.screen_dict)
    print(r1.window_dict)
    print(r1.screen_tuple)
    print(r1.window_tuple)
 """

""" s_path = 'C:/Users\Ernesto Fernandes/Desktop/projects/runescape/fishing/photos/raw_lobster.png'
    
    print(client.client_region())
    client.activate()
    result = pag.locateAllOnScreen(s_path, confidence=0.6, region=client.client_region())
    print(result)
    boxes = list(result)
    print(boxes)
    client.show_rectangles(boxes)
    print(client.boxes_cord_on_client(boxes)) """


