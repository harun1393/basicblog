from django.contrib import admin
from .models import MyBlog,Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    prepopulated_fields = {"slug":("name",)}


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','categories','date',]
    save_on_top = True
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(MyBlog, PostAdmin)
