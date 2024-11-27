"""
URL configuration for grow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
import banknifty
import adhikaribrothers
from sensex.views import *
from nifty.views import *
from penny.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('railware/',railware,name='railware'),
    path('itc/',itc,name='itc'),
    path('bengalsteels/',bengalsteels,name='bengalsteels'),
    path('banknifty/',include('banknifty.urls')),
    path('adhikaribrothers/',include('adhikaribrothers.urls')),
]
