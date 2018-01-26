from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def sign_in(request):
    # context = {}
    # context.update(csrf(request))
    if request.method == 'GET':
        return render(request, 'sign_in.html')
    elif request.method == 'POST':
        recv_json_data = json.loads(request.body)
        print(recv_json_data)
        return HttpResponseRedirect('/crm/index/')


def sign_up(request):
    return render(request, 'sign_up.html')
