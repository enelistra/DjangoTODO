from django.shortcuts import redirect, render
from todoapp.forms import UpdateForm
from todoapp.models import todoform
from django .contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cfmpass=request.POST.get('cpass')
        if password == cfmpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already in use")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email id is already in use")
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return render(request,'login.html')
        else:
            messages.info(request,'password not matching')
            return render(request,'register.html')
    return render(request,'register.html')    

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.error(request,'invalid username or password')
            return render(request,'login.html')
    return render(request,'login.html')
        
def index(request):
    user=request.user
    tasks = todoform.objects.filter(user=user)
    if request.method=='POST':
        taskname=request.POST.get('taskname')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task = todoform(taskname=taskname,priority=priority,date=date,user=user)
        task.save()
        tasks = todoform.objects.filter(user=user)
    return render(request,'index.html',{'tasks':tasks})

def update_task(request, task_id):
    task = todoform.objects.get(id=task_id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = UpdateForm(instance=task)
    return render(request, 'update.html', {'form': form,'task':task})

def delete_task(request, task_id):
    task = todoform.objects.get(id=task_id)
    task.delete()
    return redirect('index')