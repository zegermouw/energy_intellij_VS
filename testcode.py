#!/usr/bin/env python3.8

import random
import pyautogui
import sys


# Generate 1000 random integers between 1 and 1000
random_integers = [random.randint(1, 1000) for i in range(10000000)]

# Sort the integers using the sorted() function
sorted_integers = sorted(random_integers)
print(sys.argv)
if(len(sys.argv) > 1 and sys.argv[1] == 'intellij'):
    pyautogui.hotkey('alt', 'f4')
else:
    pyautogui.hotkey('ctrl', 'w')
