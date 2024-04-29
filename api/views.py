from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from tasks.models import Tasks
from .serializers import TasksSerializers
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='GET',
    operation_summary='Get all tasks',
    responses={
        200: 'Returns a list of all tasks'
    }
)
@api_view(['GET'])
def getTasks(request):
    task = Tasks.objects.all()
    serializer = TasksSerializers(task, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method='GET',
    operation_summary='Get a task by ID',
    responses={
        200: 'Returns task data',
        404: 'If the task is not found'
    }
)
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getTask(request, pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TasksSerializers(task)
    return Response(serializer.data)

@swagger_auto_schema(
    method='POST',
    operation_summary='Add a new task',
    request_body=TasksSerializers,
    responses={
        200: 'Returns data from the newly added task'
    }
)
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def addTasks(request):
    if request.method == 'POST':
        serializer = TasksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='PUT',
    operation_summary='Update a task by ID',
    responses={
        200: 'Returns the updated task data',
        400: 'If there are validation errors in the data provided',
        404: 'If the task is not found'
    }
)
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateTask(request, pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response({'detail': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = TasksSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='DELETE',
    operation_summary='Delete a task by ID',
    responses={
        204: 'If the task is successfully deleted',
        404: 'If the task is not found'
    }
)
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteTask(request, pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response({'detail': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        task.delete()
        return Response({'detail': 'Task deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)