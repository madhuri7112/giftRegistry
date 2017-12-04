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
from constants import *



def index(request):
    a = {"abc":"24"};

    return  JsonResponse({'foo':'bar'});

@csrf_exempt
def login(request):
    parameters = json.loads(request.body)
    
    if 'username' not in parameters or 'password' not in parameters:
        return appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)
    else :
       username = parameters['username']
       password = parameters['password']
       result = appManager.login(username, password)

       appManager.cacheResult(result)

    return JsonResponse(result)

@csrf_exempt
def logout(request):
    parameters = json.loads(request.body)
    if 'user_id' not in parameters:
        return appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

    user_id = parameters['user_id']
    result = appManager.logout(user_id)

    return JsonResponse(result)

@csrf_exempt
def create_registry_api(request):

    parameters = json.loads(request.body)
    user_details = appManager.get_user_details_from_request(request)

    if 'name' not in parameters or 'public' not in parameters:
        return appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

    user_id = user_details['id']
    name = parameters['name']
    public = parameters['public']
    allowed_users = parameters['allowed_users']
 
    result = appManager.create_registry(user_id, name, public, allowed_users)

    return JsonResponse(result)


@csrf_exempt
def register_new_user(request):

    parameters = json.loads(request.body)
    if 'username' not in parameters or 'password' not in parameters or 'email' not in parameters:
        return appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

    username = parameters['username']
    password = parameters['password']
    email = parameters['email']

    result = appManager.new_user(username, password, email)

    return JsonResponse(result)

@csrf_exempt
def get_registries(request):

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
    
    user_details = appManager.get_user_details_from_request(request)

    return JsonResponse(user_details)

@csrf_exempt
def assign_item(request):

    user_details = appManager.get_user_details_from_request(request)

    parameters = json.loads(request.body)
    if 'registry_item_id' not in parameters:
        appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

    registry_item_id = parameters['registry_item_id']
    res = appManager.assign_item(user_details['id'], registry_item_id)

    return JsonResponse(res)

@csrf_exempt
def unassign_item(request):

    user_details = appManager.get_user_details_from_request(request)

    parameters = json.loads(request.body)
    if 'registry_item_id' not in parameters:
        appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

    registry_item_id = parameters['registry_item_id']
    res = appManager.unassign_item(user_details['id'], registry_item_id)

    return JsonResponse(res)


def get_registry_details(request):

    print("Looking for data in cache")
    user_id = appManager.getUserIdFromCache(request)

    if user_id is None:
       print("Did not find data in cache -- CACHE MISS")
       user_details = appManager.get_user_details_from_request(request)
       user_id = user_details['id']
    else:
       print("Found data in cache -- CACHE HIT") 
    # parameters = json.loads(request.body)

    # if 'registry_id' not in parameters:
    #     appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

    registry_id = request.GET['registry_id']
    res = appManager.get_registry_details(user_id, registry_id)

    return JsonResponse(res)

@csrf_exempt
def add_item_to_registry(request):
    user_details = appManager.get_user_details_from_request(request)

    parameters = json.loads(request.body)
    if 'registry_id' not in parameters or 'item_id' not in parameters:
        return appManager.return_error_response(CODE_NOT_FOUND, MESSAGE_MISSING_PARAMETERS)

    registry_id = parameters['registry_id']
    item_id = parameters['item_id']
    
    res = appManager.add_item_to_registry(user_details['id'], registry_id, item_id)

    return JsonResponse(res)

def get_items(request):

    res = appManager.get_items()

    return JsonResponse(res)

def get_users(request):

    res = appManager.get_users()

    return JsonResponse(res)

@csrf_exempt
def forgot_password(request):

    parameters = json.loads(request.body)
    email = parameters['email']
    res = appManager.forgot_password(email)

    return JsonResponse(res)

@csrf_exempt
def add_item_to_inventory(request):

    user_details = appManager.get_user_details_from_request(request)
    
    parameters = json.loads(request.body)
    parameters['user_id'] = user_details['id']
    res = appManager.add_item_to_inventory(parameters)

    return JsonResponse(res)

@csrf_exempt
def remove_item_from_inventory(request):

    user_details = appManager.get_user_details_from_request(request)

    parameters = json.loads(request.body)
    parameters['user_id'] = user_details['id']
    res = appManager.remove_item_from_inventory(parameters)

    return JsonResponse(res)


