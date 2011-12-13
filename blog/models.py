from datetime import datetime
from django.db import models

ACTIVE, DRAFT = range(2)

STATUS_CHOICES = (
    (ACTIVE, 'Active'),
    (DRAFT, 'Draft'),
    )

class PostManager(models.Manager):
    """Returns active posts that are not in the future."""
    def published(self):
        return self.get_query_set().filter(status=ACTIVE).filter(published__lte=datetime.now()).order_by('-published')
   
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = models.TextField(blank=True, null=True)
    published = models.DateTimeField("Publish Date",default=datetime.now, help_text="Date when post will be published")
    created = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated at", auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=ACTIVE, help_text="Only Active posts will be displayed.")
    
    objects = PostManager()
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog-displaypost', None, {'slug':self.slug})
    