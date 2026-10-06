# settings.py — sección de estáticos (verificar, no duplicar)
STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'   # destino de collectstatic

# STATICFILES_DIRS ≠ STATIC_ROOT (error frecuente)
STATICFILES_DIRS = [BASE_DIR / 'static']  # fuentes adicionales

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'