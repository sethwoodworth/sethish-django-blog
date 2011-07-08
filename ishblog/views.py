from django.shortcuts import get_object_or_404, render_to_response
from django.template.defaultfilters import slugify

from ishblog.models import Entry

import os
from markdown import markdown
import yaml

def entry(request, year, slug):
    entry = get_object_or_404(Entry, slug=slug,
            pub_date__year=year,)

    return render_to_response('blog/post.html', {'entry': entry})

def list(request):
    entries = Entry.objects.filter(published=True).order_by('-pub_date').all()

    return render_to_response('blog/list.html', {'entries': entries } )

def static(request):
    return render_to_response('blog/index.html', {} )
    

def load():
    """
    Load a series of markdown and yaml files from content folders. YAML is for
    blogpost metadata and markdown files are blogpost content.
    """
    # Clearout the old db
    old_entries = Entry.objects.all()
    old_entries.delete()

    # Recreate the content of the db
    years = ['02011'] # only one year of content for now, append later
    # TODO: use this in a blog-wide yaml config file, can generate 1996-2010(c)
    for year in years:
        folder = './content/blog/' + year + '/'
        files = set([os.path.splitext(f)[0] for f in os.listdir(folder)])
        for file in files:
            meta_file   = open(folder + file + '.yaml', 'r')
            metadata    = yaml.load(meta_file)
            meta_file.close()

            post_file   = open(folder + file + '.md', 'r')
            post        = post_file.read()
            post_file.close()

            e = Entry()
            # TODO: implement django-tagging here
            # Metadata
            e.title     = metadata['title']
            e.slug      = slugify(metadata['title'])
            e.pub_date  = metadata['pub_date']
            e.published = metadata['published']
            # Post
            e.body      = post
            e.snip      = post[:139]            # 140 characters of fun
            e.save()
    pass
