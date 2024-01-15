from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from todoApp.models import Todo
from rest_framework import status

@api_view(['GET'])
def getAllTodo(request):
    allTodo = Todo.objects.order_by('id')
    serializer = TodoSerializer(allTodo, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTodoItem(request):
    newTodo = Todo.objects.create(**request.data)
    serializer = TodoSerializer(data=newTodo)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH'])
def changeTodo(request, id):
    try:
        item = Todo.objects.get(pk=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    obj = {
        'complete' : not item.complete 
    }
    serializer = TodoSerializer(instance=item, data=obj, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteAllTodo(request):
    allTodo = Todo.objects.all()
    allTodo.delete()  
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
def deleteCompTodo(request):
    completeTodo = Todo.objects.filter(complete = True)
    completeTodo.delete()
    return Response(status=status.HTTP_200_OK)
    


