import requests

def currency_convertor():
    api_key = 'cur_live_TCjxzYmE9R1CLUZLL3xAKhj2VdXfq4qSq8I1vRRn'
    url=f"https://api.currencyapi.com/v3/latest?apikey={api_key}"



    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        base_currency = data['data']['USD']['value']
        base_currency_needed=input("what base currency do you want? ")
        new_base_currency=base_currency/(data['data'][base_currency_needed.upper()]['value'])
        new_base_currency_input = float(input(f"Enter amount in {base_currency_needed}: "))
        desired_currency = input("what currency do you want to convert to? ")
        converted_currency = (new_base_currency_input * new_base_currency)* (data['data'][desired_currency.upper()]['value'])

        print(f"{converted_currency}{data['data'][desired_currency.upper()]}")
    else:
        print("something is wrong")




def main():
    while True:
        print('''
    ========curency convertor=======
    welcome to the currency convertor
    this convertor uses the latest 
    conversion rates for all currencies
    
    what do you want to do?
    1. convert currency
    2. exit
    ''')
        choice=input("option: ")
        if choice=='1':
            print('''
            Currencies must be input in
            abbreviations for example USD,
            GBP,JPY,KES,CAD.The input can 
            either be in lower case or upper 
            case.
            ''')
            currency_convertor()
        elif choice=="2":
            break
        else:
            print("invalid choice")

if __name__=="__main__":
    main()

