from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('accounts/logout/', views.signout, name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.signin, name='signin')
]