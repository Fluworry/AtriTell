from django.shortcuts import HttpResponse, get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST
from .models import Article


def article_create(request):
    if request.method == 'GET':
        print(request)
        return render(request, 'createarticle.html', {'title': 'Title', 'body': 'My new article'})
    else:
        article_title = request.POST.get('title')
        article_text = request.POST.get('text')
        Article.objects.create(title=article_title, body=article_text)
        
        return render(request, 'createarticle.html', {'title': 'Title', 'body': 'My new article'})

def article_get(request, article_url):
    article = get_object_or_404(Article, random_url_id=article_url)
    return render(request, 'createarticle.html', {'title': article.title, 'body': article.body})

