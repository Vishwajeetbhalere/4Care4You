from django.shortcuts import render
from .models import Contact


def home(request):
    return render(request, 'main/home.html')


def SCAI(request):
    return render(request, 'main/scai.html')


def ISPIN(request):
    return render(request, 'main/ispin.html')


def aboutus(request):
    return render(request, 'main/aboutus.html')


def usecase(request):
    return render(request, 'main/usecase.html')


def contact_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        city = request.POST['city']
        country = request.POST['country']
        product_interested = request.POST['product_interested']
        message = request.POST['message']
        # print(request.POST)
        contact = Contact(first_name=first_name, last_name=last_name, email=email, contact_no=contact_no,
                          city=city, country=country, product_interested=product_interested, message=message)
        contact.save()
        # print('We are using post request!')
    return render(request, 'main/contact.html')
