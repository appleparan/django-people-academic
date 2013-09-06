"""Settings for the ``people`` app."""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    ('ko', gettext('Korean')),
)
