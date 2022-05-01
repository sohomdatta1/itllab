from django.contrib import admin
import site
from . import models
# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ( 'question', 'choice_text', 'votes' )
admin.site.register(models.PollModel, PollAdmin)

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ( 'question', 'date_published' )
admin.site.register(models.QuestionModel, QuestionsAdmin)