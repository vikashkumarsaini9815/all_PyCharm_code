import razorpay
client = razorpay.Client(auth=("rzp_live_Ekvd5mHS07WMMY", "wBvQwEWZvkgcvicD0BMoGzDv"))

# data = { "amount": 10*100, "currency": "INR", "receipt": "vicky_saini_11" }
# payment = client.order.create(data=data)
# print(payment)

# {'id': 'order_JC9OoZCBEbGzbx', 'entity': 'order', 'amount': 100, 'amount_paid': 0, 'amount_due': 100, 'currency': 'INR', 'receipt': 'vicky_saini_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1648392229}




params_dict ={'razorpay_payment_id': 'pay_JC9QWQwv7JZ3ij', 'razorpay_order_id': 'order_JC9OoZCBEbGzbx', 'razorpay_signature': '68f37f112921fed5ee43b8d5822db57f6c7816ce8759a14565d419aaa89e8c55'}
ver = client.utility.verify_payment_signature(params_dict)
print(ver)



