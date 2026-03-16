import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()
    
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    # Display words per minute one line under the target text
    stdscr.addstr(1, 0, f"WPM: {wpm}")
        
    # Display every character the user has typed directly on top of the target text
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        # Display the text as red if incorrect
        if char != correct_char:
            color = curses.color_pair(2)
    
        stdscr.addstr(0, i, char, color)
    
def wpm_test(stdscr):
    target_text = "This is some test text!"
    # List to store what the user types
    current_text = []
    wpm = 0
    # Start tracking time
    start_time = time.time()
    stdscr.nodelay(True)
    
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        # Assuming an average word length of 5 characters
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        # Screen needs to be constantly clear to avoid writing words on top of each other
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        # CHeck if user has finished
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        
        try:
            # Store the key that the user types and add to list. Could cause an exception if the user doesn't press a key.
            key = stdscr.getkey()
        except:
            continue
        
        # Exit the app if the escape key is pressed
        if ord(key) == 27:
            break
        
        
        # Ensure that backspace is handled correctly
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
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
    while True:
        # Call the test function
        wpm_test(stdscr)
        
        stdscr.addstr(2, 0, "Test Completed! Press any key to continue.")
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break
 
# Intitializes curses when called   
wrapper(main)
