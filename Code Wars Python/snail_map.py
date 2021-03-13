
def snail(snail_map):
    pass


array2 = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,8],
         [7,8,9,0]]


def snail(array):
    results = []
    while len(array) > 0:
        # go right
        results += array[0]
        del array[0]
        print(array)
        if len(array) > 0:
            # go down
            for i in array:
                results += [i[-1]]
                del i[-1]
                print(array)
            # go left
            if array[-1]:
                results += array[-1][::-1]
                del array[-1]
                print(array)
               
            # go top
            for i in reversed(array):
                results += [i[0]]
                del i[0]
                print(array)

    return results


def snail2(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = zip(*array)
        array.reverse()
    return a

def snail3(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []


import numpy as np

def snail4(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m

snail5 = lambda a: list(a[0]) + snail(zip(*a[1:])[::-1]) if a else []

print(snail5(array2))

# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

