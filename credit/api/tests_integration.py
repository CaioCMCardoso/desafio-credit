from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from api.models import Card
from api.urls import urlpatterns


class CardIntegrationTest(APITestCase):
    def setUp(self):
        self.card_data = {
            'exp_date': '2025-12-31',
            'holder': 'Caio Cardoso',
            'number': '4539578763621486',
            'cvv': '123',
        }

    def test_card_creation(self):
        url = reverse('credit-card')
        response = self.client.post(url, self.card_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        card = Card.objects.last()
        self.assertEqual(card.holder, self.card_data['holder'])
        self.assertEqual(card.number, '9b3e3f5aaf37ed8d70f33a105e77666b058fc18b2df2dbd9cfd32dd1e46bca7b')
        self.assertEqual(card.brand, 'visa')
        self.assertEqual(card.exp_date.strftime('%Y-%m-%d'), '2025-12-31')

    def test_card_creation_with_missing_data(self):
        url = reverse('credit-card')
        invalid_data = {'holder': 'Caio Cardoso', 'number': '4539578763621486'}
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_card_list(self):
        url = reverse('credit-card')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Card.objects.count())

    def test_card_retrieval(self):
        card = Card.objects.create(**self.card_data)
        url = reverse('credit-card-detail', args=[card.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['holder'], self.card_data['holder'])
        self.assertEqual(response.data['number'], '4539578763621486')
        self.assertEqual(response.data['brand'], 'visa')
        self.assertEqual(response.data['exp_date'], '2025-12-31')

    def test_card_update(self):
        card = Card.objects.create(**self.card_data)
        url = reverse('credit-card-detail', args=[card.id])
        updated_data = {'holder': 'Updated Holder', 'cvv': '321'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        card.refresh_from_db()
        self.assertEqual(card.holder, updated_data['holder'])
        self.assertEqual(card.cvv, '321')

    def test_card_deletion(self):
        card = Card.objects.create(**self.card_data)
        url = reverse('credit-card-detail', args=[card.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Card.objects.filter(id=card.id).count(), 0)