import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()
    
def wpm_test(stdscr):
    target_text = "This is some test text!"
    # List to store what the user types
    current_text = []
    
    stdscr.clear()
    stdscr.addstr(target_text)
    
    while True:
        # Screen needs to be constantly clear to avoid writing words on top of each other
        stdscr.clear()
        stdscr.addstr(target_text)
        
        # Display every character the user has typed as green
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
        stdscr.refresh()
        
        
        # Store the key that the user types and add to list
        key = stdscr.getkey()
        
        # Exit the app if the escape key is pressed
        if ord(key) == 27:
            break
        
        
        # Ensure that backspace is handled correctly
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)
        
        

def main(stdscr):
    # The pairing of a foreground color of green and background of black stored as 1
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # Foreground color red, background color black, stored as 2
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # Foreground color white, background color black, stored as 3
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    # Call the start screen function
    start_screen(stdscr)
    # Call the test function
    wpm_test(stdscr)
 
# Intitializes curses when called   
wrapper(main)
