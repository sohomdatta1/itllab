from django.contrib import admin
from . import models
# Register your models here.
class WorksAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'company_name', 'salary')

admin.site.register(models.Works, WorksAdmin)

class LivesAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'street', 'city')

admin.site.register(models.Lives, LivesAdmin)