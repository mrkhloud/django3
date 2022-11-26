from django.urls import path

from .endpoint import (
    auth_view,
    views
)


urlpatterns = [
    path('', auth_view.google_login)
]
