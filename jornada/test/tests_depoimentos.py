from django.http import response
from rest_framework.test import APITestCase
from jornada.models import Reviews
from django.urls import reverse
from rest_framework import status

class ReviewsTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('reviews-list')
        self.review = Reviews.objects.create(name='name', review='review')
        self.review2 = Reviews.objects.create(name='name2', review='review2')
       
    def test_request_get_reviews_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_request_post_reviews_list(self):
        data = {
            'name': 'name3',
            'review': 'review3'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_request_delete_reviews_name2(self):
        response = self.client.delete('/reviews/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_request_put_reviews_name1_to_name4(self):
        data = {
            'name': 'name4',
            'review': 'review4'
        }
        response = self.client.put('/reviews/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_request_path_reviews_change_only_review(self):
        data = {
            'review': 'review5'
        }
        response = self.client.get('/reviews/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)