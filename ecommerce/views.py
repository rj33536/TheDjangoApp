from django.shortcuts import render
from .models import product,order

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout

from django.urls import reverse
# Create your views here.
def index(request):
    context={
        "products":product.objects.all()[:3],
		"user":request.user
    }
    return render(request,'index.html',context=context)
def catalog(request):
    context={
        "products":product.objects.all()
    }
    return render(request,'catalog.html',context=context)
def products(request):
    return render(request,'product.html')
def FAQ(request):
    return render(request,'FAQ.html')
def policy(request):
    return render(request,'policy.html')
def checkout(request,product_id):
    context={
                "error":""

            }
    if(request.method=='POST'):
        if(request.POST['name']!='' and request.POST['Mobile']!='' and request.POST['Address']!='' and request.POST['email']!=''  and request.POST['Mobile'].isdigit() ):
            f=order(name=request.POST['name'],Mobile=request.POST['Mobile'],
                    email=request.POST['email'],Address=request.POST['Address'],
                    myproduct=product_id)
            f.save()
            context={
                "error":"order submitted successfully"

            }
        else:
            context={
                "error":"please fill correct information"

            }


    return render(request,'order.html',context=context)

'''
@login_required(redirect_field_name='login')
def myblogs(request):
	user = request.user
	MyBlogs = blog.objects.filter(author = user)
	context ={
		"user":user,
		"blogs":MyBlogs,
	}
	return render(request,'cart.html',context=context)
'''
def register(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse("index"))
	try:
		username = request.POST["username"]
		password = request.POST["password"]
		email = request.POST["email"]
		name = request.POST["fullname"]
		user = User.objects.create_user(username,email,password)
		user.first_name = name
		user.save()
		if user is not None:
			auth_login(request,user)
			return HttpResponseRedirect(reverse("index"))
		return render(request,"register.html",{"message":"Unable to register"})
	except Exception as e:
		print(e)
		return render(request,"register.html",{"message":None})


def login(request):
	try:
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request,username=username,password = password)
		print(user)
		if user is not None:
			auth_login(request,user)
			print("authenticated")
			return HttpResponseRedirect(reverse("index"))
		return render(request,"login.html",{"message":"Invalid Credentials"})
	except Exception as e:
		print(e)
		return render(request,"login.html",{"message":None})

@login_required(redirect_field_name='login')
def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse("index"))
