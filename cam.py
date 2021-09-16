'''
author Artem Momatov
github/ammv/
data 15.09.2021
'''

from cv2 import VideoCapture
from npsocket import SocketNumpyArray
from time import sleep


sleep_delay = 2 #delay during error

class Cam:
    '''
    mobile, pc - tuples of IP and ports
    
    '''
    def __init__(self, mobile=('127.0.0.1', 8888), pc=('localhost', 8888)):
        self.mobile = mobile
        self.pc = pc

    def connect(self):
        try:
            self.sock_sender = SocketNumpyArray()
            self.sock_sender.initialize_sender(*self.mobile)
            print('MOBILE CONNECTION')
            self.web_cam()
        except:
            self.sock_sender = SocketNumpyArray()
            self.sock_sender.initialize_sender(*self.pc)
            print('PC CONNECTION')
            self.web_cam()
        
    def web_cam(self):
        self.cap = VideoCapture(0)       
        while True:
            frame = self.cap.read()[1]
            self.sock_sender.send_numpy_array(frame)

            
cam = Cam()
while True:
    try:
        cam.connect()
    except ConnectionError:
        sleep(sleep_delay)
    except Exception:
        sleep(sleep_delay)


    
