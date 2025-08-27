from django.db import models

class Category(models.Model):
    name = models.CharField("Kategori Adı", max_length=100, unique=True) # unique=true Bu alanın değeri her kayıtta eşsiz (tekil) olmalı.
    slug = models.SlugField("URL", max_length=110, unique=True)
    description = models.TextField("Açıklama", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
#blank=True → Formlarda boş geçilebilir (kullanıcı bu alanı doldurmasa da olur).
#null=True → Veritabanında NULL değeri alabilir (yani boş kaydedilebilir).
#auto_now_add=True kayıt eklenince otomatik ilk oluşturulma zamanı yazılır güncellenince değişmez
#auto_now=True  kayıt her güncellendiğinde en son değiştirilme zamanı yazılır

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE) #Eğer bir kategori silersen → ona bağlı tüm ürünler de silinir.
    name = models.CharField("Ürün Adı", max_length=200)
    slug = models.SlugField("URL", max_length=210, unique=True)
    description = models.TextField("Açıklama", blank=True)
    price = models.DecimalField("Fiyat", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Stok", default=0)
    image = models.ImageField("Fotoğraf", upload_to="products/", blank=True, null=True)
    is_active = models.BooleanField("Aktif mi?", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#default=0 Eğer kullanıcı bu alan için bir değer vermezse → varsayılan olarak 0 yazılır.
    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
