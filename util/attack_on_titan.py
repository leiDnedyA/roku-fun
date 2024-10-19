import time
from util.roku_commands import launch_disney_plus, keypress

DISNEY_PLUS_START_TIME_SECONDS = 20
KEY_DELAY_SECONDS = 1.5

def launch_attach_on_titan(roku_ip: str, debug=False):
    print("Launching attack on titan >:)")
    launch_disney_plus(roku_ip)
    time.sleep(DISNEY_PLUS_START_TIME_SECONDS) # It takes a while for disney plus to launch
    keypress(roku_ip, 'down')
    if debug: print(1)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(2)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(3)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(4)
    time.sleep(KEY_DELAY_SECONDS * 1.5)
    keypress(roku_ip, 'up')
    if debug: print(7)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(8)
    time.sleep(KEY_DELAY_SECONDS * 5) # Opens search page
    keypress(roku_ip, 'up')
    if debug: print(9)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(10)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(11)
    time.sleep(KEY_DELAY_SECONDS) # Opens search menu
    keypress(roku_ip, 'down')
    if debug: print(12)
    # return
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'down')
    if debug: print(14)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(15)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(16)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(17)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(18)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(19)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(20)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(21)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'up')
    if debug: print(22)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'up')
    if debug: print(23)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(24)
    # return
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(25)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(26)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(27)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(28)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(29)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(30)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(31)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(32)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'down')
    if debug: print(33)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(34)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'enter')
    if debug: print(35)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(36)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(37)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(38)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(39)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(40)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(41)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(42)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(43)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(44)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'down')
    if debug: print(45)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(46)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'left')
    if debug: print(47)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(48)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(49)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(50)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(51)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(52)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(53)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'right')
    if debug: print(54)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'up')
    if debug: print(55)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'enter')
    if debug: print(56)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(57)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'up')
    if debug: print(58)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'up')
    if debug: print(59)
    time.sleep(KEY_DELAY_SECONDS)
    keypress(roku_ip, 'select')
    if debug: print(60)
    time.sleep(KEY_DELAY_SECONDS * 6) # Loading the attack on titan info screen
    keypress(roku_ip, 'select')
    if debug: print(61)

