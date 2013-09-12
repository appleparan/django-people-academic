"""Admin classes for the ``people`` app."""
from django.contrib import admin
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from simple_translation.admin import TranslationAdmin
from simple_translation.utils import get_preferred_translation_from_lang

from . import models


class LabAdmin(TranslationAdmin):
    """Admin for the ``Lab`` model."""
    list_display = ['name', 'homepage', 'languages']

    def name(self, obj):
        lang = get_language()
        return get_preferred_translation_from_lang(obj, lang).name
    name.short_description = _('Name')


class GroupAdmin(TranslationAdmin):
    """Admin for the ``Group`` model."""
    list_display = ['name', 'languages']

    def name(self, obj):
        lang = get_language()
        return get_preferred_translation_from_lang(obj, lang).name
    name.short_description = _('Name')


class LinkAdmin(admin.ModelAdmin):
    """Admin for the ``Link`` model."""
    list_display = ['person', 'link_type', 'url', ]


class LinkInline(admin.TabularInline):
    """Inline admin for ``Link`` objects."""
    model = models.Link


class LinkTypeAdmin(TranslationAdmin):
    """Admin for the ``LinkType`` model."""
    list_display = ['name', 'ordering', 'languages', ]

    def name(self, obj):
        lang = get_language()
        return get_preferred_translation_from_lang(obj, lang).name
    name.short_description = _('Name')


class PersonAdmin(TranslationAdmin):
    """Admin for the ``Person`` model."""
    inlines = [LinkInline, ]
    list_display = [
        'roman_first_name', 'roman_last_name', 'non_roman_first_name_link',
        'non_roman_last_name', 'gender', 'title', 'role',
        'lab_name', 'email',  'phone', 'mobile', 'homepage', 
        'picture', 'resume', 'ordering', 'group', 'languages']

    change_form_template = 'admin/change_form.html' 

    def non_roman_first_name_link(self, obj):
        return u'<a href="{0}/">{1}</a>'.format(
            obj.pk, unicode(obj.non_roman_first_name))
    non_roman_first_name_link.allow_tags = True
    non_roman_first_name_link.short_description = "Non roman first name"


class RoleAdmin(TranslationAdmin):
    """Admin for the ``Role`` model."""
    list_display = ['name', 'languages', ]

    def name(self, obj):
        lang = get_language()
        return get_preferred_translation_from_lang(obj, lang).name
    name.short_description = _('Name')


admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Lab, LabAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.LinkType, LinkTypeAdmin)
