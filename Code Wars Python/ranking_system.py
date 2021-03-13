# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python


# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

# FIRST TRY , I THINK ITS A PROBLEM WITH POINTS COUNT
# class User():
#     def __init__(self,rank = -8,points=0):
#         self.rank = rank
#         self.points = points
#
#
#     def inc_progress(self,level):
#         levels = [x for x in range(-8,9) if x != 0]
#         if level in levels:
#             if self.rank  >=  level +2 :
#                 self.points += 0
#                 pass
#             if self.rank -1 == level:
#                 self.points += 1
#             if self.rank == level:
#                 self.points += 3
#             if self.rank < level:
#
#                 coef = self.rank - level
#                 self.points += 10 * coef * coef
#         # else:
#         #     raise Exception('Number not in range!')
#
#
#     def progress(self):
#         if self.rank >= 8:
#             self.rank = 8
#
#         if self.rank == -1 and (self.points // 100):
#             self.rank = 0

#         coef_2 = self.points // 100
#         if coef_2 > 0:
#             self.rank += self.points // 100
#             self.points = self.points % 100
#
#         return self.points

class User():  #did it eventually but was missreading the instructions
    #self.progress should be an attribute not method

    def __init__(self, rank=-8, progress = 0):

        self.rank = rank
        self.progress = progress

    def inc_progress(self,level):
        levels = [(index,rank) for (index,rank) in enumerate([x for x in range(-8, 9) if x != 0])]
        coef = 0
        coef_2 = 0

        if level not in [x[1] for x in levels]:
            raise Exception('Number not in range!')


        for x in levels:
            if level == x[1]:
                coef = x[0]
            if self.rank == x[1]:
                coef_2 = x[0]

        if self.rank < 8:
            if coef_2 == coef:
                self.progress += 3
            if coef_2-1  == coef:
                self.progress += 1
            if coef_2 >= coef + 2:
                self.progress += 0
            if coef_2 < coef:
                d = coef - coef_2
                self.progress += 10 * d * d


        if self.progress // 100 > 0 and self.rank < 8:
            old_rank = self.rank

            self.rank += self.progress // 100
            self.progress = self.progress % 100

            if old_rank <= -1 and self.rank >=0:
                self.rank += 1
            if self.rank >= 8:
                self.rank = 8
                self.progress = 0













user = User()
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(6)
print(user.rank)
print(user.progress)
print(user.rank)