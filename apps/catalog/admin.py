from django.contrib import admin
from .models import Category, Product #Admin paneline Category ve Product modellerini ekliyoruz.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug") 
    prepopulated_fields = {"slug": ("name",)} #prepopulated_fields → Slug alanı, name alanına göre otomatik dolsun.
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "stock", "is_active")
    list_filter = ("is_active", "category")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")
    list_editable = ("price", "stock", "is_active")
#list_editable → Listede direkt düzenlenebilir sütunlar.

#Fiyat, stok, aktiflik → liste ekranında direkt değiştirilebilir.