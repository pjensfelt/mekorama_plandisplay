import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.lines as lines
import matplotlib.transforms as tf


def addHor2(ax,x,y,nr):
  ax.add_patch(plt.Rectangle((x-0.4,y-0.4),1.8,0.8,fill=True,color=(232./255, 134./255, 147./255)))
  plt.text(x,y,str(nr),ha='center',va='center')
  ax.add_patch(plt.Circle((x,y),0.3,fill=False))
  
def addVer2(ax,x,y,nr):
  ax.add_patch(plt.Rectangle((x-0.4,y-0.4),0.8,1.8,fill=True,color=(232./255, 134./255, 147./255)))
  plt.text(x,y,str(nr),ha='center',va='center')
  ax.add_patch(plt.Circle((x,y),0.3,fill=False))
  
def addVer3(ax,x,y,nr):
  ax.add_patch(plt.Rectangle((x-0.4,y-1.4),0.8,2.8,fill=True,color=(232./255, 134./255, 147./255)))
  plt.text(x,y,str(nr),ha='center',va='center')
  ax.add_patch(plt.Circle((x,y),0.3,fill=False))

def mekodisplay(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7):

  ax = fig.add_subplot(111)
  # Draw the grid
  # Draw the horisontal lines
  for y in range(0,7):
    ax.add_line(lines.Line2D(np.array([0.5,6.5]),np.array([y+0.5, y+0.5]),lw=0.5))
  # Draw the vertical lines
  for x in range(0,7):
      ax.add_line(lines.Line2D(np.array([x+0.5, x+0.5]),np.array([0.5,6.5]),lw=0.5))

  # Put the position labels into the figure
  for x in range(1,7):
    plt.text(x,0.4,('x'+str(x)),fontsize=12,ha='center',va='top')
  for y in range(1,7):
    plt.text(0.4,y,('y'+str(y)),fontsize=12,ha='right',va='center')

  addHor2(ax,x1,y1,1)
  addVer3(ax,x2,y2,2)
  addVer3(ax,x3,y3,3)
  addHor2(ax,x4,y4,4)
  addVer3(ax,x5,y5,5)
  addVer2(ax,x6,y6,6)
  addHor2(ax,x7,y7,7)


  ax.axis('equal')
  ax.set_xlim(-1, 7)
  ax.set_ylim(-1, 7)
  ax.grid(False)
  ax.set_axis_off()

  plt.show()

def main():
  fig = plt.figure()
  mekodisplay(fig,1,4,3,4,4,5,4,3,6,3,2,1,5,1)

if __name__== "__main__":
  main()
