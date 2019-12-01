lines = []

ySplit = 319

with open("weather-canada.csv") as f:
    lines = f.readlines()

header = [lines[0]]
lines = filter(lambda l: int(l.split(",")[0]) <= ySplit, lines[1:])
header.extend(lines)

with open("weather-lower-canada.csv", "w+") as f:
    f.writelines(header)
