# Create your views here.
import simplejson

from django.http import HttpResponse, Http404
from django.shortcuts import render
from app.forms import QuoteForm
from app.models import Quote, Author, Comment

def index(request):
    template_name = 'index.html'

    quotes = Quote.objects.all()
    quote_form = QuoteForm(prefix='quote')

    context = {
        'quotes': quotes,
        'quote_form': quote_form,
    }
    return render(request, template_name, context)

def add_quote(request):
    if request.method == 'POST':
        print request.POST
        post_quote = ''
        post_comment = ''
        post_author = ''

        quote_form = QuoteForm(request.POST.copy(), prefix='quote')
        if quote_form.is_valid():
            cd = quote_form.cleaned_data
            post_quote = cd['quote']
            post_comment = cd['comment']
            post_author = cd['author']

            comment = Comment()
            comment.text = post_comment
            comment.save()

            author, created = Author.objects.get_or_create(name__iexact=post_author)
            author.name = post_author
            author.save()

            quote = Quote()
            quote.author = author
            quote.comment = comment
            quote.quote = post_quote
            quote.save()
        
        data = {
            'quote_text': post_quote,
            'quote_comment': post_comment,
            'quote_author': post_author,
        }

        return HttpResponse(simplejson.dumps(data))
    raise Http404

def delete_quote(request):
    if request.method == 'POST':
        quote_id = request.POST.get('quote_id')
        quote = Quote.objects.filter(id=quote_id)
        if quote.exists():
            quote.delete()
            return HttpResponse(simplejson.dumps({'success':'true'}))



