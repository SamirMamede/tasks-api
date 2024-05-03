from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from tasks.models import Users
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='GET',
    operation_summary='Get all users',
    responses={
        200: 'Returns a list of all users'
    }
)
@api_view(['GET'])
def getUsers(request):
    user = Users.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

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
            encrypted_password = make_password(serializer.validated_data['password'])
            serializer.validated_data['password'] = encrypted_password
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(
    method='DELETE',
    operation_summary='Delete a user by ID',
    responses={
        204: 'If the user is successfully deleted',
        404: 'If the user is not found'
    }
)
@api_view(['DELETE'])
def deleteUser(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        user.delete()
        return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)