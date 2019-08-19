def underscorifySubstring(string, substring):
  substring_locations = get_substring_locations(string, substring)
  collapsed_locations = collapse(substring_locations)
  return ''.join(underscorify(string, collapsed_locations))

def get_substring_locations(string, substring):
  substring_len = len(substring)
  substring_locations = []
  i = 0
  while i < len(string):
    location = string[i:].find(substring)
    if location == -1:
      return substring_locations

    substring_index = location + i
    substring_locations.append([substring_index, substring_index + substring_len])
    i = substring_index + 1
  return substring_locations

def collapse(locations):
  if len(locations) <= 1:
    return locations

  collapsed_locations = []
  location = locations[0]
  for i in range(1, len(locations)):
    next_location = locations[i]
    if next_location[0] <= location[1]:
      location = [location[0], next_location[1]]
    else:
      collapsed_locations.append(location)
      location = next_location
  collapsed_locations.append(location)
  return collapsed_locations

def underscorify(string, locations):
  result = []
  for i in range(len(string)):
    for location in locations:
      if location[0] == i or location[1] == i:
        result.append('_')
        break
    result.append(string[i])

  for location in locations:
    if location[1] == len(string):
      result.append('_')
      break
  return result


print(underscorifySubstring("this is a test to see if it works and test", "test"))
print(underscorifySubstring("testthis is a testtest to see if testestest it works", "test"))