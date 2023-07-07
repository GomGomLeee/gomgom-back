from django.urls import path

from .views import post_create_form_view,post_list_view, post_detail_view

app_name='posts'

urlpatterns = [
    path('',post_list_view,name='post-list-all'),
    path('create/',post_create_form_view, name='post-create'),
    path('<int:id>/', post_detail_view, name='post-detail'),
]
