from django.contrib import admin
from .models import Member
from .models import Product, Panier

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)

admin.site.register(Member, MemberAdmin)


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price",)

admin.site.register(Product, ProductAdmin)


# Register your models here.
class PanierAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity","total_price",)

admin.site.register(Panier, PanierAdmin)


