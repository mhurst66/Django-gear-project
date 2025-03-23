from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('gear/', views.gear_index, name='gear-index'),
    path('user/', views.user_index, name='user-index'),
    path('gear/<int:gear_id>/', views.gear_detail, name='gear-detail'),
    path('gear/create/', views.GearCreate.as_view(), name='gear-create'),
    path('gears/<int:pk>/update/', views.GearUpdate.as_view(), name='gear-update'),
    path('gears/<int:pk>/delete/', views.GearDelete.as_view(), name='gear-delete'),
]
