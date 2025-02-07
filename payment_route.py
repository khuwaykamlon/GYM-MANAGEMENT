@app.route('/pay', methods=['POST'])
def create_payment():
    amount = 5000  # Example: 50.00 USD in cents

    # Create a new Stripe payment session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Gym Membership',
                },
                'unit_amount': amount,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:5000/success',
        cancel_url='http://127.0.0.1:5000/cancel',
    )

    return redirect(session.url, code=303)
