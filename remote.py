import argparse
import requests
from util.attack_on_titan import launch_attach_on_titan
from util.roku_connection import scan_roku_ip, test_connection
from util.roku_commands import keypress, launch_disney_plus

def run_remote(roku_ip: str):
    key_names = ['home', 'rev', 'fwd', 'play', 'select', 'left', 'right', 'down', 'up', 'back', 'instantreplay', 'info', 'backspace', 'search', 'enter']
    while True:
        next_command = input("Enter a command, or 'help' for a list of commands:")
        if next_command.lower() in key_names:
            keypress(roku_ip, next_command.lower())
        else:
            print(f"Valid commands: {','.join(key_names)}")

if __name__ == '__main__':

    roku_ip = scan_roku_ip()
    connection_successful = test_connection(roku_ip)

    if not connection_successful:
        print(f"ERROR: connection test failed. Attempted to connect to IP: \"{roku_ip}\"")

    run_remote(roku_ip)
