from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Contacts
# Create your views here.
def index(request):
    all_contacts = Contacts.objects.all()
    print(all_contacts)
    return render(request, 'index.html', context={"members": all_contacts})

def deleteContact(request, id):
    yaroo = Contacts.objects.get(id=id)
    yaroo.delete()

    return redirect("/")

def addContact(request):
    return render(request, "addcontact.html", )

def handleContactAdd(request):
    if request.method == "POST":
        print(request.POST["myNumber"])
        newcontact= Contacts(firstname=request.POST["myFirst"],
                             lastname=request.POST["myLastname"],
                             number=request.POST["myNumber"],
                             sen=2)
        newcontact.save()

    else:   
        print("salam dadash GETE")


    return redirect("/")

def editContactPage(request,id,error="true"):
    contact= Contacts.objects.get(id=id)
    print(contact)
    return render(request, "editcontact.html",{"thecontact":contact} )

def editContactForm(request,id):
    contact= Contacts.objects.get(id=id)
    if request.method == "POST":
        valid = is_valid_contact({"fname": "", 'number':request.POST["myNumber"]})
        if valid == True:
            contact.firstname = request.POST["myFirst"]
            contact.lastname = request.POST["myLastname"]
            contact.number = request.POST["myNumber"]
            contact.sen = 2
            contact.save()
        else: 
            print(valid)
            return render(request, "editcontact.html",{"thecontact":contact, "error": valid } )
    return redirect("/")

def is_valid_contact(user):
    if len(user["number"]) != 11:
        return "داداش شماره 11 رقمیه، ها؟"
    return True
