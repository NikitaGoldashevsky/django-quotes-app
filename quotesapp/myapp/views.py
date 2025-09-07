from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F, ExpressionWrapper, IntegerField
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


def vote_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if request.method == "POST":
        vote_type = request.POST.get("vote")
        if vote_type == "like":
            quote.likes += 1
        elif vote_type == "dislike":
            quote.dislikes += 1
        quote.save()
    return redirect('random_quote')


def top_quotes(request):
    sort = request.GET.get("sort", "likes")

    quotes = Quote.objects.annotate(
        rating=ExpressionWrapper(F("likes") - F("dislikes"), output_field=IntegerField())
    )

    if sort == "likes":
        quotes = quotes.order_by("-likes")[:10]
    elif sort == "rating":
        quotes = quotes.order_by("-rating")[:10]
    elif sort == "views":
        quotes = quotes.order_by("-views")[:10]
    else:
        quotes = quotes.order_by("-likes")[:10]

    return render(request, "myapp/top_quotes.html", {"quotes": quotes, "sort": sort})
