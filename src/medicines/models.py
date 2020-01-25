from django.db.models import Q
from django.db import models
from datetime import datetime
from django.utils import timezone
import random
import os
from django.db.models.signals import pre_save, post_save
from onlinepharma.utils import unique_slug_generator
from django.urls import reverse
# Create your models here.

def get_filename_ext(filename):
	base_name = os.path.basename(filename)
	name,ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	# print(instance)
	# print(filename)
	new_filename = random.randint(1,86372463274)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return "medicines/{new_filename}/{final_filename}".format(
		new_filename=new_filename, 
		final_filename=final_filename
		)
def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url


class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True,active=True)

	def search(self,query):
		lookups=(
			Q(title__icontains= query) |
				Q(generic_name__icontains=query) |
				Q(price__icontains=query) |
				Q(description__icontains=query) 
				 # Q(tag_slug__icontains#=query)  
				)

		return self.filter(lookups).distinct()

class MedicineManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().active()

	def featured(self):  #Medicine.objects.featured()
		return self.get_queryset().filter(featured=True)

	def get_by_id(self,id):
		qs = self.get_queryset().filter(id=id)  #Medicine.object
		if qs.count()==1:
			return qs.first()
		return None

	def search(self,query):
		return self.get_queryset().active().search(query)




class Medicine(models.Model): #Medicine_catagory
	title 				= models.CharField(max_length=120)
	description			= models.TextField()
	generic_name 		= models.SlugField(blank=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	mfg_date			= models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	exp_date			= models.DateField(auto_now=False, auto_now_add=False,default=timezone.now())
	price				= models.DecimalField(decimal_places=2, max_digits=20,default=39.99)
	quantity			= models.IntegerField(default=200)
	image				= models.ImageField(upload_to=upload_image_path, null=True, blank= True)
	featured			= models.BooleanField(default=False)
	active				= models.BooleanField(default=True)


	objects = MedicineManager()

	def get_absolute_url(self):
		#return "/medicines/{generic_name}/".format(generic_name=self.generic_name)
		return reverse("medicines:detail",kwargs={"generic_name": self.generic_name})

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	@property
	def name(self):
		return self.title
	

	

def medicine_pre_save_receiver(sender,instance,*args, **kwargs):
	if not instance.generic_name:
		instance.generic_name= unique_sulg_generator(instance)

pre_save.connect(medicine_pre_save_receiver, sender = Medicine)


