"""Models for the ``people`` app."""
from django.db import models
from django.db.models.query import QuerySet
from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from django_libs.models_mixins import SimpleTranslationMixin
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
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
    ('Ms', _('Ms')),
    ('Dr', _('Dr')),
    ('Prof', _('Prof')),
]

GRP_CHOICES = [
    ('Faculty', _('Faculty')),
    ('Visitor', _('Visitor')),
    ('Postdoc', _('Postdoc')),
    ('Alumni', _('Alumni')),
    ('Graduate Stduent', _('Graduate Student')),
    ('URP', _('URP')),
]


class LinkType(SimpleTranslationMixin, models.Model):
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

    class Meta:
        ordering = ['ordering', ]

    def __unicode__(self):
        return self.get_translation().name


class LinkTypeTranslation(models.Model):
    """
    Translateable fields of the ``LinkType`` model.

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    # needed by simple-translation
    link_type = models.ForeignKey(LinkType)
    language = models.CharField(max_length=16, choices=global_settings.LANGUAGES)


class Nationality(SimpleTranslationMixin, models.Model):
    """
    The nationality of a Person.

    For translateable fields see the ``NationalityTranslation`` model.

    """
    def __unicode__(self):
        return self.get_translation().name

    class Meta:
        verbose_name_plural = _('Nationalities')


class NationalityTranslation(models.Model):
    """
    The translateable fields of the ``Nationality`` model.

    :name: E.g. 'Chinese' or 'Deutsch'

    """
    name = models.CharField(
        max_length=128,
        verbose_name=_('Name'),
    )

    # needed by simple-translation
    nationality = models.ForeignKey(Nationality)
    language = models.CharField(max_length=16, choices=global_settings.LANGUAGES)


class Role(SimpleTranslationMixin, models.Model):
    """
    People can have certain roles in an organisation.

    For translateable fields see ``RoleTranslation`` model.

    :name: The name of the role.

    """
    def __unicode__(self):
        return self.get_translation().name


class RoleTranslation(models.Model):
    """
    Translateable fields of the ``Role`` model.

    :name: The name of the role.

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Role'),
    )

    role_description = models.TextField(
        max_length=4000,
        verbose_name=_('Role description'),
        blank=True,
    )

    # needed by simple-translation
    role = models.ForeignKey(Role)
    language = models.CharField(max_length=16, choices=global_settings.LANGUAGES)


class Lab(SimpleTranslationMixin, models.Model):
    """
    The name of Lab.

    For translateable fields see the ``LabTranslation`` model.

    """
    homepage = models.CharField(
        max_length=256,
        verbose_name=_('Homepage'),
        blank=True,
    )

    def __unicode__(self):
        return self.get_translation().name


class LabTranslation(models.Model):
    """
    The translateable fields of the ``Lab`` model.

    :name: E.g. 'Numerical' or 'CFD'

    """
    name = models.CharField(
        max_length=128,
        verbose_name=_('Name'),
    )

    # needed by simple-translation
    lab_name = models.ForeignKey(Lab)
    language = models.CharField(max_length=16, choices=global_settings.LANGUAGES)


class Group(SimpleTranslationMixin, models.Model):
    """
    The name of Group.

    For translateable fields see the ``GroupTranslation`` model.

    """
    def __unicode__(self):
        return self.get_translation().name


class GroupTranslation(models.Model):
    """
    The translateable fields of the ``Group`` model.

    :name: E.g. 'Faculty' or 'Visitor'

    """
    name = models.CharField(
        max_length=128,
        verbose_name=_('Name'),
    )

    # needed by simple-translation
    group = models.ForeignKey(Group)
    language = models.CharField(max_length=16, choices=global_settings.LANGUAGES)


class PeopleQuerySet(QuerySet):
    """
        QuerySet : Filters out all people within some group
    """
    def get_people_list(self, group_):
        return self.filter(group__grouptranslation__name=group_)


class People(models.Manager):
    """
        Manager : Filters out all people within some group
    """
    def get_query_set(self):
        return PeopleQuerySet(self.model)

    def get_queryset(self):
        return PeopleQuerySet(self.model)

    def __getattr__(self, name):
        import django
        django_ver = django.VERSION
        if django_ver[0] == 1 and django_ver[1] < 6:
            return getattr(self.get_query_set(), name)
        else:
            return getattr(self.get_queryset(), name)


class Person(SimpleTranslationMixin, models.Model):
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

    picture = FilerImageField(
        verbose_name=_('Picture'),
        null=True, blank=True,
        related_name='picture',
    )

    resume  = FilerFileField(
        verbose_name=_('CV(resume)'),
        null=True, blank=True,
        related_name='resume',
    )

    ordering = models.PositiveIntegerField(
        verbose_name=_('Ordering'),
        null=True, blank=True,
    )

    nationality = models.ForeignKey(
        Nationality,
        verbose_name=_('Nationality'),
        blank=True, null=True,
    )

    people = People()

    class Meta:
        ordering = ['ordering', ]
        verbose_name_plural = _('People')

    def __unicode__(self):
        trans = self.get_translation()
        return get_name(trans)


class PersonTranslation(models.Model):
    """
    Translateable fields of the ``Person`` model.

    :short_bio: A short description of the person.
    :bio: A longer description of the person, could appear after a
      ``read more`` link behind the ``short_bio``.

    """
    short_bio = models.TextField(
        max_length=512,
        verbose_name=_('Short bio'),
        blank=True,
    )

    interests = models.TextField(
        max_length=512,
        verbose_name=_('Interests'),
        blank=True,
    )

    bio = models.TextField(
        max_length=4000,
        verbose_name=_('Biography'),
        blank=True,
    )

    prof_activities = models.TextField(
        max_length=512,
        verbose_name=_('Professional Activities'),
        blank=True,
    )

    pub = models.TextField(
        max_length=4000,
        verbose_name=_('Publication'),
        blank=True,
    )

    building = models.CharField(
        max_length=50,
        verbose_name=_('Building'),
        blank=True,
    )

    # needed by simple-translation
    person = models.ForeignKey(Person)
    language = models.CharField(max_length=16, choices=global_settings.LANGUAGES)

    def get_gender(self):
        """Returns either 'Mr.' or 'Ms.' depending on the gender."""
        if self.person.gender == 'male':
            return 'Mr'
        elif self.person.gender == 'female':
            return 'Ms'
        return ''

    def get_title(self):
        """Returns the title of the person."""
        return self.person.title

    def get_romanized_first_name(self):
        """Returns the first name in roman letters."""
        return self.person.roman_first_name

    def get_romanized_last_name(self):
        """Returns the first name in roman letters."""
        return self.person.roman_last_name

    def get_non_romanized_first_name(self):
        """Returns the non roman version of the first name."""
        return self.person.non_roman_first_name

    def get_non_romanized_last_name(self):
        """Returns the non roman version of the first name."""
        return self.person.non_roman_last_name

    def get_nickname(self):
        """Returns the nickname of a person in roman letters."""
        return self.person.chosen_name


class PersonPluginModel(CMSPlugin):
    """ 
        Model for the ``PersonPlugin`` cms plugin. 
    """
    group = models.ForeignKey( 
        Group,
        verbose_name=_('Group'),
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
