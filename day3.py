import numpy as np

raw = open("input/3.txt","r").readlines()
input_array = np.asarray([string[:-1].split(',') for string in raw], dtype=object)
#print(input_array[0], input_array[1])
#input_array = np.asarray([string.split(2) for string in input_array])
print(input_array, len(input_array))

def coordinates(instructions):
    x = 0
    y = 0
    result = [[0,0]]
    for inst in instructions:
 #       print(inst)
        if inst[0] =='R':
            print(inst)
            length = int(inst[1:])
            for i in range(1,length+1):
                result.append([x+i, y])
            x += length
        elif inst[0] == 'L':
            length = int(inst[1:])
            for i in range(1,length+1):
                result.append([x-i, y])
            x -= length
        elif inst[0] == 'U':
            length = int(inst[1:])
            for i in range(1,length+1):
                result.append([x, y+i])
            y += length            
        elif inst[0] == 'D':
            length = int(inst[1:])
            for i in range(1,length+1):
                result.append([x, y-i])
            y -= length
    return result
    
def partOne(input):
    line1 = coordinates(input[0])
    line2 = coordinates(input[1])
    intersect = [value for value in line1 if value in line2] 
    print(intersect)
#    distance = [value[0]+value[1] for value in intersect if value[0]+value[1] > 0]
#    print(min(distance))

partOne(input_array)
