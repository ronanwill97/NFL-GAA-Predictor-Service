from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt  # You might want to handle CSRF differently for AJAX requests
def create_payment(request):
    try:
        # Calculate or retrieve amount here
        amount = 500  # Amount in cents

        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='euro',
            payment_method_types=['card'],
        )

        return JsonResponse({
            'clientSecret': payment_intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=403)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']  # contains a stripe.PaymentIntent
        # Perform actions after payment success
        pass
    # ... handle other event types

    return HttpResponse(status=200)
