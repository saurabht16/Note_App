from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
from .models import Notes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NoteForm
import operator
from django.db.models import Q
import functools

# Create your views here.

@login_required
def notes_list(request):
    note_list = Notes.objects.all()
    query = request.GET.get('q')
    if query:
        query_list = query.split()
        note_list = note_list.filter(
            functools.reduce(operator.and_,
                   (Q(labels__icontains=q) for q in query_list))
        )
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()
    else:
        form = NoteForm()
    #t = loader.get_template('list.html')
    c = {
    'note_list': note_list,
    'form': form,
    }
    return render(request, 'list.html', c)
def notes_detail(request, id):
    note = Notes.objects.get(pk=id)
    form = NoteForm(request.POST or None, request.FILES or None, instance=note)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/notes/list")
    context = {
        'note_list': note,
        "form": form,
    }
    return render(request, "details.html", context)
