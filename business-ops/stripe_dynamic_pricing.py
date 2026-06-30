import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def generate_counter_offer_coupon(competitor_price, our_price):
    """Creates a temporary Stripe coupon if competitor price drops below ours."""
    if competitor_price < our_price:
        discount_percent = ((our_price - competitor_price) / our_price) * 100
        
        coupon = stripe.Coupon.create(
            percent_off=round(discount_percent + 2.0), # Beat them by 2%
            duration="once",
            name="DYNAMIC_COMPETITIVE_MATCH",
            max_redemptions=50
        )
        print(f"Generated competitive coupon: {coupon.id} at {coupon.percent_off}% off.")
        return coupon.id
    return None
