from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_quote, name='random_quote'),
	path('vote/<int:quote_id>/', views.vote_quote, name='vote_quote'),
	path('top/', views.top_quotes, name='top_quotes')
]

urlpatterns = [
    path('', views.random_quote, name='random_quote'),     
    path('top/', views.top_quotes, name='top_quotes'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('vote/<int:quote_id>/', views.vote_quote, name='vote_quote')
]
