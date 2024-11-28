from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
 
 
#Djangoの管理画面でDBを登録
 
class CafeMenu(models.Model):
    #商品カテゴリー
    CATEGORY=(('coffee','コーヒー'),
              ('espresso','エスプレッソ'),
              ('oleato','オリアート'),
              ('frappuccino','フラペチーノ'),
              ('tea','ティー'),
              ('others','その他'),
              )
    #タイトル用のフィールド
    category = models.CharField(choices=CATEGORY, max_length=20, default='coffee')
    name=models.CharField(
                verbose_name='商品名',
                max_length=100
                )
    #商品価格用のフィールド
    price=models.DecimalField(max_digits=5, decimal_places=0)
            #max_digits→このフィールドに保存できる数値の最大桁数を指定
            #decimal_places→小数点以下の桁数を指定
    #商品説明用のフィールド
    description=models.TextField()
    #商品のイメージ画像のフィールド
    image=models.ImageField(upload_to='menu_images/')
    def __str__(self):
        return self.name

#注文内容の保存
class Cart(models.Model):
    """カート全体を表すモデル"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              null=True, blank=True,
                              verbose_name='ユーザー'
    )
    session_key = models.CharField(
        max_length=40, null=True, blank=True,
        verbose_name='セッションキー'
    )  # ログインしていないユーザー用
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"Cart ({self.user or 'Guest'}) - Created at {self.created_at}"
 
    def total_price(self):
        """カート内商品の合計金額を計算"""
        return sum(item.total_price() for item in self.items.all())
   
class Order(models.Model):
    """注文全体を管理するモデル"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             null=True, blank=True,
                             verbose_name='ユーザー'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='注文日時')
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='合計金額'
    )
    STATUS_CHOICES = (
        ('pending', '支払い待ち'),
        ('confirmed', '確認済み'),
        ('completed', '完了'),
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='注文ステータス'
    )
 
    def __str__(self):
        return f"注文 {self.id} - ユーザー: {self.user or 'ゲスト'} - ステータス: {self.status}"
 
 
class OrderItem(models.Model):
    """注文内の商品を管理するモデル"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='注文')
    product = models.ForeignKey(CafeMenu, on_delete=models.CASCADE, verbose_name='商品')
    quantity = models.PositiveIntegerField(verbose_name='数量')
 
    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
 
    def total_price(self):
        """このアイテムの合計金額"""
        return self.product.price * self.quantity