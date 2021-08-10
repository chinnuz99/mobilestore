from django.shortcuts import render,redirect
from.forms import MobileCreationForm,BrandCreationForm
from.models import Brand
from.models import Mobile
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")
def mobile_create(request):
    context={}
    form=MobileCreationForm()
    context["form"]=form
    if request.method=="POST":
        form=MobileCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"mobile created")
            return redirect("addmobiles")
        else:
            messages.error(request,"mobile can't be added")
            context["form"]=form
            return render(request,"mobile_create.html",context)
    else:
        context["form"] = form
        return render(request, "mobile_create.html", context)

def mobile_list(request):
    mobiles=Mobile.objects.all()
    context={"mobiles":mobiles}
    return render(request,"list_mobile.html",context)

def mobile_update(request,id):
    mobile=Mobile.objects.get(id=id)
    form=MobileCreationForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=MobileCreationForm(data=request.POST,files=request.FILES,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("listmobiles")
        else:
            context={}
            context["form"]=form
            return render(request,"mobile_edit.html",context)

    return render(request, "mobile_edit.html", context)

def mobile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context={"mobile":mobile}
    return render(request,"mobile_detail.html",context)

def remove_mobile(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return redirect("listmobiles")

def add_brand(request):
    context={}
    form=BrandCreationForm()
    context["form"]=form
    if request.method=="POST":
        form=BrandCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"brand created")
            return redirect("home")
        else:
            messages.error(request,"brand could not be created")
            context["form"]=form
            return render(request,"add_brand.html",context)
    else:
        context["form"] = form
        return render(request,"add_brand.html",context)




def list_brand(request):
    brand=Brand.objects.all()
    context={}
    context["brands"]=brand
    return render(request,"brand_list.html",context)
def view_brand(request,id):
    brand=Brand.objects.get(id=id)
    context = {}
    context["brands"] = brand
    return render(request, "view_brand.html", context)

def remove_brand(request,id):
    brand=Brand.objects.get(id=id)
    brand.delete()
    return redirect("brands")

def update_brand(request,id):
    brand=Brand.objects.get(id=id)
    form = BrandCreationForm(instance=brand)
    context = {"form": form}
    if request.method == 'POST':
        # form=BrandCreationForm(request.POST)
        form = BrandCreationForm(instance=brand, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbrand")
        else:
          context = {}
          context["form"] = form
          return render(request, "brand_edit.html", context)


    return render(request, "brand_edit.html", context)



