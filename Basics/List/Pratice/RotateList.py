
lst = [1, 2, 3, 4, 5, 6]
n = 2

# TODO: Rotate lst by n positions using slicing and concatenation

rotated = lst[n:] + lst[:n]

print("Rotated List:", rotated)
