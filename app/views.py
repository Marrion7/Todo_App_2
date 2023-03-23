from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models
from . import forms

# Create your views here.


def ListlViews(request):
    context = {
        'title': 'title'
    }
    context['tasks'] = models.Task.objects.all()
    return render(request, 'base/tasks_view.html', context)



def Detailview(request, id):
  
    tasks = models.Task.objects.get(id=id)
    context = {
        'tasks':tasks
    }
    return render(request, 'base/tasks_detail.html', context)



def Createview(request):
   if request.method == 'POST':
       title = request.POST.get('title')
       description = request.POST.get('textarea')
    
       tasks = models.Task.objects.create(user=request.user, title=title, description=description)
       tasks.save()
       return redirect('tasks')
   context = {} 
   return render(request,'base/task_create.html', context)



def Updateview(request, pk):
    tasks = models.Task.objects.get(id=pk)
    form = forms.TaskEdit(instance=tasks)
    
    if request.method == 'POST':
       form = forms.TaskEdit(request.POST, instance=tasks )
       if form.is_valid:
           form.save()
           return redirect('tasks')
    
    context = {
        'tasks':tasks, 'form':form
    }
    return render(request,'base/task_update.html', context)

def Delete(request, pk):
    tasks = models.Task.objects.get(id=pk)
    
    if request.method == 'POST':
       tasks.delete()
       return redirect('tasks')
    
    context = {'tasks':tasks}
    return render(request, 'base/task_delete.html', context)
    pass