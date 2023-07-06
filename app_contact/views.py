from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact(request):
    allcontact = Contact.objects.all()
    return render(request, 'temp/front/contact/contact.html', {'allcontact':allcontact})