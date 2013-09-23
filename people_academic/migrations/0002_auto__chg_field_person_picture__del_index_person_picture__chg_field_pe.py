# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Person.picture' to match new field type.
        db.rename_column(u'people_academic_person', 'picture_id', 'picture')
        # Changing field 'Person.picture'
        db.alter_column(u'people_academic_person', 'picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))
        # Removing index on 'Person', fields ['picture']
        db.delete_index(u'people_academic_person', ['picture_id'])


        # Renaming column for 'Person.resume' to match new field type.
        db.rename_column(u'people_academic_person', 'resume_id', 'resume')
        # Changing field 'Person.resume'
        db.alter_column(u'people_academic_person', 'resume', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))
        # Removing index on 'Person', fields ['resume']
        db.delete_index(u'people_academic_person', ['resume_id'])


    def backwards(self, orm):
        # Adding index on 'Person', fields ['resume']
        db.create_index(u'people_academic_person', ['resume_id'])

        # Adding index on 'Person', fields ['picture']
        db.create_index(u'people_academic_person', ['picture_id'])


        # Renaming column for 'Person.picture' to match new field type.
        db.rename_column(u'people_academic_person', 'picture', 'picture_id')
        # Changing field 'Person.picture'
        db.alter_column(u'people_academic_person', 'picture_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['filer.Image']))

        # Renaming column for 'Person.resume' to match new field type.
        db.rename_column(u'people_academic_person', 'resume', 'resume_id')
        # Changing field 'Person.resume'
        db.alter_column(u'people_academic_person', 'resume_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['filer.File']))

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'people_academic.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'people_academic.grouptranslation': {
            'Meta': {'object_name': 'GroupTranslation'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'people_academic.lab': {
            'Meta': {'object_name': 'Lab'},
            'homepage': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'people_academic.labtranslation': {
            'Meta': {'object_name': 'LabTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Lab']"}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'people_academic.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.LinkType']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Person']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'people_academic.linktype': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'LinkType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'people_academic.linktypetranslation': {
            'Meta': {'object_name': 'LinkTypeTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'link_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.LinkType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'people_academic.person': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Person'},
            'chosen_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group'", 'to': u"orm['people_academic.Group']"}),
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Lab']", 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'non_roman_first_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'non_roman_last_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'ordering': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Role']", 'null': 'True', 'blank': 'True'}),
            'roman_first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'roman_last_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
        },
        u'people_academic.personpluginmodel': {
            'Meta': {'object_name': 'PersonPluginModel', 'db_table': "u'cmsplugin_personpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Group']"})
        },
        u'people_academic.persontranslation': {
            'Meta': {'object_name': 'PersonTranslation'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.TextField', [], {'max_length': '512', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Person']"}),
            'prof_activities': ('django.db.models.fields.TextField', [], {'max_length': '512', 'blank': 'True'}),
            'pub': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'})
        },
        u'people_academic.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'people_academic.roletranslation': {
            'Meta': {'object_name': 'RoleTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Role']"}),
            'role_description': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'})
        }
    }

    complete_apps = ['people_academic']