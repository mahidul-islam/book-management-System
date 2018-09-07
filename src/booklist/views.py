from django.shortcuts import render,HttpResponse
from .models import Book,BookTransactionModel
from .forms import BookTransactionModelForm
from blog.models import BlogPost
from django.views import View
from django.views.generic.edit import FormMixin
from django.views.generic import (
        ListView,
        DetailView,
        TemplateView
	)
# Create your views here.
class BookListView(ListView):
    model=Book
    def get_queryset(self, *args,**kwargs):
        qs = Book.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs;

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogpost_list'] = BlogPost.objects.all().filter(mark=True)[:5]
        context['filterbook_list']=Book.objects.all().filter(mark=True)[:9]
        # And so on for more models
        return context


class BookDetailView(DetailView):
	queryset = Book.objects.all()


class SearchItemListView(TemplateView):
    template_name = 'booklist/search_item_list.html'



class BookTransactionView(FormMixin,BookDetailView):
    form_class = BookTransactionModelForm
    template_name = 'booklist/book_transaction_detail.html'
