from django.conf.urls import include
from django.conf.urls import url
from . views import BookListView,BookDetailView,SearchItemListView,BookTransactionView
app_name='booklist'
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$',BookListView.as_view()),
    url(r'^(?P<pk>\d+)/$', BookDetailView.as_view(), name='detail' ),
    url(r'^search_item_list/$',  SearchItemListView.as_view(), name='search_item_list'),
    url(r'^(?P<pk>\d+)/booktransaction/$',  BookTransactionView.as_view(), name='selectedbook'),
    #url(r'^tweet/',include('tweets.urls',namespace='tweet')),
    #url(r'^api/tweet/',include('tweets.api.urls',namespace='tweet-api')),
    #url(r'^',include('accounts.urls',namespace='profiles')),
]
