import os


def open_stream():
    os.system('sudo systemctl start motion')
    return True

def close_stream():
    os.system('sudo systemctl stop motion')
    return False