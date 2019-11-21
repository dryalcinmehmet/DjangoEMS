"""EventApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('source/', include('source.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from EventApp.views import EventListView,EventCreateView, EventDetailView,SessionCreateView, SessionDetailView, SessionListView, UserViewSet,EventViewSet,SessionViewSet


router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/events', EventViewSet)
router.register(r'api/sessions', SessionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),    
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),

    path('event/list/', EventListView.as_view(), name='event_read'),
    path('event/create/', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_update'),

    path('session/list/', SessionListView.as_view(), name='session_read'),
    path('session/create/', SessionCreateView.as_view(), name='session_create'),
    path('session/<int:pk>/', SessionDetailView.as_view(), name='session_update')
]
