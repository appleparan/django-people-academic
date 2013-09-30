# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LinkTypeTranslation'
        db.create_table(u'people_academic_linktype_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['people_academic.LinkType'])),
        ))
        db.send_create_signal(u'people_academic', ['LinkTypeTranslation'])

        # Adding unique constraint on 'LinkTypeTranslation', fields ['language_code', 'master']
        db.create_unique(u'people_academic_linktype_translation', ['language_code', 'master_id'])

        # Adding model 'LinkType'
        db.create_table(u'people_academic_linktype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=256, blank=True)),
            ('ordering', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['LinkType'])

        # Adding model 'RoleTranslation'
        db.create_table(u'people_academic_role_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('role_description', self.gf('django.db.models.fields.TextField')(max_length=4000, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['people_academic.Role'])),
        ))
        db.send_create_signal(u'people_academic', ['RoleTranslation'])

        # Adding unique constraint on 'RoleTranslation', fields ['language_code', 'master']
        db.create_unique(u'people_academic_role_translation', ['language_code', 'master_id'])

        # Adding model 'Role'
        db.create_table(u'people_academic_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['Role'])

        # Adding model 'LabTranslation'
        db.create_table(u'people_academic_lab_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['people_academic.Lab'])),
        ))
        db.send_create_signal(u'people_academic', ['LabTranslation'])

        # Adding unique constraint on 'LabTranslation', fields ['language_code', 'master']
        db.create_unique(u'people_academic_lab_translation', ['language_code', 'master_id'])

        # Adding model 'Lab'
        db.create_table(u'people_academic_lab', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('homepage', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['Lab'])

        # Adding model 'GroupTranslation'
        db.create_table(u'people_academic_group_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['people_academic.Group'])),
        ))
        db.send_create_signal(u'people_academic', ['GroupTranslation'])

        # Adding unique constraint on 'GroupTranslation', fields ['language_code', 'master']
        db.create_unique(u'people_academic_group_translation', ['language_code', 'master_id'])

        # Adding model 'Group'
        db.create_table(u'people_academic_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['Group'])

        # Adding model 'PersonTranslation'
        db.create_table(u'people_academic_person_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('interests', self.gf('django.db.models.fields.TextField')(max_length=512, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=4000, blank=True)),
            ('prof_activities', self.gf('django.db.models.fields.TextField')(max_length=512, blank=True)),
            ('pub', self.gf('django.db.models.fields.TextField')(max_length=4000, blank=True)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['people_academic.Person'])),
        ))
        db.send_create_signal(u'people_academic', ['PersonTranslation'])

        # Adding unique constraint on 'PersonTranslation', fields ['language_code', 'master']
        db.create_unique(u'people_academic_person_translation', ['language_code', 'master_id'])

        # Adding model 'Person'
        db.create_table(u'people_academic_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='group', to=orm['people_academic.Group'])),
            ('roman_first_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('roman_last_name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('non_roman_first_name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('non_roman_last_name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('chosen_name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Role'], null=True, blank=True)),
            ('lab_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Lab'], null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('homepage', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('resume', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('ordering', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['Person'])

        # Adding model 'PersonPluginModel'
        db.create_table(u'cmsplugin_personpluginmodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Group'])),
        ))
        db.send_create_signal(u'people_academic', ['PersonPluginModel'])

        # Adding model 'Link'
        db.create_table(u'people_academic_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Person'])),
            ('link_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.LinkType'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'people_academic', ['Link'])


    def backwards(self, orm):
        # Removing unique constraint on 'PersonTranslation', fields ['language_code', 'master']
        db.delete_unique(u'people_academic_person_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'GroupTranslation', fields ['language_code', 'master']
        db.delete_unique(u'people_academic_group_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'LabTranslation', fields ['language_code', 'master']
        db.delete_unique(u'people_academic_lab_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'RoleTranslation', fields ['language_code', 'master']
        db.delete_unique(u'people_academic_role_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'LinkTypeTranslation', fields ['language_code', 'master']
        db.delete_unique(u'people_academic_linktype_translation', ['language_code', 'master_id'])

        # Deleting model 'LinkTypeTranslation'
        db.delete_table(u'people_academic_linktype_translation')

        # Deleting model 'LinkType'
        db.delete_table(u'people_academic_linktype')

        # Deleting model 'RoleTranslation'
        db.delete_table(u'people_academic_role_translation')

        # Deleting model 'Role'
        db.delete_table(u'people_academic_role')

        # Deleting model 'LabTranslation'
        db.delete_table(u'people_academic_lab_translation')

        # Deleting model 'Lab'
        db.delete_table(u'people_academic_lab')

        # Deleting model 'GroupTranslation'
        db.delete_table(u'people_academic_group_translation')

        # Deleting model 'Group'
        db.delete_table(u'people_academic_group')

        # Deleting model 'PersonTranslation'
        db.delete_table(u'people_academic_person_translation')

        # Deleting model 'Person'
        db.delete_table(u'people_academic_person')

        # Deleting model 'PersonPluginModel'
        db.delete_table(u'cmsplugin_personpluginmodel')

        # Deleting model 'Link'
        db.delete_table(u'people_academic_link')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'people_academic.grouptranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'GroupTranslation', 'db_table': "u'people_academic_group_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['people_academic.Group']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'people_academic.lab': {
            'Meta': {'object_name': 'Lab'},
            'homepage': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'people_academic.labtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'LabTranslation', 'db_table': "u'people_academic_lab_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['people_academic.Lab']"}),
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
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'ordering': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'people_academic.linktypetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'LinkTypeTranslation', 'db_table': "u'people_academic_linktype_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['people_academic.LinkType']"}),
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
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
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
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PersonTranslation', 'db_table': "u'people_academic_person_translation'"},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.TextField', [], {'max_length': '512', 'blank': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['people_academic.Person']"}),
            'prof_activities': ('django.db.models.fields.TextField', [], {'max_length': '512', 'blank': 'True'}),
            'pub': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'})
        },
        u'people_academic.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'people_academic.roletranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'RoleTranslation', 'db_table': "u'people_academic_role_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['people_academic.Role']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'role_description': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'})
        }
    }

    complete_apps = ['people_academic']
