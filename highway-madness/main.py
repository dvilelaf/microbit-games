import random
import screen
import object
import animations


# Frames per second and frame duration
fps = 10
frameDuration = 1.0 / fps  # seconds

# Vehicle sizes
vehicleSizes = {'bike': [2, 1], 'car': [2, 2], 'van': [3, 2], 'truck': [4, 2]}


###############################################################################

def spawnVehicle(objectDict, level):

    # Select a random vehicle type
    vehicleType = random.choice(list(vehicleSizes.keys()))
    vehicleSize = vehicleSizes[vehicleType]

    # Search for available positions to spawn ths vehicle
    availablePositions = [i for i in range(screen.screenSize[1])]

    if vehicleSize[1] > 1:
        availablePositions.pop()

    for name, obj in objectDict.items():
        if name is not 'player' and obj.collidable:

            for j in range(obj.size[1]):

                pos = int(obj.position[1] // 1) + j

                if pos in availablePositions:
                    availablePositions.remove(pos)

    # Find a slot with enough room for the vehicle

    indices = [i for i in range(len(availablePositions))]

    slotFound = False
    tries = 0
    maxTries = len(availablePositions)

    while(not slotFound and tries < maxTries):

        slot = random.choice(indices)

        for j in range(vehicleSize[1]):

            if (availablePositions[slot] + j) not in availablePositions:
                indices.remove(slot)
                break

            if (j + 1) is vehicleSize[1]:
                slotFound = True

        tries += 1

    if slotFound:

        vehiclePosition = [-3, availablePositions[slot]]

        # Spawn the vehicle. The speed depends on the level
        objectDict[vehicleType + str(random.randint(0, 100))] = object.object(size=vehicleSize,
                                                                              position=vehiclePosition,

                                                                              speed=[random.randint(1, level), 0])
    return slotFound


###############################################################################
def testCollisions(objectDict):

    player = objectDict['player']

    for name, obj in objectDict.items():
        if name is not 'player' and obj.collidable:

            for i in range(player.position[0], player.position[0] + player.size[0]):
                for j in range(player.position[1], player.position[1] + player.size[1]):
                    if pointInsideObject(i, j, obj):
                        return True

    return False


###############################################################################
# MAIN CODE

# Create the screen object
scr = screen.screen()

level = 1
score = 0

# Main loop
while(True):

    # New level
    objectDict = {'player': object.object(size=vehicleSizes['bike'], position=[3, 2]), }
    crash = False
    win = False
    frame = 1
    speed = 5 + level
    animations.levelStart(level)

    # Level loop
    while(not crash and not win):

        tstart = running_time()

        # Create random objects
        randNumber = random.randint(0, 3*fps)  # Approx every 3 seconds

        if randNumber is 0:
            spawnVehicle(objectDict, level)
            score += 1

        # Render the scene
        scr.renderObjectDict(objectDict)

        # Read input and update player's position
        if button_a.is_pressed():
            objectDict['player'].moveLeft()

        if button_b.is_pressed():
            objectDict['player'].moveRight()

        # Update vehicle positions. Delete if out of scene
        deletions = []

        for name, obj in objectDict.items():
            if name is not 'player':

                pi = obj.position[0] + obj.speed[0] * frameDuration
                pj = obj.position[1] + obj.speed[1] * frameDuration

                obj.setPosition([pi, pj])

                if obj.position[0] >= screen.screenSize[0]:
                    deletions.append(name)

        for name in deletions:
            del objectDict[name]

        # Check for collisions
        for name, obj in objectDict.items():
            if name is not 'player':
                crash = objectDict['player'].testCollision(obj)

                if crash:
                    break

        # Check for win
        if frame is 30 * fps:  # 30 seconds per level
            win = True

        # Play animations if needed
        if crash:
            animations.crash()
            animations.score(score)
            reset()

        if win:
            animations.win()
            animations.score(score)
            level += 1

        frame += 1

        # Sleep to keep the framerate
        if (running_time() - tstart) < frameDuration:
            sleep(frameDuration - (running_time() - tstart))

