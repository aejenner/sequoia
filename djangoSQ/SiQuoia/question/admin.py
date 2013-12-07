from django.contrib import admin
from question.models import Question, Category, Choice

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Choice)
