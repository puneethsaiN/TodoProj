from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('addtodo', views.addTodo, name='addtodo'),
	path('marktodo/<todo_id>', views.markTodo, name='mark'),
	path('unmarktodo/<todo_id>', views.unMark, name='unmarktodo'),
	path('deletemarked', views.deleteCompletedTodos, name='deletemarked'),
	path('deletealltodos', views.deleteAllTodos, name='delalltodos'),
]