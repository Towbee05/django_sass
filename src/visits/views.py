from django.shortcuts import render
from django.http import HttpResponse
from .models import PageVisits

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello, world </h1>")

def about_view (request, *args, **kwargs):
    total_qs= PageVisits.objects.all()
    qs= PageVisits.objects.filter(path= request.path)

    try: 
        percent = (qs.count() * 100) / total_qs.count();
    except: 
        percent = 0

    PageVisits.objects.create(path= request.path)
    context = {
        "queryset" : qs.count(),
        "total": total_qs.count(),
        "percent" : percent
    }
    return render(request, "snippets/welcome_user_msg.html", context)