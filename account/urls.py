from django.urls import path
from . import views

urlpatterns = [
    path('corporation/', views.corporation, name='corporation'),
    path('individual/', views.individual, name='individual'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name = 'logout'),
]