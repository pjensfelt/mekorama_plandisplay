class Tile(object):
  type = 'hor2'
  id = 1
  x = 1
  y = 1
  xmin = 1
  xmax = 6
  ymin = 1
  ymax = 6
  
  def __init__(self, type, id, x, y):
    self.type = type
    self.id = id
    self.x = x
    self.y = y
    self.xmin = 1
    self.xmax = 6
    self.ymin = 1
    self.ymax = 6
    print("Created a tile of type " + self.type + " with id=" + str(self.id) + " at position x=" + str(self.x) + " y=" + str(self.y))
  
  def moveup(self):
    raise RuntimeError('Tile t' + str(self.id) + ' of type ' + self.type + ' cannot move up')
  
  def movedown(self):
    raise RuntimeError('Tile t' + str(self.id) + ' of type ' + self.type + ' cannot move down')
  
  def moveleft(self):
    raise RuntimeError('Tile t' + str(self.id) + ' of type ' + self.type + ' cannot move left')
  
  def moveright(self):
    raise RuntimeError('Tile t' + str(self.id) + ' of type ' + self.type + ' cannot move right')

class TileHor2(Tile):
  def __init__(self, id, x, y):
    super(TileHor2, self).__init__('hor2', id,x,y)

    self.xmax = 5
    self.ymin = y
    self.ymax = y

  def moveright(self):
    if self.x + 1 > self.xmax:
      raise RuntimeError('TileHor2 ' + str(id) + ' cannot be moved right more, already at x=' + str(self.x))
    self.x += 1

  def moveleft(self):
    if self.x - 1 < self.xmin:
      raise RuntimeError('TileHor2 ' + str(id) + ' cannot be moved left more, already at x=' + str(self.x))
    self.x -= 1

class TileVer2(Tile):
  def __init__(self, id, x, y):
    super(TileVer2, self).__init__('ver2', id,x,y)
    
    self.xmin = x
    self.xmax = x
    self.ymax = 5
  
  def moveup(self):
    if self.y + 1 > self.ymax:
      raise RuntimeError('TileVer2 ' + str(id) + ' cannot be moved up more, already at y=' + str(self.y))
    self.y += 1
  
  def movedown(self):
    if self.y - 1 < self.ymin:
      raise RuntimeError('TileVer2 ' + str(id) + ' cannot be moved down more, already at y=' + str(self.y))
    self.y -= 1

class TileVer3(Tile):
  def __init__(self, id, x, y):
    super(TileVer3, self).__init__('ver3', id,x,y)
    
    self.xmin = x
    self.xmax = x
    self.ymin = 2
    self.ymax = 5
  
  def moveup(self):
    if self.y + 1 > self.ymax:
      raise RuntimeError('TileVer3 ' + str(id) + ' cannot be moved up more, already at y=' + str(self.y))
    self.y += 1
  
  def movedown(self):
    if self.y - 1 < self.ymin:
      raise RuntimeError('TileVer3 ' + str(id) + ' cannot be moved down more, already at y=' + str(self.y))
    self.y -= 1
