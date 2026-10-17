from django.urls import path, include
from .routers import router_review

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("api-test/", include(router_review.urls))
]