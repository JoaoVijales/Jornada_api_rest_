from django.http import response
from rest_framework.test import APITestCase
from jornada.models import Trips
from django.urls import reverse
from rest_framework import status

class TripsTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Trips-list')
        self.trip = Trips.objects.create(name='name', price='R$ 1200,00')
        self.trip2 = Trips.objects.create(name='name2', trip='1700,00')
        
    def test_request_get_Trips_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_request_post_Trips_list(self):
        data = {
            'name': 'name3',
            'price': 'R$ 2300,00'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_request_delete_Trips_name2(self):
        response = self.client.delete('/Trips/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_request_put_Trips_name1_to_name4(self):
        data = {
            'name': 'name4',
            'price': '3000,00'
        }
        response = self.client.put('/Trips/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_request_path_Trips_change_only_price(self):
        data = {
            'price': 'R$ 1700,00'
        }
        response = self.client.get('/Trips/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)