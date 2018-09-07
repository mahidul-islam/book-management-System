from django.contrib import admin
from .models import BookOwner,Author,Book,QuotationFromBook,BookTransactionModel
# Register your models here.

class BookModelAdmin(admin.ModelAdmin):
	list_display=["title","author","owner","mark"]
	class Meta:
		model=Book

admin.site.register(BookOwner)
admin.site.register(Book,BookModelAdmin)
admin.site.register(Author)
admin.site.register(QuotationFromBook)
admin.site.register(BookTransactionModel)
#admin.site.register(BookTransaction)
