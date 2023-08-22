from django.shortcuts import render , redirect
from django.http import HttpResponse
import qrcode
from .models import *
from django.db.models import Sum
from django.core.files.base import ContentFile
from io import BytesIO
from django.db.models import Max


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def ip(request):
    client_ip = get_client_ip(request)
    # Now you can use the client_ip in your view logic
    return HttpResponse(f"Your IP address: {client_ip}")

def create_qr(request):
    if request.method == "POST":
        link = request.POST['link']
        qrs = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,  # Adjust the size as needed
            border=0,
        )
        qrs.add_data("http://"+request.META['HTTP_HOST']+f"/scan/{request.POST['name']}")
        qrs.make(fit=True)
        img = qrs.make_image(fill_color="#200058", back_color=None)
        image = BytesIO()
        img.save(image , format="PNG")
        image.seek(0)
        try:
            new_qr = qr(
                name=request.POST['name'],
                link=link,
                counter = 0
            )
        except:
            pass
        new_qr.image.save('qr.png', ContentFile(image.read()) , save=False)
        new_qr.save()
        
        return redirect(new_qr.image.url)
    else:
        return render(request, "home.html")
    
def scand(e,name):
    to = qr.objects.get(name = name)
    to.counter += 1
    to.save()
    scaner = scan.objects.create(
        qr = to,
        ip = get_client_ip(e),
        count = to.counter
    )
    return redirect(to.link)

def desplay(e):
    data = qr.objects.all()
    return render(e , "AllQr.html" , {"data":data})

def anal(e):
    Data = qr.objects.all()
    for i in Data:
        print(i.get_day())
    return render(e , "anal.html" , {"data":Data})

