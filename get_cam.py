'''
author Artem Momatov
github/ammv/
data 15.09.2021
'''

from tkinter import Tk, Button, Canvas
from PIL import Image, ImageTk
from npsocket import SocketNumpyArray
from threading import Thread

class CamClient(Tk):
    
    def __init__(self, port=8888, delay = 15, window_size='1280x720', canvas_size=(1280, 720)):
        super().__init__()

        self.port = port
        self.delay = 15

        self.window_size = window_size
        self.canvas_size = canvas_size
        
        self.sock_receiver = SocketNumpyArray()
        self.sock_receiver.initalize_receiver(self.port)
        
        self.make_widgets()
        self.set_widgets()

        self.mainloop()
        
    def make_widgets(self):
        self.geometry(self.window_size)
        self.start_btn = Button(self, text='Start', bg='lightgreen', font='Tahoma 18', command=self.start_command)
        self.canvas = Canvas(self, width=self.canvas_size[0], height=self.canvas_size[1], bg='white')
        
    def start_command(self, *args):
        
        self.start_btn.pack_forget()
        self.canvas.pack()
        
        thread = Thread(target=self.get_imgs)
        thread.start()
        
    def set_widgets(self):
        self.start_btn.pack(expand=1)
        
    def set_img(self):
        self.img = ImageTk.PhotoImage(image=Image.fromarray(self.frame))
        self.canvas.create_image(0, 0, image = self.img, anchor = 'nw')
        
    def get_imgs(self):
        while True:
            self.frame = self.sock_receiver.receive_array()
            self.after(self.delay, self.set_img)
    
camclient = CamClient()
