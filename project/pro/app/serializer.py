from rest_framework import serializers
from .models import category, items

class CategorySerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField()
    class Meta:
        model = category
        fields = ['c_id', 'name', 'image']  

    # def get_image_url(self, obj):
    #     request = self.context.get('request')
    #     if request and hasattr(obj, 'image') and obj.image:
    #         print("obj.image.url",obj.image.url)
    #         return request.build_absolute_uri(obj.image.url)  # Build the absolute URI for the image
    #     return None  
    # print("image_url",image_url)
    

class ItemSerializer(serializers.ModelSerializer):
    
    category = serializers.PrimaryKeyRelatedField(queryset=category.objects.all())

    class Meta:
        model = items
        fields = ['i_id', 'name', 'image', 'category']  
