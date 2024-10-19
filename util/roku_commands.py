import requests

def keypress(roku_ip: str, key: str) -> bool:
    command_url = f'{roku_ip}keypress/{key}'
    r = requests.post(command_url)
    return r.ok
