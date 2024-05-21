from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm

def home(request):
    todo_tasks = Tarea.objects.filter(status='To Do')
    doing_tasks = Tarea.objects.filter(status='Doing')
    done_tasks = Tarea.objects.filter(status='Done')
    context = {'todo_tasks': todo_tasks, 'doing_tasks': doing_tasks, 'done_tasks': done_tasks}
    return render(request, 'todo/home.html', context)

def agregar(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    context = {'form': form}
    return render(request, 'todo/agregar.html', context)

def eliminar(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('home')

from django.http import JsonResponse

def editar(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'todo/editar.html', {'form': form})

