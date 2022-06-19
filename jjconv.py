import sys, os
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Convert image files between different formats.')
parser.add_argument('image', metavar='', type=str, help='input image file')
parser.add_argument('-r', help='rename file')
args = parser.parse_args()
input_path = args.path()

def validate_file():
    """Checks that file exists and is in a supported format"""

    

#def main():

#if __name__ == "__main__":
    #main()

#for path in sys.path:
    #print(path)

#print("the argument is", sys.argv)



