from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Comida
from .forms import Menuform
from django.http import HttpResponse
from django.template import RequestContext, Template
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def asignacion_menu(request):
    if request.method == "POST":
        form = Menuform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = Menuform()
    return render(request, 'pedidos/ingresar.html', {'form': form})