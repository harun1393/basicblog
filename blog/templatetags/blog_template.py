from django import template
from blog.models import Category, MyBlog

register = template.Library()


@register.inclusion_tag('blog/cats.html')
def get_sidebar():
    category = Category.objects.all()
    posts    = MyBlog.objects.all()[:5]
    return {'cats': category, 'posts':posts}
