from django.db import models

class Entry(models.Model):
    # loaded via yaml file
    title       = models.CharField(max_length=140)
    slug        = models.SlugField()
    pub_date    = models.DateTimeField('Date Published')
    published   = models.BooleanField(default=False)
    # by way of markdown files
    snip        = models.CharField(max_length=140)
    body        = models.TextField()

    class Meta:
        verbose_name        = 'entry'
        verbose_name_plural = 'entries'

    def get_absolute_url(self):
        return u'/blog/0%d/%02d/%s/' % (self.pub_date.year, self.pub_date.month, self.slug)

    def __unicode__(self):
        return u'%s' % (self.title,)
