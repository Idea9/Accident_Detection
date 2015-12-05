import re
import array
vectorFile = open("vectors.txt")
frameStartIndexes = []
frames = []
last = 0
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def seperate_list(frame, file, newFramePoint):
    last = 0
    for new in newFramePoint:
        if last:
            frames.append(file[last:new])
        last = new

pureVectorFile = remove_values_from_list(vectorFile, "\n")

for line in pureVectorFile:
    if re.search("P ", line):
        frameStartIndexes.append(pureVectorFile.index(line))

seperate_list(frames, pureVectorFile, frameStartIndexes)

print frames[0]