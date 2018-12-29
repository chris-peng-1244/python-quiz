def rectangles(rec1, rec2):
  left_x = max(rec1["top_left"][0], rec2["top_left"][0])
  right_x = min(rec1["top_left"][0] + rec1["dimensions"][0], rec2["top_left"][0] + rec2["dimensions"][0])

  top_y = min(rec1["top_left"][1], rec2["top_left"][1])
  bottom_y = max(rec1["top_left"][1] + rec1["dimensions"][1], rec2["top_left"][1] + rec2["dimensions"][1])

  if left_x > right_x or bottom_y > top_y:
    return 0

  return (right_x - left_x) * (top_y - bottom_y)
