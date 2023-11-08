# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]

from django.urls import path, re_path
from data_analysis import views

urlpatterns = [
    path("", views.index, name="home"),
    re_path(r"^test", views.test, name="test"),
    path(r"^train", views.train, name="train"),
]
