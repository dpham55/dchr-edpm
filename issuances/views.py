import datetime
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Issuance, Chapter, IssuanceContent, ChapterSection

# Create your views here.

class HomeView(generic.ListView):
	template_name = 'issuances/home.html'
	context_object_name = 'latest_issuance_list'
	model = Issuance

	def get_queryset(self):
		return Issuance.objects.filter(publish__lte=timezone.now()).exclude(publish__exact=None).exclude(expiration_date__lte=timezone.now()).order_by('-effective_date')[0:3]

class IssuanceView(generic.DetailView):
	template_name = 'issuances/issuance.html'
	model = Issuance

class ChapterView(generic.DetailView):
	template_name = 'issuances/chapter.html'
	model = Chapter
	slug_field = 'slug'
	slug_url_kwarg = 'slug'

class SearchView(generic.ListView):
	template_name = 'issuances/search.html'
	model = Chapter