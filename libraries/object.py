from screen import standardBrightness

# Object class handles game objects that are rendered on the display

class object:

    def __init__(self, size=[1, 1], position=[0.0, 0.0], speed=[0, 0],
                 shape=None, brightness=standardBrightness, collidable=True):

        self.size = size
        self.position = position
        self.speed = speed
        self.brightness = brightness
        self.collidable = collidable

        if shape is None:
            self.shape = [[brightness for j in range(size[1])] for i in range(size[0])]
        else:
            self.size = [len(shape), len(shape[0])]
            self.shape = shape


    def moveUp(self):
        self.position[0] -= 1


    def moveDown(self):
        self.position[0] += 1


    def moveLeft(self):
        self.position[1] -= 1


    def moveRight(self):
        self.position[1] += 1


    def setPosition(self, position):
        self.position = position


    def setSpeed(self, speed):
        self.speed = speed


    def setBrightness(self, brightness):
        self.brightness = brightness


    def isPointInside(self, i, j):
    
        return (i >= self.position[0]) and \
               (i < self.position[0] + self.size[0]) and \
               (j >= self.position[1]) and \
               (j < self.position[1] + self.size[1])


    def testCollision(obj):

        if obj.collidable and self.collidable:

            for i in range(int(obj.position[0]), int(obj.position[0]) + obj.size[0]):
                for j in range(int(obj.position[1]), int(obj.position[1]) + obj.size[1]):
                    if self.isPointInside(i, j):
                        return True

        return False
