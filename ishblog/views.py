from django.shortcuts import get_object_or_404, render_to_response
from django.template.defaultfilters import slugify

from ishblog.models import Entry

import os
from markdown import markdown
import yaml

def entry(request, year, month, day, slug):
    entry = get_object_or_404(Entry, slug=slug,
            pub_date__year=year, pub_date__month=month, pub_date__day=day,)

    return render_to_response('blog/entry.html', {'entry': entry})

def list(request):
    entries = Entry.objects.filter(published=True).order_by('-pub_date').all()

    return render_to_response('blog/list.html', {'entries': entries } )

def load():
    years = ['02011']
    for year in years:
        folder = './content/blog/' + year
        files = [ospath.splitext(f)[0] for f in os.listdir(folder)
        for file in files:
            metadata    = open(file + '.yaml', 'r')
            post        = open(file + '.md', 'r')
            e = Entry()

            # Metadata
            e.title     = file
            e.slug      = slugify(file)
            e.pub_date  = metadata['pub_date']
            # TODO: [


