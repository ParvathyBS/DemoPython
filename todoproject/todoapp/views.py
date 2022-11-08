from django.shortcuts import render, redirect

from .forms import taskform
from .models import Task


def home(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', )
        date = request.POST.get('date', )
        task = Task(name=name, priority=priority, date=date)
        task.save()

    return render(request, 'todo.html', {'t': task1})


def donetask(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def edittask(request, id):
    task = Task.objects.get(id=id)
    form = taskform(request.POST or None, request.FILES, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'task': task})
