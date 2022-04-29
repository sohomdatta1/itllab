from django.contrib import admin
import site
from . import models
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_of_visits', 'num_of_likes')

admin.site.register(models.Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'views')

admin.site.register(models.Page, PageAdmin)