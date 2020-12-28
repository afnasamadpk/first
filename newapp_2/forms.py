from django import forms
from .models import Products,Category
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','price','image','description','category']

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        del self.fields['password']
