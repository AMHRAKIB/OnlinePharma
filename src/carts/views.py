from django.shortcuts import render, redirect

# Create your views here.
from orders.models import Order
from .models import Cart
from medicines.models import Medicine

def cart_home(request):
	cart_obj, new_obj= Cart.objects.new_or_get(request)
	# medicines = cart_obj.medicines.all()
	# total = 0
	# for x in medicines:
	# 	total += x.price
	# print(total)
	# cart_obj.total = total
	# cart_obj.save()
	return render(request, "carts/home.html", {"cart":cart_obj})



def cart_update(request):
	print(request.POST)
	medicine_id = request.POST.get('medicine_id')
	if medicine_id is not None:
		try:
			medicine_obj = Medicine.objects.get(id=medicine_id)
		except Medicine.DoesNotExist:
			print("Show message to user, medicine is gone?")
			return redirect("cart:home")
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if medicine_obj in cart_obj.medicines.all():
			cart_obj.medicines.remove(medicine_obj)
		else:	
			cart_obj.medicines.add(medicine_obj) #cart_obj.medicines.add(obj)
		request.session['cart_items'] = cart_obj.medicines.count()


	return redirect("cart:home")
	#return redirect(medicine_obj.get_absolute_url())
	

def checkout_home(request):
	cart_obj, cart_created= Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created and cart_obj.medicines.count() == 0:
		return redirect("cart:home")
	else:
		order_obj, new_order_obj= Order.objects.get_or_create(cart=cart_obj)
	return render(request,"carts/checkout.html",{"object": order_obj})








