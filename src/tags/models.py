from django.db import models
from django.db.models.signals import pre_save, post_save
from onlinepharma.utils import unique_slug_generator
from django.urls import reverse
from medicines.models import Medicine
# Create your models here.

class Tag(models.Model):
	title 		= models.CharField(max_length=120)
	slug		= models.SlugField()
	timestamp	= models.DateTimeField(auto_now_add=True)
	active		= models.BooleanField(default=True)
	medicines	= models.ManyToManyField(Medicine, blank=True)


	def __str__(self):
		return self.title

def tag_pre_save_receiver(sender,instance,*args, **kwargs):
	if not instance.slug:
		instance.slug= unique_sulg_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender = Tag)

