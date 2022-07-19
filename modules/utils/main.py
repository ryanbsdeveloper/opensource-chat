from datetime import datetime
import requests
from PIL import ImageFont
import matplotlib.font_manager as fm

def hour():
    now = datetime.now().strftime('%H:%M')
    return now


def access_internet():
    try:
        requests.get('https://www.google.com')
        return True
    except:
        return False


def width_label(texto):
    arial = ImageFont.truetype(fm.findfont(fm.FontProperties('Sans Serif')), 19)
    return arial.getsize_multiline(texto)[0] + 11
   
