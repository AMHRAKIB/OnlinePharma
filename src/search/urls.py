

from django.conf.urls import url


from .views import ( 
		SearchMedicineView,
	   )

urlpatterns = [
	
	url(r'^$', SearchMedicineView.as_view(), name='query'),
	
    
]

