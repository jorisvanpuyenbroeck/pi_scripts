import cv2
from live.stream import open_stream, close_stream

def take_picture():
  # close stream, otherwise it will interfere with the picture
  stream = close_stream()
  # take picture
  webcam = cv2.VideoCapture(1)
  ret, frame = webcam.read()
  rotate = cv2.rotate(frame, cv2.ROTATE_180)
  cv2.imwrite('/home/orangepi/pi_scripts/mouse_trap/ai/mousetrap.bmp', frame)
  del (webcam)
  # open stream
  stream = open_stream()
