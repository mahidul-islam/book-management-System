from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static
from django.urls import include
from django.conf.urls import url
from booklist.views import BookListView
import profiles.urls
import accounts.urls
import booklist.urls
import blog.urls
from . import views

# Personalized admin site settings like title and header
admin.site.site_title = 'Bookshare Site Admin'
admin.site.site_header = 'Bookshare Administration'


urlpatterns = [
    url(r'^$',BookListView.as_view() ,name='home'),
    url(r'home/', views.HomePage.as_view()),
    url(r'^about/', views.AboutPage.as_view(), name='about'),
    url(r'^category/', views.CategoryPage.as_view(),name='category'),
    url(r'^users/', include(profiles.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^book/', include(booklist.urls,namespace='booklist')),
    url(r'^blog/',include("blog.urls" ,namespace='blog')),
    url(r'', include(accounts.urls)),

]



# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
