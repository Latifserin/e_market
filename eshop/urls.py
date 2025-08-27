from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),      # Anasayfa, hakkımızda, iletişim
    path("urunler/", include("apps.catalog.urls")),  # Katalog rotaları
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin başlıklarını Türkçeleştir
admin.site.site_header = "E-Mağaza Yönetim Paneli"
admin.site.site_title = "E-Mağaza Admin"
admin.site.index_title = "Kontrol Paneli"
