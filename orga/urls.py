from django.urls import include, path
from rest_framework import routers
import orga.views  as views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'newsarticles', views.NewsArticleViewSet)
router.register(r'events', views.EventViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]