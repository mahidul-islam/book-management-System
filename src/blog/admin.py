from django.contrib import admin
from .models import BlogPost

class BlogPostModelAdmin(admin.ModelAdmin):
    list_display = ["title","writter","mark"]
    class Meta:
        model=BlogPost
# Register your models here.
admin.site.register(BlogPost,BlogPostModelAdmin)
