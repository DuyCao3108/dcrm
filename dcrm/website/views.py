from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html", {})


def link(request):
    return render(request, "link.html", {})