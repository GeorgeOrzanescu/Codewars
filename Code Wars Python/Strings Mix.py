# Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

# s1 = "A aaaa bb c"

# s2 = "& aaa bbb c d"

# s1 has 4 'a', 2 'b', 1 'c'

# s2 has 3 'a', 3 'b', 1 'c', 1 'd'

# So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

# We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

# The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

# In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

# Hopefully other examples can make this clearer.

# s1 = "my&friend&Paul has heavy hats! &"
# s2 = "my friend John has many many friends &"
# mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

# s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
# s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
# mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

# s1="Are the kids at home? aaaaa fffff"
# s2="Yes they are here! aaaaa fffff"
# mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"



# FIRST DRAFT
# def mix(s1, s2):
    
#     first = [x for x in s1 if x.islower() and s1.count(x) >1]
#     second = [x for x in s2 if x.islower() and s2.count(x) >1]

#     first_bigger = '1:'
#     second_bigger = '2:'
#     equal = '=:'
    
#     first_results = []
#     second_results = []
#     equal_results = []

#     for letter in set(first):
#         if first.count(letter) > second.count(letter):
#             first_results.append((first_bigger+letter,first.count(letter)))
#         elif first.count(letter) == second.count(letter):
#             equal_results.append((equal+letter,first.count(letter)))
#         else:
#             second_results.append((second_bigger+letter,second.count(letter)))
        

#     for letter in set(second):
#         if first.count(letter) > second.count(letter):
#             first_results.append((first_bigger+letter,first.count(letter)))
#         elif first.count(letter) == second.count(letter):
#             equal_results.append((equal +letter,first.count(letter)))
#         else:
#             second_results.append((second_bigger+letter,second.count(letter)))

#     total = first_results+second_results+equal_results
#     print(sorted(set(total),key =lambda x : x[1],reverse=True))
        





# SECOND DRAFT   SUCCESS 
def mix(s1, s2):
    first = []
    second = []
    equal =[]
    result =''


    for letter in s1:
        if letter.islower() and s1.count(letter) >1 :
            first.append('1:'+letter*s1.count(letter))
    for letter in s2:
        if letter.islower() and s2.count(letter) >1 :
            second.append('2:'+letter*s2.count(letter))
    for letter in set(first):
        for letter2 in set(second):
            if letter[2] == letter2[2] and len(letter) == len(letter2):
                equal.append('=:'+letter[2:])
    

    first = [x for x in list(set(first)) if x[2:] not in [x[2:] for x in equal]]
    second = [x for x in list(set(second)) if x[2:] not in [x[2:] for x in equal]]
    
    for x in sorted(sorted(first+second+equal),key =lambda x : len(x.split(':')[1]),reverse=True):
        if x.split(':')[1] not in result:
            result += '/'+x

        
        
    return result[1:]
    




    
print(mix("Are they here", "yes, they are here"))  #"2:eeeee/2:yy/=:hh/=:rr"
print(mix("looping is fun but dangerous", "less dangerous than coding")