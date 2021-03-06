# -*- coding: utf-8 -*-
"""Models for the ``people`` app."""
from django.db import models
from django.db.models.query import QuerySet
from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode

from cms.models.pluginmodel import CMSPlugin
from hvad.models import TranslatableModel, TranslatedFields
from localized_names.templatetags.localized_names_tags import get_name

from . import settings


# Hack to have these strings translated
mr = _('Mr')
mrs = _('Ms')


GENDER_CHOICES = [
    ('male', _('male')),
    ('female', _('female')),
]

TITLE_CHOICES = [
    ('Un', _(' ')),
    ('Ms', _('Ms.')),
    ('Dr', _('Dr.')),
    ('Prof', _('Prof.')),
]


class LinkType(TranslatableModel):
    """
    A link type could be ``Facebook`` or ``Twitter`` or ``Website``.

    This is masterdata that should be created by the admins when the site is
    deployed for the first time.

    For translateable fields see ``LinkTypeTranslation`` model.

    :ordering: Enter numbers here if you want links to be displayed in a
      special order.

    """
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug'),
        help_text=_(
            'Use this field to define a simple identifier that can be used'
            ' to style the different link types (i.e. assign social media'
            ' icons to them)'),
        blank=True,
    )

    ordering = models.PositiveIntegerField(
        verbose_name=_('Ordering'),
        null=True, blank=True,
    )

    translations = TranslatedFields(
        name = models.CharField(
            max_length=256,
            verbose_name=_('Name'),
        )
    )

    class Meta:
        ordering = ['ordering', ]

    def __unicode__(self):
        return smart_unicode(self.lazy_translation_getter('name', 'LinkType: %s' % self.pk))


class Role(TranslatableModel):
    """
    People can have certain roles in an organisation.

    For translateable fields see ``RoleTranslation`` model.

    :name: The name of the role.

    """

    translations = TranslatedFields(
        name = models.CharField(
            max_length=256,
            verbose_name=_('Role'),
        ),

        role_description = models.TextField(
            max_length=4000,
            verbose_name=_('Role description'),
            blank=True,
        )
    )

    def __unicode__(self):
        return smart_unicode(self.lazy_translation_getter('name', 'Role: %s' % self.pk))


class Lab(TranslatableModel):
    """
    The name of Lab.

    For translateable fields see the ``LabTranslation`` model.

    """
    homepage = models.CharField(
        max_length=256,
        verbose_name=_('Homepage'),
        blank=True,
    )

    translations = TranslatedFields(
        name = models.CharField(
            max_length=128,
            verbose_name=_('Name'),
        )
    )

    def __unicode__(self):
        return smart_unicode(self.lazy_translation_getter('name', 'Lab: %s' % self.pk))


class Group(TranslatableModel):
    """
    The name of Group.

    For translateable fields see the ``GroupTranslation`` model.

    """
    translations = TranslatedFields(
        name = models.CharField(
            max_length=128,
            verbose_name=_('Name'),
        )
    )

    def __unicode__(self):
        return smart_unicode(self.lazy_translation_getter('name', 'Group: %s' % self.pk))


class Person(TranslatableModel):
    """
    A model that holds information about a person.

    For translateable fields see ``PersonTitle`` model.

    :roman_first_name: The first name in roman letters.
    :roman_last_name: The last name in roman letters.
    :non_roman_first_name: The first name in non roman letters.
    :non_roman_last_name: The last name in non roman letters.
    :gender: The gender of the person.
    :title: The title of the person.
    :role: Role of the person within the organisation.
    :labname: Lab name that the person belongs
    :email: Email address of the person.
    :phone: Phonenumber of the person.
    :mobile: Mobile number of the person.
    :homepage: A Homepage address of the person.
    :picture: A picture of the person.
    :resume: A CV(Resume) of the person.
    :ordering: Enter numbers if you want to order the list of persons on your
      site in a special way.
    :nationality: The nationality of a person.
    :group: A category shown in homepage

    """
    group = models.ForeignKey(
        Group,
        related_name='group',
        verbose_name=_('Homepage Group'),
        blank=False,
    )

    roman_first_name = models.CharField(
        max_length=256,
        verbose_name=_('Roman first name'),
    )

    roman_last_name = models.CharField(
        max_length=256,
        verbose_name=_('Roman last name'),
        blank=True,
    )

    non_roman_first_name = models.CharField(
        max_length=256,
        verbose_name=_('Non roman first name'),
        blank=True
    )

    non_roman_last_name = models.CharField(
        max_length=256,
        verbose_name=_('Non roman last name'),
        blank=True,
    )

    chosen_name = models.CharField(
        max_length=256,
        verbose_name=_('Chosen name'),
        blank=True,
    )

    gender = models.CharField(
        max_length=16,
        choices=GENDER_CHOICES,
        verbose_name=_('Gender'),
        blank=True,
    )

    title = models.CharField(
        max_length=16,
        choices=TITLE_CHOICES,
        verbose_name=_('Title'),
        blank=True,
    )

    role = models.ForeignKey(
        Role,
        verbose_name=_('Role'),
        null=True, blank=True,
    )

    lab_name = models.ForeignKey(
        Lab,
        verbose_name=_('Lab Name'),
        null=True, blank=True,
    )

    email = models.EmailField(
        verbose_name=_('Email'),
        blank=True,
    )

    phone = models.CharField(
        max_length=32,
        verbose_name=_('Phone'),
        blank=True,
    )

    mobile = models.CharField(
        max_length=32,
        verbose_name=_('Mobile'),
        blank=True,
    )

    homepage = models.URLField(
        verbose_name=_('Homepage'),
        blank=True,
    )

    picture = models.ImageField(
        verbose_name=_('Picture'),
        upload_to='people-academic/picture/%Y/%m/%d',
        null=True, blank=True,
    )

    resume  = models.FileField(
        verbose_name=_('CV(resume)'),
        upload_to='people-academic/resume/%Y/%m/%d',
        null=True, blank=True,
    )

    ordering = models.PositiveIntegerField(
        verbose_name=_('Ordering'),
        null=True, blank=True,
    )

    translations = TranslatedFields(
        interests = models.TextField(
            max_length=512,
            verbose_name=_('Interests'),
            blank=True,
        ),

        bio = models.TextField(
            max_length=4000,
            verbose_name=_('Biography'),
            blank=True,
        ),

        prof_activities = models.TextField(
            max_length=512,
            verbose_name=_('Professional Activities'),
            blank=True,
        ),

        pub = models.TextField(
            max_length=4000,
            verbose_name=_('Publication'),
            blank=True,
        ),

        building = models.CharField(
            max_length=50,
            verbose_name=_('Building'),
            blank=True,
        ),
    )

    def get_gender(self):
        """Returns either 'Mr.' or 'Ms.' depending on the gender."""
        if self.gender == 'male':
            return 'Mr'
        elif self.gender == 'female':
            return 'Ms'
        return ''

    def get_title(self):
        """Returns the title of the person."""
        return self.title

    def get_romanized_first_name(self):
        """Returns the first name in roman letters."""
        return self.roman_first_name

    def get_romanized_last_name(self):
        """Returns the first name in roman letters."""
        return self.roman_last_name

    def get_non_romanized_first_name(self):
        """Returns the non roman version of the first name."""
        return self.non_roman_first_name

    def get_non_romanized_last_name(self):
        """Returns the non roman version of the first name."""
        return self.non_roman_last_name

    def get_nickname(self):
        """Returns the nickname of a person in roman letters."""
        return self.chosen_name

    class Meta:
        ordering = ['ordering', ]
        verbose_name_plural = _('People')

    def __unicode__(self):
        return smart_unicode(get_name(self))


class PersonPluginModel(CMSPlugin):
    """ 
        Model for the ``PersonPlugin`` cms plugin. 
    """
    group = models.ForeignKey( 
        Group,
        verbose_name=_('Group'),
        blank=False,
    )

    def copy_relations(self, oldinstance):
        self.group = oldinstance.group

    def __unicode__(self):
        return self.group.__unicode__()


class Link(models.Model):
    """
    A person can have many links.

    """
    person = models.ForeignKey(
        Person,
        verbose_name=_('Person'),
    )

    link_type = models.ForeignKey(
        LinkType,
        verbose_name=_('Link type'),
    )

    url = models.URLField(
        verbose_name=_('URL'),
    )

    def __unicode__(self):
        return self.url
