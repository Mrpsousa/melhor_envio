from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from ..models import Round, Point, PointRound, RoundName, RoundPointHistory
from ..serializers import RoundSerializer
import json 

url_base = 'http://127.0.0.1:8000/api/'


class RoundTest(TestCase):

    client = Client()

    def setUp(self):
        self.valid_payload = {'name': 'Ronda Válida',
                              'start_date': '2050-01-01',
                              'start_time': '02:01:01',
                              'frequency': 'diariamente'}

        self.invalid_payload = {'name': 123} 

        self.valid_r_round_payload = {'name': "Ronda Teste"} 

        self.valid_r_name_payload = {"name": "Ronda 01",
                                     "round_id": 1}

        self.invalid_r_name_payload = {'name': 123,
                                       'start_date' : None,
                                       'start_time' : None,
                                       'frequency' : None}

        self.round_novo = Round.objects.create(name='Ronda Nova',
                                               start_date='2050-02-02',
                                               start_time='02:02:02',
                                               frequency='semanalmente')

        self.point = Point.objects.create(name='Ponto teste',
                                          lat=-32.12378352,
                                          lng=-33.63258352,
                                          map_id=1,
                                          x=765,
                                          y=346,
                                          teta=56)

        self.round = Round.objects.create(name='Ronda teste',
                                               start_date='2050-02-02',
                                               start_time='02:02:02',
                                               frequency='semanalmente')

        PointRound.objects.create(action='passagem',
                                  thermal_photo='foto base 64',
                                  visible_photo='foto base 64',
                                  point=self.point,
                                  round=self.round)

        self.history = RoundPointHistory.objects.create(thermal_photo="foto base 64",
                                                        visible_photo="foto base 64",
                                                        point_name="Ponto B",
                                                        lat=11.312314,
                                                        lng=12.123143,
                                                        action="passagem",
                                                        start_date="2021-01-18",
                                                        start_time="02:02:02",
                                                        frequency="diaria",
                                                        round_id=1)

    def test_create_valid_full_round(self):
        response = self.client.post(reverse('rounds'), data=json.dumps
                                    (self.valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_valid_half_round(self):
        response = self.client.post(reverse('rounds'), data=json.dumps
                                    (self.valid_r_round_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_round(self):
        response = self.client.post(reverse('rounds'), data=json.dumps
                                    (self.invalid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_all_round(self):
        response = self.client.get(reverse('rounds'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_one_round(self):
        response = self.client.get(
            reverse('round', kwargs={'pk': self.round_novo.pk}))
        round = Round.objects.get(pk=self.round_novo.pk)
        serializer = RoundSerializer(round)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_round(self):
        response = self.client.get(
            reverse('round', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_round(self):
        response = self.client.put(
            reverse('round', kwargs={'pk': self.round_novo.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_round(self):
        response = self.client.put(
            reverse('round', kwargs={'pk': 30}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_delete_round(self):
        response = self.client.delete(
            reverse('round', kwargs={'pk': self.round_novo.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_round(self):
        response = self.client.delete(
            reverse('round', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_alreaday_deleted_round(self):
        self.client.delete(
            reverse('round', kwargs={'pk': self.round_novo.pk}))
        response = self.client.delete(
            reverse('round', kwargs={'pk': self.round_novo.pk}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# --------------------------------------------------------------------------------------

    def test_list_all_round_details(self):
        response = self.client.get(reverse('rounddetails',
                                           kwargs={'id': self.round.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bad_id_round_details(self):
        response = self.client.get(reverse('rounddetails',
                                           kwargs={'id': 0}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# --------------------------------------------------------------------------------------
    def test_list_empty_roundname(self):
        response = self.client.get(reverse('roundname'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_roundname(self):
        valid_r_name_payload = {'name': 'Ronda Válida', 'round_id': 1}
        response = self.client.post(reverse('roundname'), data=json.dumps
                                    (valid_r_name_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_roundname(self):
        response = self.client.post(reverse('roundname'), data=json.dumps
                                    (self.invalid_r_name_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_roundname(self):
        RoundName.objects.create(name='Ronda Nova', round_id=1)
        response = self.client.get(reverse('roundname'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_valid_roundname(self):
        RoundName.objects.create(name='Ronda Nova', round_id=1)
        response = self.client.post(reverse('roundname'), data=json.dumps
                                    (self.valid_r_name_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# --------------------------------------------------------------------------------------

    def test_get_history_valid(self):
        response = self.client.get(
            f'{url_base}rounds/history/{self.history.date}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_history_empty(self):
        response = self.client.get(f'{url_base}rounds/history/2000-01-01/')
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_history_invalid_date(self):
        response = self.client.get(f'{url_base}rounds/history/200-01-234/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
