from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, \
    ShowProfilePageView, EditProfilePageView, CreateProfilePageView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile/', CreateProfilePageView.as_view(), name='create_profile_page'),
]
