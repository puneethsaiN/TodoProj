from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import todoForm
import requests

# Create your views here.
def index(request):
	url = f'{request.path}/getAllTodo/'
	todo_list = requests.get(url)
	form = todoForm()
	context = {'todo_list' : todo_list.json(), 'form' : form}
	return render(request, "index.html", context)

@require_POST
def addTodo(request):
	url = f'{request.path}/addTodoItem/'
	form = todoForm(request.POST)
	if form.is_valid():
		obj = {
			'text' : request.POST['text']
		}
		requests.post(url, json=obj)
	return redirect('index') #redirect to same page to refresh

def toggleTodo(request, todo_id):
	url = F'{request.path}/changeTodo/{todo_id}/'
	requests.patch(url)
	return redirect('index')

# def deleteCompletedTodos(request):
# 	Todo.objects.filter(complete='True').delete()
# 	return redirect('index')

# def deleteAllTodos(request):
# 	Todo.objects.all().delete()
# 	return redirect('index')

def deleteAllTodo(request):
	url = F'{request.path}/deleteAllTodo/'
	requests.delete(url)
	return redirect('index')

def deleteCompTodo(request):
	url = F'{request.path}/deleteCompTodo/'
	requests.delete(url)
	return redirect('index')

