import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization":"viXux8DorwPIEd1fv3JU1YF8Yn5zaOqK97IJ4fPDmHkzAOtNyhDbmM4CgjuR","variables_values":"kartoos se panga tumhe padega mhnga","route":"otp","numbers":"9887223813"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)