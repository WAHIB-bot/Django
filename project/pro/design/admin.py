from django.contrib import admin
from .models import Banner,Banner_grid,featured_prod

class SingletonModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Banner.objects.exists()

    def changelist_view(self, request, extra_context=None):
        try:
            banner = Banner.get_solo()
            return self.change_view(request, object_id=str(banner.id))
        except Banner.DoesNotExist:
            return super().changelist_view(request, extra_context)

admin.site.register(Banner, SingletonModelAdmin)



@admin.register(Banner_grid)
class BannerGridAdmin(admin.ModelAdmin):
    list_display = ['heading', 'updated_at']

from django.contrib import admin
from .models import Slider

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading', 'updated_at')

@admin.register(featured_prod)
class FeaturedProdAdmin(admin.ModelAdmin):
    list_display = ('heading', 'item')
