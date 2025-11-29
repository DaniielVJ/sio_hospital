# Codigo de terceros
from django.contrib import admin
# Codigo que nosotros definimos
from ..models import TestVih


@admin.register(TestVih)
class TestVihAdmin(admin.ModelAdmin):
    pass
