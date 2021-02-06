from karel.stanfordkarel import *


def main():
    """Each problem uses a different world (e.g. problem 1 uses world lab01_1.kwld, etc.), so it
    is necessary for us to change the world each time we move from problem to problem.

    Run the TrackKarel configuration for problem 1.
    """

    travel_and_place_beeper()





def travel_and_place_beeper():
    """Instructs Karel to run a full lap around an 8x7 track. Runs on world lab01_1.kwld.

    pre-condition: Assumes Karel starts at position (1, 1), facing north
    post-condition: Karel is facing north, and ending in the same position as the pre-condition
    """
    pass


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
