from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.SignUp, name='SignUp'), 
    path('SignUp',views.SignUp, name='SignUp'), 
    path('SignIn',views.SignIn, name='SignIn'), 
    path('Welcome',views.Welcome, name='Welcome'),
    path('CovidiaTest',views.CovidiaTest, name='CovidiaTest'),
    path('SignOut',views.SignOut, name='SignOut')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)