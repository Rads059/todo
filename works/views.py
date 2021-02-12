from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):

    works = Works.objects.all() 

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context =  {'works':works, 'form':form}
    return render(request,'works/list.html', context)

def updateWorks(request, pk):

    works= Works.objects.get(id=pk)

    form = TaskForm(instance=works)
    context = {'form':form}

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=works)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'works/update_works.html', context)


def deleteWorks(request, pk):
    item = Works.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')


    context = {'item':item}
    return render(request, 'works/delete.html', context)