from . import views
from django.urls import path

urlpatterns=[
    path('',views.apply),
    path('show',views.show),
    path('login',views.login),
    path('college',views.college)
]