import os
import sys

image = './data/images/zidane.jpg'

os.system(f'python detect.py --weights yolov5s.pt --class 0 --save-txt --device mps --source {image}')