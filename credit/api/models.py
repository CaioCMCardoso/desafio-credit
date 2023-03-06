from django.db import models
import uuid
import datetime
import calendar
import hashlib
from django.core.exceptions import ValidationError
from django.utils import timezone
from creditcard import CreditCard


def validate_exp_date(date):
    # Validar exp_date
    if date < datetime.date.today():
        raise ValueError('Invalid expiration date.')

def validate_holder(holder):
    if len(holder) < 2:
        raise ValidationError("Invalid holder's name.")
     
def validate_number(number):
    # Validar number
    if not CreditCard(number).is_valid():
        raise ValidationError('Invalid card number.')
        
def validate_cvv(cvv):
    # Validar cvv
    if cvv and len(cvv) not in [3, 4]:
        raise ValidationError("CVV must have 3 or 4 digits.")


class Card(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )
    exp_date = models.DateField(validators=[validate_exp_date])
    holder = models.CharField(validators=[validate_holder], max_length=255)
    number = models.CharField(validators=[validate_number], max_length=16)
    cvv = models.CharField(validators=[validate_cvv], max_length=4, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        self.brand = CreditCard(self.number).get_brand()
        last_day = calendar.monthrange(self.exp_date.year, self.exp_date.month)[1]
        self.exp_date = self.exp_date.replace(day=last_day)  # altera o dia da data de expiração para o último dia do mês
        # Criptografar o número
        self.number = hashlib.sha256(self.number.encode('utf-8')).hexdigest()

        super(Card, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Cards"