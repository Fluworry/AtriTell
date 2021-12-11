from django.shortcuts import HttpResponse, render
from django.views.decorators.http import require_GET, require_POST


@require_GET
def article_type_show(request):
    return render(request, 'TypeChoice.html')


@require_POST
def article_type_choice(request):
    article_type = request.POST.get('type')
