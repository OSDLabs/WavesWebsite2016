from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    if request.user.is_authenticated():
        username = request.user.username
        context = {
            "username" : username,
        }
    else:
        context = {}
    
    return render(request, "index.html",context)

def contact(request):
    if request.user.is_authenticated():
        username = request.user.username
        context = {
            "username" : username,
        }
    else:
        context = {}
    
    return render(request, "contact.html",context)


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response