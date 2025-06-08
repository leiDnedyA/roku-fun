import requests
import sys

from util.roku_connection import scan_roku_ip

DISNEY_PLUS_CHANNEL_ID = "291097"
# AOT_ID = "9c91ffa3-dc20-48bf-8bc5-692e37c76d88"
AOT_ID = "6d5b2a65-2bd7-4d87-8c07-c239bbcbd4f8"
AOT_ID = "04c97b72-504b-47f2-9c6f-fe13d9aea82f"
AOT_MEDIATYPE = "movie"

def keypress(roku_ip: str, key: str) -> bool:
    command_url = f'{roku_ip}keypress/{key}'
    r = requests.post(command_url)
    return r.ok

def launch_disney_plus(roku_ip: str) -> bool:
    # r = requests.post(f'{roku_ip}search/browse?title=the%20neverending%20story')
    r = requests.post(f'{roku_ip}launch/{DISNEY_PLUS_CHANNEL_ID}?contendId={AOT_ID}&MediaType={AOT_MEDIATYPE}')
    return r.ok


def launch_disney_plus_content(roku_ip: str, content_id: str) -> bool:
    r = requests.post(f'{roku_ip}launch/{DISNEY_PLUS_CHANNEL_ID}?contentId={content_id}&MediaType=series')
    return r.ok

def get_bitmaps(roku_ip: str):
    r = requests.get(f'{roku_ip}query/r2d2-bitmaps')
    print(r.text)

