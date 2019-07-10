# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:21:15 2019

@author: Toshiba Dina Nurhayati
"""

import numpy as np
import cv2
 
# background hitam
img = np.zeros((512,512,3), np.uint8)

# garis vertikal 1
img = cv2.line(img,(50,100),(50,400),(128,0,128),15)

# garis vertikal 2
img = cv2.line(img,(150,230),(150,400),(147,112,219),15)

# garis vertikal 3
img = cv2.line(img,(250,300),(250,400),(255,20,147),15)

# garis vertikal 4
img = cv2.line(img,(340,230),(340,400),(221,160,221),15)

# garis vertikal 5
img = cv2.line(img,(440,400),(440,100),(176,48,96),15)

# membuat persegi
img = cv2.rectangle(img,(480,30),(20,450),(255,0,255),10)

# membuat teks
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Dina Nurhayati',(120,120), font, 1,(240,128,128),4,cv2.LINE_AA)

# membuat teks
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'4816040138',(130,200), font, 1,(221,160,221),3,cv2.LINE_AA)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# untuk menyimpan data hasil output
cv2.imwrite('tugascitradigital1.png', img)