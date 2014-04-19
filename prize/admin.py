from django.contrib import admin

from prize.models import Bank
from prize.models import BankService
from prize.models import Location
from prize.models import Participant
from prize.models import Prize
from prize.models import PrizeType


admin.site.register(Bank)
admin.site.register(BankService)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Prize)
admin.site.register(PrizeType)