# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PrizeType'
        db.create_table(u'prize_prizetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(max_length=150)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('value', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'prize', ['PrizeType'])

        # Adding model 'Prize'
        db.create_table(u'prize_prize', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prize.PrizeType'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date_retrieved', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_redeemed', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'prize', ['Prize'])

        # Adding model 'Address'
        db.create_table(u'prize_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('address_line_2', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'prize', ['Address'])

        # Adding model 'Bank'
        db.create_table(u'prize_bank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(max_length=150)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prize.Address'])),
        ))
        db.send_create_signal(u'prize', ['Bank'])

        # Adding model 'BankService'
        db.create_table(u'prize_bankservice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(max_length=150)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'prize', ['BankService'])

        # Adding model 'Participant'
        db.create_table(u'prize_participant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('given_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('family_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prize.Address'])),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone_number', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('prize', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prize.Prize'])),
        ))
        db.send_create_signal(u'prize', ['Participant'])

        # Adding M2M table for field bank_services on 'Participant'
        m2m_table_name = db.shorten_name(u'prize_participant_bank_services')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participant', models.ForeignKey(orm[u'prize.participant'], null=False)),
            ('bankservice', models.ForeignKey(orm[u'prize.bankservice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['participant_id', 'bankservice_id'])


    def backwards(self, orm):
        # Deleting model 'PrizeType'
        db.delete_table(u'prize_prizetype')

        # Deleting model 'Prize'
        db.delete_table(u'prize_prize')

        # Deleting model 'Address'
        db.delete_table(u'prize_address')

        # Deleting model 'Bank'
        db.delete_table(u'prize_bank')

        # Deleting model 'BankService'
        db.delete_table(u'prize_bankservice')

        # Deleting model 'Participant'
        db.delete_table(u'prize_participant')

        # Removing M2M table for field bank_services on 'Participant'
        db.delete_table(db.shorten_name(u'prize_participant_bank_services'))


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
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '150'})
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