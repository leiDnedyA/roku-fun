import argparse
import requests
from util.attack_on_titan import launch_attach_on_titan
from util.roku_connection import scan_roku_ip, test_connection
from util.roku_commands import keypress, launch_disney_plus, launch_disney_plus_content

def run_remote(roku_ip: str):
    key_names = ['home', 'rev', 'fwd', 'play', 'select', 'left', 'right', 'down', 'up', 'back', 'instantreplay', 'info', 'backspace', 'search', 'enter']
    while True:
        last_input = input("Enter a command, or 'help' for a list of commands:")
        split_input = last_input.split(' ')
        next_command = split_input[0]
        repeat_count = 1
        if len(split_input) > 1:
            repeat_count = split_input[1]
            try:
                repeat_count = int(repeat_count)
            except ValueError:
                print(f"Error: second argument must be an integer value.")
                repeat_count = 1
        for i in range(repeat_count if repeat_count else 1):
            if next_command.lower() in key_names:
                keypress(roku_ip, next_command)
            elif not keypress(roku_ip, next_command):
                print(f"Valid commands: {','.join(key_names)}")

if __name__ == '__main__':

    roku_ip = scan_roku_ip()
    connection_successful = test_connection(roku_ip)

    if not connection_successful:
        print(f"ERROR: connection test failed. Attempted to connect to IP: \"{roku_ip}\"")

    launch_disney_plus_content(roku_ip, '12271aec-bda3-4979-88a1-cb18cfd28901')
