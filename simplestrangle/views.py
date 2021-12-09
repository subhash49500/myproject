from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, subhash. You're at the short strangle index.")


def createnewposition(request):
    return HttpResponse("Here have to create new position")

def continueoldposition(request):
    return HttpResponse("Here have to continue old position")

def closeallpositions(request):
    return HttpResponse("Here have to close all positions")



