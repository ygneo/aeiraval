# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document'
        db.create_table(u'aeiraval_app_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uploadDate', self.gf('django.db.models.fields.DateField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aeiraval_app.Service'])),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'aeiraval_app', ['Document'])

        # Adding model 'Group'
        db.create_table(u'aeiraval_app_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('startDate', self.gf('django.db.models.fields.DateTimeField')()),
            ('endDate', self.gf('django.db.models.fields.DateTimeField')()),
            ('courseName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('responsibleUser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'aeiraval_app', ['Group'])

        # Adding model 'Attendance'
        db.create_table(u'aeiraval_app_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('reportedType', self.gf('django.db.models.fields.IntegerField')()),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aeiraval_app.Group'])),
            ('reportedUser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'aeiraval_app', ['Attendance'])

        # Adding model 'Fees'
        db.create_table(u'aeiraval_app_fees', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dateRegistered', self.gf('django.db.models.fields.DateTimeField')()),
            ('amountPaid', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aeiraval_app.Group'])),
        ))
        db.send_create_signal(u'aeiraval_app', ['Fees'])

        # Adding field 'Person.family'
        db.add_column(u'aeiraval_app_person', 'family',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['aeiraval_app.Family']),
                      keep_default=False)

        # Adding field 'Person.group'
        db.add_column(u'aeiraval_app_person', 'group',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['aeiraval_app.Group']),
                      keep_default=False)

        # Adding field 'Person.attendance'
        db.add_column(u'aeiraval_app_person', 'attendance',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['aeiraval_app.Attendance']),
                      keep_default=False)

        # Adding field 'Person.documents'
        db.add_column(u'aeiraval_app_person', 'documents',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['aeiraval_app.Document']),
                      keep_default=False)

        # Adding field 'Person.notes'
        db.add_column(u'aeiraval_app_person', 'notes',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Document'
        db.delete_table(u'aeiraval_app_document')

        # Deleting model 'Group'
        db.delete_table(u'aeiraval_app_group')

        # Deleting model 'Attendance'
        db.delete_table(u'aeiraval_app_attendance')

        # Deleting model 'Fees'
        db.delete_table(u'aeiraval_app_fees')

        # Deleting field 'Person.family'
        db.delete_column(u'aeiraval_app_person', 'family_id')

        # Deleting field 'Person.group'
        db.delete_column(u'aeiraval_app_person', 'group_id')

        # Deleting field 'Person.attendance'
        db.delete_column(u'aeiraval_app_person', 'attendance_id')

        # Deleting field 'Person.documents'
        db.delete_column(u'aeiraval_app_person', 'documents_id')

        # Deleting field 'Person.notes'
        db.delete_column(u'aeiraval_app_person', 'notes')


    models = {
        u'aeiraval_app.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reportedType': ('django.db.models.fields.IntegerField', [], {}),
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
            'attendance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aeiraval_app.Attendance']"}),
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