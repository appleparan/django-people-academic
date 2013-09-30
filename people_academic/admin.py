# -*- coding: utf-8 -*-
"""Admin classes for the ``people`` app."""
from django.contrib import admin
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from hvad.admin import TranslatableAdmin
from hvad.utils import get_translation_aware_manager

from . import models


class LabAdmin(TranslatableAdmin):
    """Admin for the ``Lab`` model."""
    hvad_list_display = [u'hvad__name', u'homepage', u'language', ]


class GroupAdmin(TranslatableAdmin):
    """Admin for the ``Group`` model."""
    hvad_list_display = [u'hvad__name', u'language', ]


class LinkAdmin(admin.ModelAdmin):
    """Admin for the ``Link`` model."""
    hvad_list_display = [u'person', u'link_type', u'url', ]


class LinkInline(admin.TabularInline):
    """Inline admin for ``Link`` objects."""
    model = models.Link


class LinkTypeAdmin(TranslatableAdmin):
    """Admin for the ``LinkType`` model."""
    hvad_list_display = [u'hvad__name', u'ordering', u'language', ]


class PersonAdmin(TranslatableAdmin):
    """Admin for the ``Person`` model."""
    inlines = [LinkInline, ]
    hvad_list_display = [
        u'roman_first_name', u'roman_last_name', u'non_roman_first_name_link',
        u'non_roman_last_name', u'gender', u'title', u'role',
        u'lab_name', u'email',  u'phone', u'mobile', u'homepage', 
        u'picture', u'resume', u'ordering', u'group', u'language', 
        u'hvad__interests', u'hvad__bio', u'hvad__prof_activities',
        u'hvad__pub', u'hvad__building',
        ]

    #change_form_template = u'admin/change_form.html'

    def non_roman_first_name_link(self, obj):
        return u'<a href="{0}/">{1}</a>u'.format(
            obj.pk, unicode(obj.non_roman_first_name))
    non_roman_first_name_link.allow_tags = True
    non_roman_first_name_link.short_description = "Non roman first name"


class RoleAdmin(TranslatableAdmin):
    """Admin for the ``Role`` model."""
    hvad_list_display = [u'have__name', u'language', ]


admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Lab, LabAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.LinkType, LinkTypeAdmin)
