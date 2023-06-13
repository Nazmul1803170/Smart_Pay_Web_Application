from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('registration', registration ,name='registration'),
    path('addcard/', addcard, name='addcard'),
    path('tripping/', tripping, name='tripping'),
    path('recharge/', addRecharge, name='recharge'),
    path('bus_reg/', bus_registration, name='bus_reg'),
]