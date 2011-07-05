from markdown import markdown
from django.shortcuts import get_object_or_404, render_to_response

from ishblog.models import Entry

def entry(request, year, month, day, slug):
    entry = get_object_or_404(Entry, slug=slug,
            pub_date__year=year, pub_date__month=month, pub_date__day=day,)

    return render_to_response('blog/entry.html', {'entry': entry})

def list(request):
    entries = Entry.objects.filter(published=True).order_by('-pub_date').all()

    return render_to_response('blog/list.html', {'entries': entries } )
