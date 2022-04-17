
import pyautogui as pag
import sys 

sys.path.insert(0, '../RUNESCAPE/rs_window')

from rs_window import Client_Window, Rectangle




class Fishing():
    path = 'C:/Users/Ernesto Fernandes/Desktop/projects/runescape/fishing/photos/'
    def __init__(self):
        self.state = 1
        self.client = Client_Window()
        self.client.activate()
        self.confidence = 0.6
        self.char_rectangle = Rectangle(((11, 33),(516, 337)), 'w')
        self.char_rectangle_list = self.char_rectangle.screen_tuple


    def show_fish_on_screen(self, fish):
        self.client.activate()
        fish_path =  self.path + fish + str('.png')
        result = pag.locateAllOnScreen(fish_path, confidence=self.confidence, region=self.client.client_region())
        self.client.show_rectangles(result)

    def click_on_fish(self, fish):
        fish_path =  self.path + fish + str('.png')
        fish_location = pag.locateCenterOnScreen(fish_path, confidence=self.confidence, region=self.char_rectangle_list)
        if fish_location:
            pag.moveTo(*fish_location, 0.1) 
            pag.click()
            print(f'Clicked on fish at postion {fish_location}')
            return True
        else:
            return False
    
    def find_banker_boy(self):
        for x in range(1,6):
            fish_path =  self.path + 'bank' + str(x) + str('.png')
            bank_location = pag.locateCenterOnScreen(fish_path, confidence=self.confidence, region=self.char_rectangle_list)
            if bank_location:
                pag.moveTo(*bank_location)
                pag.click()
                return True 
            if x == 5:
                return False



if __name__ == '__main__':
    fish = Fishing()
    print(fish.find_banker_boy())

