from django import forms

from localflavor.us.forms import USPhoneNumberField
from localflavor.us.forms import USStateSelect
from localflavor.us.forms import USZipCodeField


class PrizeRetrievalForm(forms.Form):
    given_name = forms.CharField(max_length=50)
    family_name = forms.CharField(max_length=50)
    address_line_1 = forms.CharField(max_length=150)
    address_line_2 = forms.CharField(max_length=150)
    city = forms.CharField(max_length=50)
    state = USStateSelect()
    zip_code = USZipCodeField()
    email_address = forms.EmailField()
    phone_number = USPhoneNumberField()
    method_text = forms.BooleanField(widget=forms.HiddenInput)
    method_email = forms.BooleanField(widget=forms.HiddenInput)

    def __init__(self):
        pass


class PrizeRedemptionForm(forms.Form):
    def __init__(self):
        pass