from django.apps import AppConfig


class BikeblogConfig(AppConfig):
    """
    Provides primary key type for bikeblog app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bikeblog'
