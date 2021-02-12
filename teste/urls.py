from .api import ConsumerViewSet, DbPopulateViewSet, ServiceViewSet
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
    url(r'^consumers/$', ConsumerViewSet.as_view(list_actions), name='consumers'),
    url(r'^services/$', ServiceViewSet.as_view(list_actions), name='services'),  
    path('db/populate/',  DbPopulateViewSet.as_view(), name='calcs'),
    
]


