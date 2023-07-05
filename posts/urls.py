from django.urls import path
from .views import post_create_form_view
app_name='posts'

urlpatterns = [
    path('create/',post_create_form_view, name='post-create'),
]
