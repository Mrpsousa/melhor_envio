
from common.status_msgs import status_msg
import pandas as pd
import csv

#
# TODO Pandoc - gerador de documentação
#


def requests_by_consumer():
    '''
       Doc string relativo ao código
    '''
    try:
        consumer_table = pd.read_csv('general_data.csv')
        consumers = consumer_table[['consumer_id', 'count']].groupby(
            'consumer_id').sum()
        consumers.to_csv('relatorio_requests_by_consumer.csv')
        return status_msg.sucess_data_200("Generated Requests by Consumer")
    except Exception as err:
        return status_msg.error_500(err)


def requests_by_service():
    '''
       Doc string relativo ao código
    '''
    try:
        consumer_table = pd.read_csv('general_data.csv')
        consumers = consumer_table[['service_id', 'count']].groupby(
            'service_id').sum()
        consumers.to_csv('relatorio_requests_by_service.csv')
        return status_msg.sucess_data_200("Generated Requests by Service")
    except Exception as err:
        return status_msg.error_500(err)


def average_time():
    '''
       Doc string relativo ao código
    '''
    try:
        writer = csv.writer(open("relatorio_average.csv", 'w'))
        writer.writerow(['service_id',
                         'average_latency_proxy',
                         'average_latency_gateway',
                         'average_latency_request'])

        consumer_table = pd.read_csv('general_data.csv')
        data_sum = consumer_table[['service_id', 'latency_proxy',
                                   'latency_gateway',
                                   'latency_request', 'count']].groupby(
            'service_id').sum()

        i = 0
        for data in range(len(data_sum.index)):
            writer.writerow([data_sum.index[i],
                             data_sum.iat[i, 0] / data_sum.iat[i, 3],
                             data_sum.iat[i, 1] / data_sum.iat[i, 3],
                             data_sum.iat[i, 2] / data_sum.iat[i, 3]
                             ])

            i += 1
        return status_msg.sucess_data_200("Generated Average")
    except Exception as err:
        return status_msg.error_500(err)
