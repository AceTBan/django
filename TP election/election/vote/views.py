 
from django.shortcuts import get_object_or_404, render
 
from django.http import HttpResponse, HttpResponseRedirect
from .models import Elections, Choice
from django.template import loader
from django.urls import reverse

from django.views import generic


def index(request):
   
    latest_question_list = Elections.objects.order_by("-publish_date")[:5]
    context = {"question_list": latest_question_list}
    return render(request, "sondage/index.html", context)


def detail(request, question_id):
     
    question = get_object_or_404(Elections, pk=question_id)
    return render(request, "sondage/detail.html",{"question":question})

def results(request, question_id):
    
    question = get_object_or_404(Elections,pk=question_id)
    return render(request, "sondage/results.html", {"question":question})

def vote(request, question_id):
 
    question = get_object_or_404(Elections, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request,"sondage/detail.html",{"question":question,"error_message":"Vous devez choisir !!",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("sondage:results", args=(question_id,)))

    
class IndexView(generic.ListView):
    template_name = "sondage/index.html"
    context_object_name = "question_list"

def get_queryset(self):
    return Elections.objects.order_by("-publish_date")[:5]

class DetailView(generic.DetailView):
    model = Elections
    template_name = "sondage/detail.html"

class ResultsView(generic.DetailView):
    model = Elections
    template_name = "sondage/results.html"