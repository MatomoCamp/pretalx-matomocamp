from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class PluginApp(AppConfig):
    name = "pretalx_matomocamp"
    verbose_name = "Pretalx Extension for the MatomoCamp"

    class PretalxPluginMeta:
        name = gettext_lazy("Pretalx Extension for the MatomoCamp")
        author = "Lukas Winkler"
        description = gettext_lazy("Short description")
        visible = True
        version = "0.0.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = "pretalx_matomocamp.PluginApp"
