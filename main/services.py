import stripe

from config.settings import STRIPE_SECRET_KEY
from main.models import Course, Payment


stripe.api_key = STRIPE_SECRET_KEY


def create_stripe_checkout_session(course_id):
    course = Course.objects.get(pk=course_id)

    product = stripe.Product.create(name=course.title)
    price = stripe.Price.create(unit_amount=course.price, currency='usd', product=product.get('id'))
    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
        mode="payment",
    )
    return session


def get_stripe_payment(pk):

    payment = Payment.objects.get(pk=pk)

    payment_detail = stripe.checkout.Session.retrieve(
        payment.stripe_id,
    )

    return payment_detail