
Vue index avec appel de methode was_published_recently




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    question_list = []
    for i in latest_question_list:
        if i.was_published_recently():
            question_list.append(i)
    context = {'question_list': question_list}


    vue vote avec appel de methode vote


    def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'sondage/detail.html', {'question':question,'error_message': 'Vous devez choisir!',})
    else:
        question.vote(request.POST['choice'])
        return HttpResponseRedirect(reverse('sondage:results', args=(question_id,)))


        méthode vote du model Question


        def vote(self, choice_id):
        choice = self.choice_set.get(pk=choice_id)
        choice.votes += 1
        return choice