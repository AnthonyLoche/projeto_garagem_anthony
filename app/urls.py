from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from garagem.views import AcessorioViewSet, CorViewSet, ModeloViewSet, VeiculoViewSet

router = DefaultRouter()
router.register(r'acessorios', AcessorioViewSet, basename='acessorio')
router.register(r'cores', CorViewSet, basename='cor')
router.register(r'modelos', ModeloViewSet, basename='modelo')
router.register(r'veiculos', VeiculoViewSet, basename='veiculo')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
