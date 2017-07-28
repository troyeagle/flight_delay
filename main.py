'''
Get flight delay data, in python3
'''

import re
from datetime import date, timedelta
import requests


def get_date(dt):
    ''' request variflight'''
    res = requests.get('http://www.variflight.com/schedule/SHA-XMN-9C8807.html?AE71649A58c77=&fdate=' + dt.strftime('%Y%m%d'))
    pattern = re.compile(r'<li class="age"><span>(.*?)</span>')
    match = pattern.search(res.text)
    old_pattern = re.compile(r'<div class="old_state">(.*?)</div>')
    old_match = old_pattern.search(res.text)
    print('9C8807', dt, old_match.group(1), match.group(1))

if __name__ == '__main__':
    LOOP = date(2017, 6, 1)
    for x in range(1, 50):
        try:
            get_date(LOOP)
        except AttributeError:
            pass
        LOOP += timedelta(days=1)
