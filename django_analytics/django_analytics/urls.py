# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]

from django.urls import path, re_path
from data_analysis import views as da_views
from model_testing import views as mt_views

urlpatterns = [
    path("", da_views.index, name="home"),
    re_path(r"^test", mt_views.test, name="test"),
    re_path(r"^train", mt_views.train, name="train"),
]
