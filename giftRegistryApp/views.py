# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

import appManager

CODE_NOT_FOUND = 404
CODE_FORBIDDEN = 403

MESSAGE_MISSING_PARAMETERS = "Missing parameters"
MESSAGE_NOT_LOGGED_IN  = "You are not logged in."
KEY_HTTP_TOKEN = 'HTTP_AUTHORIZATION'

def index(request):
    a = {"abc":"24"};

    return  JsonResponse({'foo':'bar'});

@csrf_exempt
def login(request):
    parameters = json.loads(request.body)
    
    if 'username' not in parameters or 'password' not in parameters:
        appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)
    else :
       username = parameters['username']
       password = parameters['password']
       result = appManager.login(username, password)

    return JsonResponse(result)

@csrf_exempt
def logout(request):
    parameters = json.loads(request.body)
    if 'user_id' not in parameters:
        appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

    user_id = parameters['user_id']
    result = appManager.logout(user_id)

    return JsonResponse(result)

def create_registry_api(request):

    headers = request.headers
    token = headers['token']
    user_id = appManager.fetch_user_id(token)

@csrf_exempt
def register_new_user(request):

    parameters = json.loads(request.body)
    if 'username' not in parameters or 'password' not in parameters or 'email' not in parameters:
        appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

    username = parameters['username']
    password = parameters['password']
    email = parameters['email']

    result = appManager.new_user(username, password, email)

    return JsonResponse(result)

@csrf_exempt
def get_registries(request):

    # if KEY_HTTP_TOKEN not in request.META:
    #    appManager.return_error_response(CODE_FORBIDDEN, MESSAGE_NOT_LOGGED_IN);
    # #parameters = json.loads(request.body)
    # token = request.META[KEY_HTTP_TOKEN]
    # user = appManager.fetch_user_details(token)
    # user_id = user['id']

    user_details = appManager.get_user_details_from_request(request)

    #return {'user_id': user_id}
    result = appManager.get_registries(user_details['id'])

    return JsonResponse(result)

@csrf_exempt
def change_password(request):

    parameters = json.loads(request.body)
    user_details = appManager.get_user_details_from_request(request)
    password = parameters['password']

    result = appManager.change_password(user_details['id'], password)

    return JsonResponse(result)

def get_user_details(request):
    # if KEY_HTTP_TOKEN not in request.META:
    #    appManager.return_error_response(CODE_FORBIDDEN, MESSAGE_NOT_LOGGED_IN);

    # token = request.META[KEY_HTTP_TOKEN]
    # user = appManager.fetch_user_details(token)

    user_details = appManager.get_user_details_from_request(request)

    return JsonResponse(user_details)

   

