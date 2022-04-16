from pynput.mouse import Controller
import mss
import mss.tools
#from rs_window import Client_Window
import json
import time 


path = 'C:/Users/Ernesto Fernandes/Desktop/projects/runescape/rs_screen_input/'


def mouse_position():
    mouse = Controller()
    current_mouse_position = mouse.position
    return current_mouse_position

""" def many_window_locations(key_name, json_name, n):
    dictionary = {}
    position = 0
    client = Client_Window()
    while position < n:
        dictionary[json_name +': ' + str(position)] = client.get_location_on_window()
        position += 1
        time.sleep(0.2)
    with open( json_name +".json", "w") as outfile:
        json.dump(dictionary, outfile)

def many_screen_locations(key_name, json_name, n):
    dictionary = {}
    position = 0
    client = Client_Window()
    while position < n:
        dictionary[json_name +': ' + str(position)] = client.get_location_on_screen()
        position += 1
        time.sleep(0.2)
    with open( json_name +".json", "w") as outfile:
        json.dump(dictionary, outfile) """


#gets a screen shot for the location 
def save_sc_shot(rectangle, path=path):
    with mss.mss() as sct:
        # The screen part to capture
        monitor = rectangle
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output= path + output)
        print(output)

def rectangle(top_left, bottom_right):
    x1, y1 = top_left
    x2, y2 = bottom_right
    width  = x2 - x1
    height = y2 - y1
    return {'left': x1, 'top':y1, 'width':width, 'height':height}

def de_rectangle(left, top, width, height):
    top_left = left, top
    bottom_right = left + width, top + height
    return list(top_left) + list(bottom_right)
