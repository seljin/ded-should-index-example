from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from pizzeria.models import Pizza


@registry.register_document
class PizzaDocument(Document):

    class Index:
        name = 'pizzas'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    def should_index_object(self, obj):
        print(obj.toppings.all(), obj.toppings.filter(name='Pepperoni').exists())
        return obj.toppings.filter(name='Pepperoni').exists()

    class Django:
        model = Pizza

        fields = [
            'name',
        ]
