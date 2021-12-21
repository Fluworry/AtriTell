from django.shortcuts import HttpResponse, render
from django.views.decorators.http import require_GET, require_POST

from .models import Article


@require_GET
def article_type_show(request):
    return render(request, 'createarticle.html')


# @require_POST
# def article_type_choice(request):
#     article_type = request.POST.get('type')
