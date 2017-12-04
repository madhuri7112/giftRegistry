import requests
import json
from constants import *

SERVICES_DOMAIN_URL = "http://localhost:3000/giftAway"
SECRET_TOKEN = "secret_token"




def make_post_request(url, params):

    post_url = SERVICES_DOMAIN_URL + url
   
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'Authorization': SECRET_TOKEN
    }

    r = requests.post(post_url, data = json.dumps(params), headers = headers)

    return r.json()

def make_get_request(url, params):

    get_url = SERVICES_DOMAIN_URL + url

    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'Authorization': SECRET_TOKEN
    }

    r = requests.get(get_url, params = params, headers = headers)

    return r.json()

def get_security_key():

     return SECRET_TOKEN
