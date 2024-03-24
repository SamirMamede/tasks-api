from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([])
def getTasks(request):
    user = {'name': 'Samir', 'age': 32, 'Task': 'Wash a car'}
    return Response(user)