from django.shortcuts import render, HttpResponse
from . import models

def index(request):
    return render(request, 'guest/index.html', {})


def submit(request):
    if request.method=="POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        number_of_guest = request.POST["number_of_guest"]
        attending = request.POST["attending"]
        message = request.POST["message"]
        models.Guest.objects.create(name=name,phone=phone, number_of_guest= number_of_guest, attending= attending, message=message)

        result ='<div class="alert alert-info">Success! your message is sent</div>'
        return HttpResponse(result)
    return render(request, 'guest/index.html', {})
