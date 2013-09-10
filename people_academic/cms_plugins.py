"""django-cms plugins for the ``people`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Person, PersonPluginModel


class PersonPlugin(CMSPluginBase):
    model = PersonPluginModel
    name = _("Person Plugin for Academic person")
    render_template = "people_academic/person_list.html"

    def render(self, context, instance, placeholder):
        #people = Person.people.get_people_list(PersonPluginModel.group)
        group = instance.group
        people = Person.objects.all().filter(group__grouptranslation__name__exact=group)
        context.update({
            'plugin': instance,
            'group': instance.group,
            'people': people,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(PersonPlugin)
