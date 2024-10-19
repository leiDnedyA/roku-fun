import argparse
from util.scan_roku_ip import scan_roku_ip

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A script for doing stuff with roku TV")
    ip = scan_roku_ip()
