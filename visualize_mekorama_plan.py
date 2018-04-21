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
    print(action)

finally:
  in_file.close()
