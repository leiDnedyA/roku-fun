import argparse
import requests
from util.roku_connection import scan_roku_ip, test_connection
from util.roku_commands import keypress

key_names = ['home', 'rev', 'fwd', 'play', 'select', 'left', 'right', 'down', 'up', 'back', 'instantreplay', 'info', 'backspace', 'search', 'enter']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A script for doing stuff with roku TV")
    roku_ip = scan_roku_ip()
    connection_successful = test_connection(roku_ip)

    if not connection_successful:
        print(f"ERROR: connection test failed. Attempted to connect to IP: \"{roku_ip}\"")

    while True:
        next_command = input("Enter a command, or 'help' for a list of commands:")
        if next_command.lower() in key_names:
            keypress(roku_ip, next_command.lower())
        else:
            print(f"Valid commands: {','.join(key_names)}")

    keypress_home_url = f'{roku_ip}keypress/home'
    print(test_connection(roku_ip))
    r = requests.post(keypress_home_url, data={})
    print(r)
