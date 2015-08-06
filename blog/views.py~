from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from .models import MyBlog

# Create your views here.
def home(request):
    post = MyBlog.objects.all()
    return render(request,'blog/index.html',
                              {'post':post,}
                              )