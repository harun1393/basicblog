from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from .models import MyBlog,Category


# Create your views here.
def home(request):
    post = MyBlog.objects.all()
    recent_post = MyBlog.objects.all()[:5]
    category_list = Category.objects.all()
    context_dict  = {'categories':category_list,'post':post,'recent_post':recent_post,}
    return render(request,'blog/index.html',context_dict
                              )


def detail(request, slug):
    blog_post = get_object_or_404(MyBlog, slug=slug)
    return render(request, 'blog/detail.html', {'post':blog_post})


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        posts = MyBlog.objects.filter(categories=category)
        context_dict['posts'] = posts
        context_dict['category'] = category

    except Category.DoesNotExist:
        pass
    return  render(request, 'blog/category.html',context_dict)
