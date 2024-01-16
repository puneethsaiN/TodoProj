from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import todoForm
import requests

# Create your views here.
base_url = "https://web-production-5c36a.up.railway.app"
def index(request):
	url = f'{base_url}/getAllTodo/'
	todo_list = requests.get(url)
	form = todoForm()
	context = {'todo_list' : todo_list.json(), 'form' : form}
	return render(request, "index.html", context)

@require_POST
def addTodo(request):
	url = f'{base_url}/addTodoItem/'
	form = todoForm(request.POST)
	if form.is_valid():
		obj = {
			'text' : request.POST['text']
		}
		requests.post(url, json=obj)
	return redirect('index') #redirect to same page to refresh

def toggleTodo(request, todo_id):
	url = f'{base_url}/changeTodo/{todo_id}/'
	requests.patch(url)
	return redirect('index')

# def deleteCompletedTodos(request):
# 	Todo.objects.filter(complete='True').delete()
# 	return redirect('index')

# def deleteAllTodos(request):
# 	Todo.objects.all().delete()
# 	return redirect('index')

def deleteAllTodo(request):
	url = f'{base_url}/deleteAllTodo/'
	requests.delete(url)
	return redirect('index')

def deleteCompTodo(request):
	url = f'{base_url}/deleteCompTodo/'
	requests.delete(url)
	return redirect('index')

