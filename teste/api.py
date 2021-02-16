from rest_framework import viewsets
from rest_framework.views import APIView
from .models import WorkData
from .utils.serializers import WorkDataSerializer
from .services.populate_service import populate, to_csv
from .services.statistics_service import (requests_by_service,
                                          requests_by_consumer,
                                          average_time)


class WorkDataViewSet(viewsets.ModelViewSet):
    '''
        Retorna os dados gerais salvos no banco
    '''
    queryset = WorkData.objects.all()
    serializer_class = WorkDataSerializer


class DbPopulateView(APIView):
    '''
        Popula o banco com dados no .txt
    '''
    def get(self, request):
        return populate()


class CsvServiceView(APIView):
    '''
       Gera CSV com os dados do banco
    '''
    def get(self, request):
        return to_csv()


class RequestsByServiceView(APIView):
    '''
       Retorna quantidade de Requisições por consumidor;
    '''
    def get(self, request):
        return requests_by_service()


class RequestsByConsumerView(APIView):
    '''
        Retorna quantidade de Requisições por serviço;
    '''
    def get(self, request):
        return requests_by_consumer()


class AverageTimeView(APIView):
    '''
    retrona Tempo médio de request, proxy e gateway por serviço.
    '''
    def get(self, request):
        return average_time()
