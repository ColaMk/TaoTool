from pykeyboard import *
from pymouse import *
from PIL import ImageGrab
import aircv as ac
import cv2
import win32api, win32con

m = PyMouse() #建立鼠标对象
k = PyKeyboard() #建立键盘对象

def getpos(filename):
    find = ac.imread(filename)
    mx, my = m.screen_size()
    img = ImageGrab.grab(bbox=(0, 0, mx, my))
    img.save('screen.jpg')
    sc = ac.imread('screen.jpg')

    # find the match position
    pos = ac.find_template(sc, find)
    x,y = pos['result']
    m.move(int(x),int(y))
    m.click(int(x),int(y))

def kb(x):
    k.type_string(x)

def forall(filename):
    find = ac.imread(filename)
    mx = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) 
    my = win32api.GetSystemMetrics(win32con.SM_CYSCREEN) 
    print(mx,my)
    img = ImageGrab.grab(bbox=(0, 0, mx, my))
    img.save('screen.jpg')
    sc = ac.imread('screen.jpg')

    # find the match position
    pos = ac.find_template(sc, find)
    x,y = pos['result']
    y = y + (my/20)
    m.move(int(x),int(y))
    m.click(int(x),int(y))
    m.click(int(x),int(y))
    m.click(int(x),int(y))
    m.click(int(x),int(y))

def got(filename):
    find = ac.imread(filename)
    mx = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) 
    my = win32api.GetSystemMetrics(win32con.SM_CYSCREEN) 
    print(mx,my)
    img = ImageGrab.grab(bbox=(0, 0, mx, my))
    img.save('screen.jpg')
    sc = ac.imread('screen.jpg')

    # find the match position
    pos = ac.find_template(sc, find)
    x,y = pos['result']
    return (int(x),int(y))

def cli(x,y):
    m.move(int(x),int(y))
    m.click(int(x),int(y))