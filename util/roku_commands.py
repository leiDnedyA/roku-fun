import requests

DISNEY_PLUS_CHANNEL_ID = "291097"

def keypress(roku_ip: str, key: str) -> bool:
    command_url = f'{roku_ip}keypress/{key}'
    r = requests.post(command_url)
    return r.ok

def launch_disney_plus(roku_ip: str) -> bool:
    r = requests.post(f'{roku_ip}launch/{DISNEY_PLUS_CHANNEL_ID}')
    return r.ok
