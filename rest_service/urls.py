from django.urls import include, path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', views.StoreViewset, basename='test')

urlpatterns = [
    path('', include(router.urls))
]
