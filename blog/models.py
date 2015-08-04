from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('name',max_length=125)
    slug = models.SlugField('slug', unique=True)
    description = models.TextField('description')

    def __unicode__(self):
        return self.name


class MyBlog(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField(unique=True,max_length=255)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    categories = models.ForeignKey(Category,blank=True,null=True)
    photo = models.ImageField(upload_to="media/", blank=True,null=True)


    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.home',args=[self.slug])
