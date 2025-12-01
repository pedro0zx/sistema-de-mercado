from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework import routers
from produtos.views import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

def api_root(request):
    return JsonResponse({
        "message": "Bem-vindo à API do Mercado!",
        "endpoints": {
            "produtos": "/api/produtos/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]



