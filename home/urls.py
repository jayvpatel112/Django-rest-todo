from django.urls import path
from .views import homeView, todoView, TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename='todo')

urlpatterns = [
    path("home/", homeView.as_view()),
    path("todo/", todoView.as_view())
]

urlpatterns += router.urls