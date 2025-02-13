from django.shortcuts import render
from .forms import CryptoForm
import requests

def get_crypto_price(coin, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    return data.get(coin, {}).get(currency, None)

def convert_crypto(amount, coin, currency):
    price = get_crypto_price(coin, currency)
    if price is not None:
        return amount * price
    return None

def crypto_view(request):
    price = None
    converted_amount = None
    if request.method == 'POST':
        form = CryptoForm(request.POST)
        if form.is_valid():
            coin = form.cleaned_data['coin']
            currency = form.cleaned_data['currency']
            amount = form.cleaned_data['amount']
            price = get_crypto_price(coin, currency)
            if price is not None:
                converted_amount = convert_crypto(amount, coin, currency)
    else:
        form = CryptoForm()

    return render(request, 'cryptoapp/crypto_converter.html', {
        'form': form,
        'price': price,
        'converted_amount': converted_amount,
    })
