import os

from TSNet import TSNet
import argparse

parser = argparse.ArgumentParser(description='Image Deinterlace')
parser.add_argument('--img_path', default="1.png", type=str)
parser.add_argument('--fraction', default=1, type=float)
parser.add_argument('--model', default="./models/TSNet_advanced.model", type=str)
parser.add_argument('--gpu', default=0, type=int)
# parser.add_argument('--input', default="./", type=str)
parser.add_argument('--output', default="./results/", type=str)
args = parser.parse_args()

print(args)

model = TSNet()

# for file in os.listdir(args.input):
#     if file.endswith(".png") or file.endswith(".jpg"):
#         args.img_path = os.path.join(args.input + file)
model.deinterlace(args)
