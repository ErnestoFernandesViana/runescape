import cv2 as cv 
import numpy as np
import sys
import time 
import pyautogui as pag

sys.path.insert(0, '../runescape/rs_window')

from rs_window import Client_Window, Rectangle
from bag import Bag 
from bank import Bank 
from fishing import Fishing


fish = 'raw_monkfish'

class Fisher():
    def __init__(self):
        self.fishing = True
        self.banking = not(self.fishing)
        self.fish = None 
        self.job = Fishing()
        self.bag = Bag()
        self.bank = Bank()

    def toggle(self):
        self.fishing = not(self.fishing)
        self.banking = not(self.banking)



fisher = Fisher()
fisher.fish  = fish
client = Client_Window()

client.adjust_window('S')

while True:
    if fisher.fishing:
        if fisher.job.click_on_fish(fish):
            last_slot_empty =  True
            while fisher.bag.check_last_space_empty():
                time.sleep(30)
                client.activate()
                pass
            fisher.toggle()
            print('Fisher is now going to bank!')
        else:
            time.sleep(3)
            print('Fish could not be found on screen.')
            continue
    else:
        while not(fisher.bank.check_bank_open()):
            while not(fisher.job.find_banker_boy()):
                pass
                if fisher.bank.check_bank_open():
                    break
            time.sleep(4)
        print('Opened bank.')
        fisher.bank.deposit_item(fisher.fish, hm='all')
        fisher.bank.deposit_item('raw_manta_ray', hm='all')
        print('Depositing all fishes.')
        fisher.bank.close_bank()
        print('Closed Bank')
        fisher.toggle()
        print('Back to fishing')
        time.sleep(1)
        pag.click(client.convert_window_to_screen_cord((370, 335)))
        time.sleep(1)







