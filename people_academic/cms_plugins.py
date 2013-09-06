"""django-cms plugins for the ``people`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import PersonPluginModel


class PersonPlugin(CMSPluginBase):
    model = PersonPluginModel
    name = _("Person Plugin for Academic person")
    render_template = "people_academic/person_list.html"

    def render(self, context, instance, placeholder):
        context.update({
            'plugin': instance,
            'person': instance.person,
            'group': instance.group,
        })
        return context


plugin_pool.register_plugin(PersonPlugin)