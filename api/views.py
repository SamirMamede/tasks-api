from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks.models import Tasks
from .serializers import TasksSerializers

@api_view(['GET'])
#@permission_classes([])
def getTasks(request):
    tasks = Tasks.objects.all()
    serializers = TasksSerializers(tasks, many=True)
    return Response(serializers.data)