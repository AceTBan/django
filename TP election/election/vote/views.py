from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue a l'index de notre vote")