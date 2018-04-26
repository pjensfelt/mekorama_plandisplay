import matplotlib.pyplot as plt
import sys
import argparse
import tile
import mekorama_display

parser = argparse.ArgumentParser(description='Visualize mekorama level26 plan')
parser.add_argument('-f', '--planfile', dest='planfile', required=True,
                    help='path to the plan file to visualize')

args = parser.parse_args()

tiles = []
tiles.append(tile.TileHor2(1, 1, 4))
tiles.append(tile.TileVer3(2, 3, 4))
tiles.append(tile.TileVer3(3, 4, 5))
tiles.append(tile.TileHor2(4, 4, 3))
tiles.append(tile.TileVer3(5, 6, 3))
tiles.append(tile.TileVer2(6, 2, 1))
tiles.append(tile.TileHor2(7, 5, 1))

fig = plt.figure()
mekorama_display.mekodisplay(fig, tiles)

try:
  in_file = open(args.planfile, 'r')
  
  for action in in_file.readlines():
    
    if "cost" in action:
      break
    elif "move" not in action:
      print("Unexpected statement in plan. Skipping " + action)
      continue

    print("Got action: " + action)

    words = action.split()
    i = int(words[1][1]) - 1
    #print("Tile number " + str(i+1) + " was at position " + str(tiles[i].x) + ", " + str(tiles[i].y))
    
    if words[0][-4:] != tiles[i].type:
      raise RuntimeError('\nAction: ' + action + 'is not properly formated, t' + str(i+1) + ' is not a ' + words[0][-4:])
    
    if "moveup" in action:
      tiles[i].moveup()
    elif "movedown" in action:
      tiles[i].movedown()
    elif "moveright" in action:
      tiles[i].moveright()
    elif "moveleft" in action:
      tiles[i].moveleft()
    else:
      print("Bugger!!!")
      exit()
    #print("Tile number " + str(i+1) + " now at position " + str(tiles[i].x) + ", " + str(tiles[i].y))

    mekorama_display.mekodisplay(fig, tiles)

finally:
  in_file.close()

print("Close the figure window to end")
plt.show()

