#! /usr/bin/env python3
# stopwatch.yp - A simple stopwatch program.

import time
import pyperclip

# Display the program's instructions.
print(
    'Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.'
)
input()
print("Started.")
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        output = []
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        output_str = f"Lap #{str(lap_num).rjust(2, ' ')}: {str(total_time).rjust(6, ' ')} ({str(lap_time).rjust(6, ' ')})"
        print(output_str)
        output.append(output_str)
        lap_num += 1
        last_time = time.time()
        pyperclip.copy(output)
except KeyboardInterrupt:
    # Handl ethe Ctrl-C exception to keep its error message from displaying.
    print("\nDone.")
