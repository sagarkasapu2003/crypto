from django import forms

class CryptoForm(forms.Form):
    coin = forms.CharField(label='Coin Name', max_length=100)
    currency = forms.CharField(label='Currency Symbol', max_length=10)
    amount = forms.FloatField(label='Number of Coins')
