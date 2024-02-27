with open("circle.txt", "r") as FileCircle:
    a, b = map(float, FileCircle.readline().split())
    r = float(FileCircle.readline())
with open("dots.txt", "r") as FileDots:
    for line in FileDots:
        x, y = map(float, line.split())
        if (x - a) * (x - a) + (y - b) * (y - b) == r * r:
            print('0')
        if (x - a) * (x - a) + (y - b) * (y - b) < r * r:
            print('1')
        if (x - a) * (x - a) + (y - b) * (y - b) > r * r:
            print('2')
