import re
import array
vectorFile = open("vectors.txt")
frameStartIndexes = []
frames = []
last = 0
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def seperate_list(list, newFramePoint):
    return 0;

pureVectorFile = remove_values_from_list(vectorFile, "\n")
for line in pureVectorFile:
    if re.search("P ", line):
        frameStartIndexes.append(pureVectorFile.index(line))

for new in frameStartIndexes:
    if last:
        frames.append(pureVectorFile[last:new])
    last = new