from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from carts.models import Cart
from .models import Medicine

# Create your views here.

class MedicineFeaturedListView(ListView):
	template_name = "medicines/list.html"

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Medicine.objects.all().featured()



class MedicineFeaturedDetailView(DetailView):
	queryset = Medicine.objects.all().featured()
	template_name = "medicines/featured_detail.html"


	# def get_queryset(self,*args,**kwargs):
	# 	request = self.request
	# 	return Medicine.objects.featured()




class MedicineListView(ListView):
	#queryset = Medicine.objects.all()
	template_name = "medicines/list.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(MedicineListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Medicine.objects.all()


def medicine_list_view(request):
	queryset = Medicine.objects.all()
	context ={
		'object_list': queryset
	}
	return render(request, "medicines/list.html",context)

class MedicineDetailGenericView(DetailView):
	queryset = Medicine.objects.all()
	template_name = "medicines/detail.html"

	def get_context_data(self, *args, **kwargs):
		context= super(MedicineDetailGenericView,self).get_context_data(*args,**kwargs)
		
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		generic_name = self.kwargs.get('generic_name')
		#instance = get_object_or_404(Medicine, generic_name=generic_name,active=True)
		try:
			instance = Medicine.objects.get(generic_name=generic_name,active=True)
		except Medicine.DoesNotExist:
			raise Http404("Not Found")
		except Medicine.MultipleObjectsReturned:
			qs = Medicine.objects.filter(generic_name=generic_name, active=True)
			instance = qs.first()
		except:
			raise Http404("xDD")
		return instance




class MedicineDetailView(DetailView):
	queryset = Medicine.objects.all()
	template_name = "medicines/detail.html"
	


	def get_context_data(self, *args, **kwargs):
		context = super(MedicineDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Medicine.objects.get_by_id(pk)
		if instance is none:
			raise Http404("Product doesnt exist")
		return instance


	# def get_queryset(self,*args,**kwargs):
	# 	request = self.request
	# 	pk = self.kwargs.get('pk')
	# 	return Medicine.objects.filter(pk=pk)



def medicine_detail_view(request, pk=None, *args, **kwargs):
	instance = Medicine.objects.all(pk=pk, featured= True) #id
	#instance = get_object_or_404(Medicine, pk=pk, featured=True)
	# try:
	# 	instance = Medicine.objects.get(id=pk)
	# except Medicine.DoesNotExist:
	# 	print('no medicine here')
	# 	raise Http404("Medicine does not exist")
	# except:
	# 	print("xD")

	instance = Medicine.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesn't exist")
	#print(instance)

	# qs = Medicine.objects.filter(id=pk)
	# if qs.exists() and qs.count()==1: #length(qs)
	# 	instance = qs.first()
	# else:
	# 	raise Http404("Medicine does not exist")



	context ={
		'object': instance
	}
	return render(request, "medicines/detail.html",context)

