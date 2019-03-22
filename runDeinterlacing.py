import os

from TSNet import TSNet, TSNet_single_load
import argparse

parser = argparse.ArgumentParser(description='Image Deinterlace')
parser.add_argument('--model', default="./models/TSNet_advanced.model", type=str, help="Default model")
parser.add_argument('--gpu', default=-1, type=int, help="GPU instance <0,1>, default is CPU")
parser.add_argument('--input_list', default="./images.txt", type=str, help="Path to images file list")
parser.add_argument('--output', default="./results/", type=str, help="Path to output folder")
args = parser.parse_args()

print(args)

model = TSNet()
model.deinterlace(args)

# model = TSNet_single_load()
# model.deinterlace(args)