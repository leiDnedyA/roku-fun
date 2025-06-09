import socket
import requests

def scan_roku_ip() -> str:
    request_host =  "239.255.255.250"
    payload_string_unicode = f"""M-SEARCH * HTTP/1.1\r\nHost: {request_host}\r\nMan: "ssdp:discover"\r\nST: roku:ecp\r\n\r\n"""
    payload_bytestring = payload_string_unicode.encode()
    port = 1900

    # Scan network for roku
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(payload_bytestring, (request_host, port))
    response, _ = s.recvfrom(4096)
    s.close()
    response_decoded = response.decode()

    if (response_decoded.split()[2] != 'OK'):
        raise Exception("No roku device found on network :(")

    for line in response_decoded.split('\n'):
        if line.startswith('LOCATION'):
            device_ip = line.split(': ')[1][:-1] # removes the newline char from the end
            # print(device_ip)
            return device_ip
    
    raise Exception("There was a problem finding the roku device on your network.")

def test_connection(roku_ip: str) -> bool:
    ping_url = f'{roku_ip}query/device-info'
    r = requests.get(ping_url)
    return r.ok


