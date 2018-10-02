from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import ChapterSection, Issuance

#By default, all the fields of your model will be used. You can configure the index by creating a subclass of AlgoliaIndex and using the register decorator:

@register(ChapterSection)
class ChapterSectionIndex(AlgoliaIndex):
    fields = ('title', 'num', 'chapter', 'content')
    settings = {
				'searchableAttributes': ['title','content',],
				'attributesForFaceting': ['chapter',]
    }
    index_name = 'Chapters'

@register(Issuance)
class IssuanceIndex(AlgoliaIndex):
	fields = ('title', 'chapter_searchable','contents','slug')
	settings= {
				'searchableAttributes': ['title','contents'],
				'attributesForFaceting': ['chapter',]
	}
	index_name = 'Issuances'