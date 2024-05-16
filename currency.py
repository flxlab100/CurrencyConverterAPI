import requests
API_KEY= 'fca_live_yxeh5KesWcrm2oUiVmrbpfPfojD1Nmt5mDNfZo5R'
BASE_URL=f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
CURRENCIES= ['USD','CAD','EUR','AUD','CNY']

def convert_currency(base):
    currencies=','.join(CURRENCIES)
    url=f'{BASE_URL}&base_currency={base}&currencies={currencies}'
    try:
       reponese=requests.get(url)
       data=reponese.json()
       print(data)
       return data
    except Exception as e:
        print(e)
        return None
convert_currency('CAD')