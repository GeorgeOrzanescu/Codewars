# def longest_slide_down(pyramid):
#     max_sum = 0

#     for i in range(0,len(pyramid)):
#         max_sum += max(pyramid[i])

#     print(max_sum)


# def longest_slide_down(pyramid):
#     max_sum = 0

#     while len(pyramid) > 0:

#         max_sum += max(pyramid[0])
#         del pyramid[0]

#         print(max_sum)


# def longest_slide_down(pyramid):     problem with the i , i dont know how to make it not change back to 1 every time the loop starts again 
#     max_sum = 0

#     while len(pyramid) > 0:
#         i = 1
#         x , y = (i-1, i+1)
        
#         max_sum += max(pyramid[0][x:y])
#         i = pyramid[0].index(max(pyramid[0][x:y]))
        
#         del pyramid[0]
        
#         print(max_sum)




# def longest_slide_down(pyramid):          # closer but i think he means only consecutive numbers not one above each other!!!  so have to not include the middle index when y > 0
#     max_sum = 0 
#     y = 0

#     while len(pyramid) > 0:
        
        
#         if y == 0:
#             max_sum += max(pyramid[0][y:y+2])
#             y = pyramid[0].index(max(pyramid[0][y:y+2]))
            
            
#             del pyramid[0]
#         else:
#             max_sum += max(pyramid[0][y-1:y+2])
#             y = pyramid[0].index(max(pyramid[0][y-1:y+2]))
            
            
#             del pyramid[0]



#     return max_sum




#this is actualy more harder , because they whore meaning to find the largest sum posibble !!!!
# # meaning some times you could choose a smaller number because the next row will be larger
 
# def longest_slide_down(pyramid):   ### I got tangled up in slices:))  but maybe closer
#     max_sum = pyramid[0][0]
#     del pyramid[0] 
#     y = 0
    
#     while len(pyramid) > 1:
#         print(y)
       
#         if y == 0:
#             # max_sum += max(pyramid[0][y:y+2])
#             y = pyramid[0].index(max(pyramid[0][y:y+2]))
#             if max(pyramid[1][y:y+2]) > max(pyramid[1][y:y+3]):
#                 max_sum += max(pyramid[0][y:y+2])
#             else:
#                 y += 1
#                 max_sum += pyramid[0][1] 
#             print('y - 0')
#             del pyramid[0]


#         else:
#             if max(pyramid[1][y:y+1]) > max(pyramid[1][y:y+3]):
#                 print(max(pyramid[1][y:y+1]),"------",max(pyramid[1][y:y+3]))
#             # max_sum += max(pyramid[0][y:y+2])
#                 y = pyramid[0].index(max(pyramid[0][y:y+2]))
#                 print(f' {y} y if in row below first is bigger then second')
#                 max_sum += max(pyramid[0][y:y+2])
#             else:
#                 print(max(pyramid[1][y:y+1]),"------",max(pyramid[1][y:y+3]))
#                 y = pyramid[0].index(max(pyramid[0][y:y+1])) +1
#                 print(f' {y} y if in row below second is bigger then first')
#                 max_sum += pyramid[0][y]
                

#             del pyramid[0]
                     
#         print(max_sum)

#     return max_sum
        
def longest_slide_down(pyramid):  #this is resolved using graph theory ( i looked the solution up)
        pyramid = [row for row in reversed(pyramid)]
        result = pyramid[0]

        for index in range(1,len(pyramid)):
            next_row = pyramid[index]
            for i in range(len(next_row)):
                print(result)
                result[i] = next_row[i] + max(result[i],result[i+1])
            
                
            
        print(result)    
            
                
def longest_slide_down2(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))]
    return res.pop() 
  


print(longest_slide_down([[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92]
            ]))


test=[[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
            ]

print(longest_slide_down(test))