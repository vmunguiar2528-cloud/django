import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()

# Crear tablas automaticamente al arrancar (Render)
if os.environ.get("RENDER"):
    from django.core.management import call_command
    try:
        call_command("migrate", interactive=False)
    except Exception as e:
        print("Error en migrate:", e)