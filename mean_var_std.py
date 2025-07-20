import numpy as np
import pprint as pp
# mean, variance, standard deviation, max, min, sum
def calculate(lst):

    if len(lst) != 9:
        raise TypeError("Please insert 9 of numbers")
    
    array = np.array(lst)
    array = np.array(lst).reshape(3, 3)

    rsl = {
        'mean': [
            array.mean(axis=0).tolist(),
            array.mean(axis=1).tolist(),
            array.mean().item()
        ],
        'variance': [
            array.var(axis=0).tolist(),
            array.var(axis=1).tolist(),
            array.var().item()
        ],
        'standard deviation': [
            array.std(axis=0).tolist(),
            array.std(axis=1).tolist(),
            array.std().item()
        ],
        'max': [
            array.max(axis=0).tolist(),
            array.max(axis=1).tolist(),
            array.max().item()
        ],
        'min': [
            array.min(axis=0).tolist(),
            array.min(axis=1).tolist(),
            array.min().item()
        ],
        'sum': [
            array.sum(axis=0).tolist(),
            array.sum(axis=1).tolist(),
            array.sum().item()
        ]
    }

    print("{")
    keys = list(rsl.keys())
    for i in range(len(keys)):
        key = keys[i]
        value = rsl[key]
        print(f"  '{key}' : {value}", end="")
        if i < len(keys) -1 :
            print(",")
        else: print("")
    print("}")
    
calculate([0,1,2,3,4,5,6,7,8])