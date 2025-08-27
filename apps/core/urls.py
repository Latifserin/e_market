from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("hakkimizda/", views.about, name="about"),
    path("iletisim/", views.contact, name="contact"),
]
