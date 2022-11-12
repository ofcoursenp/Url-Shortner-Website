from django.shortcuts import render,HttpResponse
from . main import shortnen
from .models import UrlsGiven
# Create your views here.

def index(req):
    sites = UrlsGiven.objects.all()
    if req.POST.get('website'):
        link = shortnen(req.POST.get('website'))
        context = {
            'url':link,
            'val':sites
        }
        website = link
        Web = UrlsGiven(url=link)
        # for val in sites:
        #     print(val)
        Web.save()
        return render(req,'index.html',context)
    return render(req,'index.html')

