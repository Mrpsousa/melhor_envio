
from common.status_msgs import status_msg
import pandas as pd

#
#TODO retorno do dados em forma de API
#
def requests_by_consumer():
    '''
       Comentário relativo ao código 
    '''
    try:
        consumer_table = pd.read_csv('out.csv')
        consumers = consumer_table[['consumer_id', 'count']].groupby('consumer_id').sum()
        print(consumers) #apagar depois
        consumers.to_csv('relatorio_requests_by_consumer.csv')
        return status_msg.sucess_data_200("foi consumer")
    except Exception as err:
        return status_msg.error_500(err)
        

def requests_by_service():
    '''
       Comentário relativo ao código  
    '''
    try:    
        consumer_table = pd.read_csv('out.csv')
        consumers = consumer_table[['service_id', 'count']].groupby('service_id').sum()
        print(consumers) #apagar depois
        consumers.to_csv('relatorio_requests_by_service.csv')
        return status_msg.sucess_data_200("foi service")
    except Exception as err:
        return status_msg.error_500(err)


def average_time():
    '''
       Comentário relativo ao código 
    '''
    consumer_table = pd.read_csv('out.csv')
    proxy = consumer_table[['service_id', 'latency_proxy', 'latency_gateway', 'latency_request', 'count']].groupby('service_id').sum()
    
    i = 0
    for data in range(len(proxy.index)):
        print(f'{proxy.index[i]} : {proxy.iat[i,0] / proxy.iat[i,3]}')
        i += 1

    return status_msg.sucess_data_200("foi average_time")
