from django.shortcuts import render,redirect,HttpResponse
from .models import Products,Category
from .forms import ProductModelForm,CategoryModelForm,RegistrationForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def home(request):
    category = Category.objects.all()

   
    context={ 
        
        'category':category

          
    }

    return render(request,"home.html",context)


@login_required(login_url="/login/")
def add_products(request):
    if request.method =='POST':
        form = ProductModelForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=FALSE)
            obj.user = request.user
            obj.save()
            return redirect('home')
        else:
            return render(request,'add_product.html',{'form':form})

    else:
        form = ProductModelForm()
        return render(request,'add_products.html',{'form':form})
@login_required(login_url="/login/")
def show_products(request,id):
    category = Category.objects.get(id=id)
    products = category.products_set.all()
    context = {
        'products':products
    }
    return render(request,'show_products.html',context)

def edit_products(request,id):
    product = Products.objects.get(id = id)
    if request.method =='POST':
        form = ProductModelForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:


            return render(request,'add_product.html',{'form':form})

    else:

        form = ProductModelForm(instance=product)
        return render(request,'add_products.html',{'form':form})



def delete(request,id):
    product = Products.objects.get(id=id) 
    category_id =  product.category.id
    product.delete()  
    return redirect(f'/show/{category_id}/')


@login_required(login_url="/login/")
def add_category(request):
    if request.method =='POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'add_category.html',{'form':form})

    else:
        form = CategoryModelForm()
        return render(request,'add_category.html',{'form':form})


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'register.html',{'form':form})

    else:
        form = RegistrationForm()
        return render(request,'register.html',{'form':form})

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('user name is incorrect')

    return render(request,'login.html')


def log_out(request):
    logout(request)
    return redirect('/login/')



def edit_user(request):
    
    if request.method =='POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'register.html',{'form':form})

    else:
        form = UserChangeForm()
        return render(request,'register.html',{'form':form})

def change_password(request):

    if request.method =='POST':
        form = PasswordChangeForm(data = request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(form.user)
            return redirect('home')
        else:
            return render(request,'register.html',{'form':form})

    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'register.html',{'form':form})



def edit_edit(request):
    return render(request,"edit.html")

# def show_categoris(request):
#     category = Category.objects.all()
   
#     context={ 
        
#         'category':category    
#     }

#     return render(request,"home.html",context)





