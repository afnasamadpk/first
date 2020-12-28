"""project_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from newapp_2.views import home,show_products,add_products,edit_products,delete,add_category,register,log_in,log_out,edit_user,change_password,edit_edit

urlpatterns = [

    path('',home,name='home'),
    path('show/<int:id>/',show_products,name='show_products'),
    path('products/',add_products,name="add_products"),
    path('edit/<int:id>/',edit_products ,name="edit_products"),
    path('delete/<int:id>/',delete, name="delete"),
    path('category/',add_category,name="add_category"),
    path('register/',register,name="register"),
    path('login/',log_in,name="login"),
    path('logout/',log_out,name="logout"),
    path('edituser/',edit_user, name="edit_user"),
    path('changepassword/',change_password, name="change_password"),
    path('editedit/',edit_edit,name = 'edit_edit')

    # path('showc/',show_categoris,name="show_categoris")

    
    
    
]
