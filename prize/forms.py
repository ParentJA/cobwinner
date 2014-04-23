from django import forms
from django.db.models import Q

from localflavor.us.forms import USPhoneNumberField
from localflavor.us.forms import USStateField
from localflavor.us.forms import USStateSelect
from localflavor.us.forms import USZipCodeField

from prize.models import Address
from prize.models import Participant
from prize.models import Prize

import random

import re


ZIP_CODE_PATTERN = r'\d{5}(-\d{4})?'


class PrizeRetrievalForm(forms.Form):
    given_name = forms.CharField(max_length=50)
    family_name = forms.CharField(max_length=50)
    address_line_1 = forms.CharField(max_length=150)
    address_line_2 = forms.CharField(max_length=150)
    city = forms.CharField(max_length=50)
    state = USStateField(widget=USStateSelect)
    zip_code = USZipCodeField()
    email_address = forms.EmailField()
    phone_number = USPhoneNumberField()
    method = forms.CharField(widget=forms.HiddenInput(attrs={'value': 'email'}), initial='email')

    def __init__(self, *args, **kwargs):
        super(PrizeRetrievalForm, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(PrizeRetrievalForm, self).clean()

        if cleaned_data.get('zip_code') is None:
            raise forms.ValidationError('The zip code must be in one of these formats: ##### or #####-####.')

        return cleaned_data

    def participant_exists(self):
        return Participant.objects.filter(
            Q(email_address=self.cleaned_data.get('email_address')) |
            Q(phone_number=self.cleaned_data.get('phone_number'))
        ).exists()

    def retrieve_prize(self):
        cleaned_data = self.cleaned_data

        address, created = Address.objects.get_or_create(
            address_line_1=cleaned_data.get('address_line_1'),
            address_line_2=cleaned_data.get('address_line_2'),
            city=cleaned_data.get('city'),
            state=cleaned_data.get('state'),
            zip_code=cleaned_data.get('zip_code')
        )

        participant = Participant(
            given_name=cleaned_data.get('given_name'),
            family_name=cleaned_data.get('family_name'),
            address=address,
            phone_number=cleaned_data.get('phone_number'),
            email_address=cleaned_data.get('email_address')
        )

        # TODO: Make sure prizes still exist...
        prizes = Prize.objects.exclude(date_retrieved__isnull=False)
        prize = random.choice(prizes)
        prize.retrieve(participant)

        participant.save()


class PrizeRedemptionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        pass