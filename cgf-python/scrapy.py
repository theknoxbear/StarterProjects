import re

import requests


def extractLinkRegEx(txt):
    tgs = re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1', re.IGNORECASE)

def printList(lst):
    for one in lst:
      print('Level 1 -> ' + 1)

r = requests.get('https://lifeisbalance.co.uk')
printList(extractLinkRegEx(r.text))
