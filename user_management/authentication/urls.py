from django.urls import path
from authentication.views import RegisterView, GroupView,AddUserToGroupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_by_login'),
    path('login/refresh_login_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('creategroup/', GroupView.as_view(), name='create_group'),
    path('AddUserToGroup/', AddUserToGroupView.as_view(), name='add_user_to_group'),
]