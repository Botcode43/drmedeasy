from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[path('signup/',signup,name="signup"),
             path('login/', login, name='login'),
             path('userpage/', userpage, name='userpage'),
            #  path('/', userpage, name='userpage')
             path('doctor_search/', search_doctors, name='doctor_search'),
             path('doctor_result/', doctor_result, name='doctor_result'),
             path('home_page/', home_page, name='home_page'),
               path('appointmet/',book_appointment,name="form_"),
    path('appointment/success/',appointment_success,name="appointment_success"),

             ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)