from datetime import datetime

def hour():
    now = datetime.now().strftime('%H:%M')
    return now

