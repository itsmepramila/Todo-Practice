from django.shortcuts import render, HttpResponseRedirect
from todo_app.models import Todo

# Create your views here.

def todo_list(request):
    
    todos=Todo.objects.all()
    return render(
        request,
        "bootstrap/todo_list.html",
        {"todos":todos},
        )
    
def todo_create(request):
    if request.method == "GET":
        return render(request, "todo_create.html")
    else:
        Todo.objects.create(title=request.POST['title'])
        return HttpResponseRedirect("/")

def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return HttpResponseRedirect("/")

def todo_update(request, pk):
    if request.method == "GET":
        todo = Todo.objects.get(pk=pk)
        return render(request, "bootstrap/todo_update.html", {'todo': todo})
    else:  # POST
        todo = Todo.objects.get(pk=pk)
        todo.title = request.POST.get("title")  # Corrected accessing POST data
        todo.save()
        return HttpResponseRedirect("/")
    
