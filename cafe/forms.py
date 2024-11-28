from django import forms

class SearchForm(forms.Form):
    # コーヒー = forms.CharField(label='コーヒー', max_length=100, required=False)
    # エスプレッソ = forms.CharField(label='エスプレッソ', max_length=100, required=False)
    # オリアート = forms.CharField(label='オリアート', max_length=100, required=False)
    # フラペチーノ = forms.CharField(label='フラペチーノ', max_length=100, required=False)
    # ティー = forms.CharField(label='ティー', max_length=100, required=False)
    # その他 = forms.CharField(label='その他', max_length=100, required=False)
    query = forms.CharField(label='検索', max_length=100, required=False)
