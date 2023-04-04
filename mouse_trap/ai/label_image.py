import time
import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite


def is_mouse():
  image = './ai/mousetrap.bmp'
  model_file = './ai/model_unquant.tflite'
  input_mean = 127.5
  input_std = 127.5
  num_threads = 1
  labels = ['0 sock', '1 mouse', '2 background']

  interpreter = tflite.Interpreter(
      model_path= model_file,
      num_threads= num_threads)
  interpreter.allocate_tensors()

  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()

  # check the type of the input tensor
  floating_model = input_details[0]['dtype'] == np.float32

  # NxHxWxC, H:1, W:2
  height = input_details[0]['shape'][1]
  width = input_details[0]['shape'][2]
  img = Image.open(image).resize((width, height))

  # add N dim
  input_data = np.expand_dims(img, axis=0)

  if floating_model:
    input_data = (np.float32(input_data) - input_mean) / input_std

  interpreter.set_tensor(input_details[0]['index'], input_data)

  start_time = time.time()
  interpreter.invoke()
  stop_time = time.time()

  output_data = interpreter.get_tensor(output_details[0]['index'])
  results = np.squeeze(output_data)

  top_k = results.argsort()[-5:][::-1]

  for i in top_k:
    if floating_model:
      print('{:08.6f}: {}'.format(float(results[i]), labels[i]))
    else:
      print('{:08.6f}: {}'.format(float(results[i] / 255.0), labels[i]))

  print('time: {:.3f}ms'.format((stop_time - start_time) * 1000))

  if results[1] > results[0]:
      return True
  else:
      return False