from time import sleep
from utils.settings import BASE_URL
import requests

RETRIES = 3

def api_request(method, path, **kwargs):
    url = f"{BASE_URL}{path}"

    for i in range (RETRIES):
        r = requests.request(method, url, timeout=5, **kwargs)
        if r.status_code < 500 or i == RETRIES -1:
            return r

        sleep(1 << i)
