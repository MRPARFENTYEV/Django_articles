from django.shortcuts import render
# from .models import Article
from .models import Article,Tag,Scope
#
#
def articles_list(request):
    template = 'articles/news.html'
    article_object = Article.objects.all()
    tag = Tag.objects.all()
    # scope = Scope.objects.all()
    context = {'object_list': article_object}
#     context = {'object_list': article_object}
#     context ={}
#
#
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
#
    return render(request, template, context)
