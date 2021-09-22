
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color

# Create a subtype of Plant
class Flower(Plant):
    def __init__(self,color, petals):
#call plant's iniit method
        Plant.__init__(self,color)

        self.__petals = petals

    def get_petals(self):
        return self.__petals
    
