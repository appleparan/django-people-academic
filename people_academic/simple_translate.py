"""Registering translated models for the ``hero_slider`` app."""
from simple_translation.translation_pool import translation_pool

from .models import (
    Nationality,
    NationalityTranslation,
    Lab,
    LabTranslation,
    LinkType,
    LinkTypeTranslation,
    Person,
    PersonTranslation,
    Role,
    RoleTranslation,
)


translation_pool.register_translation(Nationality, NationalityTranslation)
translation_pool.register_translation(Lab, LabTranslation)
translation_pool.register_translation(LinkType, LinkTypeTranslation)
translation_pool.register_translation(Person, PersonTranslation)
translation_pool.register_translation(Role, RoleTranslation)
