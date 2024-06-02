from django.urls import path

from .views import SignUpView, log_out

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', log_out, name='logout')
]
