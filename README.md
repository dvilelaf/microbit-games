# BBC Micro::bit games and apps
A collection of simple games and apps for the bbc micro::bit.

- Highway madness: go fast on your motorbike and dodge all the other vehicles
- Snake: the classic snake game
- Mimic: a simon-like game
- Alien invasion: a space invaders-like game


# Installation
###Method A
Connect your micro::bit to the computer and use [mu editor](http://codewith.mu/) to flash the main scripts to the microbit.
###Method B
Use the provided installer scripts

1. Install the required utils

    ```
    sudo apt-get install python-pip
    pip install microfs
    ```

2. Add your *username* to the dialout group

    ```
    sudo usermod -a -G dialout <username>
    ```

3. Give execution permissions to installer script

    ```
    sudo chmod 764 install.sh
    ```

4. Connect your micro::bit to the computer, wait a few seconds and install a game by using the installer script

    ```
    ./install.sh <gamename>
    ```

