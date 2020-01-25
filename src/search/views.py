from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from medicines.models import Medicine
# Create your views here.

class SearchMedicineView(ListView):
	
	template_name = "search/view.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SearchMedicineView,self).get_context_data(*args,**kwargs)
		query= self.request.GET.get('q')
		context['query'] = query
		#SearchQuery.objects.create(query=query)
		return context


	def get_queryset(self,*args,**kwargs):
		request = self.request
		method_dict = request.GET
		query = method_dict.get('q', None)
		print(query)
		if query is not None:
			return Medicine.objects.search(query)
		return Medicine.objects.featured()
		# __icontains = field contains this 
		# __iexact = fields is exactly this