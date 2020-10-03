from django.urls import path
from .views import post_list, post_new, post_detail


urlpatterns = [
    path('', post_list, name="post_list"),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('post/new', post_new, name='post_new'),
]