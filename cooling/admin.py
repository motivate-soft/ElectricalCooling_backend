from django.contrib import admin

from cooling.models import Cooling


class CoolingAdmin(admin.ModelAdmin):
    model = Cooling
    list_display = ['name', 'components', 'losses', 'faces', 'passages', 'fluids']


admin.site.register(Cooling)
