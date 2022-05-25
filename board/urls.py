from django.urls import include, path
from rest_framework import routers
from board import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'terms', views.TermViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
