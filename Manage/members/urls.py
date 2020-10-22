from django.urls import path
from .views import *

urlpatterns = [

    path('signup_cls/', SignUpAPIView.as_view(), name='signup_cls'),
    path('login_cls/', LoginAPIView.as_view(), name='login_cls'),
    path('logout_func/', logout_view, name='logout_func'),


]