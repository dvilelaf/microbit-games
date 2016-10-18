from microbit import *


class screen:
    
    def __init__(self):
        self.matrix = [[0, 0, 9, 0, 0],
                       [0, 0, 9, 0, 0],
                       [0, 9, 9, 9, 0],
                       [0, 9, 9, 9, 0],
                       [9, 0, 0, 0, 9]]
        self.render()

    def update(self, matrix):
        self.matrix = matrix
        self.render()

    def render(self):
        self.image = self.string()
        display.show(Image(self.image))

    def string(self):
        string = ""
        for row in self.matrix:
            for i in row:
                string += str(i)
            string += ':'
        return string[:-1]

    def setBrightness(self, newBrightness):

        if newBrightness > 9:
            newBrightness = 9
        if newBrightness < 1:
            newBrightness = 1

        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] > 0:
                    self.matrix[i][j] = newBrightness

        self.render()
        
        
class object:

    def __init__(self, size = [1, 1], position = [0, 0]):
        self.size = size  
        self.position = position
        self.speed = [0, 0]

    def moveup:
        self.position[0] -= 1

    def movedown:
        self.position[0] += 1

    def moveleft:
        self.position[1] -= 1

    def moveright:
        self.position[1] += 1


class cannon(object):
    
    def __init__(self):
        self.size = [1, 1]
        self.position = [4,2]

    def shoot:
        
        
# Game

scr = screen()


while(True):


