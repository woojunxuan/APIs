from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def sign_in(request):
    # context = {}
    # context.update(csrf(request))
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        print(request)
        recv_json_data = json.loads(request.body)
        print(recv_json_data)
    return render(request, 'sign_in.html')

def sign_up(request):
    return render(request, 'sign_up.html')
