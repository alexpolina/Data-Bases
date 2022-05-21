from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.loginPage, name="loginPage"),
    path('loginUser/', views.loginUser, name="loginUser"),
    path('reg/', views.reg, name="reg"),
    path('regNewUser/', views.regNewUser, name="regNewUser"),
    path('logout/', views.logoutUser, name="logout"),
    path('addToCart/', views.addToShopingCart, name="addToCart"),
    path('ordering/',  views.ordering, name="ordering")
]