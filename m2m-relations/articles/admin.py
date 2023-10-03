from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

# class RelationshipInlineFormset(BaseInlineFormSet):
class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        its_main = 0

        for form in self.forms:
           # super().clean()

           ISMain = form.cleaned_data.get('is_main')
           if ISMain == True:
               its_main += 1
               if its_main > 1:
                   raise ValidationError('Основным может быть только один раздел')


        super().clean()




@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']



class RelationshipInline(admin.TabularInline):
    model = Scope
    extra = 1
    # formset = [RelationshipInlineFormset]
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    list_display = ['id', 'title', 'text', 'published_at']
    list_filter = ['id', 'title']

