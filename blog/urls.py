from django.urls import path
from . views import BlogListViews

urlpatterns = [
    path('', BlogListViews.as_view(), name = 'home')
]

