from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user) #User konsolda gözüküyor!
    sozluk = { #Context sözlük olmak zorunda
        "ad":"orçun",
        "soyad":"madran"
    }
    return render(request, 'home.html', sozluk)

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>İletişim</h1>")