from django.urls import path, include

from rest_framework import routers

from . import views
from . import api_views

router = routers.DefaultRouter()
router.register(r'characters', api_views.CharacterViewSet, basename='characters')

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('character/<int:pk>', views.CharacterView.as_view(), name='character'),
    path('create-character/', views.CreateCharacterView.as_view(), name='create_character'),
    path('api/v1/', include(router.urls)),
    path('api/v1/generate-biography/', api_views.CharacterBiographyView.as_view(), name='generate_biography'),
    path('api/v1/generate-portrait/', api_views.CharacterPortraitView.as_view(), name='generate_portrait'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
