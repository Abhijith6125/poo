"""training_center URL Configuration
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path,re_path
from registration import views

urlpatterns = [
    re_path(r'^registration',include("registration.urls")),
    path('admin/', admin.site.urls),
    re_path(r'^$',views.Home,name="Home"),
]
