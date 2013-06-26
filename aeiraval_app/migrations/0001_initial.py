# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Family'
        db.create_table(u'aeiraval_app_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('meeting_persons', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('father', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='father', null=True, to=orm['aeiraval_app.Person'])),
            ('mother', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mother', null=True, to=orm['aeiraval_app.Person'])),
            ('genogram', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'aeiraval_app', ['Family'])

        # Adding model 'Person'
        db.create_table(u'aeiraval_app_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('houseNumber', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('floor', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('door', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('postalCode', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mobilephone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('isParticipatingInPE', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('socialSecurityNumber', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('nationalIdNumber', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('dateOfBirth', self.gf('django.db.models.fields.DateTimeField')()),
            ('placeOfBirth', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hasPR', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hasPT', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('personType', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'aeiraval_app', ['Person'])

        # Adding model 'Contact'
        db.create_table(u'aeiraval_app_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('referrer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('expedient_year', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aeiraval_app.Service'])),
        ))
        db.send_create_signal(u'aeiraval_app', ['Contact'])

        # Adding model 'Service'
        db.create_table(u'aeiraval_app_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'aeiraval_app', ['Service'])


    def backwards(self, orm):
        # Deleting model 'Family'
        db.delete_table(u'aeiraval_app_family')

        # Deleting model 'Person'
        db.delete_table(u'aeiraval_app_person')

        # Deleting model 'Contact'
        db.delete_table(u'aeiraval_app_contact')

        # Deleting model 'Service'
        db.delete_table(u'aeiraval_app_service')


    models = {
        u'aeiraval_app.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'expedient_year': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'referrer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Service']"})
        },
        u'aeiraval_app.family': {
            'Meta': {'object_name': 'Family'},
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'father'", 'null': 'True', 'to': u"orm['aeiraval_app.Person']"}),
            'genogram': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting_persons': ('django.db.models.fields.TextField', [], {}),
            'mother': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mother'", 'null': 'True', 'to': u"orm['aeiraval_app.Person']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'aeiraval_app.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'dateOfBirth': ('django.db.models.fields.DateTimeField', [], {}),
            'door': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'floor': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'hasPR': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hasPT': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'houseNumber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isParticipatingInPE': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mobilephone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nationalIdNumber': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'personType': ('django.db.models.fields.IntegerField', [], {}),
            'placeOfBirth': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'postalCode': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'socialSecurityNumber': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'aeiraval_app.service': {
            'Meta': {'object_name': 'Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['aeiraval_app']