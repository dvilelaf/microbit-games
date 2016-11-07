from microbit import *
import random

# Snake initialization
alive = True
snake = [[2,3], [2,2], [2,1]]
speed = [0,1]
food = [random.randint(0,4), random.randint(0,4)]
score = 0

# Images
wrong = Image("50005:05050:00500:05050:50005")
numbers = ["05550:00050:05550:00050:05550",
           "05550:00050:05550:05000:05550",
           "00500:05500:00500:00500:05550"]

# Get ready: 3...2...1

for number in numbers:
    display.show(Image(number))
    sleep(300)
    display.clear()
    sleep(500)

time = 0.0

while alive:

    # Check user input
    if button_a.is_pressed():
        speed = [-speed[1], speed[0]]
        # Wait for button release
        while button_a.is_pressed():
            1

    if button_b.is_pressed():
        speed = [speed[1], -speed[0]]
        # Wait for button release
        while button_b.is_pressed():
            1

    # Update position
    if time > 1.0:
        snake.pop()
        snake.insert(0, [snake[0][0] + speed[0], snake[0][1] + speed[1]])
        time = 0.0

    # Keep the snake inside the screen
    for point in snake:
        if point[0] < 0 or point[0] > 4:
            point[0] = point[0] - speed[0] * 5

        if point[1] < 0 or point[1] > 4:
            point[1] = point[1] - speed[1] * 5

    # Check collisions
    if snake[0] in snake[1:]:
        alive = False

    # Check if food has been eaten and spawn more
    if snake[0] == food:
        score += 1
        snake.append(snake[-1])
        food = [random.randint(0,4), random.randint(0,4)]

    # Render
    frame = [[0 for i in range(5)] for j in range(5)]

    for point in snake:
        frame[point[0]][point[1]] = 5

    frame[food[0]][food[1]] = 7

    for i in range(5):
        for j in range(5):
            display.set_pixel(j, i, frame[i][j])

    time += 0.1


for i in range(10):
    display.show(wrong)
    sleep(50)
    display.clear()
    sleep(50)

display.scroll("Score: " + str(score))
reset()
