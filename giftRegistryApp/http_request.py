import requests
import json

SERVICES_DOMAIN_URL = "http://localhost:8000/giftAway"
SECRET_TOKEN = "secret_token"




def make_post_request(url, params):

    post_url = SERVICES_DOMAIN_URL + url
   
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

    r = requests.post(post_url, data = json.dumps(params), headers = headers)

    return r.json()

def make_get_request(url, params):

    get_url = SERVICES_DOMAIN_URL + url

    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

    r = requests.get(get_url, params = json.dumps(params), headers = headers)

    return r.json()

def get_security_key():

     return SECRET_TOKEN
