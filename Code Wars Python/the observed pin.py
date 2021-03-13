import itertools

# def get_pins(observed):
#     key = [[1,2,3],[4,5,6],[7,8,9],[0]]
    
#     final = []
#     for i in range(1,len(observed)+1):
#         final.append(tuple(itertools.combinations(observed,i)))
#     print(final)
#     result = []

    
#     for t in final:
#         for elem in t:
#             for i in range(len(elem)):
#                 result.append(f'{elem[i]}')
            
#     print(result)
        



# def get_pins(observed):
#     matches = [[0,8],[1,2,4],[1,2,3,5],[2,3,6],[1,4,5,7],[2,4,5,6,8],[3,5,6,9],[4,7,8],[5,7,8,9,0],[6,8,9]]
#     combinations = [matches[int(n)] for n in observed]  #using the number as index

#     test = list(itertools.product(*combinations)) 
 
#     result = []
#     for tup in test:
#         result.append(''.join(str(x) for x in tup))  # converting tuple to string

#     return result
    

adjacents = {
  '1': ['2', '4'],
  '2': ['1', '5', '3'],
  '3': ['2', '6'],
  '4': ['1', '5', '7'],
  '5': ['2', '4', '6', '8'],
  '6': ['3', '5', '9'],
  '7': ['4', '8'],
  '8': ['5', '7', '9', '0'],
  '9': ['6', '8'],
  '0': ['8'],
}

def get_pins(observed):
  if len(observed) == 1:
    return adjacents[observed] + [observed]


  return [a + b for a in adjacents[observed[0]] + [observed[0]] for b in get_pins(observed[1:])]


print(get_pins('24'))
