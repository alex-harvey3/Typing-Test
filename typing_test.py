import curses
from curses import wrapper

def main(stdscr):
    # The pairing of a foreground color of green and background of black stored as 1
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # Foreground color red, background color black, stored as 2
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # Foreground color white, background color black, stored as 3
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    
    stdscr.clear()
    stdscr.addstr("Hello World!")
    stdscr.refresh()
    stdscr.getkey()
 
# Intitializes curses when called   
wrapper(main)