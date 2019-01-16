from django.shortcuts import render
from .models import product,order
# Create your views here.
def index(request):
    context={
        "products":product.objects.all()[:3]
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