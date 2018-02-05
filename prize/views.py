# Django imports.
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

# Local imports.
from prize.models import Address, Participant, Prize, PrizeType
from prize.forms import PrizeRedemptionForm, PrizeRetrievalForm


class PrizeRetrievalView(FormView):
    form_class = PrizeRetrievalForm
    template_name = 'prize/prize_retrieval.html'

    def form_valid(self, form):
        # Pick random prize.
        prize = Prize.objects.filter(retrieved_ts__isnull=True).order_by('?')[0]
        prize.retrieved_ts = now()
        prize.save()

        address = Address.objects.create(
            address1=form.cleaned_data.get('address1'),
            address2=form.cleaned_data.get('address2'),
            city=form.cleaned_data.get('city'),
            state=form.cleaned_data.get('state'),
            zip_code=form.cleaned_data.get('zip_code')
        )

        participant = Participant.objects.create(
            given_name=form.cleaned_data.get('given_name'),
            family_name=form.cleaned_data.get('family_name'),
            address=address,
            phone=form.cleaned_data.get('phone'),
            email=form.cleaned_data.get('email'),
            prize=prize
        )

        return super().form_valid(form)

    def get_success_url(self):
        form = self.get_form(self.get_form_class())
        participant = Participant.objects.get(email=form.data['email'])
        return reverse('prize-retrieve-success', kwargs={'code': participant.prize.code})


class PrizeRedemptionView(FormView):
    form_class = PrizeRedemptionForm
    template_name = 'prize/prize_redemption.html'
    success_url = reverse_lazy('prize-redeem-success')

    def form_valid(self, form):
        participant = Participant.objects.get(
            Q(email=form.cleaned_data.get('email')) |
            Q(phone=form.cleaned_data.get('phone'))
        )
        participant.prize.redeemed_ts = now()
        participant.prize.save()

        return super().form_valid(form)


class PrizeTypeListView(ListView):
    model = PrizeType
    template_name = 'prize/prize_type_list.html'


class PrizeReportView(TemplateView):
    template_name = 'prize/prize_report.html'
