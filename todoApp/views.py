from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import todoForm

# Create your views here.
def index(request):
	todo_list = Todo.objects.order_by('id')
	form = todoForm()
	context = {'todo_list' : todo_list, 'form' : form}
	return render(request, "index.html", context)

@require_POST
def addTodo(request):
	form = todoForm(request.POST)
	if form.is_valid():
		todo_entry = Todo(text = request.POST['text'])
		todo_entry.save()
	return redirect('index') #redirect to same page to refresh

def markTodo(request, todo_id):
	todo = Todo.objects.get(id = todo_id)
	todo.complete = True
	todo.save()
	return redirect('index')

def deleteCompletedTodos(request):
	Todo.objects.filter(complete='True').delete()
	return redirect('index')

def deleteAllTodos(request):
	Todo.objects.all().delete()
	return redirect('index')

def unMark(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.complete = False
	todo.save()
	return redirect('index')
