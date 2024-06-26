"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
admin.site.site_header = "Software Eng Admin"
admin.site.site_title = "Software Eng Admin Portal"
admin.site.index_title = "Welcome to Software Eng Portal"
# This is for dbms
from django.conf import settings
from django.conf.urls.static import static
# Upto here

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('noadminpresent/', admin.site.urls),
    path('',include('home.urls')),
    path('dbms/',include('dbms.urls'))

]
# This is for dbms
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Upto here
urlpatterns += staticfiles_urlpatterns()