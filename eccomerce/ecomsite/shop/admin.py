from django.contrib import admin
from .models import Products
from .models import Products,Order
# Register your models here.

admin.site.site_header = "JAGUARETE KAA S.A"
admin.site.site_title = "JAGUARETE KAA S.A"
admin.site.index_title = "Manage JAGUARETE KAA S.A shop"




class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="defaut")

    change_category_to_default.short_description ='Default Category' 
    list_display = ( 'title','discount_price','category','description',)
    search_fields = ('title','category')
    actions = ('change_category_to_default',)
    fields =('title','price','description','discount_price')
    

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)