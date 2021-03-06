from screen_input import mouse_position, save_sc_shot, rectangle
import time 
import keyboard

"""Module designed to take ease prints and cordenates from screen"""

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

while True:
    print('m :  Get locations on the screen \n \
    s : Get screenshot between two pixels')
    answer = input('What do you want?')
    if answer == 'm':
        print('Hit "h" to get location on the screen! \n \
        Hit "s" to get a screen shot')
        while True:
            if keyboard.is_pressed('h'):
                mouse_position()
                time.sleep(0.2)
            if keyboard.is_pressed('q'):
                break

    if answer == 's':
        print('Hit "h" to take the top-left of the image. \n \
        Hit "h" again to the bottom-right of the image!')
        while True:
            if keyboard.is_pressed('h'):
                top_left = mouse_position()
                time.sleep(0.2)
                break
        while True:
            if keyboard.is_pressed('h'):
                bottom_right = mouse_position()
                time.sleep(0.2)
                break
        path = input('Insert directory path. Default is this programs folder')
        if path:
            save_sc_shot(rectangle(top_left, bottom_right), path)
        else:
            save_sc_shot(rectangle(top_left, bottom_right))
        print("Screen-shot saved.")
        break

    if answer == 'q':
        break 

