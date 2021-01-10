from django.contrib import admin

from planes.models import PlanarCard


@admin.register(PlanarCard)
class PlanarCardAdmin(admin.ModelAdmin):
    pass
