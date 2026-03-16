import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing test!")
    stdscr.addstr("\nChoose a difficulty! Easy (E), Intermediate (I), or Hard (H): ")
    stdscr.refresh()
    difficulty = stdscr.getkey()
    
    # Choose the test based on difficulty
    if difficulty == "E":
        with open("easy.txt", "r") as file:
            target_text = file.read().strip()
    elif difficulty == "I":
        with open("intermediate.txt", "r") as file:
            target_text = file.read().strip()
    elif difficulty == "H":
        with open("hard.txt", "r") as file:
            target_text = file.read().strip()
    else:
        print("Invalid choice")
        target_text = ""
    
    return target_text
        
    
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    # Display words per minute one line under the target text
    stdscr.addstr(4, 0, f"WPM: {wpm}")
    height, width = stdscr.getmaxyx()
    increment = 0
        
    # Display every character the user has typed directly on top of the target text
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        # Display the text as red if incorrect
        if char != correct_char:
            color = curses.color_pair(2)
        print("i: ", i)
        print("width: ", width)
        if i >= width:
            stdscr.addstr(1, i - (i-increment), char, color)
            increment = increment + 1
        else:
            stdscr.addstr(0, i, char, color)
    
def wpm_test(stdscr, target_text):
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
        
        # Check if user has finished. ONly ends if everything typed is correct.
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
    target = start_screen(stdscr)
    while True:
        # Call the test function
        wpm_test(stdscr, target)
        
        stdscr.addstr(2, 0, "Test Completed! Press any key to continue.")
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break
 
# Intitializes curses when called   
wrapper(main)
