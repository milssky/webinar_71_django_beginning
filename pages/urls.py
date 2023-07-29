from django.urls import path

from . import views


urlpatterns = [
    path("", views.index_view),
    path("users/<int:id>/", views.get_users)  # http://127.0.0.1:8000/users/1/
]
