# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from app.models import *

def index(request):
    template_name = 'index.html'
    quotes = Quote.objects.all()
    context = {
        'quotes':quotes
    }
    return render(request, template_name, context)

def add_quote(request):
    if request.method == 'POST':
        quote_text = request.POST.get('quote_text')
        quote_comment = request.POST.get('quote_comment')
        quote_author = request.POST.get('quote_author')

        comment = Comment()
        comment.text = quote_comment
        comment.save()

        author,created = Author.objects.get_or_create(name=quote_author)
        author.save()

        quote = Quote()
        quote.author = author
        quote.comment = comment
        quote.quote = quote_text
        quote.save()
        
        data = {
            'quote_text':quote_text,
            'quote_comment':quote_comment,
            'quote_author':quote_author,
        }
        import simplejson
        return HttpResponse(simplejson.dumps(data))




