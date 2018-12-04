import datetime
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Chapter(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=800, blank=True, null=True)
	shorthand = models.SlugField(max_length=3, unique=True, null=True)

	def __str__(self):
		return self.shorthand

	@property
	def recent_issuance_list(self):
		return self.issuance_set.filter(publish__lte=timezone.now()).exclude(publish__exact=None).exclude(expiration_date__lte=datetime.datetime.now().date()).order_by('-effective_date')[0:3]

	def active_issuance_list(self):
		return self.issuance_set.filter(publish__lte=timezone.now()).exclude(publish__exact=None).exclude(expiration_date__lte=datetime.datetime.now().date()).order_by('-effective_date')

	def section_list(self):
		return self.chaptersection_set.order_by(pk)

	def nonblank_titles(self):
		return self.chaptersection_set.exclude(title__isnull=True).exclude(title__exact='')


class ChapterSection(models.Model):
	title = models.CharField(max_length=200,blank=True)
	num = models.CharField('Section Number', unique=True, max_length=10)
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	content = RichTextField()
	position = models.PositiveSmallIntegerField('position',null=True)
	class Meta:
		ordering = ['position']


class Issuance(models.Model):
	title = models.CharField(max_length=200)
	effective_date = models.DateField('Effective Date')
	expiration_date = models.DateField('Expiration Date', blank=True, null=True)
	chapter = models.ManyToManyField(Chapter)
	banner_image = models.ImageField('Banner Image', upload_to='media/issuance_banners/', default='media/images/placeholder_banner.jpg', null=True, blank=True)
	slug = models.SlugField(max_length=200, unique=True, null=True)
	publish = models.DateTimeField('published', blank=True, null=True, default=None)
	legacy_id = models.CharField('Legacy ID (Leave blank if not legacy)', max_length=30, blank=True, null=True, default=None)
	lastmodified = models.DateTimeField('Last Modified', auto_now=True)

	def chapter_searchable(self):
	    return self.chapter.first()

	def i_number():
			num = Issuance.objects.filter(legacy_id__exact=None).filter(publish__lte=timezone.now()).exclude(publish__exact=None).count()
			if num == None:
				return 1
			else:
				return num + 1

	issuance_number = models.IntegerField('Issuance Number', blank=True, null=True, default=i_number)

	def is_active(self):
		now = datetime.datetime.now().date()
		if self.expiration_date is None:
			return True
		else:
			return now <= self.expiration_date

	is_active.admin_order_field = 'expiration_date'
	is_active.boolean = True
	is_active.short_description = 'Active Issuance?'

	def is_published(self):
		now = datetime.datetime.now().date()
		if self.publish is None:
			return False
		else:
			return True

	def __str__(self):
		return self.title

	def i_id(self):
		if self.legacy_id is None:
			return "I-" + str(self.publish.year) + "-" + str(self.issuance_number)
		else:
			return self.legacy_id

	i_id.short_description = 'Issuance ID'
	i_id.admin_order_field = 'issuance_number'

	def contents(self):
	    contents = []
	    for i in self.issuance_content.all():
	        contents.append(i.content)
	    return ' '.join(contents)

	@property
	def published_list(self):
		return self.issuance.objects.filter(publish__lte=timezone.now()).exclude(publish__exact=None).order_by('publish')


class Attachment(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(blank = True, null = True)
	issuance = models.ForeignKey(Issuance, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class IssuanceContent(models.Model):
	header = models.CharField(max_length=150)
	content = RichTextField()
	issuance = models.ForeignKey(Issuance, related_name='issuance_content', on_delete=models.CASCADE)

	def __str__(self):
		return self.header

	def issuance_slug(self):
		return self.issuance.slug

	def chapter(self):
	 	return self.issuance.chapter.first()