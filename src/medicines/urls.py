

from django.conf.urls import url


from .views import( 
		MedicineListView,
		MedicineDetailGenericView,
		
	   )

urlpatterns = [
	url(r'^$', MedicineListView.as_view(), name='list'),
	url(r'^(?P<generic_name>[\w-]+)/$', MedicineDetailGenericView.as_view(), name='detail'),
    
]

