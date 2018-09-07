from django.views import generic
from booklist.models import Book

class HomePage(generic.TemplateView):
	model=Book

	template_name = "home.html"



class AboutPage(generic.TemplateView):
    template_name = "about.html"

class CategoryPage(generic.TemplateView):
	template_name = "categories.html"
