import requests
import payu_sdk
client = payu_sdk.payUClient({"key":"FZn5Bu","salt":"uSESXnsRktc1QJUFsUaVCYsPnnC4P7BL"})
params = {"txnid":"LImp8l8tmToJ6x","amount":"10","productinfo":"redme","firstname":"pankaj","email":"pankaj.jkishore@gmail.com"}
apiHash = payu_sdk.Hasher.APIHash(params)
url = "https://secure.payu.in/_payment"
print(apiHash)

payload = "key=FZn5Bu&txnid=LImp8l8tmToJ6x&amount=10.00&firstname=pankaj&email=pankaj.jkishore@gmail.com&phone=9785012088&productInfo=redme\
&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash={}".format(apiHash)
headers = { "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" }


response = requests.request("POST", url, data=payload, headers=headers)


f = open("new.html",'w')
f.write(response.text)
f.close()

