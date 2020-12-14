from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.views.generic.base import TemplateView

app_name = 'CT'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='About'),
    path('', views.client_list, name='client_list'),
    path('client_list', views.client_list, name='client_list'),
    path('client/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('client/<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('mealtrack_list', views.mealtrack_list, name='mealtrack_list'),
    path('mealtrack/add/', views.mealtrack_new, name='mealtrack_new'),
    path('mealtrack/<int:pk>/edit/', views.mealtrack_edit, name='mealtrack_edit'),
    path('mealtrack/<int:pk>/delete/', views.mealtrack_delete, name='mealtrack_delete'),
]
