from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Banner,Banner_grid,Slider,featured_prod
from .serializers import BannerSerializer,BannerGridSerializer,SliderSerializer,FeaturedProdSerializer

class BannerAPIView(APIView):
    def get(self, request):
        try:
            banner = Banner.get_solo()
            serializer = BannerSerializer(banner)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Banner.DoesNotExist:
            return Response({'error': 'Banner not found'}, status=status.HTTP_404_NOT_FOUND)


class BannerGridListAPIView(APIView):
    def get(self, request):
        banners = Banner_grid.objects.all()
        serializer = BannerGridSerializer(banners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SliderListAPIView(APIView):
    def get(self, request):
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

class FeaturedProdListAPIView(APIView):
    def get(self, request):
        featured_prods = featured_prod.objects.all()
        serializer = FeaturedProdSerializer(featured_prods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)       