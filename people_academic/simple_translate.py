"""Registering translated models for the ``hero_slider`` app."""
from simple_translation.translation_pool import translation_pool

from .models import (
    Lab,
    LabTranslation,
    Group,
    GroupTranslation,
    LinkType,
    LinkTypeTranslation,
    Person,
    PersonTranslation,
    Role,
    RoleTranslation,
)


translation_pool.register_translation(Lab, LabTranslation)
translation_pool.register_translation(Group, GroupTranslation)
translation_pool.register_translation(LinkType, LinkTypeTranslation)
translation_pool.register_translation(Person, PersonTranslation)
translation_pool.register_translation(Role, RoleTranslation)
