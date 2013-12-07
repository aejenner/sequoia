from django.contrib import admin
from question.models import Question, Category3, Category2, Category1, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	max_num = 4
	extra = 4

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Category',	{'fields':['category']}),
		('Question',	{'fields': ['text']}),
	]
	inlines = [ChoiceInline]

#class CategoryAdmin

#admin.site.register(Category1)
#admin.site.register(Category2)
#admin.site.register(Category3)
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
