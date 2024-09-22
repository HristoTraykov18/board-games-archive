from django.apps import AppConfig


class UnmatchedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'unmatched'
