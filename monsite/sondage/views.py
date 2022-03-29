# from multiprocessing import context
# from re import template
# from unittest import loader
# from urllib import response
from multiprocessing import AuthenticationError, context
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import Citizen, Question, Choice
# from django.template import loader
from django.urls import reverse

from django.views import generic

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils import timezone

def index(request):
    # # # return HttpResponse("Bienvenue a l'index de notre sondage")

    # # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # # output = "<br>" .join([q.question_text for q in latest_question_list])
    # # return HttpResponse(output)

    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("sondage/index.html")
    # context = {"question_list": latest_question_list}
    # return HttpResponse(template.render(context, request))

    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"question_list": latest_question_list}
    return render(request, "sondage/index.html", context)


def detail(request, question_id):
    # # return HttpResponse("Voici la question numéro %s." % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("La question n'existe pas")
    # return render(request, "sondage/detail.html", {"question":question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "sondage/detail.html",{"question":question})

    

def results(request, question_id):
    # response = "Voici les votes de la question numéro %s."
    # return HttpResponse(response % question_id)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "sondage/results.html", {"question":question})

def vote(request, question_id):
    # return HttpResponse("vous votez pour la question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
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
        # return Question.objects.order_by("-pub_date")[:5]
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "sondage/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "sondage/results.html"

def my_login(request):
    return render(request,"sondage/login.html")

def register(request):
    return render(request,"sondage/register.html")

def my_logout(request):
        return render(request,"sondage/logout.html")

def registered(request):
    name = request.POST["user_name"]
    firstname = request.POST["user_firstname"]
    pwd = request.POST["user_pwd"]
    email = request.POST["user_email"]
    username= firstname[0].lower() + "." + name.lower()
    user = User.objects.create_user(username, email, pwd)
    citizen = Citizen(user=user)
    user.last_name = name
    user.first_name = firstname
    user.save()
    citizen.save()
    context = {"user": user}
    return render(request,'sondage/registered.html', context)

def welcome(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user= authenticate(request, username=username,password=password)
    context = {"user":user}
    if user is not None:
        login(request,user)
        return render(request,"sondage/welcome.html",context)
    else:
        return render(request, "sondage/error_log.html")
    
def my_logout(request):
    logout(request)
    return render(request,"sondage/logout.html")

def profil(request):
    citizen = Citizen.objects.get(user=request.user)
    context = {"citizen":citizen}
    return render(request,"sondage/profil.html", context)

def become(request):
    request.user.citizen.electeur = True
    request.user.citizen.save()
    return IndexView.as_view()(request)