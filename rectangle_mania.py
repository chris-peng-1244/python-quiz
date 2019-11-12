def rectangleMania(coords):
  coordMap = buildCoordMap(coords)
  totalRect = 0
  for point in coords:
    totalRect += findClockwiseRect(point, point, coordMap, 'up')
  return totalRect

def buildCoordMap(coords):
  coordMap = {}
  for coord in coords:
    key = (coord[0], coord[1])
    coordMap[key] = {
      'left': [],
      'right': [],
      'down': [],
      'up': []
    }
    for xCoord in coords:
      if isLeft(coord, xCoord):
        coordMap[key]['left'].append(xCoord)
      if isRight(coord, xCoord):
        coordMap[key]['right'].append(xCoord)
      if isUp(coord, xCoord):
        coordMap[key]['up'].append(xCoord)
      if isDown(coord, xCoord):
        coordMap[key]['down'].append(xCoord)
  return coordMap

def isLeft(coord1, coord2):
  return coord2[0] < coord1[0] and coord2[1] == coord1[1]

def isRight(coord1, coord2):
  return coord2[0] > coord1[0] and coord2[1] == coord1[1]

def isUp(coord1, coord2):
  return coord2[0] == coord1[0] and coord2[1] > coord1[1]

def isDown(coord1, coord2):
  return coord2[0] == coord1[0] and coord2[1] < coord1[1]

def findClockwiseRect(origin, point, coordMap, direction):
  pointTuple = point[0], point[1]
  if direction == 'left':
    if origin in coordMap[pointTuple]['left']:
      return 1
    return 0
  nextDirection = findNextDirection(direction)
  rectCount = 0
  for p in coordMap[pointTuple][direction]:
    rectCount += findClockwiseRect(origin, p, coordMap, nextDirection)
  return rectCount

def findNextDirection(direction):
  if direction == 'up':
    return 'right'
  elif direction == 'right':
    return 'down'
  elif direction == 'down':
    return 'left'
  return direction

print(rectangleMania([
  [0,0],
  [0,1],
  [1,1],
  [1,0],
  [2,1],
  [2,0],
  [3,1],
  [3,0],
]))