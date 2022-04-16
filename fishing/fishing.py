
import pyautogui as pag
import sys 

sys.path.insert(0, '../RUNESCAPE/rs_window')

from rs_window import Client_Window




class Fishing():
    path = 'C:/Users/Ernesto Fernandes/Desktop/projects/runescape/fishing/photos/'
    def __init__(self):
        self.client = Client_Window()
        self.confidence = 0.6


    def show_fish_on_screen(self, fish):
        self.client.activate()
        fish_path =  self.path + fish + str('.png')
        result = pag.locateAllOnScreen(fish_path, confidence=self.confidence, region=self.client.client_region())
        self.client.show_rectangles(result)

    def click_on_fish(self, fish):
        fish_path =  self.path + fish + str('.png')
        fish_location = pag.locateCenterOnScreen(fish_path, confidence=self.confidence, region=self.client.client_region())
        pag.moveTo(*fish_location, 0.1) 
        pag.click()
        print(f'Clicked on fish at postion {fish_location}')


if __name__ == '__main__':
    fish = Fishing()
    result = fish.click_on_fish('raw_lobster')
    #fish.show_fish_on_screen('raw_lobster')
    print(result)