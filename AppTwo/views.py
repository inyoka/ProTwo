from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'my_text':'My text inserted from views.py 2'}
    return render(request, 'AppTwo/index.html', context= my_dict)


def help(request):
    help_dict = {'my_help':'My help!!! text inserted from views.py'}
    return render(request, 'AppTwo/help.html', context= help_dict)
