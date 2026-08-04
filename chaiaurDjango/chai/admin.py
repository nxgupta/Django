from django.contrib import admin
from .models import ChaiVariety, Store, ChaiReview, ChaiCertificate
# Register your models here
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    fk_name = 'chai'
    extra = 1

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created_at')
    inlines = [ ChaiReviewInline ]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number',)

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)