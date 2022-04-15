import pyautogui as pag

attrs = lambda x : [y for y in dir(x) if not y.startswith('_')]

class Client_Window():
    def __init__(self,client_name = 'Simplicity+'):
        self.client_name = client_name
        self.window = pag.getWindowsWithTitle(self.client_name)[0]
        self.topleft_cord = tuple(x for x in self.window.topleft)
        self.window.activate()

    def top_left_cord(self):
        return self.topleft_cord
    
    def activate(self):
        self.window.activate()






if __name__ == '__main__':
    client = Client_Window()
    print(attrs(client.window))
    print(client.topleft_cord)
    print(client.top_left_cord())