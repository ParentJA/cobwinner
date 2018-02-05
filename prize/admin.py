# Django imports.
from django.contrib import admin

# Local imports.
from prize.models import Address, Bank, BankService, Participant, Prize, PrizeType


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = ('address1', 'address2', 'city', 'state', 'zip_code',)
    list_display = ('address1', 'address2', 'city', 'state', 'zip_code',)


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    fields = ('name', 'branch_name', 'address', 'phone',)
    list_display = ('name', 'branch_name', 'address', 'phone',)


# @admin.register(BankService)
# class BankServiceAdmin(admin.ModelAdmin):
#     fields = ('name', 'display_name',)
#     list_display = ('prize_type', 'code', 'retrieved_ts', 'redeemed_ts',)


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    fields = ('given_name', 'family_name', 'address', 'email', 'phone', 'prize',)
    list_display = ('given_name', 'family_name', 'address', 'email', 'phone', 'prize',)


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    actions = ('unredeem',)
    fields = ('prize_type', 'code', 'retrieved_ts', 'redeemed_ts',)
    list_display = ('prize_type', 'code', 'retrieved_ts', 'redeemed_ts',)
    list_filter = ('retrieved_ts', 'redeemed_ts',)

    def unredeem(self, request, queryset):
        queryset.update(retrieved_ts=None, redeemed_ts=None, signature='')

    unredeem.short_description = 'Un-redeem prize'


@admin.register(PrizeType)
class PrizeTypeAdmin(admin.ModelAdmin):
    fields = ('name', 'display_name', 'value',)
    list_display = ('name', 'display_name', 'value',)
