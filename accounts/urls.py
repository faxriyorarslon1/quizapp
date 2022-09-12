from django.urls import path
from knox import views as knox_views
# 'from accounts.views import registration_view
from . import views
app_name = "account"

urlpatterns = [
   path('register/',views.register_api),
   path('user/',views.get_user_data),
   path('login/',views.login_api),
   path('logout/',knox_views.LogoutView.as_view()),
   path('logoutall/',knox_views.LogoutAllView.as_view())
]
