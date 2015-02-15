from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail, BadHeaderError

from django.shortcuts import get_object_or_404, render


from porfolio.models import Work, ContactForm
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_work_list = Work.objects.order_by('-pub_date')[:6]
    context = {'latest_work_list': latest_work_list}
    return render(request, 'porfolio/index.html', context)

def detail(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    return render(request, 'porfolio/detail.html', {'work': work})

def contactview(request):
        subject = request.POST.get('topic', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')

        if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, ['change@this.com'])
                except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/contact/thankyou/')
        else:
            return render_to_response('contacts.html', {'form': ContactForm()})
    
        return render_to_response('contacts.html', {'form': ContactForm()},
            RequestContext(request))

def thankyou(request):
        return render_to_response('thankyou.html')


        