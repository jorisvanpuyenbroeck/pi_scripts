##pip install opencv-python
##pip install flask
##pip install numpy

import ffmpeg
import cv2
import subprocess

# video_format = "flv"
# server_url = "http://192.168.137.2:6666"

# def start_streaming(width, height,fps):
#     process = (
#         ffmpeg
#         .input('pipe:', format='rawvideo',codec="rawvideo", pix_fmt='bgr24', s='{}x{}'.format(width, height))
#         .output(
#             server_url + '/stream',
#             #codec = "copy", # use same codecs of the original video
#             listen=1, # enables HTTP server
#             pix_fmt="yuv420p",
#             preset="ultrafast",
#             f=video_format
#         )
#         .overwrite_output()
#         .run_async(pipe_stdin=True)
#     )
#     return process

# def init_cap():
#     cap = cv2.VideoCapture(1)
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     return cap, width, height

# def run():
#     cap, width, height = init_cap()
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     streaming_process = start_streaming(width, height,fps)
#     while True:
#         ret, frame = cap.read()
#         if ret:
#             streaming_process.stdin.write(frame.tobytes())
#         else:
#             break
#     streaming_process.stdin.close()
#     streaming_process.wait()
#     cap.release()

# if __name__ == "__main__":
#     run()

def stream_vnc():
  webcam = cv2.VideoCapture(1)
  while True:
    ret, frame = webcam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  webcam.release()
  cv2.destroyAllWindows()

def take_picture():
  webcam = cv2.VideoCapture(1)
  ret, frame = webcam.read()
  rotate = cv2.rotate(frame, cv2.ROTATE_180)
  cv2.imwrite('/home/orangepi/pi_scripts/mouse_trap/tests/mousetrap.bmp', frame)
  del (webcam)

# take_picture()