from django.db import models

# Create your models here.
class MyBlog(models.Model):
    title = models.CharField(max_length=125)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __unicode__(self):
        return self.title