import pyautogui as pag
import sys 
import cv2 as cv
import numpy as np

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
        thickness = 1
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
                cordenates[0] -= client.topleft_cord[0]
                cordenates[2] -= client.topleft_cord[0]
                cordenates[1] -= client.topleft_cord[1]
                cordenates[3] -= client.topleft_cord[1]
                top_left = (cordenates[0], cordenates[1])
                bottom_right = (cordenates[2], cordenates[3])
                print(cordenates)
                cv.rectangle(open_cv_image, top_left, bottom_right, color, thickness)
        cv.imshow('rectangle',open_cv_image)
        cv.waitKey()
        cv.destroyAllWindows()



"""     def screen_to_client_window(*cordenates):
        #se for um retângulo passa uma lista, se for top_left, uma tuple
        if isinstance(cordenates, list):
            new_cord = cordenates.copy()
            new_cord[0] -= self.window.topleft_cord[0]
            new_cord[1] -= self.window.topleft_cord[1]
            return new_cord
        if isinstance(cordenates, tuple):
            new_cord = [0,0]
            new_cord[0] = list(cordenates[0])
            new_cord[1] = list(cordenates[1])
            new_cord[0][0] -= self.window.topleft_cord[0]
            new_cord[0][1] -= self.window.topleft_cord[1]
            new_cord[1][0] -= self.window.bottomright_cord[0]
            new_cord[1][1] -= self.window.bottomright_cord[1]
            return new_cord """





if __name__ == '__main__':
    s_path = 'C:/Users\Ernesto Fernandes/Desktop/projects/runescape/fishing/photos/shrimp.png'
    client = Client_Window()
    print(client.client_region())
    """ print(attrs(client.window)) """
    client.activate()
    result = pag.locateAllOnScreen(s_path, confidence=0.6, region=client.client_region())
    boxes = list(result)
    print(boxes)
    client.show_rectangles(boxes)
    
    



