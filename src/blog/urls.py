from django.conf.urls import include
from django.conf.urls import url
from .views import BlogPostView,BlogPostDetailView
app_name='blog'
urlpatterns = [
        url(r'^$',BlogPostView.as_view()),
        url(r'^(?P<pk>\d+)/$', BlogPostDetailView.as_view(), name='detail' ),
]
