from django.contrib import admin

# Register your models here.
from .models import Medicine

class MedicineAdmin(admin.ModelAdmin):
	list_display = ['__str__','generic_name']
	class Meta:
		model = Medicine



admin.site.register(Medicine, MedicineAdmin)