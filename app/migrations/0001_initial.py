# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('app_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 8, 0, 0), auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 8, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('app', ['Author'])

        # Adding model 'Comment'
        db.create_table('app_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 8, 0, 0), auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 8, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('app', ['Comment'])

        # Adding model 'Quote'
        db.create_table('app_quote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Author'])),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Comment'])),
            ('quote', self.gf('django.db.models.fields.TextField')()),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 8, 0, 0), auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 8, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('app', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('app_author')

        # Deleting model 'Comment'
        db.delete_table('app_comment')

        # Deleting model 'Quote'
        db.delete_table('app_quote')


    models = {
        'app.author': {
            'Meta': {'object_name': 'Author'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 8, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 8, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'app.comment': {
            'Meta': {'object_name': 'Comment'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 8, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 8, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'app.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Author']"}),
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Comment']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 8, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 8, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['app']