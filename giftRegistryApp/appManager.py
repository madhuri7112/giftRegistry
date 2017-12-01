
import http_request

KEY_HTTP_TOKEN = 'HTTP_AUTHORIZATION'

LOGIN_URL = '/createtoken'
LOGOUT_URL = '/logout'
USER_FROM_TOKEN_URL = '/userfromtoken'
NEW_USER_REGISTRATION_URL = '/registeruser'
CREATE_REGISTRY = '/createregistry'
GET_REGISTRIES_URL = '/registries'
CHANGE_PASSWORD_URL = '/changepassword'


def login(username, password):

    params = {
    'username': username, 
    'password': password
    }
    
    res = http_request.make_post_request(LOGIN_URL, params)
    
    return res

def logout(user_id):

    params = {
      'user_id' : user_id
    }
    res = http_request.make_post_request(LOGOUT_URL, params)
   
    return res


def fetch_user_details(token):

    params = {
      'token' : token
    }

    res = http_request.make_get_request(USER_FROM_TOKEN_URL, params)

    return res

def new_user(username, password, email):

    params = {
    'username': username, 
    'password': password,
    'email': email
    }
    
    res = http_request.make_post_request(NEW_USER_REGISTRATION_URL, params)
    
    return res

def get_registries(user_id):

    
    params = {
       'user_id': user_id
    }

    res = http_request.make_get_request(GET_REGISTRIES_URL, params)

    return res

def change_password(user_id, password):

    params = {
       'user_id' : user_id,
       'password' : password
    }

    res = http_request.make_post_request(CHANGE_PASSWORD_URL, params)
    
    return res

def get_user_details_from_request(request):
    if KEY_HTTP_TOKEN not in request.META:
       return_error_response(CODE_FORBIDDEN, MESSAGE_NOT_LOGGED_IN);
    token = request.META[KEY_HTTP_TOKEN]
    user = fetch_user_details(token)
    
    return user

def return_error_response(code, message):
     error = {
        "error_code" : code,
        "error_message" :message
     }

def create_registry():

    return