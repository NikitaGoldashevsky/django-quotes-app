from django.shortcuts import render
from .models import Quote
import random

def random_quote(request):
    quotes = list(Quote.objects.all())
    if quotes:
        # выбор цитаты с учетом веса
        weights = [q.weight for q in quotes]
        quote = random.choices(quotes, weights=weights, k=1)[0]
        # увеличение счетчика просмотров
        quote.views += 1
        quote.save()
    else:
        quote = None

    return render(request, 'myapp/random_quote.html', {'quote': quote})
