##pip install opencv-python

import cv2
import numpy as np
#c = cv2.VideoCapture(1)
 
# while(1):
#   _,f = c.read()
#   cv2.imshow('e2',f)
#   if cv2.waitKey(5)==27:
#     break
 
# cv2.destroyAllWindows()

webcam = cv2.VideoCapture(1)
return_value, image = webcam.read()
rotate = cv2.rotate(image, cv2.ROTATE_180)
cv2.imwrite('/home/orangepi/pi_scripts/mouse_trap/tests/mousetrap.bmp', rotate)
del (webcam)