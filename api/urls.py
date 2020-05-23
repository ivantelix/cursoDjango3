from django.urls import path
from api import views
from api.api import UserAPI

urlpatterns = [
    path('example-post/', views.example_post, name="example-post"),
    path('example-get/', views.example_get, name="example-get"),
    path('create_user/', UserAPI.as_view(), name='api_create_user'),
]
