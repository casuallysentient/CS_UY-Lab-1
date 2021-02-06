from karel.stanfordkarel import *


def main():
    """Each problem uses a different world (e.g. problem 1 uses world lab01_1.kwld, etc.), so it
    is necessary for us to change the world each time we move from problem to problem.

    Run the TrackKarel configuration for problem 1.
    """
    run_lap()


def run_lap():
    """Instructs Karel to run a full lap around an 8x7 track. Runs on world lab01_1.kwld.

    pre-condition: Assumes Karel starts at position (1, 1), facing north
    post-condition: Karel is facing north, and ending in the same position as the pre-condition
    """
    for x in range(3):
        turn_left()  # performs one right turn by making a for loop of turning left 3 times
    for x in range(4):  # for loop that executes the action of moving forward and turning left four times
        while front_is_clear():
            move()
        turn_left()  # executes a left turn after karel has reached a wall, opening up a new path and allowing the for loop to run again
    turn_left()  # final left turn to ensure karel is facing the right way


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
