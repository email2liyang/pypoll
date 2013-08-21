# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book

def hello(request):
    return HttpResponse('hello world %s %s' % (request.get_full_path(),request.get_host(),))

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render_to_response('books/search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search team')
        elif len(q) > 20:
            errors.append('Please enter at most 20 chars')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('books/search_result.html',{'books':books,'query':q})

    return render_to_response('books/search_form.html',{'errors':errors})
