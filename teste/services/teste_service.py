import json
from common.status_msgs import status_msg
from ..models import Consumer, Service


def obj_list():
    datas = open('logs.txt').readlines()
    for data in datas:
        data_new = json.loads(data)
        Consumer.objects.create(consumer_id=data_new['authenticated_entity'][
            'consumer_id']['uuid'])
        Service.objects.create(service_id=data_new['service']['id'],
                               latency_proxy=data_new['latencies']['proxy'],
                               latency_gateway=data_new['latencies'][
                                   'gateway'],
                               latency_request=data_new['latencies'][
                                   'request'])

    return status_msg.sucess_data_200("Consumers and Services populated")


