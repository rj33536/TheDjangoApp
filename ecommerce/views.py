from django.shortcuts import render
from .models import product
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