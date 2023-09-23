from django.shortcuts import render
# from .models import Article
from .models import Article,Tag,Scope
#
#
def articles_list(request):
    # tags = {}
    template = 'articles/news.html'
    article_object = Article.objects.all()

    # tags= Article.scopes.all()
    # print(Article.scopes)
    # for a in article_object:
    #     id = a.id
    #     tags[id]=[]
    #     scope = Scope.objects.filter(article_id = id)
    #     for iter in scope:
    #         tags[id].append(iter.tag)
    #         print(iter.tag)
    #     # print(scope.tag)
    # context = {'object_list': article_object,
    #            'tag':tags}
    context = {'object_list': article_object}
#     context ={}
#
#
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
#
    return render(request, template, context)
