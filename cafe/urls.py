
from django.urls import path
from . import views
from .views import SearchView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'cafe'

urlpatterns = [

    path('',views.IndexView.as_view(),name='base'),
    path('menu/',views.MenuView.as_view(), name='menu'),
    path('map/',views.MapView.as_view(), name='map'),
    path('search/', SearchView.as_view(), name='search'),
    path('mobile/',views.MobileView.as_view(),name='mobile'),
    path('mobile_order/',views.Mobile_OrderView.as_view(),name='mobile_order'),
    path('mobile_order_py/',views.Mobile_pyView.as_view(),name='mobile_order_py'),
    path('mobile_tyumon/',views.Mobile_tyumonView.as_view(),name='mobile_tyumon'),
 
    #サイドバー(メニュー)
    path('menu/coffee',views.CoffeeDetail.as_view(), name='coffee'),
    path('menu/espresso',views.EspressoDetail.as_view(), name='espresso'),
    path('menu/frappuccino',views.FrapputinoDetail.as_view(), name='frappuccino'),
    path('menu/oleato',views.OleatoDetail.as_view(), name='oleato'),
    path('menu/tea',views.TeaDetail.as_view(), name='tea'),
    path('menu/others',views.OthersDetail.as_view(), name='others'),
 
    #サイドバー(モバイルオーダー)
    path('mobile_order/coffee_m',views.CoffeeMobile.as_view(), name='coffee_m'),
    path('mobile_order/espresso_m',views.EspressoMobile.as_view(), name='espresso_m'),
    path('mobile_order/frappuccino_m',views.FrapputinoMobile.as_view(), name='frappuccino_m'),
    path('mobile_order/oleato_m',views.OleatoMobile.as_view(), name='oleato_m'),
    path('mobile_order/tea_m',views.TeaMobile.as_view(), name='tea_m'),
    path('mobile_order/others_m',views.OthersMobile.as_view(), name='others_m'),  # 検索ビューのURL設定

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)







