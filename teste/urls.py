from .api import (DbPopulateView, WorkDataViewSet, RequestsByConsumerView,
                  RequestsByServiceView, CsvServiceView, AverageTimeView)
from django.conf.urls import url
from django.urls import path


list_actions = {
    'get': 'list',
    # 'post': 'create'
}


single_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}


urlpatterns = [
    url(r'^workdata/$', WorkDataViewSet.as_view(list_actions),
        name='work_data'),
    path('db/populate/',  DbPopulateView.as_view(), name='populate'),
    path('to/csv/',  CsvServiceView.as_view(), name='generate_csv'),
    path('requests/consumer/',  RequestsByConsumerView.as_view(),
         name='requests_by_consumer'),
    path('requests/service/',  RequestsByServiceView.as_view(),
         name='requests_by_service'),
    path('average/time/',  AverageTimeView.as_view(), name='average_time'),

]
