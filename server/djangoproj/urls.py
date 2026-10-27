"""
URL configuration for djangoproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from djangoapp import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('contact', views.contact),
    path('signup', views.signup),
    path('signout', views.signout),
    path('admin/', admin.site.urls),
    path('djangoapp/register', views.register),
    path('djangoapp/login', views.login_user),
    path('djangoapp/logout', views.logout_user),
    path('djangoapp/get_cars', views.get_cars),
    path('fetchDealers', views.get_dealers),
    path('fetchDealer/<int:dealer_id>', views.get_dealer),
    path('fetchDealers/<str:state>', views.get_dealers_by_state),
    path('fetchReviews/dealer/<int:dealer_id>', views.get_reviews),
    path('analyze/<path:review_text>', views.analyze_review),
]
