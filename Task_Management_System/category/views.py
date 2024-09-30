from django.shortcuts import render,redirect
from category.forms import CategoryForm

# Create your views here.


def Mycategory(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Mycategory')

    else:
        form = CategoryForm()
    return render(request,'add_category.html',{'form' : form})