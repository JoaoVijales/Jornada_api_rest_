from django.http import response
from rest_framework.test import APITestCase
from jornada.models import Destinos
from django.urls import reverse
from rest_framework import status

class DestinosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Destinos-list')
        self.depoimento = Destinos.objects.create(nome='Nome', preco='R$ 1200,00')
        self.depoimento2 = Destinos.objects.create(nome='Nome2', depoimento='depoimento2')
        
    def test_requisicao_get_destinos_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_post_destinos_list(self):
        data = {
            'nome': 'Nome3',
            'preco': 'R$ 2300,00'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_destinos_Nome2(self):
        response = self.client.delete('/destinos/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_destinos_Nome1_para_Nome4(self):
        data = {
            'nome': 'Nome4',
            'preco': '3000,00'
        }
        response = self.client.put('/destinos/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_path_destinos_Nome1_apenas_preco(self):
        data = {
            'preco': 'R$ 1700,00'
        }
        response = self.client.get('/destinos/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)