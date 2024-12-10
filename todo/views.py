from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Task

def tasklist(request):
    if request.method == 'POST':
        if 'add_task' in request.POST:
            # Dodawanie nowego zadania
            title = request.POST.get('title')
            if title:
                Task.objects.create(title=title)
        elif 'delete_task' in request.POST:
            # Usuwanie zadania
            task_id = request.POST.get('task_id')
            task = Task.objects.get(id=task_id)
            task.delete()
        elif 'complete_task' in request.POST:
            # Oznaczanie jako wykonane
            task_id = request.POST.get('task_id')
            task = Task.objects.get(id=task_id)
            task.completed = not task.completed
            task.save()
        return redirect('tasklist')

    tasks = Task.objects.all()
    return render(request, 'todo/tasklist.html', {'tasks': tasks})

