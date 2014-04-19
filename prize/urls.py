from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('prize.views',
    url(r'^(?P<code>\w{2}\d{2}\w)$', 'prize_retrieval', name='prize_retrieval'),
    url(r'^redeem$', 'prize_redemption', name='prize_redemption'),
    url(r'^list$', 'prize_list', name='prize_list'),
    url(r'^report$', 'prize_report', name='prize_report'),
)