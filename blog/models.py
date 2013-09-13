from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=60, unique=true)
	slug = models.SlugField(max_length=60, unique=true)
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ManyToMany('blog.Category')

	def __unicode__(self):
		return '%s' % self.title





class Category(models.Model):
	title = models.CharField(max_length=60, unique=true)
	slug = models.SlugField(max_length=60, unique=true)

	def __unicode__(self):
		return '%s' % self.title

	

