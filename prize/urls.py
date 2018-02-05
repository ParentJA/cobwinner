# Django imports.
from django.urls import path, re_path
from django.views.generic.base import TemplateView

# Local imports.
from .views import PrizeTypeListView, PrizeRedemptionView, PrizeReportView, PrizeRetrievalView

urlpatterns = [
    path('prize-type/list/', PrizeTypeListView.as_view(), name='prize-type-list'),
    path('prize/redeem/success/',
         TemplateView.as_view(template_name='prize/prize_redemption_success.html'), name='prize-redeem-success'),
    re_path(r'prize/redeem/', PrizeRedemptionView.as_view(), name='prize-redeem'),
    path('prize/report/', PrizeReportView.as_view(), name='prize-report'),
    path('prize/retrieve/success/<str:code>/',
         TemplateView.as_view(template_name='prize/prize_retrieval_success.html'), name='prize-retrieve-success'),
    path('prize/retrieve/', PrizeRetrievalView.as_view(), name='prize-retrieve'),
]
