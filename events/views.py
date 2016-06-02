from django.shortcuts import render

# Create your views here.
def Events(request):
	return render(request,"events.html")