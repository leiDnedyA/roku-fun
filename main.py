import argparse
import requests
from util.attack_on_titan import launch_attach_on_titan
from util.get_media_id import get_disney_plus_play_id
from util.roku_connection import scan_roku_ip, test_connection
from util.roku_commands import get_bitmaps, keypress, launch_disney_plus, launch_disney_plus_content

roku_ip = scan_roku_ip()
connection_successful = test_connection(roku_ip)
query = input("Search for a show: ")
disney_plus_id = get_disney_plus_play_id(query)
if disney_plus_id:
    launch_disney_plus_content(roku_ip, disney_plus_id)
