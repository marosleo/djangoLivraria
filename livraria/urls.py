#Urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

#Specular
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

#Rest Framework
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#Views
from core.views import AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroViewSet

#Media
from media.router import router as media_router

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    #Admin
    path("admin/", admin.site.urls),
    #SimpleJWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #API
    path("api/", include(router.urls)),
    #Media
    path("api/media/", include(media_router.urls)),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    )
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
