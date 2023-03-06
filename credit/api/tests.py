from django.test import TestCase
from django.utils import timezone
from api.models import Card
import hashlib
import calendar
import datetime

class CardModelTest(TestCase):
    def setUp(self):
        self.card_data = {
            'exp_date': timezone.now().date() + timezone.timedelta(days=365),
            'holder': 'Caio Cardoso',
            'number': '4539578763621486',
            'cvv': '123',
        }



    def test_card_creation(self):
        card = Card.objects.create(**self.card_data)
        self.assertEqual(card.holder, self.card_data['holder'])
        self.assertEqual(card.number, hashlib.sha256(self.card_data['number'].encode('utf-8')).hexdigest())
        self.assertEqual(card.brand, 'visa')
        last_day = calendar.monthrange(self.card_data['exp_date'].year, self.card_data['exp_date'].month)[1]
        expected_date_str = self.card_data['exp_date'].strftime('%Y-%m-') + str(last_day)
        expected_date = datetime.datetime.strptime(expected_date_str, '%Y-%m-%d').date()
        self.assertEqual(card.exp_date, expected_date)
        card = Card.objects.create(**self.card_data)
        self.assertEqual(card.holder, self.card_data['holder'])
        self.assertEqual(card.number, hashlib.sha256(self.card_data['number'].encode('utf-8')).hexdigest())
        self.assertEqual(card.brand, 'visa')
        last_day = calendar.monthrange(self.card_data['exp_date'].year, self.card_data['exp_date'].month)[1]
        expected_date = self.card_data['exp_date'].strftime('%Y-%m-') + str(last_day)
        self.assertEqual(card.exp_date.strftime('%Y-%m-%d'), expected_date)
    
    def test_card_number_encryption(self):
        card = Card.objects.create(**self.card_data)
        self.assertNotEqual(card.number, self.card_data['number'])
    
    def test_card_brand_detection(self):
        card = Card.objects.create(**self.card_data)
        self.assertEqual(card.brand, 'visa')
        card.number = '5555555555554444'
        card.save()
        self.assertEqual(card.brand, 'master')