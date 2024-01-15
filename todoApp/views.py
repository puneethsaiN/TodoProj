from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import todoForm
import requests

# Create your views here.
def index(request):
	url = 'http://127.0.0.1:8000/getAllTodo/'
	todo_list = requests.get(url)
	form = todoForm()
	context = {'todo_list' : todo_list.json(), 'form' : form}
	return render(request, "index.html", context)

@require_POST
def addTodo(request):
	url = 'http://127.0.0.1:8000/addTodoItem/'
	form = todoForm(request.POST)
	if form.is_valid():
		obj = {
			'text' : request.POST['text']
		}
		requests.post(url, json=obj)
	return redirect('index') #redirect to same page to refresh

def toggleTodo(request, todo_id):
	url = F'http://127.0.0.1:8000/changeTodo/{todo_id}/'
	requests.patch(url)
	return redirect('index')

# def deleteCompletedTodos(request):
# 	Todo.objects.filter(complete='True').delete()
# 	return redirect('index')

# def deleteAllTodos(request):
# 	Todo.objects.all().delete()
# 	return redirect('index')

def deleteAllTodo(request):
	url = F'http://127.0.0.1:8000/deleteAllTodo/'
	requests.delete(url)
	return redirect('index')

def deleteCompTodo(request):
	url = F'http://127.0.0.1:8000/deleteCompTodo/'
	requests.delete(url)
	return redirect('index')

