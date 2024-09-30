from django.shortcuts import render,redirect
from task.models import TaskModel
from task.forms import TaskForm


# Create your views here.
def Mytask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Mytask')
    else:
        form = TaskForm()
    return render(request,'add_task.html',{'form':form})

def show_task(request):
    data = TaskModel.objects.all()
    return render(request,'show_task.html',{'data': data})

def edit_task(request,id):
    task =TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    return render(request,'add_task.html',{'form' : form})

def delete_task(request,id):
    task =TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_task')
    

