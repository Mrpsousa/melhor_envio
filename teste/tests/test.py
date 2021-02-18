from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse


class TesteTest(TestCase):

    client = Client()

    def setUp(self):
        pass

    def test_sucess_get_workdata(self):
        response = self.client.get(reverse('work_data'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sucess_get_populate(self):
        response = self.client.get(reverse('populate'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sucess_get_generate_csv(self):
        response = self.client.get(reverse('generate_csv'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sucess_get_requests_by_consumer(self):
        response = self.client.get(reverse('requests_by_consumer'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sucess_get_requests_by_service(self):
        response = self.client.get(reverse('requests_by_service'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sucess_get_average_time(self):
        response = self.client.get(reverse('average_time'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #
    # Failed requests
    #

    def test_unsuccess_get_populate(self):
        response = self.client.get(reverse('populate'))
        self.assertEqual(response.status_code, status.
                         HTTP_500_INTERNAL_SERVER_ERROR)

    def test_unsuccess_get_generate_csv(self):
        response = self.client.get(reverse('generate_csv'))
        self.assertEqual(response.status_code, status.
                         HTTP_500_INTERNAL_SERVER_ERROR)

    def test_unsuccess_get_requests_by_consumer(self):
        response = self.client.get(reverse('requests_by_consumer'))
        self.assertEqual(response.status_code, status.
                         HTTP_500_INTERNAL_SERVER_ERROR)

    def test_unsuccess_get_requests_by_service(self):
        response = self.client.get(reverse('requests_by_service'))
        self.assertEqual(response.status_code, status.
                         HTTP_500_INTERNAL_SERVER_ERROR)

    def test_unsuccess_get_average_time(self):
        response = self.client.get(reverse('average_time'))
        self.assertEqual(response.status_code, status.
                         HTTP_500_INTERNAL_SERVER_ERROR)
