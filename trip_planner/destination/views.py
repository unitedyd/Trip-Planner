
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CityForm

def index(request):
    return HttpResponse("Enter the trip destination here")

def get_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = CityForm()

    return render(request, 'city.html', {'form': form})
# Create your views here.
