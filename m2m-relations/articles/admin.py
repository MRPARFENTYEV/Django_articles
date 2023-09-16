from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope



# class RelationshipInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             # В form.cleaned_data будет словарь с данными
#             # каждой отдельной формы, которые вы можете проверить
#             form.cleaned_data
#             # вызовом исключения ValidationError можно указать админке о наличие ошибки
#             # таким образом объект не будет сохранен,
#             # а пользователю выведется соответствующее сообщение об ошибке
#             raise ValidationError('Тут всегда ошибка')
#         return super().clean()  # вызываем базовый код переопределяемого метода

@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug']

class RelationshipInline(admin.TabularInline):
    model = Scope
    extra = 2
    # formset = RelationshipInlineFormset
@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    list_display = ['id','title','text','published_at']
    list_filter = ['id','title']
# #



