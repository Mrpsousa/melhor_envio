from rest_framework import viewsets
from rest_framework.views import APIView
from .models import WorkData
from .utils.serializers import WorkDataSerializer
from .services.populate_service import populate, to_csv
from .services.statistics_service import (requests_by_service,
                                          requests_by_consumer,
                                          average_time)


class WorkDataViewSet(viewsets.ModelViewSet):
    queryset = WorkData.objects.all()
    serializer_class = WorkDataSerializer


class DbPopulateView(APIView):
    def get(self, request):
        return populate()


class CsvServiceView(APIView):
    def get(self, request):
        return to_csv()


class RequestsByServiceView(APIView):
    def get(self, request):
        return requests_by_service()


class RequestsByConsumerView(APIView):
    def get(self, request):
        return requests_by_consumer()


class AverageTimeView(APIView):
    def get(self, request):
        return average_time()