import re
import array
vectorFile = open("vectors.txt")
test = open("text.txt", "r+")
frameStartIndexes = []
frames = []

# Funckja do dowolnego lini o danym stringu
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def seperate_list(frame, file, newFramePoint):
    last = 0
    for new in newFramePoint:
        if last:
            frames.append(file[(last+1):new])
        last = new

pureVectorFile = remove_values_from_list(vectorFile, "\n")

for line in pureVectorFile:
    if re.search("P ", line):
        frameStartIndexes.append(pureVectorFile.index(line))

seperate_list(frames, pureVectorFile, frameStartIndexes)
i = 0
for frame in frames:
    i += 1
    print "nowy kurwa frame", i
    for macroblock in frame:
        macroblock = macroblock.split()
        print ((float)(macroblock[2]) * (float)(macroblock[2])) + ((float)(macroblock[3]) + (float)(macroblock[3]))