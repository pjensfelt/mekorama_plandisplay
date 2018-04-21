class Tile:
  type = 'hor2'
  x = 1
  y = 1
  id = 1
  xmin = 1
  xmax = 6
  ymin = 1
  ymax = 6
  
  def __init__(self, type, x, y, id):
    self.type = type
    self.x = x
    self.y = y
    self.id = id
  
    if type == "hor2":
      self.xmin = 1
      self.xmax = 5
      self.ymin = y
      self.ymax = y
    elif type == "ver2":
      self.xmin = x
      self.xmax = x
      self.ymin = 1
      self.ymax = 5
    elif type == "ver3":
      self.xmin = x
      self.xmax = x
      self.ymin = 2
      self.ymax = 5
    else:
      self.xmin = 1
      self.xmax = 6
      self.ymin = 1
      self.ymax = 6
      print("ERROR: Unknown type " + self.type)
    print("Created a tile of type " + self.type + " with id= " + str(self.id) + " at position x=" + str(self.x) + " y=" + str(self.y))

  def moveup(self):
    if self.type.find("hor") >= 0:
      print("ERROR: " + self.type + " cannot be moved up!!!!!")
      return
    if self.y + 1 > self.ymax:
      print("ERROR: " + self.type + " cannot be moved up more, already at y=" + str(self.y))
      return
    self.y = self.y + 1

  def movedown(self):
    if "hor" in self.type:
      print("ERROR: " + self.type + " cannot be moved down!!!!!")
      return
    if self.y - 1 < self.ymin:
      print("ERROR: " + self.type + " cannot be moved down more, already at y=" + str(self.y))
      return
    self.y = self.y - 1

  def moveright(self):
    if "ver" in self.type:
      print("ERROR: " + self.type + " cannot be moved left!!!!!")
      return
    if self.x + 1 > self.xmax:
      print("ERROR: " + self.type + " cannot be moved right more, already at x=" + str(self.x))
      return
    self.x = self.x + 1

  def moveleft(self):
    if "ver" in self.type:
      print("ERROR: " + self.type + " cannot be moved right!!!!!")
      return
    if self.x - 1 < self.xmin:
      print("ERROR: " + self.type + " cannot be moved down more, already at x=" + str(self.x))
      return
    self.x = self.x - 1
