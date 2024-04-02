from django.urls import path,include
from .views import signup, login ,userpage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[path('signup/',signup,name="signup"),
             path('login/', login, name='login'),
             path('userpage/', userpage, name='userpage')]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)