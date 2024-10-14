from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[path('signup/',signup,name="signup"),
             path('login/', login, name='login'),
             path('userpage/', userpage, name='userpage'),
            #  path('/', userpage, name='userpage')
             path('doctor_search/', search_doctors, name='search'),
             path('doctor_result/', doctor_result, name='doctor_result'),
             ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)