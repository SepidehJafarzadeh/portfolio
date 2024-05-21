from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'images', views.ImageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

