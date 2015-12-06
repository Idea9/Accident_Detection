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

i = 0
totalMotion = []
vectorLength = []
for frame in frames:
    vLength = []
    for macroblock in frame:
        macroblock = macroblock.split()
        vLength.append(vector_length(macroblock[2], macroblock[3]))
    vectorLength.append(vLength)
    totalMotion.append(sum(vLength))

print totalMotion