"""
URL configuration for URLshortner project.

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
from django.urls import path

from urls.views import AllUrls, UrlDetail, index, MakeUrls, RedirectUrl, RegisterUser, AllUsers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/all/', AllUrls.as_view()),
    path ('api/<int:pk>/',UrlDetail.as_view()),
    # path ('index/',index),
    path('api/shorten/',MakeUrls.as_view()),
    path('<int:id>/',RedirectUrl.as_view()),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path ('register/', RegisterUser.as_view(), name='register'),
    path('users/', AllUsers.as_view())

]
