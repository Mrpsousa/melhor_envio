from .api import (TesteViewSet)
from django.conf.urls import url

list_actions = {
    'get': 'list',
    'post': 'create'
}


single_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}


urlpatterns = [
    url(r'^tests/$', TesteViewSet.as_view(list_actions), name='testes'),
    url(r'^test/(?P<pk>\d+)/$', TesteViewSet.as_view(single_actions),
        name='teste'),       
]


