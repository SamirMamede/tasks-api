from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks.models import Tasks
from .serializers import TasksSerializers

@api_view(['GET'])
def getTasks(request):
    task = Tasks.objects.all()
    serializer = TasksSerializers(task, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTasks(request):
    serializer = TasksSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)