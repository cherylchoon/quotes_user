from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..login.models import User
from .models import Quote, Fav
from .forms import QuoteForm
from django.contrib import messages

def login_reg(request):
    return redirect(reverse('users:user_index'))

def index(request):
    user_id = request.session['user_id']
    exclude_quote = Fav.objects.filter(user=user_id)
    exclude_id = []
    for q in exclude_quote:
        exclude_id += str(q.quote.id)
    context = {
        'quoteForm': QuoteForm(),
        'allQuotes': Quote.objects.exclude(id__in=exclude_id).order_by('-created_at'),
        'favQuotes': Fav.objects.filter(user=user_id)
    }
    return render(request, 'quotes/index.html', context)

def add_quotes(request):
    if request.method == 'POST':
        quoteForm = QuoteForm(request.POST)
        messages.add_message(request, messages.ERROR, quoteForm.errors)
        if quoteForm.is_valid():
            user_id = request.session['user_id']
            result = Quote.objects.add_quotes(request.POST, user_id)
            return redirect(reverse('quotes:quotes_index'))
        else:
            return redirect(reverse('quotes:quotes_index'))

def add_fav(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['user_id'])
        quote = Quote.objects.get(id=request.POST['quote_id'])
        try:
            Fav.objects.get(user=user, quote=quote)
        except:
            new_fav = Fav.objects.create(user=user, quote=quote)
    return redirect(reverse('quotes:quotes_index'))

def delete_fav(request):
    if request.method == 'POST':
        fav_id = request.POST['fav_id']
        Fav.objects.get(id=fav_id).delete()
        return redirect(reverse('quotes:quotes_index'))

def user_info(request, id):
    context = {
        'user_info': User.objects.get(id=id),
        'quotes': Quote.objects.filter(user=id)
    }
    return render(request, 'quotes/userinfo.html', context)
