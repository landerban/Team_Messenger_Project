from django.urls import path
from . import views
app_name='users'
urlpatterns = [
    path('register',views.user_register,name="register"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('<int:userid>',views.user_profile,name="profile"),
    path('api/get_user',views.get_user,name="get_user"),
    path('api/create_user',views.create_user,name="create_user"),
]