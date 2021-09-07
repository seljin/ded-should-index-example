# ded-should-index-example

requirements :
---------------
- Running elasticsearch
- Python virtualenv

How to test :
--------------

> pip install -r requirements.txt

> ./manage.py migrate

> Change ELASTICSEARCH_DSL['default']['hosts'] in settings.py

> ./manage.py shell
>> from pizzeria.models import Pizza <br>
> pizza = Pizza.objects.first() <br>
> pizza.save()
> 
>> curl http://elasticsearch-hostname:9200/pizzas/_search/
> 
> Our pizza is indexed, everything is fine
> 
>> pizza.delete() <br>
> 
> We can see should_index_object print no toppings and False <br>
> Which is normal in django ways but our pizza is still indexed while not existing in database
