from django.shortcuts import render
from django.http import HttpResponse

from .models import Qr_generate_web

# Create your views here.
def home(request, url):
    if request.method == 'GET':
        return render(request, 'qr_app/home.html')

    if request.method == 'POST':
        qr = Qr_generate_web()
        qr.generate(url)
        ## REDIRECT TIL ANDET
        return redirect('qr_app/home.html')

def new_qr_web(request):
    pass
