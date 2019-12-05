
import http_request
from constants import *
from django.core.cache import cache


LOGIN_API = '/createtoken'
LOGOUT_API = '/logout'
USER_FROM_TOKEN_API = '/userfromtoken'
NEW_USER_REGISTRATION_API = '/registeruser'
# CREATE_REGISTRY = '/createregistry'
GET_REGISTRIES_API = '/registries'
CHANGE_PASSWORD_API = '/changepassword'
ASSIGN_ITEM_API = '/assignitem'
UNASSIGN_ITEM_API = '/unassignitem'
CREATE_REGISTRY_API = '/createregistry'
GET_REGISTRY_DETAILS_API = '/getregistry'
ADD_ITEM_REGISTRY_API = '/additemtoregistry'
REMOVE_ITEM_REGISTRY_API = '/removeitemfromregistry'
GET_ITEMS_API = '/items'
GET_USERS_API = '/getusers'
FORGOT_PASSWORD_API = '/forgotpassword'
ADD_ITEM_TO_INVENTORY_API = "/additemtoinventory"
REMOVE_ITEM_FROM_INVENTORY_API = "/removeitemfrominventory"


def cacheResult(result):
    
    if 'token' in result and 'user_id' in result:
        token = result['token']
        user_id = result['user_id']

        cache.set(token, user_id, 30)

def getUserIdFromCache(request):

    if KEY_HTTP_TOKEN not in request.META:
       return return_error_response(CODE_FORBIDDEN, MESSAGE_NOT_LOGGED_IN);

    token = request.META[KEY_HTTP_TOKEN]
    user_id = cache.get(token)

    return user_id





def logout(user_id):

    params = {
      'user_id' : user_id
    }
    res = http_request.make_post_request(LOGOUT_API, params)
   
    return res


def fetch_user_details(token):

    params = {
      'token' : token
    }

    res = http_request.make_get_request(USER_FROM_TOKEN_API, params)

    return res

def new_user(username, password, email):

    params = {
    'username': username, 
    'password': password,
    'email': email
    }
    
    res = http_request.make_post_request(NEW_USER_REGISTRATION_API, params)
    
    return res

def get_registries(user_id):

    
    params = {
       'user_id': user_id
    }

    res = http_request.make_get_request(GET_REGISTRIES_API, params)

    return res

def change_password(user_id, password):

    params = {
       'user_id' : user_id,
       'password' : password
    }

    res = http_request.make_post_request(CHANGE_PASSWORD_API, params)
    
    return res

def get_user_details_from_request(request):
    if KEY_HTTP_TOKEN not in request.META:
       return return_error_response(CODE_FORBIDDEN, MESSAGE_NOT_LOGGED_IN);

    token = request.META[KEY_HTTP_TOKEN]
    user = fetch_user_details(token)
    
    return user

def return_error_response(code, message):
     error = {
        "error_code" : code,
        "error_message" :message
     }

     return error

def assign_item(user_id, registry_item_id):

    params = {
        'user_id': user_id,
        'registry_item_id': registry_item_id
    }
    res = http_request.make_post_request(ASSIGN_ITEM_API, params)
    
    return res

def unassign_item(user_id, registry_item_id):

    params = {
        'user_id': user_id,
        'registry_item_id': registry_item_id
    }
    res = http_request.make_post_request(UNASSIGN_ITEM_API, params)
    
    return res

def create_registry(user_id, name, public, allowed_users):

    params = {
         'user_id': user_id,
         'name': name,
         'public': public,
         'allowed_users': allowed_users
    }
    res = http_request.make_post_request(CREATE_REGISTRY_API, params)

    return res

def get_registry_details(user_id, registry_id):

    params = {
         'user_id': user_id,
         'registry_id': registry_id
    }
    res = http_request.make_get_request(GET_REGISTRY_DETAILS_API, params)

    return res

def add_item_to_registry(user_id, registry_id, item_id):

    params = {
        'user_id' : user_id,
        'registry_id': registry_id,
        'item_id': item_id
    }
    res = http_request.make_post_request(ADD_ITEM_REGISTRY_API, params)

    return res

def remove_item_from_registry(user_id, registry_id, item_id):

    params = {
        'user_id' : user_id,
        'registry_id': registry_id,
        'item_id': item_id
    }
    res = http_request.make_post_request(REMOVE_ITEM_REGISTRY_API, params)

    return res

def get_items():

    params = {}
    res = http_request.make_get_request(GET_ITEMS_API, params)

    return res

def get_users():

    params = {}
    res = http_request.make_get_request(GET_USERS_API, params)

    return res

def forgot_password(email):

    params = {'email': email}
    res = http_request.make_post_request(FORGOT_PASSWORD_API, params)

    return res

def add_item_to_inventory(params):

    res = http_request.make_post_request(ADD_ITEM_TO_INVENTORY_API, params)

    return res

def remove_item_from_inventory(params):

    res = http_request.make_post_request(REMOVE_ITEM_FROM_INVENTORY_API, params)

    return res


