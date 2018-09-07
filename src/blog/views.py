from django.shortcuts import render,HttpResponse
from .models import BlogPost
from django.views.generic import (
        ListView,
        DetailView
	)
# Create your views here.
class BlogPostView(ListView):
	model=BlogPost

class BlogPostDetailView(DetailView):
    queryset = BlogPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogpost_list'] = BlogPost.objects.all().filter(mark=True)[:5]
        return context
