import os

from TSNet import TSNet
import argparse

parser = argparse.ArgumentParser(description='Image Deinterlace')
parser.add_argument('--fraction', default=1, type=float)
parser.add_argument('--model', default="./models/TSNet_advanced.model", type=str)
parser.add_argument('--gpu', default=0, type=int)
parser.add_argument('--input_list', default="./images.txt", type=str)
parser.add_argument('--output', default="./results/", type=str)
args = parser.parse_args()

print(args)

model = TSNet()

model.deinterlace(args)
