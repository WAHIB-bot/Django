from rest_framework import serializers
from .models import Banner,Banner_grid,Slider,featured_prod

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__' 



class BannerGridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner_grid
        fields = '__all__'  



class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__' 

class FeaturedProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = featured_prod
        fields = '__all__'        