from django.shortcuts import render
from .models import product,order
# Create your views here.
def index(request):
    return render(request,'index.html')
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
    if(request.method=='POST'):
        f=order(name=request.POST['name'],Mobile=request.POST['Mobile'],
                email=request.POST['email'],Address=request.POST['Address'],
                myproduct=product_id)
        f.save()
        print('saved')


    return render(request,'order.html')       