import threading
import os
import requests
import json
import time
import csv
import io
import MySQLdb
import pytest


class reportingapi():
    data = {'grant_type': 'password', 'client_secret': '413elqq52m0wkgc8wcwc0k88g04go4k8o8oswk84wsg8o80s0k',
            'client_id': '9_4q0da7s42l8g040g4oscs8gw4k4cogcowoccgkc84kswksgcko',
            'username': 'carlos.attafuah@theexchangelab.com', 'password': 'Dem0Dem0'}
    r = requests.get('http://metalab.odin.tel-dev.io/oauth/v2/token?', params=data)
    authdata = "Bearer" + " " + str(r.json())
    if r.status_code == 200:
        print(authdata)
    else:
        print (" The authorization process failed" + " "  + str(r.status_code))
    headers = {"Connection": "keep-alive", "Authorization": authdata, "Content-Length": '102',
               "Content-Type": "application/json"}
    headers2 = {"Accept": "*/*", "Authorization": authdata}





