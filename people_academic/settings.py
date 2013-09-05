"""Settings for the ``people`` app."""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

gettext = lambda s: s

display_type_choices = [
    ('small', _('small')),
    ('big', _('big')),
]

LANGUAGES = (
    ('en', gettext('English')),
    ('ko', gettext('Korean')),
)


DISPLAY_TYPE_CHOICES = getattr(
    settings, 'PERSON_PLUGIN_DISPLAY_TYPE_CHOICES', display_type_choices)
