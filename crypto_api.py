import requests

def getUserInput():
    # Input a cryptocurrency: bitcoin, ethereum, dogecoin
    cryptoNames = input('Input a cryptocurrency: ')
    vs_currency = input('Input a currency: ')
    print("\n")
    cryptoNames = cryptoNames.replace(" ", "")
    # print(cryptoNames)
    return cryptoNames, vs_currency    
    


def main():
    
    nameCrypto = getUserInput()
    # print(nameCrypto)
    names = nameCrypto[0]
    currency = nameCrypto[1]
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': nameCrypto[0], 'vs_currencies': nameCrypto[1]}
    response = requests.get(url, params=params)
    dict = response.json()
    # print(str(dict) + "22")
    for name in names.split(','):
        if (name in dict.keys()):
            # The price of eos is 0.872004 USD
            # The price of bitcoin is 0.872004 USD
            # The price of ethereum is 0.872004 USD    
            print("The price of " + name + " is " + str(dict[name][currency]) + " " + str.upper(currency) + '\n')
        else:
            print("Not a valid crypto coin!")
main()

