from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


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



