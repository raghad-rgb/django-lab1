from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Trainee.objects.create(name=name, email=email)
        return redirect('trainee_list')
    return render(request, 'trainee/add_trainee.html')

def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == "POST":
        trainee.name = request.POST.get('name')
        trainee.email = request.POST.get('email')
        trainee.save()
        return redirect('trainee_list')
    return render(request, 'trainee/update_trainee.html', {'trainee': trainee})

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect('trainee_list')
