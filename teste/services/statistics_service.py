
from common.status_msgs import status_msg
import pandas as pd


def requests_by_consumer():
    try:
        consumer_table = pd.read_csv('out.csv')
        consumers = consumer_table[['consumer_id', 'count']].groupby('consumer_id').sum()
        print(consumers) #apagar depois
        consumers.to_csv('relatorio_requests_by_consumer.csv')
        return status_msg.sucess_data_200("foi consumer")
    except Exception as err:
        return status_msg.error_500(err)
        

def requests_by_service():
    try:    
        consumer_table = pd.read_csv('out.csv')
        consumers = consumer_table[['service_id', 'count']].groupby('service_id').sum()
        print(consumers) #apagar depois
        consumers.to_csv('relatorio_requests_by_service.csv')
        return status_msg.sucess_data_200("foi service")
    except Exception as err:
        return status_msg.error_500(err)

#TODO

def average_time():
    consumer_table = pd.read_csv('out.csv')
    proxy = consumer_table[['service_id', 'latency_proxy']].groupby('service_id').sum()
    print(proxy)
    # new_proxy=proxy.mean(axis=0)
    # print(new_proxy)
    # consumers.to_csv('relatorio_requests_by_service.csv')
    return status_msg.sucess_data_200("foi service")
