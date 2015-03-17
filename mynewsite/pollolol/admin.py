from django.contrib import admin
from pollolol.models import Question, Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields':['question_text']}),
                (
                  'Date Information', {'fields':['pub_date'], 'classes':['collapse']}
                )
                ]