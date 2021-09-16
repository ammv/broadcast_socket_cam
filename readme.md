The program works on devices located on the same network (local).

The task of the program is to broadcast the image of the video camera to another device located in the same network, via sockets.

cam.py - a file that acts as a sender of video camera images.
get_cam.py - a file that performs the role of a recipient

If you are going to broadcast video camera images to your phone, you should specify the IP of the phone on the network when creating an instance
of the Cam class in the file cam.py.

File cam.py you can rename it to cam. pyw(run without a console)

Preparation: to a device with a camera download cam.py and npsocket, download to the receiving device get_cam.py and npsocket.

How to get started:
- Launch cam.py
- Launch get_cam.py
- Wait until the interface appears with the Start button in the window get_cam.py
- Press Start

The code was checked on a laptop and a phone. A file was running on the laptop cam.py, on the phone get_cam.py.

To run the code on the phone(Android), the Pydroid 3 application was used.
Many thanks to the creators https://github.com/ekbanasolutions/numpy-using-socket