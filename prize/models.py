# Django imports.
from django.db import models

# Third-party imports.
from localflavor.us.models import USStateField
from phonenumber_field.modelfields import PhoneNumberField


class PrizeType(models.Model):
    name = models.SlugField(max_length=150)
    display_name = models.CharField(max_length=150)
    value = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.display_name


class Prize(models.Model):
    prize_type = models.ForeignKey('prize.PrizeType', related_name='prizes', on_delete=models.CASCADE)
    code = models.CharField(max_length=14, unique=True)
    retrieved_ts = models.DateTimeField(blank=True, null=True)
    redeemed_ts = models.DateTimeField(blank=True, null=True)

    @property
    def is_retrieved(self):
        return self.retrieved_ts is not None

    @property
    def is_redeemed(self):
        return self.redeemed_ts is not None

    def __str__(self):
        return f'{self.code} ({self.prize_type.display_name})'


class Address(models.Model):
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = USStateField()
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        addresses = [self.address1]
        if self.address2:
            addresses.append(self.address2)
        address = ', '.join(addresses)
        return f'{address}, {self.city}, {self.state} {self.zip_code}'


class Bank(models.Model):
    name = models.CharField(max_length=150)
    branch_name = models.CharField(max_length=150)
    address = models.ForeignKey('prize.Address', related_name='banks', on_delete=models.CASCADE)
    phone = PhoneNumberField()

    def __str__(self):
        return f'{self.name}, {self.branch_name}'


class BankService(models.Model):
    name = models.SlugField(max_length=150)
    display_name = models.CharField(max_length=150)

    def __str__(self):
        return self.display_name


class Participant(models.Model):
    given_name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    address = models.ForeignKey('prize.Address', related_name='participants', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True)
    prize = models.ForeignKey('prize.Prize', related_name='participants', on_delete=models.CASCADE)
    bank_services = models.ManyToManyField('prize.BankService', related_name='participants')

    def __str__(self):
        return f'{self.given_name} {self.family_name}'
