from django.http import response
from rest_framework.test import APITestCase
from jornada.models import Depoimentos
from django.urls import reverse
from rest_framework import status

class DepoimnetosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Depoimentos-list')
        self.depoimento = Depoimentos.objects.create(nome='Nome', depoimento='depoimento')
        self.depoimento2 = Depoimentos.objects.create(nome='Nome2', depoimento='depoimento2')
       
    def test_requisicao_get_depoimentos_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_post_depoimentos_list(self):
        data = {
            'nome': 'Nome3',
            'depoimento': 'depoimento3'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_depoimentos_Nome2(self):
        response = self.client.delete('/depoimentos/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_requisicao_put_depoimentos_Nome1_para_Nome4(self):
        data = {
            'nome': 'Nome4',
            'depoimento': 'depoimento4'
        }
        response = self.client.put('/depoimentos/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_path_depoimentos_Nome1_apenas_depoimento(self):
        data = {
            'depoimento': 'depoimento5'
        }
        response = self.client.get('/depoimentos/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)