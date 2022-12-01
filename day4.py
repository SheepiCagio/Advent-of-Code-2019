import numpy as np
import copy
import matplotlib.pyplot as plt

width = 25 
height = 6
layerLen = width * height

raw = open("input/4.txt","r").readlines()
 
input_array = np.asarray([raw[0][i:i + layerLen] for i in range(0, len(raw[0]), layerLen)])
input_array = np.asarray([[*string] for string in input_array])
input_array = np.asarray([[int(x) for x in string] for string in input_array])

def partOne(input):
    result = np.asarray([np.count_nonzero(layer == 0) for layer in input])
    layerResult = np.where(result == min(result))
    print(np.count_nonzero(input[layerResult] == 1) * np.count_nonzero(input[layerResult] == 2))

def partTwo(input):
    result = []
    for pixel in range(0,len(input[0])):
        result.append(2)
        for layer in input:
            #print(layer, layer[pixel])
            if layer[pixel] == 0:
                result[pixel] = 0
                break
            elif layer[pixel] == 1:
                result[pixel] = 1
                break
            elif layer[pixel] == 2:
                continue
    result = np.asarray(result).reshape(height,width)
    X,Y = np.meshgrid(np.arange(result.shape[1]), np.arange(result.shape[0]))
    plt.scatter(X.flatten(), Y.flatten(), c=result.flatten())
    plt.show()

    

partOne(input_array)
partTwo(input_array)
#[text[i:i + 5] for i in range(0, len(text), 5)]