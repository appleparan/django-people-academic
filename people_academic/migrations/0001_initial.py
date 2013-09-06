# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LinkType'
        db.create_table(u'people_academic_linktype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=256, blank=True)),
            ('ordering', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'people_academic', ['LinkType'])

        # Adding model 'LinkTypeTranslation'
        db.create_table(u'people_academic_linktypetranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('link_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.LinkType'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['LinkTypeTranslation'])

        # Adding model 'Nationality'
        db.create_table(u'people_academic_nationality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'people_academic', ['Nationality'])

        # Adding model 'NationalityTranslation'
        db.create_table(u'people_academic_nationalitytranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Nationality'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['NationalityTranslation'])

        # Adding model 'Role'
        db.create_table(u'people_academic_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'people_academic', ['Role'])

        # Adding model 'RoleTranslation'
        db.create_table(u'people_academic_roletranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('role_description', self.gf('django.db.models.fields.TextField')(max_length=4000, blank=True)),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Role'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['RoleTranslation'])

        # Adding model 'Lab'
        db.create_table(u'people_academic_lab', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('homepage', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal(u'people_academic', ['Lab'])

        # Adding model 'LabTranslation'
        db.create_table(u'people_academic_labtranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('lab_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Lab'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['LabTranslation'])

        # Adding model 'Group'
        db.create_table(u'people_academic_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'people_academic', ['Group'])

        # Adding model 'GroupTranslation'
        db.create_table(u'people_academic_grouptranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('group_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Group'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['GroupTranslation'])

        # Adding model 'Person'
        db.create_table(u'people_academic_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Group'])),
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
            ('homepage', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='picture', null=True, to=orm['filer.Image'])),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume', null=True, to=orm['filer.File'])),
            ('ordering', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Nationality'], null=True, blank=True)),
        ))
        db.send_create_signal(u'people_academic', ['Person'])

        # Adding model 'PersonTranslation'
        db.create_table(u'people_academic_persontranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_bio', self.gf('django.db.models.fields.TextField')(max_length=512, blank=True)),
            ('interests', self.gf('django.db.models.fields.TextField')(max_length=512, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=4000, blank=True)),
            ('prof_activities', self.gf('django.db.models.fields.TextField')(max_length=512, blank=True)),
            ('pub', self.gf('django.db.models.fields.TextField')(max_length=4000, blank=True)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Person'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'people_academic', ['PersonTranslation'])

        # Adding model 'PersonPluginModel'
        db.create_table(u'cmsplugin_personpluginmodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people_academic.Person'])),
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
        # Deleting model 'LinkType'
        db.delete_table(u'people_academic_linktype')

        # Deleting model 'LinkTypeTranslation'
        db.delete_table(u'people_academic_linktypetranslation')

        # Deleting model 'Nationality'
        db.delete_table(u'people_academic_nationality')

        # Deleting model 'NationalityTranslation'
        db.delete_table(u'people_academic_nationalitytranslation')

        # Deleting model 'Role'
        db.delete_table(u'people_academic_role')

        # Deleting model 'RoleTranslation'
        db.delete_table(u'people_academic_roletranslation')

        # Deleting model 'Lab'
        db.delete_table(u'people_academic_lab')

        # Deleting model 'LabTranslation'
        db.delete_table(u'people_academic_labtranslation')

        # Deleting model 'Group'
        db.delete_table(u'people_academic_group')

        # Deleting model 'GroupTranslation'
        db.delete_table(u'people_academic_grouptranslation')

        # Deleting model 'Person'
        db.delete_table(u'people_academic_person')

        # Deleting model 'PersonTranslation'
        db.delete_table(u'people_academic_persontranslation')

        # Deleting model 'PersonPluginModel'
        db.delete_table(u'cmsplugin_personpluginmodel')

        # Deleting model 'Link'
        db.delete_table(u'people_academic_link')


    models = {
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'people_academic.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'people_academic.grouptranslation': {
            'Meta': {'object_name': 'GroupTranslation'},
            'group_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Group']"}),
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
        u'people_academic.nationality': {
            'Meta': {'object_name': 'Nationality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'people_academic.nationalitytranslation': {
            'Meta': {'object_name': 'NationalityTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Nationality']"})
        },
        u'people_academic.person': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Person'},
            'chosen_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Group']"}),
            'homepage': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Lab']", 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Nationality']", 'null': 'True', 'blank': 'True'}),
            'non_roman_first_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'non_roman_last_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'ordering': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'picture'", 'null': 'True', 'to': "orm['filer.Image']"}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume'", 'null': 'True', 'to': "orm['filer.File']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Role']", 'null': 'True', 'blank': 'True'}),
            'roman_first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'roman_last_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
        },
        u'people_academic.personpluginmodel': {
            'Meta': {'object_name': 'PersonPluginModel', 'db_table': "u'cmsplugin_personpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Group']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people_academic.Person']"})
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
            'pub': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            'short_bio': ('django.db.models.fields.TextField', [], {'max_length': '512', 'blank': 'True'})
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