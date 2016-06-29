from django.shortcuts import render,redirect
from help.models import *
from help.forms import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def HelpView(request):
    helpOut = []
    current_user = request.user
    helpList = HelpMessage.objects.all()
    for helps in helpList:
        if current_user==helps.user:
            helpOut.append(helps)


    if request.method=='POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                helpExchange = HelpMessage()
                helpExchange.message = form.cleaned_data['message']
                helpExchange.messageDateTime = timezone.now()
                helpOut.append(helpExchange)
                helpExchange.user = current_user
                helpExchange.save()


                return render(request, "help.html", {'helpList':helpOut, 'confirmation':"confirmation"})


    else:
        emptyForm = QueryForm()

        for helps in helpOut:
            if helps.reply == "Waiting.......":
                return render(request, "help.html", {'helpList':helpOut})
        return render(request, "help.html", {'helpList':helpOut, 'helpForm':emptyForm})
