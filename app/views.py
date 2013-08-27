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

            quote = Quote()

            if post_comment:
                print 'post_comment',post_comment
                comment = Comment()
                comment.text = post_comment
                comment.save()
                quote.comment = comment

            author, created = Author.objects.get_or_create(name__iexact=post_author)
            if post_author:
                author.name = post_author
            else:
                author.name = 'Anonymous'
            author.save()

            quote.author = author
            quote.quote = post_quote
            quote.save()
        else:
            print "Quote_form is not valid!"
        
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
    else:
        raise Http404

def edit_quote(request):
    if request.method == 'POST':
        quote_form = QuoteForm(request.POST.copy(), prefix='quote')
        print request.POST
        if quote_form.is_valid() and quote_form.has_changed():
            print request.POST
            quote_id = request.POST.get('quote_id')
            print 'quote_id', quote_id
            quote = Quote.objects.filter(id=quote_id)
            request_post = ''
            for key,value in request.POST.items():
                request_post += key
                request_post += value
            return HttpResponse(request_post)
        return HttpResponse('form not valid or changed')
    else:
        raise Http404
