# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.views.generic import ListView
from books.models import Book, Publisher
from books.forms import ContactForm
from django.template import RequestContext
import csv
from reportlab.pdfgen import canvas

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favourite_publishers'



def hello(request):
    return HttpResponse('hello world %s %s' % (request.get_full_path(),request.get_host(),))

def escape(request):
    return render_to_response('books/escape.html',{'data':'<script>document.write("abc")</script>'})

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

def contact(reqeust):
    if reqeust.method == 'POST':
        form = ContactForm(reqeust.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'],cd['message'],cd.get('email','noreply@example.com'),'siteowner@example.com')
            return HttpResponseRedirect('/book/contact/thanks')
    else:
        form = ContactForm(initial={'subject':'I love your site'})
    return render_to_response('books/contact_form.html',{'form':form},context_instance=RequestContext(reqeust))

def passengers_csv(request):
    PASSENGERS=[146,184,235,200,226,251,299,273,281,304,203]
    #create the http resonse object with appropriate CSV header
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition']='attachment;filename=passengers.csv'

    #create CSV writer using http response as a "file"
    writer = csv.writer(response)
    writer.writerow(['Year','Passengers'])
    for (year,num) in zip(range(1995,2006),PASSENGERS):
        writer.writerow([year,num])
    return response

def hello_pdf(reqeust):
    #create response object with a appropriate PDF headers
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition']='attachment;filename=hello.pdf'

    #create PDF Object,using the response object as it's file
    p = canvas.Canvas(response)

    #Draw thing on pdf
    p.drawString(100,100,"hello world");
    p.showPage()
    p.save()

    return response







