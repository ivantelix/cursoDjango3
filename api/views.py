from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializerMeta

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializerMeta


@api_view(['POST'])
@parser_classes([JSONParser])
def example_post(request, format=None):
    return Response({'received data': request.data['name']})

@api_view(['GET'])
@parser_classes([JSONParser])
def example_get(request, format=None):
    return Response({'received data': request.query_params['name']})