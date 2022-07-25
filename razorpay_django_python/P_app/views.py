from django.shortcuts import render, HttpResponse
from P_app.models import *
from P_app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
import sys
import razorpay
from payment_D import settings
# import requests
# import json

# Create your views here.

class Order_payment(APIView):
    def post(self, request,formate = None):
        currency = "INR"
        data = request.data
        name = data['name']
        amount = data['amount']
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        # # id = razorpay_order["id"]
        # # razorpay_order_obj = Order.objects.create(
        # #     name=name, amount=amount, provider_order_id=[id]
        # )
                
        # order id of newly created order.
        razorpay_order = razorpay_order['id']
        callback_url = 'paymenthandler/'
    
        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
    
        return render(request, 'index.html', context=context)