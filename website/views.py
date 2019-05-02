from django.shortcuts import render

# Create your views here.
from website.models import ContactUs


def index(request):
    return render(request, 'index.html', {})


def contact_us(request):
    if request.method == 'POST':
        ContactUs.objects.create(email=request.POST.get('email'),
                                 name=request.POST.get('name'),
                                 message=request.POST.get('message')
                                 )
    return render(request, 'index.html', {})
