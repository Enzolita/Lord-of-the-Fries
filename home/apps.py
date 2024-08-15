from django.apps import AppConfig
from django.db.utils import OperationalError


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'




class LordOfTheFriesConfig(AppConfig):
    name = 'lord_of_the_fries'

    def ready(self):
        from django.contrib.sites.models import Site
        try:
            if not Site.objects.filter(domain='127.0.0.1:8000').exists():
                Site.objects.create(domain='127.0.0.1:8000', name='Localhost')
        except OperationalError:
            pass
