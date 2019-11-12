def apartmentHunting(blocks, reqs):
  reqDistances = []
  for req in reqs:
    reqDistances.append(findDistances(blocks, req))

  minDistance = float('inf')
  minIdx = 0
  for i in range(len(blocks)):
    distance = 0
    for reqDistance in reqDistances:
      distance = max(distance, reqDistance[i])
    if minDistance > distance:
      minIdx = i
      minDistance = distance
  return minIdx
  
def findDistances(blocks, req):
  distances = [float('inf') for _ in blocks]
  # Caculate distance from left to right
  lastReqIdx = -1
  for i in range(len(blocks)):
    if blocks[i][req] == True:
      lastReqIdx = i
    if lastReqIdx >= 0:
      distances[i] = min(distances[i], i - lastReqIdx)

  # Calculate distance from right to left
  lastReqIdx = -1
  for i in range(len(blocks)-1, -1, -1):
    if blocks[i][req] == True:
      lastReqIdx = i
    if lastReqIdx >= 0:
      distances[i] = min(distances[i], lastReqIdx - i)
  return distances

apartments = [
  {
    'gym': True,
    'school': True,
    'store': False,
  },
  {
    'gym': False,
    'school': False,
    'store': False,
  },
  {
    'gym': False,
    'school': True,
    'store': False,
  },
  {
    'gym': False,
    'school': False,
    'store': False,
  },
  {
    'gym': False,
    'school': False,
    'store': True,
  },
  {
    'gym': True,
    'school': False,
    'store': False,
  },
  {
    'gym': False,
    'school': False,
    'store': False,
  },
  {
    'gym': False,
    'school': False,
    'store': False,
  },
  {
    'gym': False,
    'school': False,
    'store': False,
  },
  {
    'gym': False,
    'school': True,
    'store': False,
  },
]

print(apartmentHunting(apartments, [ 'gym', 'school', 'store' ]))