from datetime import date

from django.db import models

from localflavor.us.models import PhoneNumberField
from localflavor.us.models import USStateField

from south.modelsinspector import add_introspection_rules


add_introspection_rules([], [
    '^localflavor\.us\.models\.PhoneNumberField',
    '^localflavor\.us\.models\.USStateField'
])


class PrizeType(models.Model):
    name = models.SlugField(max_length=150)
    display_name = models.CharField(max_length=150)
    value = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return self.display_name


class Prize(models.Model):
    type = models.ForeignKey(PrizeType)
    code = models.CharField(max_length=20)
    date_retrieved = models.DateField(blank=True, null=True)
    date_redeemed = models.DateField(blank=True, null=True)
    signature = models.CharField(max_length=150)

    def is_retrieved(self):
        return self.date_retrieved is not None

    def is_redeemed(self):
        return self.date_redeemed is not None and self.signature is not None

    def retrieve(self, participant):
        participant.prize = self

        self.date_retrieved = date.today()

    def redeem(self, signature):
        self.signature = signature
        self.date_redeemed = date.today()

    def __unicode__(self):
        return '%s (%s)' % (self.code, self.type.display_name)


class Address(models.Model):
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = USStateField()
    zip_code = models.CharField(max_length=10)

    def __unicode__(self):
        address = [self.address_line_1]

        if self.address_line_2 is not None:
            address.append(self.address_line_2)

        address.append(self.city)

        return '%s, %s %s' % (', '.join(address), self.state, self.zip_code)


class Bank(models.Model):
    name = models.CharField(max_length=150)
    branch_name = models.CharField(max_length=150)
    address = models.ForeignKey(Address)
    phone_number = PhoneNumberField()

    def __unicode__(self):
        return '%s, %s' % (self.name, self.branch_name)


class BankService(models.Model):
    name = models.SlugField(max_length=150)
    display_name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.display_name


class Participant(models.Model):
    given_name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address)
    email_address = models.EmailField()
    phone_number = PhoneNumberField()
    prize = models.ForeignKey(Prize)
    bank_services = models.ManyToManyField(BankService, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.given_name, self.family_name)