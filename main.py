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

#Obliczamy tottalny ruch w calej ramce
totalMotion = []
vectorLength = []
for frame in frames:
    vLength = []
    for macroblock in frame:
        macroblock = macroblock.split()
        vLength.append(vector_length(macroblock[2], macroblock[3]))
    vectorLength.append(vLength)
    totalMotion.append(sum(vLength))

# Kazda ramka dzielona jest na 9 blokow o rownych rozmiarach
# Do kazdego z bloku wpisywana jest suma dlugosci wekktorow ruchu w tym bloku
# Wszystkie Bloki z ramki zapisujemy do jednej listy
# areaMotion = []
# i = 0
# for frame in frames:
#     area0, area1, area2, area3, area4, area5, area6, area7, area8 = ([] for i in range(9))
#     FrameByArea = []
#     for macroblock in frame:
#         macroblock = macroblock.split()
#         x = int(macroblock[0])
#         y = int(macroblock[1])
#         currentVector = vector_length(macroblock[2], macroblock[3])
#         if x<107 and y<66:
#             area0.append(currentVector)
#         elif x<210 and x>=107 and y<66:
#             area1.append(currentVector)
#         elif x>210 and y<66:
#             area2.append(currentVector)
#         elif x<107 and y<126 and y>=67:
#             area3.append(currentVector)
#         elif x<210 and x>=107 and y<126 and y>=67:
#             area4.append(currentVector)
#         elif x>210 and y<126 and y>=67:
#             area5.append(currentVector)
#         elif x<107 and y>=126:
#             area6.append(currentVector)
#         elif x<210 and x>=107 and y>=126:
#             area7.append(currentVector)
#         elif x>210 and y>=126:
#             area8.append(currentVector)
#         else:
#             print "makroblok nie pasuje do zadnego obszaru"
#     FrameByArea.extend((sum(area0)/totalMotion[i], sum(area1)/totalMotion[i], sum(area2)/totalMotion[i], sum(area3)/totalMotion[i], sum(area4)/totalMotion[i], sum(area5)/totalMotion[i], sum(area6)/totalMotion[i], sum(area7)/totalMotion[i], sum(area8)/totalMotion[i]))
#     areaMotion.append(FrameByArea)
#     i += 1
#
# print areaMotion

i = 0
angleMotion = []
for frame in frames:
    angle0, angle1, angle2, angle3, angle4, angle5, angle6, angle7 = ([] for i in range(8))
    FrameByAngle = []
    for macroblock in frame:
        macroblock = macroblock.split()
        currentVector = vector_length(macroblock[2], macroblock[3])
        if currentVector != 0:
            currentAngle = math.degrees(math.atan2(float(macroblock[3]), float(macroblock[2])))
            if -22.5 <= currentAngle < 22.5:
                angle0.append(currentVector)
            elif 22.5 <= currentAngle < 67.5:
                angle1.append(currentVector)
            elif 67.5 <= currentAngle < 112.5:
                angle2.append(currentVector)
            elif 112.5 <= currentAngle < 157.5:
                angle3.append(currentVector)
            elif 157.5 <= currentAngle <= 180.0 or -180.0 <= currentAngle < -157.5:
                angle4.append(currentVector)
            elif -157.5 <= currentAngle < -112.5:
                angle5.append(currentVector)
            elif -112.5 <= currentAngle < -67.5:
                angle6.append(currentVector)
            elif -67.5 <= currentAngle < -22.5:
                angle7.append(currentVector)
            else:
                print "makroblok nie pasuje do zadnego obszaru"
    FrameByAngle.extend((sum(angle0)/totalMotion[i], sum(angle1)/totalMotion[i], sum(angle2)/totalMotion[i], sum(angle3)/totalMotion[i], sum(angle4)/totalMotion[i], sum(angle5)/totalMotion[i], sum(angle6)/totalMotion[i], sum(angle7)/totalMotion[i]))
    angleMotion.append(FrameByAngle)
    i += 1

print angleMotion
