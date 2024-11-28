from django.contrib import admin

# Register your models here.
# cafe/admin.py

from .models import CafeMenu  # CafeMenuモデルをインポート

# CafeMenuモデルをadminに登録
admin.site.register(CafeMenu)
