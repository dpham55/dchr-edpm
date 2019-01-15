import datetime, re
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.contrib.admin import SimpleListFilter
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

from .models import Issuance, IssuanceContent, Chapter, Attachment, ChapterSection


# Classes for CKEditor App/Plug-in
class ChapterSectionAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	class meta:
		model = ChapterSection

class IssuanceAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	class meta:
		model = Issuance

class IssuanceContentAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	class meta:
		model = IssuanceContent

# Admin stuff
class ChapterInline(admin.TabularInline):
	model = Issuance.chapter.through
	extra = 0
	verbose_name = 'Related issuances/chapter'
	verbose_name_plural = 'Related issuance/chapters'

class ChapterSectionInline(SortableStackedInline):
	model = ChapterSection
	extra = 0
	verbose_name = 'Section'
	verbose_name_plural = 'Sections'

class IssuanceContentInline(SortableStackedInline):
	model = IssuanceContent
	extra = 0
	verbose_name = 'Issuance Section'
	verbose_name_plural = 'Issuance Sections'

class AttachmentInline(admin.TabularInline):
	model = Attachment
	extra = 0

class ActiveFilter(SimpleListFilter):
	title = 'currently active'
	parameter_name = 'active'

	def lookups(self, request, model_admin):
		return (
			('Yes', ('Yes')),
			('No', ('No')),
		)

	def queryset(self, request, queryset):
		if self.value() == 'Yes':
			return queryset.exclude(expiration_date__lte=datetime.datetime.now().date())
		if self.value() == 'No':
			return queryset.exclude(expiration_date__gte=datetime.datetime.now().date()).exclude(expiration_date__isnull=True)

class ChapterAdmin(NonSortableParentAdmin):
	fieldsets = [
		(None,						{'fields':['title','chapter_no','description',]})
	]
	inlines = [ChapterSectionInline]
	list_display = ('chapter_no','title')

class ChapterSectionAdmin(admin.ModelAdmin):
	form = ChapterSectionAdminForm
	fieldsets = [
		(None,						{'fields':['title','num','content',]})
	]

class IssuanceAdmin(NonSortableParentAdmin):
	# form var Req by CKEditor
	#form = IssuanceAdminForm

	# Regular Django
	fieldsets = [
		('ISSUANCE INFO',           {'fields': ['title','slug','legacy_id','issuance_number','effective_date','expiration_date']}),
		('Publish',     			{'fields': ['banner_image','publish',]}),
	]
	inlines = [ChapterInline, IssuanceContentInline, AttachmentInline,]
	list_display = ('i_id','title','effective_date','expiration_date','is_active','publish','lastmodified')
	list_filter = [ActiveFilter,'effective_date','expiration_date','chapter',]
	search_fields = ['title','content',]
	prepopulated_fields = {'slug': ('title',)}

class IssuanceContentAdmin(admin.ModelAdmin):
	form = IssuanceContentAdminForm
	fieldsets = [
		(None,						{'fields': ['header','content',]}),
	]

class AttachmentAdmin(admin.ModelAdmin):
	readonly_fields = ('issuance',)
	pass


# Register your models here.
admin.site.register(Issuance, IssuanceAdmin)
admin.site.register(Chapter, ChapterAdmin)
#admin.site.register(Attachment, AttachmentAdmin)