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


for frame in frames:
    area0, area1, area2, area3, area4, area5, area6, area7, area8 = ([] for i in range(9))
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
            print "no kurwa sprobuj"
    print len(area0), len(area1), len(area2), len(area3), len(area4), len(area5), len(area6), len(area7), len(area8)
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