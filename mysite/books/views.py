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
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('books/search_result.html',{'books':books,'query':q})
    else:
        message = 'empty'
        return HttpResponse(message)
