from django.urls import path
from . import views

app_name = 'issuances'
urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('issuances/<slug:slug>/', views.IssuanceView.as_view(), name='issuance_detail'),
	path('chapter/<slug:slug>/', views.ChapterView.as_view(), name='chapter_detail'),
	path('search/', views.SearchView.as_view(), name='search_detail'),
]