from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Consumer, Service
from .serializers import ConsumerSerializer, ServiceSerializer
from .services.teste_service import obj_list


class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class DbPopulateViewSet(APIView):
    def get(self, request):
        return obj_list()



