from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='POST',
    operation_summary='Register new user',
    request_body=UserSerializer,
    responses={
        200: 'User register successfully'
    }
)
@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)