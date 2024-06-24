from django.shortcuts import render, redirect
from .models import Url
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
import random,string 

def RendomUrl():
    return "".join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(10)])

def dashboard(request):
    if request.method == "POST":
        URL = request.POST["URL"]
        shortedUrl = request.POST.get("shortedUrl", None)
        if not shortedUrl:
            shortedUrl = RendomUrl()
        
        try:
            # request.user.url_set(target_url-url)
            Url.objects.create(user=request.user, target_url = URL, short_url=shortedUrl).save()
            messages.success(request, "Shorted Successfully")
            return redirect("dashboard")
        except:
            messages.error(request, "ShortedUrl already in used! Refresh")
            return render(request, "dashboard.html", {"url":URL, "shortedUrl":shortedUrl})

    site = get_current_site(request)
    return render(request, "dashboard.html", {"domain":site})

def redirect_to_target_page(request,shortedUrl):
    obj = Url.objects.get(short_url = shortedUrl)
    URL = obj.target_url
    return redirect(URL)