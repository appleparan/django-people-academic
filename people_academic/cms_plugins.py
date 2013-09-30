# -*- coding: utf-8 -*-
"""django-cms plugins for the ``people`` app."""
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from hvad.utils import get_translation_aware_manager
from .models import Person, PersonPluginModel


class PersonPlugin(CMSPluginBase):
    model = PersonPluginModel
    name = _("Person Plugin for Academic person")
    render_template = "people_academic/person_list.html"

    def render(self, context, instance, placeholder):
        #people = Person.people.get_people_list(PersonPluginModel.group)
        lang = get_language()
        group = instance.group
        people = get_translation_aware_maanger(Person) \
            .language() \
            .filter(group__name__exact=group) \
            .order_by('ordering')
        context.update({
            'plugin': instance,
            'group': instance.group,
            'people': people,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(PersonPlugin)
