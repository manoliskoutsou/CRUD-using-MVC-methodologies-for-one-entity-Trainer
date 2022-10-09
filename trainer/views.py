from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import Trainer
from .forms import TrainerForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect("home")
    else:
         form = UserCreationForm()
    return render(request,"trainer/signup.html", {"form" : form})

def login_user(request):
    errors = {}
    if request.method == "POST":
        uname = request.POST['username']
        pword = request.POST['password']
        user = authenticate(request, username = uname, password = pword)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            if not uname:
                errors["empty_username"] = "please enter username"
            elif not pword:
                errors["empty_password"] = "please enter password"
            elif user is None:
                errors["invalid"] = "username and password do not match"
    return render(request, "trainer/login.html", errors) 

def log_out(request):
    logout(request)
    return redirect("login_user")

def home(request):
    all_trainers_list = Trainer.objects.all()
    context = {'all_trainers_list' : all_trainers_list}
    return render(request, 'trainer/home.html', context)

def createTrainer(request):
    form = TrainerForm()
    if request.method == "POST":
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print(form.errors)
    context = {"form" : form}  
    return render(request, "trainer/create_trainer.html", context)

def edit_trainer(request, id):
    trainerToEdit = Trainer.objects.get(id = id)
    context = {"trainer" : trainerToEdit}
    if request.method == "POST":
        newFirstName = request.POST['trainer_firstName']
        newLastName = request.POST['trainer_lastName']
        newSubject = request.POST['trainer_subject']
        trainerToEdit.firstName = newFirstName
        trainerToEdit.lastname = newLastName
        trainerToEdit.subject =  newSubject
        trainerToEdit.save()
        return redirect("home")
    else:
         print("Try again")
    return render(request, "trainer/edit_trainer.html", context)

def delete_trainer(request, id):
    trainer = Trainer.objects.get(id = id)
    if request.method == "POST":
       trainer.delete()
       return redirect("home")
    else:
        context = {'trainer': trainer}
        return render(request, "trainer/delete_trainer.html", context)
        
    

