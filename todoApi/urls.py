from django.urls import path
from . import views as apiViews
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('getAllTodo/', apiViews.getAllTodo),
    path('addTodoItem/', apiViews.addTodoItem),
    path('changeTodo/<int:id>/', apiViews.changeTodo),
    path('deleteCompTodo/', apiViews.deleteCompTodo),
    path('deleteAllTodo/', apiViews.deleteAllTodo),
]

urlpatterns = format_suffix_patterns(urlpatterns)
