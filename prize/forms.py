# Django imports.
from django import forms
from django.db.models import Q

# Third-party imports.
from localflavor.us.forms import USStateField, USStateSelect, USZipCodeField
from phonenumber_field.formfields import PhoneNumberField

# Local imports.
from prize.models import Address, Participant, Prize


class PrizeRetrievalForm(forms.Form):
    given_name = forms.CharField(max_length=50)
    family_name = forms.CharField(max_length=50)
    address1 = forms.CharField(max_length=150)
    address2 = forms.CharField(max_length=150, required=False)
    city = forms.CharField(max_length=50)
    state = USStateField(widget=USStateSelect)
    zip_code = USZipCodeField()
    email = forms.EmailField()
    phone = PhoneNumberField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()

        # Check if prizes exist.
        if not Prize.objects.filter(retrieved_ts__isnull=True).exists():
            raise forms.ValidationError('All prizes have been retrieved.')

        # Check if participant already exists.
        address = Address.objects.filter(
            address1=cleaned_data.get('address1'),
            city=cleaned_data.get('city'),
            state=cleaned_data.get('state'),
            zip_code=cleaned_data.get('zip_code')
        ).exists()

        if address:
            raise forms.ValidationError('You have already registered.')

        participant = Participant.objects.filter(
            Q(email=cleaned_data.get('email')) |
            Q(phone=cleaned_data.get('phone'))
        ).exists()

        if participant:
            raise forms.ValidationError('You have already registered.')


class PrizeRedemptionForm(forms.Form):
    email = forms.EmailField(required=False)
    phone = PhoneNumberField(required=False)
    code = forms.CharField(max_length=14)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()

        # User must specify either an email or a phone.
        if not cleaned_data.get('email') and not cleaned_data.get('phone'):
            raise forms.ValidationError('You must specify either an email or a phone.')

        # Check prize.
        try:
            participant = Participant.objects.get(
                Q(email=self.cleaned_data.get('email')) |
                Q(phone=self.cleaned_data.get('phone'))
            )
        except Participant.DoesNotExist:
            raise forms.ValidationError('A participant with that email or phone does not exist.')
        else:
            if participant.prize.code != self.cleaned_data.get('code'):
                raise forms.ValidationError('Incorrect code.')
            if participant.prize.is_redeemed:
                raise forms.ValidationError('Prize is already redeemed.')
