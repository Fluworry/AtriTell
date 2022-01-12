from django.shortcuts import HttpResponse, get_object_or_404, render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Note


def account_register(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        user_email = request.POST.get('email')
        user_name = request.POST.get('username')
        user_pass = request.POST.get('pass')

        user = User.objects.create_user(user_name, user_email, user_pass)
        user.save()
    
    
def account_auth(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        user_name = request.POST.get('username')
        user_pass = request.POST.get('pass')

        user = authenticate(username=user_name, password=user_pass)

        if user is not None:
            pass
        else:
            pass


def note_create(request):
    if request.method == 'GET':
        print(request)
        return render(request, 'note.html', {'title': 'Title', 'body': 'My new note'})
    else:
        note_title = request.POST.get('title')
        note_text = request.POST.get('text')
        note = Note.objects.create(title=note_title, body=note_text)
        return redirect('/' + str(note.random_url_id))


def note_get_or_save(request, note_url):
    if request.method == 'GET':
        note = get_object_or_404(Note, random_url_id=note_url)
        return render(request, 'note.html', {'title': note.title, 'body': note.body})
    else:
        note_title = request.POST.get('title')
        note_text = request.POST.get('text')
        Note.objects.filter(random_url_id=note_url).update(title=note_title, body=note_text)
        return redirect('/' + str(note_url))
