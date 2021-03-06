"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from user.views import loginView, logoutView, Register
from tasks.views import *
from categories.views import *

urlpatterns = [
    path('board/', board, name='board'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('home/', home, name='home'),
    path('category/create/', CategoryCreate.as_view(), name='createcategory'),
    path('category/list', CategoryListView.as_view(), name='listcategory'),
    path('category/delete/<int:id>/', deleteCategory, name='deletecategory'),
    path('category/<int:id>/edit', CategoryUpdate.as_view(), name='editcategory'),
    path('task/create/', CreateTask.as_view(), name='createtask'),
    path('task/list/', TaskListView.as_view(), name='listtask'),
    path('task/update/<int:id>/', UpdateTask.as_view(), name='updatetask'),
    path('task/delete/<int:id>/', DeleteTask.as_view(), name='deletetask'),
    path('task/<int:id>/', jsonTasks, name='endpoint'),
    path('board/<int:id>/', board, name='board'),

]

