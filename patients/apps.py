from django.apps import AppConfig


class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patients'
    verbose_name = 'إدارة المرضى والأطباء'

    def ready(self):
        import patients.signals
