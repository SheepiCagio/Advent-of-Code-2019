import numpy as np

raw = open("input/1.txt","r").readlines()
input_array = np.asarray([int(string[:-1]) for string in raw])

#print(input_array)
def calculate(input):
    input = np.floor(input/3)-2
    return input

def partOne(input):
    outcome = calculate(input)
    print(sum(np.intc(outcome)))

def partTwo(input):
    result = 0
    for load in input:
        fuel = calculate(load)
        while fuel >= 0:
            result = result + fuel
            fuel = calculate(fuel)
    print(result)

partOne(input_array)
partTwo(input_array)