
import random
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.db.models import Q  # Qオブジェクトをインポート
from .models import CafeMenu
from .forms import SearchForm
from django.utils.timezone import localtime,now  #日付の取得　localtimeで日本時間を表示
from django.core.mail import send_mail #メール送信
from django.conf import settings
from django.shortcuts import redirect
import logging
  
    

class MapView(TemplateView):
    template_name= 'map.html'


class SearchView(TemplateView):
    template_name = 'search.html'
    paginate_by=6

    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET or None)  # 検索フォームの初期化
        results = CafeMenu.objects.all()  # 初期状態で全件取得

        if form.is_valid():  # フォームが有効な場合
            query = form.cleaned_data.get('query')  # フォームから検索キーワードを取得
            if query:  # キーワードが空でない場合
                results = results.filter(
                    Q(name__icontains=query) | Q(category__icontains=query)
                )
        
        return render(request, self.template_name, {'form': form, 'results': results})
    
# ログ設定
logger = logging.getLogger(__name__)
 
#トップページView
class IndexView(TemplateView):
    template_name = 'base.html'
    #1ページに表示するレコードの件数
 
 
#メニューView
class MenuView(ListView):
    template_name = 'menu.html'  # レンダリングするテンプレート
    context_object_name = 'orderby_records'  # object_listキーに別名を設定
    model = CafeMenu  # 使用するモデルを指定
    paginate_by = 6  # 1つのページに6つ表示
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = 'menu'  # 現在のカテゴリ名を追加
        return context
 
 
#各カテゴリーごとのクラス(メニュー)
#コーヒー
class CoffeeDetail(ListView):
    template_name = 'coffee_list.html'
    context_object_name = 'orderby_records'
    model = CafeMenu
    paginate_by = 6
 
    def get_queryset(self):
        return CafeMenu.objects.filter(category='coffee')   #カテゴリーの絞り込みをして抽出
 
#エスプレッソ
class EspressoDetail(ListView):
    template_name = 'espresso_list.html'
    context_object_name = 'orderby_records'
    model = CafeMenu
    paginate_by = 6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='espresso')
   
#フラペチーノ
class FrapputinoDetail(ListView):
    template_name='frappuccino_list.html'
    context_object_name = 'orderby_records'
    model=CafeMenu
    paginate_by=6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='frappuccino')
 
#オリアート
class OleatoDetail(ListView):
    template_name='oleato_list.html'
    context_object_name = 'orderby_records'
    model=CafeMenu
    paginate_by=6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='oleato')
 
#ティー
class TeaDetail(ListView):
    template_name='tea_list.html'
    context_object_name = 'orderby_records'
    model=CafeMenu
    paginate_by=6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='tea')
 
#その他
class OthersDetail(ListView):
    template_name='others_list.html'
    context_object_name = 'orderby_records'
    model=CafeMenu
    paginate_by=6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='others')
 
 
#各カテゴリーごとのクラス(モバイルオーダー)
#コーヒー
class CoffeeMobile(ListView):
    template_name = 'coffee_m.html'
    context_object_name = 'orderby_records'
    model = CafeMenu
    paginate_by = 6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='coffee')
 
#エスプレッソ
class EspressoMobile(ListView):
    template_name = 'espresso_m.html'
    context_object_name = 'orderby_records'
    model = CafeMenu
    paginate_by = 6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='espresso')
   
#フラペチーノ
class FrapputinoMobile(ListView):
    template_name='frappuccino_m.html'
    context_object_name = 'orderby_records'
    model=CafeMenu
    paginate_by=6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='frappuccino')
 
#オリアート
class OleatoMobile(ListView):
    template_name='oleato_m.html'
    context_object_name = 'orderby_records'
    model=CafeMenu
    paginate_by=6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='oleato')
 
#ティー
class TeaMobile(ListView):
    template_name='tea_m.html'
    context_object_name = 'orderby_records'
    model=CafeMenu
    paginate_by=6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='tea')
 
#その他
class OthersMobile(ListView):
    template_name='others_m.html'
    context_object_name = 'orderby_records'
    model=CafeMenu
    paginate_by=6
    def get_queryset(self):
        return CafeMenu.objects.filter(category='others')
 
 
 
 
#モバイルオーダーView
class MobileView(TemplateView):
    template_name='mobile.html'
 
#商品選択ページ
class Mobile_OrderView(ListView):
    template_name='mobile_order.html'
    context_object_name = 'orderby_records'  # object_listキーに別名を設定
    model = CafeMenu  # 使用するモデルを指定
    paginate_by=6  #1つのページに6つ表示
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        # セッションから選択された商品を取得（例として、商品IDのリストを使う）
        selected_items = self.request.session.get('selected_items', [])  # セッションから選んだ商品を取得
        total_price = sum(float(item.get('price', 0)) for item in selected_items)  # 商品価格を合計
       
        # 合計金額と商品情報をコンテキストに追加
        context['total_price'] = total_price
        context['selected_items'] = selected_items
 
        return context
 
    def send_order_email(self, order_number, selected_items, total_price):
        """
        注文内容を Gmail に送信する関数
        :param order_number: 注文番号
        :param selected_items: 選択された商品のリスト
        :param total_price: 合計金額
        :param sender_email: ログイン中のユーザーのメールアドレス
        """
        # 注文情報をメールで送信
        subject = f"注文番号: {order_number} の確認"
        message = f"以下の内容で注文を受け付けました。\n\n"
        for item in selected_items:
            message += f"商品名: {item['name']} - 価格: {item['price']}円\n"
        message += f"\n合計金額: {total_price}円"
       
        # 受信者のメールアドレス（仮に 'user@example.com'）ここ変える
        recipient_list = ['djangotailang71@gmail.com']
 
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
 
    def post(self, request, *args, **kwargs):
        # 注文確認の POST リクエストを受けたときに処理を実行
        order_number = random.randint(100000, 999999)  # ランダムな注文番号を生成
       
        # セッションから選択した商品を取得
        selected_items = request.session.get('selected_items', [])
        total_price = sum(item['price'] for item in selected_items)
       
        # メールを送信
        self.send_order_email(order_number, selected_items, total_price)
       
        # 注文情報をセッションに保存
        request.session['order_number'] = order_number
       
        # 注文完了ページにリダイレクト
        return redirect('cafe:mobile_tyumon')  # 注文完了ページにリダイレクト
 
 
#注文確認ページ
class Mobile_pyView(TemplateView):
    template_name='mobile_order_py.html'
 
#注文完了ページ
class Mobile_tyumonView(TemplateView):
    template_name = 'mobile_tyumon.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = now().date()  # 今日の日付を取得
        current_time = localtime(now())  # 現在の日付と時刻を取得
        context['current_date'] = current_time.strftime('%Y-%m-%d')  # 年-月-日形式
        context['current_time'] = current_time.strftime('%H:%M:%S')  # 時:分:秒形式
 
        # セッションに注文番号が保存されていないか、または日付が異なる場合
        if not self.request.session.get('order_number') or self.request.session.get('order_date') != str(today):
            # 注文番号を生成する処理
            order_number = self.generate_unique_order_number()
            self.request.session['order_number'] = order_number
            self.request.session['order_date'] = str(today)  # 日付も保存してチェック
 
        # セッションから注文番号を取得
        context['order_number'] = self.request.session['order_number']
        return context
 
    def generate_unique_order_number(self):
        # すでに生成済みの注文番号を確認する仕組み（例: キャッシュやデータベース）
        used_numbers = self.get_used_order_numbers()
       
        # 一意な注文番号を生成
        while True:
            order_number = random.randint(100000, 999999)
            if order_number not in used_numbers:
                self.save_order_number(order_number)  # 保存
                return order_number
 
    def get_used_order_numbers(self):
        # 過去に使用された注文番号を取得（ここでは仮に空リストとしています）
        # 例えばキャッシュやDBに保存して取得する形を想定
        return []
 
    def save_order_number(self, order_number):
        # 生成した番号を保存する仕組み（キャッシュやDBに保存する処理を実装）
        # ここでは仮の処理としてパスしています
        pass


