"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views



#code for video 6

#urlpatterns = [
 #   path('admin/', admin.site.urls),
 #  path('',views.index,name='index'), # path('about/',views.about,name='about'),]

#code for video 7,8 & 9

#urlpatterns = [
   # path('admin/', admin.site.urls),
    #path('',views.index,name='index'),
    #path('removepunc',views.removepunc,name='rempunc'),
    #path('capitalizefirst',views.capfirst,name='capfirst'),   
    #path('newlineremove',views.newlineremove,name='newlineremove'), 
    #path('spaceremove',views.spaceremove,name='spaceremove'),
    #path('charcount',views.charcount,name='charcount'),
#]

#code for video 10

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze',views.analyze,name='analyze'),
    path('ex1',views.ex1,name='ex1'),
]    