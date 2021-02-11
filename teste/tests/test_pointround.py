from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from ..models import PointRound, Point, Round
from ..serializers import PointRoundSerializer
import json 


class PointTest(TestCase):

    client = Client()

    def setUp(self):
        self.point = Point.objects.create(name='Ponto Gama',
                                          lat=-32.12378352,
                                          lng=-33.63258352,
                                          map_id=1,
                                          x=765,
                                          y=346,
                                          teta=56)

        self.round = Round.objects.create(name='Ronda Nova',
                                               start_date='2050-02-02',
                                               start_time='02:02:02',
                                               frequency='semanalmente')

        self.valid_payload = {
            'action': 'inspeção',
            'thermal_photo': 'foto base 64',
            'visible_photo': 'foto base 64',
            'point': self.point.id,
            'round': self.round.id}

        self.invalid_payload = {
            'thermal_photo': 'foto base 64',
            'visible_photo': 'foto base 64',
            'point': self.point.id,
            'round': self.round.id}

        self.pointround_novo = PointRound.objects.create(action='passagem',
                                                         thermal_photo='foto base 64',
                                                         visible_photo='foto base 64',
                                                         point=self.point,
                                                         round=self.round)

    def test_create_valid_pointround(self):
        response = self.client.post(reverse('pointRounds'), data=json.dumps
                                    (self.valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_pointround(self):
        response = self.client.post(reverse('pointRounds'), data=json.dumps
                                    (self.invalid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_all_pointround(self):
        response = self.client.get(reverse('pointRounds'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_one_pointround(self):
        response = self.client.get(
            reverse('pointRound', kwargs={'pk': self.pointround_novo.pk}))
        point = PointRound.objects.get(pk=self.pointround_novo.pk)
        serializer = PointRoundSerializer(point)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_pointround(self):
        response = self.client.get(
            reverse('pointRound', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_pointround(self):
        response = self.client.put(
            reverse('pointRound', kwargs={'pk': self.pointround_novo.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_pointround(self):
        response = self.client.put(
            reverse('pointRound', kwargs={'pk': self.pointround_novo.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_pointround(self):
        response = self.client.delete(
            reverse('pointRound', kwargs={'pk': self.pointround_novo.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_pointround(self):
        response = self.client.delete(
            reverse('pointRound', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
