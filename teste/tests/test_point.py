from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from ..models import Point
from ..serializers import PointSerializer
import json 


class PointTest(TestCase):

    client = Client()

    def setUp(self):
        self.valid_array = []
        self.invalid_array = []

        self.valid_payload = {
            'name': 'Ponto Alfa',
            'lat': -35.12378352,
            'lng': -34.34434554,
            'map_id': 1,
            'x': 123,
            'y': 432,
            'teta': 90}

        self.invalid_payload = {
            'name': 'Ponto Beta',
            'lat': -36.12378352,
            'lng': 'valor str',
            'map_id': 1,
            'x': 333,
            'y': 123,
            'teta': 80}

        self.valid_array.append(self.valid_payload)
        self.invalid_array.append(self.invalid_payload)

        self.point_novo = Point.objects.create(name='Ponto Gama',
                                               lat=-32.12378352,
                                               lng=-33.63258352,
                                               map_id=1,
                                               x=983,
                                               y=832,
                                               teta=42
                                               )

    def test_create_valid_point(self):
        response = self.client.post(reverse('points'), data=json.dumps
                                    (self.valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_point(self):
        response = self.client.post(reverse('points'), data=json.dumps
                                    (self.invalid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_all_point(self):
        response = self.client.get(reverse('points'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_one_point(self):
        response = self.client.get(
            reverse('point', kwargs={'pk': self.point_novo.pk}))
        point = Point.objects.get(pk=self.point_novo.pk)
        serializer = PointSerializer(point)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_point(self):
        response = self.client.get(
            reverse('point', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_point(self):
        response = self.client.put(
            reverse('point', kwargs={'pk': self.point_novo.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_point(self):
        response = self.client.put(
            reverse('point', kwargs={'pk': self.point_novo.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_point(self):
        response = self.client.delete(
            reverse('point', kwargs={'pk': self.point_novo.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_point(self):
        response = self.client.delete(
            reverse('point', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# ------------------------------------------------------------------------------
    def test_create_valid_setpoint(self):
        response = self.client.post(reverse('setpoints'), data=json.dumps
                                    (self.valid_array),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bad_setpoint(self):
        response = self.client.post(reverse('setpoints'), data=json.dumps
                                    (self.invalid_array),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
