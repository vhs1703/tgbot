



import stripe

import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode



def get_payment_link(product_id,link):

    stripe.api_key = 'sk_test_51Ong6HJrdIO4YObvfPnric8LaycBt0gOaTL756jGvjLeAFhqLD7DgBBtjMSQXiGlJR07qq4Qo1EWkkzna9DdA2nK00YzUMao4u'

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': product_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url=link.invite_link,
            cancel_url='https://google.com/',
        )
        session.success_url
        return session.url

    except stripe.error.StripeError as e:
        print("Error creating checkout session:", e)


    



