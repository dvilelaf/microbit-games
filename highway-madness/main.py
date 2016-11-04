from microbit import *
import random

# Position (i,j) and speed indexes
pi = 0
pj = 1
s  = 2

# Player, enemies and score initialization
player = [3.0, 2.0, 0.0]
enemies = []
score = 0

# Main loop
while True:

    # Read input and update player speed
    player[s] = 0.0

    if button_a.is_pressed():
        player[s] = -0.2

    if button_b.is_pressed():
        player[s] = 0.2

    # Update player position
    player[pj] += player[s]

    # Keep player inside the screen
    if player[pj] < 0:
        player[pj] = 0

    if player[pj] > 4:
        player[pj] = 4

    # Create random enemies
    if random.randint(0, 25) is 0 and len(enemies) < 2:
        enemies.append([-2.0, random.randint(0, 3), 0.1])

    # Update enemy positions and delete if out of scene
    deletions = []

    for i in range(len(enemies)):

        enemies[i][pi] += enemies[i][s]

        if enemies[i][pi] > 5:
            deletions.append(i)

    for i in deletions:
        enemies.pop(i)
        score += 1

    # Check collisions
    for enemy in enemies:
        if (player[pi] >= enemy[pi])     and \
           (player[pi] <  enemy[pi] + 1) and \
           (player[pj] >= enemy[pj])     and \
           (player[pj] <  enemy[pj] + 2):

           display.scroll('CRASH!')
           display.scroll('Score: ' + str(score))
           reset()

    # Update pixels
    pixels = [[0 for i in range(5)] for j in range(5)]

    pixels[int(player[pi])    ][int(player[pj])] = 5
    pixels[int(player[pi]) + 1][int(player[pj])] = 5

    for enemy in enemies:
        for i in range(2):
            for j in range(2):
                y = i + int(enemy[pi])
                x = j + int(enemy[pj])

                if x >= 0 and x<5 and y >=0 and y < 5:
                    pixels[y][x] = 5

    # Render
    for i in range(5):
        for j in range(5):
            display.set_pixel(j, i, pixels[i][j])


