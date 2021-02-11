from rest_framework import viewsets, status
from rest_framework.views import APIView
from datetime import datetime
import json
import re
from .models import Teste
from rest_framework.response import Response
from .serializers import TesteSerializer


class TesteViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Teste.objects.all()
    serializer_class = TesteSerializer

