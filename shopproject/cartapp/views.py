from django.shortcuts import render, redirect, get_object_or_404
from shopapp.models import product
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,pr_id):
    pr=product.objects.get(id=pr_id)
    try:
        cart=Cart.objects.get(c_id=cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(c_id=cart_id(request))
        cart.save()
    try:
        cart_item=CartItem.objects.get(prod=pr,cart=cart)
        if cart_item.quantity < cart_item.prod.stock:
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(prod=pr,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cartapp:cart_detail')

def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(c_id=cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total +=(cart_item.prod.price * cart_item.quantity)
            counter +=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,pr_id):
    cart=Cart.objects.get(c_id=cart_id(request))
    produc = get_object_or_404(product,id=pr_id)
    cart_item=CartItem.objects.get(prod=produc,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartapp:cart_detail')

def full_remove(request,pr_id):
    cart = Cart.objects.get(c_id=cart_id(request))
    produc = get_object_or_404(product, id=pr_id)
    cart_item = CartItem.objects.get(prod=produc, cart=cart)
    cart_item.delete()
    return redirect('cartapp:cart_detail')


