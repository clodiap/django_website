from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, "home.html", {})

def about(request):
  my_name = "Hello my name is Clodiap."
  return render(request, "about.html", {"myname" : my_name})

def contact(request):
  return render(request, "contact.html", {})
