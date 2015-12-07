import re
import math

vectorFile = open("vectors.txt")
test = open("text.txt", "r+")
frameStartIndexes = []
frames = []

# Funckja do dowolnego lini o danym stringu
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

# Funkcja rozdzielajaca liste na mniejsze porcje wg index'u wskazanych punktow
def seperate_list(frame, file, newFramePoint):
    last = 0
    for new in newFramePoint:
        if last:
            frames.append(file[(last+1):new])
        last = new

# Funkcja liczaca dlugosc wektora
def vector_length(x, y):
    return math.sqrt(float(x) * float(x) + float(y) * float(y))

# Usuwamy z otworzonego pliku puste linie
pureVectorFile = remove_values_from_list(vectorFile, "\n")

# Szukamy poczatku ramek P, niezbedne do podzielenia pliku
for line in pureVectorFile:
    if re.search("P ", line):
        frameStartIndexes.append(pureVectorFile.index(line))

# Dzielimy otworzony plik na ramki
seperate_list(frames, pureVectorFile, frameStartIndexes)

areaMotion = []
for frame in frames:
    area0, area1, area2, area3, area4, area5, area6, area7, area8 = ([] for i in range(9))
    FrameByArea = []
    for macroblock in frame:
        macroblock = macroblock.split()
        x = int(macroblock[0])
        y = int(macroblock[1])
        currentVector = vector_length(macroblock[2], macroblock[3])
        if x<107 and y<66:
            area0.append(currentVector)
        elif x<210 and x>=107 and y<66:
            area1.append(currentVector)
        elif x>210 and y<66:
            area2.append(currentVector)
        elif x<107 and y<126 and y>=67:
            area3.append(currentVector)
        elif x<210 and x>=107 and y<126 and y>=67:
            area4.append(currentVector)
        elif x>210 and y<126 and y>=67:
            area5.append(currentVector)
        elif x<107 and y>=126:
            area6.append(currentVector)
        elif x<210 and x>=107 and y>=126:
            area7.append(currentVector)
        elif x>210 and y>=126:
            area8.append(currentVector)
        else:
            print "makroblok nie pasuje do zadnego obszaru"
    FrameByArea.extend((sum(area0), sum(area1), sum(area2), sum(area3), sum(area4), sum(area5), sum(area6), sum(area7), sum(area8)))
    areaMotion.append(FrameByArea)

print areaMotion

# i = 0
# totalMotion = []
# vectorLength = []
# for frame in frames:
#     vLength = []
#     for macroblock in frame:
#         macroblock = macroblock.split()
#         vLength.append(vector_length(macroblock[2], macroblock[3]))
#     vectorLength.append(vLength)
#     totalMotion.append(sum(vLength))
#
# print totalMotion