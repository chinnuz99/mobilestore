from django import forms
from django.forms import ModelForm
from.models import Mobile,Brand

class MobileCreationForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "brand": forms.Select(attrs={"class": "form-select"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "os": forms.TextInput(attrs={"class": "form-control"}),
            "memory": forms.TextInput(attrs={"class": "form-control"}),
            "specs": forms.TextInput(attrs={"class": "form-control"}),
            "images": forms.FileInput(attrs={"class": "form-control"}),


        }
class BrandCreationForm(ModelForm):
    class Meta:
        model= Brand
        fields="__all__"
        widgets={
           "brand_name":forms.TextInput(attrs={"class":"form-control"})

        }
# class UpdateMobileForm(ModelForm):
#     class Meta:
#         model= Mobile
#         fields="__all__"
#         widgets={
#             "mobile_name"
#
#         }
