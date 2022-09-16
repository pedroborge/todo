from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import HttpResponse

from .models import Task

from .forms import TaskForm

# Create your views here.
def helloWorld(request):
    return HttpResponse("Hello World! porra")

def tasklist(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render( request, "tasks/list.html", {"tasks": tasks})

def newTask(request):
    if request.Method == "POST":
        form = Task.Form(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.done = "doing"
            task.save()
            return redirect("/")

    else:
        form = TaskForm()   
        return render( request, "tasks/addtask.html", {"form":form})

def editTask(request, id):
    task = get_object_or_404(Task, pk = id)
    form = TaskForm(instance = task)

    if(request.method == "POST"):
        return False
    else:
        return render(request, "tasks/edittask.html", {"form": form, "task": task})

def yourname(request, name):
    return render( request, "tasks/yourname.html", {'name':name})

def taskView(request, id):
    task = get_object_or_404(Task, pk = id)
    return render( request, "tasks/task.html", {"task":task})

