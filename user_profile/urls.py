from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .views import profile_detail, edit_profile

urlpatterns = [

    path('', profile_detail, name='profile_detail'),
    path('edit/', edit_profile, name='profile_edit'),

    path('change-password/',
         auth_views.PasswordChangeView.as_view(
             template_name='profile/change_password.html',
             success_url=reverse_lazy('profile_detail')
         ),
         name='change_password'
    ),
]