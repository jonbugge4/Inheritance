
class Athlete:
    def __init__(self,ht,wt,bodyfat):
        self.__ht = ht
        self.__wt = wt
        self.__bf = bodyfat

    def get_ht(self):
        return self.__ht

    def get_wt(self):
        return self.__wt

    def get_bf(self):
        return self.__bf



class Football_Player(Athlete):
# inherites athelte traist but also adds more traits-- 
#position, team --> need 5 traits to create a player
# 3 for "athelete, 2 more for football player"

    def __init__(self,ht,wt,bodyfat,position,team):

        Athlete.__init__(self,ht,wt,bodyfat)

        self.__position = position
        self.__team = team
# only need two get clauses because they are accessed in the 
#super clause

    def get_position(self):
        return self.__position

    def get_team(self):
        return self.__team










    
