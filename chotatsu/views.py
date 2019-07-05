from django.shortcuts import render
from .models import Chotatsu

# Create your views here.

def chotatsu_list(request):
    context = {
        "qs":Chotatsu.objects.all()
    }
    return render(request, "chotatsu.html", context)
