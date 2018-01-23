from django.shortcuts import render
# from forms import SignInForm

def index(request):
    return render(request, 'index.html')


def login(request):
    # context = {}
    # if request.method == 'GET':
    #     form = SignInForm
    # if request.method == 'POST':
    #     form = SignInForm(request.POST)
    # context['form'] = form
    return render(request, 'sign_in.html')

def register(request):
    return render(request, 'sign_up.html')
