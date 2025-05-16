from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form= ContactForm()
    
    if request.method=="POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name', '')
            email=request.POST.get('email', '')
            content=request.POST.get('content', '')
            #enviamos el correo y redirecionamos
            email=EmailMessage(
                'La Caffetiera: Nuevo mensage de contacto',
                "De {{<}}>\n\nEscribió: \n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ['rpindes@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
            
            #Si todo ha ido bien, redireccionamos ok
            
                return redirect(reverse('contact')+ "?Ok")
            except:
            #Algo no ha ido bien, redireccionamos a Fail
            
                return redirect(reverse('contact')+ "?fail")
        
    return render(request, "contact/contact.html", {'form':contact_form})