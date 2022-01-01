from django.shortcuts import HttpResponse, get_object_or_404, render, redirect
from django.views.decorators.http import require_GET, require_POST
from .models import Note


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


