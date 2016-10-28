from microbit import *

# Screen properties

screenSize = [5, 5]  # rows, columns
minBrightness = 0
maxBrightness = 9
standardBrightness = 5

# Screen class handles the display and renders given objects

class screen:
    
    def __init__(self):

        self.clear()
        self.render()


    def clear(self):

        self.matrix = [[minBrightness for j in range(screenSize[1])] for i in range(screenSize[0])]


    def update(self, matrix):

        self.matrix = matrix


    def render(self):

        for i in range(screenSize[0]):
            for j in range(screenSize[1]):
                display.set_pixel(j, i, self.matrix[i][j])
                

    def renderObjectDict(self, objectDict):

        self.clear()

        for name, obj in objectDict.items():
            for i in range(obj.size[0]):
                for j in range(obj.size[1]):

                    if obj.shape[i][j] is minBrightness:
                        continue

                    x = int(obj.position[0] // 1) + i
                    y = int(obj.position[1] // 1) + j

                    if x >= 0 and \
                       x < screenSize[0] and \
                       y >= 0 and \
                       y < screenSize[1]:

                        self.matrix[x][y] = obj.brightness

        self.render()
