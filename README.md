Sethish's Django-powered static blog generator
----------------------------------------------

This is a django project that eats Markdown and YAML files and spits out a 
staticly generated website for deployment. 

A lot of work remains to make this a long term sustainable project. Right now too many things are hard-coded, and the django part is not separable form the content folder/arena.

Roadmap
=======
### v.1-alpha
This release is to get my project out the door and a static site generated
- finish first post
+ make css/html render properly
+ make affordances for static pages (hardcode in urls.py?)
- write script to crawl/render all pages

### v.2-beta
This release is the functional version for my purposes.
- make static generation auto push/deploy
- separate content from 'trans-blog-rifier'
- cleanup nagging css issues
- rss feed generation
- robots.txt generation
- Fix spacing of mid-post h3s
- add blockquote indenting and style change (boarder and bgcolor?)
- make method for static pages

### v.3-beta2
This is approaching my complete desired feature set
- integrate Discus for comments
- integrate django-tagging
- generate smarter metadata
- a jquery twitter/feed widget
- scripts to enable editing (vim -O $TITLE.md $TITLE.yaml: $title, timestamp)

