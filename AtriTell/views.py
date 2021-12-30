from django.shortcuts import HttpResponse, render
from django.views.decorators.http import require_GET, require_POST
from .models import Article

from uuid import uuid4

def article_create(request):
    if request.method == 'GET':
        print(request)
        return render(request, 'createarticle.html')
    else:
        article_title = request.POST.get('title')
        article_text = request.POST.get('text')
        Article.objects.create(title=article_title, body=article_text, random_url_id=uuid4())
        
        return render(request, 'createarticle.html')

def article_get(request):
    pass


