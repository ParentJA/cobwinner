# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Bank.display_name'
        db.delete_column(u'prize_bank', 'display_name')

        # Adding field 'Bank.branch_name'
        db.add_column(u'prize_bank', 'branch_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Bank.phone_number'
        db.add_column(u'prize_bank', 'phone_number',
                      self.gf('localflavor.us.models.PhoneNumberField')(default='000-000-0000', max_length=20),
                      keep_default=False)


        # Changing field 'Bank.name'
        db.alter_column(u'prize_bank', 'name', self.gf('django.db.models.fields.CharField')(max_length=150))
        # Removing index on 'Bank', fields ['name']
        db.delete_index(u'prize_bank', ['name'])


    def backwards(self, orm):
        # Adding index on 'Bank', fields ['name']
        db.create_index(u'prize_bank', ['name'])

        # Adding field 'Bank.display_name'
        db.add_column(u'prize_bank', 'display_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Deleting field 'Bank.branch_name'
        db.delete_column(u'prize_bank', 'branch_name')

        # Deleting field 'Bank.phone_number'
        db.delete_column(u'prize_bank', 'phone_number')


        # Changing field 'Bank.name'
        db.alter_column(u'prize_bank', 'name', self.gf('django.db.models.fields.SlugField')(max_length=150))

    models = {
        u'prize.address': {
            'Meta': {'object_name': 'Address'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'prize.bank': {
            'Meta': {'object_name': 'Bank'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prize.Address']"}),
            'branch_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'})
        },
        u'prize.bankservice': {
            'Meta': {'object_name': 'BankService'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '150'})
        },
        u'prize.participant': {
            'Meta': {'object_name': 'Participant'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prize.Address']"}),
            'bank_services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prize.BankService']", 'null': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'prize': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prize.Prize']"})
        },
        u'prize.prize': {
            'Meta': {'object_name': 'Prize'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'date_redeemed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_retrieved': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prize.PrizeType']"})
        },
        u'prize.prizetype': {
            'Meta': {'object_name': 'PrizeType'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['prize']