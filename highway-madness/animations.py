from microbit import *

###############################################################################

def levelStart(level):
    
    # Level screen
    display.scroll("L" + str(level))

    # Countdown 3...2...1
    numbers = ["05550:00050:00550:00050:05550",
               "05550:00050:05550:05000:05550",
               "00500:05500:00500:00500:05550"]

    for number in numbers:
        display.show(Image(number))
        sleep(500)
        display.clear()
        sleep(500)

    # Blinking flag
    flag = "50505:05050:50505:05050:50505"

    for i in range(10):
        display.show(Image(flag))
        sleep(25)
        display.clear()
        sleep(25)


###############################################################################

def crash():
    
    # Explosion
    frames = ["00000:00000:00900:00000:00000",
              "00000:09990:09590:09990:00000",
              "99999:95559:95559:95559:99999",
              "55555:55555:55555:55555:55555",
              "00000:05550:05550:05550:00000",
              "00000:00000:00500:00000:00000",
              "00000:00000:00000:00000:00000"]

    for frame in frames:
        display.show(Image(frame))
        sleep(100)


###############################################################################

def win():
    
    # Flag
    frames = ["50505:05050:50505:05050:50505",
              "05050:50505:05050:50505:05050"]

    for i in range(7):
        for frame in frames:
            display.show(Image(frame))
            sleep(200)


###############################################################################

def score(score):
    
    display.scroll("SCORE: " + str(score))


###############################################################################