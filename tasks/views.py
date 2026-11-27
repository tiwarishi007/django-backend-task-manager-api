from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET', 'POST'])
def get_tasks(request):

    if request.method == 'POST':
        serializer = TaskSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH', 'DELETE'])
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=204)
    
    serializer = TaskSerializer(
        task,
        data = request.data,
        partial = (request.method == 'PATCH')
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)

    return Response(serializer.errors, status=400)

