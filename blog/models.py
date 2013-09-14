from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ManyToManyField('blog.Category')

    def __unicode__(self):
        return '%s' % self.title



class Category(models.Model):
    title = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    def __unicode__(self):
        return '%s' % self.title

    

