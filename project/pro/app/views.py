from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import category,items
from .serializer import CategorySerializer,ItemSerializer
from rest_framework import status 

class CategoryListView(APIView):
    def get(self, request):
        try:
            categories = category.objects.all()  
            if categories.exists():
                serializer = CategorySerializer(categories, many=True, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)  
            else:
                return Response({'detail': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)  
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

class ItemListView(APIView):
    def get(self, request):
        try:
            item = items.objects.all()  
            if item.exists():
                serializer = ItemSerializer(item, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK) 
            else:
                return Response({'detail': 'No items found'}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def category_display(request):
    return render('category.html',request)    


