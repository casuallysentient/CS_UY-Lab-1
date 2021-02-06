from karel.stanfordkarel import *


def main():
    """Each problem uses a different world (e.g. problem 1 uses world lab01_1.kwld, etc.), so it
    is necessary for us to change the world each time we move from problem to problem.

    Run the ContainerKarel configuration for problem 2.
    """

    fill_container()


def turn_right():  # function to turn right
    for x in range(3):
        turn_left()


def left_u_turn():  # function to make a u turn to the left
    turn_left()
    move()
    turn_left()
    put_beeper()


def right_u_turn():  # function to make a u turn to the right
    turn_right()
    move()
    turn_right()
    put_beeper()


def fill_line():  # places a beeper on every square until karel hits a wall
    while front_is_clear():
        move()
        put_beeper()


def fill_container():
    """
    Your solution to problem 2 goes here.
    Don't forget to remove the pass keyword!

    pre-condition: Assumes Karel starts at position (1, 1), facing north
    post-condition: Every open space within the container ((2, 5) to (6, 2)) has a beeper and Karel is standing at (2, 6) facing North.
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()  # by this point karel is standing right in front of the entrance to the container
    fill_line()  # fills out the first line of the container
    for x in range(2):  # for loop that fills out all the remaining lines in the container
        left_u_turn()
        fill_line()
        right_u_turn()
        fill_line()
    for x in range(2):  # for loop that moves karel to his final position back by the entrance
        turn_right()
        while front_is_clear():
            move()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
