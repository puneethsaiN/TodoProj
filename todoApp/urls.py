from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('addtodo', views.addTodo, name='addtodo'),
	path('toggletodo/<int:todo_id>', views.toggleTodo, name='toggle'),
	path('delAllTodo/', views.deleteAllTodo, name='deletemarked'),
	path('delCompTodo/', views.deleteCompTodo, name='delalltodos'),
]