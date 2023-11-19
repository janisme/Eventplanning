from django.apps import AppConfig
from events.database_initializer import initialize_database

class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'




