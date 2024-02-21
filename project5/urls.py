"""project5 URL Configuration

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
from django.urls import path,include
from App import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include('django.contrib.auth.urls')),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('second/',views.second,name='second'),
    path('list/',views.list,name='list'),
    path('spare/',views.acessories,name='acessories'),
    path('checkout/', views.checkout, name='checkout'),
     path('contact/', views.contact, name='contact'),
    # path('checkout_success/', views.checkout, name='checkout_success'),
  
    path('feedback/', views.feedback, name='feedback'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    path('places/<str:place>/', views.places, name='places'),
    path('types/<str:type>/', views.types, name='types'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:vehicle_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:spare_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)