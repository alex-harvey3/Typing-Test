import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()
    
def main(stdscr):
    # The pairing of a foreground color of green and background of black stored as 1
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # Foreground color red, background color black, stored as 2
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # Foreground color white, background color black, stored as 3
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    # Call the start screen function
    start_screen(stdscr)
 
# Intitializes curses when called   
wrapper(main)