from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from . import views   

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#Register viewsets below
#router.register(r'enquiries', EnquiriesViewSet)

urlpatterns = [
    path('', views.base, name="base"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]