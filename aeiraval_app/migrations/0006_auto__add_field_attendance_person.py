# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Attendance.person'
        db.add_column(u'aeiraval_app_attendance', 'person',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['aeiraval_app.Person']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Attendance.person'
        db.delete_column(u'aeiraval_app_attendance', 'person_id')


    models = {
        u'aeiraval_app.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Person']"}),
            'reportedType': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'reportedUser': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'aeiraval_app.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'expedient_year': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'referrer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Service']"})
        },
        u'aeiraval_app.document': {
            'Meta': {'object_name': 'Document'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Service']"}),
            'uploadDate': ('django.db.models.fields.DateField', [], {})
        },
        u'aeiraval_app.family': {
            'Meta': {'object_name': 'Family'},
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'father'", 'null': 'True', 'to': u"orm['aeiraval_app.Person']"}),
            'genogram': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mother': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mother'", 'null': 'True', 'to': u"orm['aeiraval_app.Person']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'aeiraval_app.fees': {
            'Meta': {'object_name': 'Fees'},
            'amountPaid': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'dateRegistered': ('django.db.models.fields.DateTimeField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'aeiraval_app.group': {
            'Meta': {'object_name': 'Group'},
            'courseName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'endDate': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'responsibleUser': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'startDate': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'aeiraval_app.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'dateOfBirth': ('django.db.models.fields.DateTimeField', [], {}),
            'documents': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Document']"}),
            'door': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Family']"}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'floor': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Group']"}),
            'hasPR': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hasPT': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'houseNumber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isParticipatingInPE': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mobilephone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nationalIdNumber': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {}),
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