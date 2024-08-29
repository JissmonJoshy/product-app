from django.shortcuts import render,redirect
from .models import Product
import os


def home(request):
    return render(request,'add_product.html')

def add(request):
    if request.method=="POST":
        p_name=request.POST['name']
        p_price=request.POST['price']
        p_quantity=request.POST['quantity'] 
        p_image=request.FILES.get('image')

        pro=Product(pro_name=p_name,pro_price=p_price,
                    pro_quantity=p_quantity,pro_image=p_image)
        
        print("Save data.........")
        pro.save()
    return redirect('show')

def show(request):
    prod=Product.objects.all()
    return render(request,'show_product.html',{'prod':prod})

def editpage(request,pk):
    prd=Product.objects.get(id=pk)
    return render(request,'edit.html',{'prd':prd})

def edit_product(request,pk):
    if request.method=="POST":
        prds=Product.objects.get(id=pk)
        prds.pro_name=request.POST.get('name')
        prds.pro_price=request.POST.get('price')
        prds.pro_quantity=request.POST.get('quantity')
        if len(request.FILES)!=0:
            if len(prds.pro_image)>0:
                os.remove(prds.pro_image.path)
                prds.pro_image = request.FILES.get('image')
            prds.save()
            return redirect('show')
        return render(request,'edit.html')


def deletepage(request,pk):
    pr=Product.objects.get(id=pk)
    pr.delete()
    return redirect('show')
