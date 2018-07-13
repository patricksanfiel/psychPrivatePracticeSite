from django.shortcuts import render, redirect
from .models import Therapist, Client
from .forms import ClientForm

# Create your views here.
def index(request):
    return render(request, 'clients/index.html')

def team(request):
    therapists = Therapist.objects.all()
    return render(request, 'clients/team.html', {"therapists":therapists})

def location(request):
    return render(request, 'clients/location.html')

def services(request):
    return render(request, 'clients/services.html')
    # return render(request, 'clients/services.html')

def new_appointment(request):
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save(commit=True)
        return redirect("/")
    return render(request, 'clients/form.html', {'form':form})
