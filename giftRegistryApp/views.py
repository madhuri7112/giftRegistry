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

MESSAGE_MISSING_PARAMETERS = "Missing parameters"

def index(request):
    a = {"abc":"24"};

    return  JsonResponse({'foo':'bar'});

@csrf_exempt
def login(request):
    parameters = json.loads(request.body)
    if 'username' not in parameters or 'password' not in parameters:
        return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)
    else :
       username = parameters['username']
       password = parameters['password']
       result = appManager.login(username, password)

    return JsonResponse(result)

@csrf_exempt
def logout(request):
    parameters = json.loads(request.body)
    if 'user_id' not in parameters:
        return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

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
        return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

    username = parameters['username']
    password = parameters['password']
    email = parameters['email']

    result = appManager.new_user(username, password, email)

    return JsonResponse(result)
    
def return_error_response(code, message):
     error = {
        "error_code" : code,
        "error_message" :message
     }
