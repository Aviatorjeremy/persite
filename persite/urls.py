from django.conf.urls import patterns, include, url
from blog.views import dashboard

urlpatterns = patterns('',
    (r'^dashboard/', dashboard.as_view()),
)
