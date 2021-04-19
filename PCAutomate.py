
from ppadb.client import Client
import numpy
import time
from mss import mss

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device detected')
    quit()

device = devices[0]

top = {'left': 1235, 'top': 1330, 'width': 1, 'height':  1}
left = {'left': 1145, 'top': 1461, 'width': 1, 'height':  1}
mid = {'left': 1218, 'top': 1461, 'width': 1, 'height':  1}
right = {'left': 1282, 'top': 1461, 'width': 1, 'height':  1}

sct = mss()

top_pixel = numpy.array(sct.grab(top))[0][0]
left_pixel = numpy.array(sct.grab(left))[0][0]
middle_pixel = numpy.array(sct.grab(mid))[0][0]
right_pixel = numpy.array(sct.grab(right))[0][0]
total = 0

while True:
    print(total)
    device.shell('input tap 545 1800')
    time.sleep(5)
    top_pixel = numpy.array(sct.grab(top))[0][0]
    left_pixel = numpy.array(sct.grab(left))[0][0]
    middle_pixel = numpy.array(sct.grab(mid))[0][0]
    right_pixel = numpy.array(sct.grab(right))[0][0]
    if((top_pixel[0] > 210) and (top_pixel[1] > 230) and (top_pixel[2] > 230)):
        device.shell('input tap 545 1800')
        print("white")
        time.sleep(1)
        device.shell('input tap 545 1800')
        print(".")
        time.sleep(5)
        device.shell('input tap 545 1800')
        print("..")
        total = total + 5
        time.sleep(8)
    if((top_pixel[0] > 200) and (top_pixel[1] < 220) and (top_pixel[2] < 160)):
        device.shell('input tap 545 1800')
        print("blue")
        time.sleep(3.65)
        device.shell('input tap 545 1800')
        print(".")
        time.sleep(3.35)
        device.shell('input tap 545 1800')
        total = total + 30
        print("..")
        time.sleep(8)
    if((top_pixel[0] < 100) and (top_pixel[1] > 230) and (top_pixel[2] > 240)):
        device.shell('input tap 545 1800')
        print("gold")
        time.sleep(2)
        device.shell('input tap 545 1800')
        print(".")
        time.sleep(5.5)
        device.shell('input tap 545 1800')
        total = total + 50
        print("..")
        time.sleep(10)