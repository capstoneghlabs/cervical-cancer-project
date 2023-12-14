import tflite_runtime.interpreter as tflite
from PIL import Image
import cv2
import numpy as np
import time
import argparse

import os, psutil
os.environ["USE_GPU_INFERENCE"]="1"

def preprocess_image(x, mode='caffe'):
    
    x = x.astype(np.float32)

    if mode == 'tf':
        x /= 127.5
        x -= 1.
    elif mode == 'caffe':
        x -= [103.939, 116.779, 123.68]

    return x


def resize_image(img, min_side=800, max_side=1333):
    """ Resize an image such that the size is constrained to min_side and max_side.

    Args
        min_side: The image's min side will be equal to min_side after resizing.
        max_side: If after resizing the image's max side is above max_side, resize until the max side is equal to max_side.

    Returns
        A resized image.
    """
    # compute scale to resize the image
    scale = compute_resize_scale(img.shape, min_side=min_side, max_side=max_side)

    # resize the image with the computed scale
    img = cv2.resize(img, None, fx=scale, fy=scale)

    return img, scale
def compute_resize_scale(image_shape, min_side=800, max_side=1333):
    
    (rows, cols, _) = image_shape

    smallest_side = min(rows, cols)

    # rescale the image so the smallest side is min_side
    scale = min_side / smallest_side

    # check if the largest side is now greater than max_side, which can happen
    # when images have a large aspect ratio
    largest_side = max(rows, cols)
    if largest_side * scale > max_side:
        scale = max_side / largest_side

    return scale

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
      '-e', '--ext_delegate', help='external_delegate_library path')
    parser.add_argument(
      '-m', '--model', help='model path')
    parser.add_argument(
      '-o',
      '--ext_delegate_options',
      help='external delegate options, \
            format: "option1: value1; option2: value2"')

    args = parser.parse_args()
    ext_delegate = None
    ext_delegate_options = {}
    model = None
    if args.ext_delegate_options is not None:
        options = args.ext_delegate_options.split(';')
        for o in options:
            kv = o.split(':')
            if (len(kv) == 2):
                ext_delegate_options[kv[0].strip()] = kv[1].strip()
            else:
                raise RuntimeError('Error parsing delegate option: ' + o)

    
    
    if args.ext_delegate is not None:
        print('Loading external delegate from {} with args: {}'.format(
            args.ext_delegate, ext_delegate_options))
        ext_delegate = [
            tflite.load_delegate(args.ext_delegate, ext_delegate_options)
        ]
    if args.model is not None:
        model = args.model 
    else:
        print("Model path not specified")
        exit()
    interpreter = tflite.Interpreter(
        model_path=str(args.model),
       )
    interpreter.allocate_tensors()
    

    
    input_index = interpreter.get_input_details()[0]["index"]
    image = Image.open('Validation/images/MJ-01323_2022_06_22_10_48.jpg').convert('RGB')
    image = image.rotate(90)

    image = np.asarray(image)
    image = image[:, :, ::-1].copy()

    image, scale = resize_image(image)

    interpreter.set_tensor(input_index, np.reshape(image.astype(np.uint8), (1, 1067,  800,    3)))

    start = time.time()
    interpreter.invoke()
    inference_time = time.time() - start
    print(f"Warmup: {inference_time}")
    inferences = []
    score  = None
    for path in os.listdir('Validation/images/'):
        image = Image.open('Validation/images/'+path).convert('RGB')
        
        image = image.rotate(90)

        image = np.asarray(image)
        image = image[:, :, ::-1].copy()

        image, scale = resize_image(image)
        
        interpreter.set_tensor(input_index, np.reshape(image.astype(np.uint8), (1, 1067,  800,    3)))

        start = time.time()
        interpreter.invoke()
        inference_time = time.time() - start

        scores = interpreter.get_tensor(interpreter.get_output_details()[0]["index"])

        predicted = scores.argmax()
        
        print(f"{path}: {predicted}")        
    ")
