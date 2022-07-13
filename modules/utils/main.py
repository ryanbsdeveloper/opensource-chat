from datetime import datetime
import requests

def hour():
    now = datetime.now().strftime('%H:%M')
    return now

def access_internet():
    try:
        requests.get('https://www.google.com')
        return True
    except:
        return False

