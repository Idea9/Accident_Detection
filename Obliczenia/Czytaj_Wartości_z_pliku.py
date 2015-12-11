import numpy as np
import re
import math

sample = "Umbrella_on_sight"
vectorFile = open("Vectors/" + sample + ".txt")
frameStartIndexes = []
frames = []
f = open('klasyfikatory/Total_Pure_v1.txt', 'r+')

# Funckja do dowolnego lini o danym stringu
def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


# Funkcja rozdzielajaca liste na mniejsze porcje wg index'u wskazanych punktow
def seperate_list(frame, file, newFramePoint):
    last = 0
    for new in newFramePoint:
        if last:
            frames.append(file[(last + 1):new])
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

features = remove_values_from_list(f, "\n")
i = 0
for feature in features:
    if i == 1:
        maximum = float(feature)
    if i == 3:
        threshold = float(feature)
    i += 1

print maximum, threshold

# Obliczamy tottalny ruch w calej ramce
totalMotion = np.array([0])
frameNumber = 0
for frame in frames:
    frameNumber += 1
    vLength = []
    for macroblock in frame:
        macroblock = macroblock.split()
        vLength.append(vector_length(macroblock[2], macroblock[3]))
    a = sum(vLength)
    totalMotion = np.append(totalMotion, a + 0.000001)

print "Liczba ramek z wektorami ruchu: ", frameNumber