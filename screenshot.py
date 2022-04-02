import pyautogui
import numpy as np
from tool import moni as mn
import cv2


a, b = mn.got("ks.png")
img = pyautogui.screenshot(region=[a-180, b-140, 240, 40])  # x,y,w,h
img.save('screenshot2.png')
img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)