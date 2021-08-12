from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from customer import forms
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth.models import User
from owner.models import Mobile
# Create your views here.

class RegistrationView(TemplateView):
    form_class=forms.RegistrationForm
    template_name = "registration.html"
    model= User
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context={}
            context["form"]=form
            return render(request,self.template_name,self.context)

class SignInView(TemplateView):
    template_name = "login.html"
    form_class=forms.LoginForm
    context={}
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("customerhome")
            else:
                self.context["form"]=form
                return render(request, self.template_name, self.context)


class CustomerHomeView(ListView):
    template_name = "customer_home.html"
    model=Mobile
    context_object_name = "mobiles"
class ProductDetailView(DetailView):
    template_name = "productdetail.html"
    model = Mobile
    context_object_name = "mobile"






