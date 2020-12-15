# accounts/urls.py
from django.urls import path, include

from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('accounts.urls')),
]