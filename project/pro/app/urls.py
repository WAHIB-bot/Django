from django.urls import path
from . import views
from .views import CategoryListView,ItemListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category'),
    path('item', ItemListView.as_view(), name='item'),
    path('category_display', views.category_display, name='category_display'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)