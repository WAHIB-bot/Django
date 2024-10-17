from django.urls import path
from .views import BannerAPIView,BannerGridListAPIView,SliderListAPIView,FeaturedProdListAPIView

urlpatterns = [
    path('banner', BannerAPIView.as_view(), name='banner-api'),
    path('banner-grid/', BannerGridListAPIView.as_view(), name='banner-grid-list'),
    path('slider/', SliderListAPIView.as_view(), name='banner-grid-list'),
    path('featured_product/', FeaturedProdListAPIView.as_view(), name='banner-grid-list'),
]
