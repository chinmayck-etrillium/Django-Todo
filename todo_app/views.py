from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.db import IntegrityError
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'todo_app/home.html')

def signupuser(request): 
    if request.method == "GET":
        return render(request,'todo_app/signup.html',{"form":UserCreationForm()})
    
    else:
        if request.POST['password1'] == request.POST['password2']: 
            try:   
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
                
            except IntegrityError:
                return render(request,'todo_app/signup.html',{"form":UserCreationForm() ,"error":"Username already exists!"})
        else:
            
            return render(request,'todo_app/signup.html',{"form":UserCreationForm() ,"error":"Passwords didn't match"})
        
def loginuser(request):
    if request.method == "GET":
        return render(request,'todo_app/login.html',{"form":AuthenticationForm()})
    
    else:
      user =  authenticate(request , username=request.POST['username'], password=request.POST['password'])
      if(not user):
          return render(request, 'todo_app/login.html', {"error":"Username or password didnot match! "})
      else:
          login(request,user)
          return redirect('home')
        
@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
@login_required   
def createtodos(request):
    if request.method == "GET":
        return render(request,'todo_app/create.html',{'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo=form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('home')
        except ValueError:
            return render(request,'todo_app/create.html',{{'error':'Bad data passed in!'}})
@login_required        
def showtodos(request):
    todos=Todo.objects.filter(user=request.user,datecompleted__isnull=True)
    return render(request,'todo_app/showtodo.html',{"todos":todos})
@login_required
def todo(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk, user=request.user)
    if(request.method=="GET"):
        form = TodoForm(instance=todo)
        return render(request, 'todo_app/todo.html', {"todo":todo,"form":form})
    else:
        try:
            form = TodoForm(request.POST,instance=todo)
            form.save()
            return redirect('showtodos')
        except ValueError:
            return render(request,'todo_app/todo.html',{{"form":form,'error':'Something went wrong!'}})
        
@login_required        
def completedtodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk, user=request.user)
    if(request.method=="POST"):
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('showtodos')
@login_required
def deletetodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk,user=request.user)
    if(request.method == "POST"):
        todo.delete()
        return redirect('showtodos')
@login_required    
def showcompletedtodos(request):
    todos=Todo.objects.filter(user=request.user,datecompleted__isnull=False).order_by('-datecompleted')
    return render(request,'todo_app/showcompletedtodos.html',{"todos":todos})