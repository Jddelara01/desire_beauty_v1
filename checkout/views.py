from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "The bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NvDytHgiTRrCIKhx5mLEdWHcerucfFb27qfnrVYco6mLonOTaCqzyuN25VF9l5hsB4Nkp8KKAEX4Gnlw72zLjuK00cQActR8X',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
