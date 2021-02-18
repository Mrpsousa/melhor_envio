import json
import csv
from common.status_msgs import status_msg
from ..models import WorkData
from ..utils.queries_helper import chunked_queryset_iterator
from django.db import transaction


@transaction.atomic
def populate():
    '''
       Popula o banco de dados
    '''
    try:
        datas = open('logs.txt').readlines()
        for data in datas:
            data_new = json.loads(data)
            WorkData.objects.create(consumer_id=data_new[
                'authenticated_entity'][
                'consumer_id']['uuid'],
                service_id=data_new['service']['id'],
                latency_proxy=data_new['latencies'][
                'proxy'],
                latency_gateway=data_new['latencies'][
                'gateway'],
                latency_request=data_new['latencies'][
                'request'])

        return status_msg.sucess_data_200("Consumers and Services populated")
    except Exception as err:
        transaction.set_rollback(True)
        return status_msg.error_500(err)


def to_csv():
    '''
       Gera CSV
    '''
    try:
        writer = csv.writer(open("general_data.csv", 'w'))
        writer.writerow(['consumer_id', 'service_id', 'latency_proxy',
                         'latency_gateway', 'latency_request', 'count'])

        datas = WorkData.objects.prefetch_related()

        for data in chunked_queryset_iterator(datas, 20):
            writer.writerow([data.consumer_id,
                             data.service_id,
                             data.latency_proxy,
                             data.latency_gateway,
                             data.latency_request,
                             1])

        return status_msg.sucess_data_200("Generated CSV")
    except Exception as err:
        return status_msg.error_500(err)
