from django.urls import path, include
from .views import (CountryAPIViewSet, CityAPIViewSet, AddressAPIViewSet, CustomersAPIViewSet, CommentAPIViewSet,
                    CategoryAPIViewSet, ProductAPIViewSet, CartAPIViewSet, BillingAPIViewSet)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="SHOP FOOD API",
        default_version='v1',
        description="Demo SHOP FOOD API",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='srmslogan6040@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)

router = DefaultRouter()
router.register('country', viewset=CountryAPIViewSet)
router.register('city', viewset=CityAPIViewSet)
router.register('address', viewset=AddressAPIViewSet)
router.register('customers', viewset=CustomersAPIViewSet)
router.register('comments', viewset=CommentAPIViewSet)
router.register('category', viewset=CategoryAPIViewSet)
router.register('products', viewset=ProductAPIViewSet)
router.register('cart', viewset=CartAPIViewSet)
router.register('billing', viewset=BillingAPIViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
    path('api-auth/', include('rest_framework.urls')),
]
