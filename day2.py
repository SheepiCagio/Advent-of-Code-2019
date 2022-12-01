import numpy as np
import copy

raw = open("input/2.txt","r").readlines()
input_array=np.asarray(raw[0].split(','))
input_array = np.asarray([int(string) for string in input_array])
#print(input_array, len(input_array))


def IntCode(input):
    for x in range(0,len(input)-1,4):
        if input[x] == 1:
            input[input[x+3]] = input[input[x+1]] + input[input[x+2]]
        elif input[x] == 2:
            input[input[x+3]] = input[input[x+1]] * input[input[x+2]]
        elif input[x] == 99:
            break
    return input[0]

def partOne(inputOne):
    input1 = copy.deepcopy(inputOne)
    input1[1] = 12           
    input1[2] = 2
    print(IntCode(input1))

def partTwo(two):
    for x in range(0,100):
        for y in range(0,100):
            inputTwo = copy.deepcopy(two)
            inputTwo[1] = x
            inputTwo[2] = y
            result = IntCode(inputTwo)
            if result == 19690720:
                print(x*100+y)
                break
partOne(input_array)
partTwo(input_array)

