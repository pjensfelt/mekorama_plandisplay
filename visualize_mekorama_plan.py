import matplotlib as plt
import sys
import argparse

parser = argparse.ArgumentParser(description='Visualize mekorama level26 plan')
parser.add_argument('-f', '--planfile', dest='planfile', required=True,
                    help='path to the plan file to visualize')

args = parser.parse_args()

try:
  in_file = open(args.planfile, 'r')
  
  for action in in_file.readlines():
    words = action.split();
    if "moveup" in action:
      print("Moving " + words[1] + " up");
    elif "movedown" in action:
      print("Moving " + words[1] + " down");
    elif "moveright" in action:
      print("Moving " + words[1] + " right");
    elif "moveleft" in action:
      print("Moving " + words[1] + " left");
    elif "cost":
      break
    else:
      print("Bugger!!!")
      exit()

finally:
  in_file.close()
