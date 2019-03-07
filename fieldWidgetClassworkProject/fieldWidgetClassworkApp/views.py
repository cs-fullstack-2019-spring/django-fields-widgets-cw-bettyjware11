from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SuperHeroForm
from .models import SuperHero

# Create your views here.
def index(request):
    if(request.method=="POST"):
        form=SuperHeroForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
        else:
            print("ERROR!!!!!!!!!!")
    return render(request, "fieldwidgetClassworkApp/welcome.html", {"form": SuperHeroForm()})


def applicationInfo(request):
    #put all the user's information from the HTML page into this new form variable
    form = SuperHeroForm(request.POST)
    #create user entry into the variable superhero
    superhero = SuperHero.objects.get(name=request.user)

    if form.is_valid():

        form.save()
        return redirect("application")
    else:
        context = {"form":form, "errors":form.errors}
        return render(request, "fieldWidgetClassworkApp/application.html", context)
