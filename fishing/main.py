import cv2 as cv 
import numpy as np
import sys
import time 

sys.path.insert(0, '../runescape/rs_window')

from rs_window import Client_Window, Rectangle
from bag import Bag 
from bank import Bank 
from fishing import Fishing


fish = 'raw_lobster'

class Fisher():
    def __init__(self):
        self.fishing = True
        self.banking = not(self.fishing)
        self.fish = None 
        self.job = Fishing()
        self.bag = Bag()
        self.bank = Bank()

    def toggle(self):
        self.fishing = False
        self.banking = not(self.fishing)



fisher = Fisher()
fisher.fish  = fish
client = Client_Window()

client.adjust_window('S')

while True:
    if fisher.fishing:
        if fisher.job.click_on_fish(fish):
            last_slot_empty =  True
            while fisher.bag.check_last_space_empty():
                time.sleep(10)
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
            time.sleep(2)
            while not(fisher.job.find_banker_boy()):
                time.sleep(3)
        fisher.bank.deposit_item(fisher.fish, how='all')
        fisher.bank.close_bank()
        fisher.toggle()





