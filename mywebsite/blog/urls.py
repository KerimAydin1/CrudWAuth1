# blog/urls.py

from django.urls import path, include
from .views import BlogViewSet, SignUpView, HomePageView, AboutPageView, ContactPageView, authView
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import authView, home

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Home Page
    path('about/', AboutPageView.as_view(), name='about'),  # About Us Page
    path('contact/', ContactPageView.as_view(), name='contact'),  # Contact Us Page
    path('signaup/', SignUpView.as_view(), name='signup'),  # Sign Up Page
    path('api/', include(router.urls)),  # API URLs
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="authView"),
]   