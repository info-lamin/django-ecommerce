from django.apps import AppConfig


class EcomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecom'

    def ready(self) -> None:
        from ecom import signals
        super().ready()
